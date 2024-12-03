"""Final Delta Load Pipeline using twitter-api-client with debugging."""

import os
import json
import logging
import traceback
from datetime import datetime
from pathlib import Path
import requests
from github import Github
from twitter.scraper import Scraper
from collections import defaultdict

# Configure logging for debugging
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all levels of log messages
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log', mode='w'),  # Overwrite log file each run
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DeltaLoadETL:
    def __init__(self):
        self.staging_dir = Path("data/staging")
        self.processed_dir = Path("data/processed")
        self.last_run_file = self.staging_dir / "last_run.json"
        self.staging_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            self.load_env_variables()
            self.init_api_clients()
        except Exception as e:
            logger.error(f"Initialization failed: {e}")
            logger.error(traceback.format_exc())
            raise

    def load_env_variables(self):
        from dotenv import load_dotenv
        load_dotenv()
        
        # Validate environment variables
        required_vars = [
            'TWITTER_CT0', 
            'TWITTER_AUTH_TOKEN', 
            'TWITTER_USER_ID', 
            'GITHUB_TOKEN', 
            'GITHUB_USERNAME', 
            'RAINDROP_ACCESS_TOKEN'
        ]
        
        for var in required_vars:
            if not os.getenv(var):
                raise ValueError(f"Missing required environment variable: {var}")
        
        # Twitter auth using cookies
        self.twitter_ct0 = os.getenv('TWITTER_CT0')
        self.twitter_auth_token = os.getenv('TWITTER_AUTH_TOKEN')
        self.twitter_user_id = os.getenv('TWITTER_USER_ID')
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.github_username = os.getenv('GITHUB_USERNAME')
        self.raindrop_token = os.getenv('RAINDROP_ACCESS_TOKEN')
        
        logger.info("Environment variables loaded successfully.")

    def init_api_clients(self):
        # Initialize Twitter scraper using cookies
        try:
            logger.info("Initializing Twitter scraper...")
            self.twitter_api = Scraper(cookies={
                "ct0": self.twitter_ct0,
                "auth_token": self.twitter_auth_token
            })
            logger.info("Twitter scraper initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize Twitter scraper: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")
            self.twitter_api = None

        # Initialize GitHub API client
        try:
            logger.info("Initializing GitHub API client...")
            self.github_api = Github(self.github_token)
            # Test connection by getting user
            user = self.github_api.get_user()
            logger.info(f"GitHub API client initialized. Logged in as: {user.login}")
        except Exception as e:
            logger.error(f"Failed to initialize GitHub API client: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")
            self.github_api = None

        # Initialize Raindrop.io headers
        try:
            logger.info("Initializing Raindrop.io API...")
            self.raindrop_headers = {'Authorization': f'Bearer {self.raindrop_token}'}
            # Test connection
            response = requests.get('https://api.raindrop.io/rest/v1/collections', headers=self.raindrop_headers)
            response.raise_for_status()
            logger.info("Raindrop.io API headers initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize Raindrop.io API: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")
            self.raindrop_headers = None

    def get_last_run_data(self):
        """Retrieve last run data, creating a new file if it doesn't exist."""
        try:
            if self.last_run_file.exists():
                with open(self.last_run_file, 'r') as f:
                    return json.load(f)
            else:
                # Create initial last run data
                initial_data = {
                    'last_processed_time': '2000-01-01T00:00:00+00:00'  # Far in the past
                }
                return initial_data
        except Exception as e:
            logger.error(f"Error reading last run file: {e}")
            # Return a default dict if reading fails
            return {'last_processed_time': '2000-01-01T00:00:00+00:00'}

    def save_last_run_data(self, data):
        """Save last run data to file."""
        try:
            with open(self.last_run_file, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Updated last run data: {data}")
        except Exception as e:
            logger.error(f"Error saving last run data: {e}")

    def fetch_twitter_data(self):
        """Fetch most recent tweets and likes from Twitter with minimal batch retrieval."""
        if not self.twitter_api:
            logger.error("Twitter API client not initialized.")
            return None

        # Load last run data to get the last processed timestamp
        try:
            last_run_data = self.get_last_run_data()
            last_processed_time = last_run_data.get('last_processed_time')
        except Exception as e:
            logger.warning(f"Could not retrieve last run data: {e}")
            last_processed_time = None

        try:
            # Fetch tweets with minimal retrieval
            logger.info("Fetching Twitter tweets and replies...")
            tweets = []
            tweet_iterator = self.twitter_api.tweets_and_replies(count=1)  # Retrieve just 1 tweet
            
            for tweet in tweet_iterator:
                # Check last processed time
                tweet_time = datetime.fromisoformat(tweet['created_at'])
                if last_processed_time:
                    last_processed_datetime = datetime.fromisoformat(last_processed_time)
                    if tweet_time <= last_processed_datetime:
                        break
                
                tweets.append(tweet)
                break  # Ensure only 1 tweet is retrieved
            
            logger.info(f"Fetched {len(tweets)} new tweets.")

            # Fetch likes with minimal retrieval
            logger.info("Fetching Twitter likes...")
            likes = []
            likes_iterator = self.twitter_api.likes(count=1)  # Retrieve just 1 like
            
            for like in likes_iterator:
                # Check last processed time
                like_time = datetime.fromisoformat(like['created_at'])
                if last_processed_time:
                    last_processed_datetime = datetime.fromisoformat(last_processed_time)
                    if like_time <= last_processed_datetime:
                        break
                
                likes.append(like)
                break  # Ensure only 1 like is retrieved
            
            logger.info(f"Fetched {len(likes)} new likes.")

            # Update last processed time to the most recent tweet/like time
            if tweets or likes:
                all_items = tweets + likes
                most_recent_time = max(
                    datetime.fromisoformat(item['created_at']) 
                    for item in all_items
                )
                last_run_data['last_processed_time'] = most_recent_time.isoformat()
                self.save_last_run_data(last_run_data)

            return {
                'tweets_and_replies': tweets,
                'likes': likes
            }
        except Exception as e:
            logger.error(f"Error fetching Twitter data: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")
            return None

    def save_to_staging(self, source, data_type, data):
        if not data:
            logger.debug(f"No new data to save for {source} {data_type}.")
            return
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.staging_dir / f"{source}_{data_type}_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.debug(f"Saved {len(data)} items to {filename}")

    def fetch_github_data(self):
        logger.info("Fetching GitHub data...")
        last_run = self.get_last_run_data()
        last_starred_at = last_run.get('github_last_starred_at')
        new_stars = []
        try:
            user = self.github_api.get_user(self.github_username)
            starred_repos = user.get_starred()
            logger.debug("Retrieved starred repositories.")
            for repo in starred_repos:
                starred_at = repo.starred_at
                if last_starred_at and starred_at <= datetime.fromisoformat(last_starred_at):
                    logger.debug("No new starred repositories found.")
                    break
                star_data = {
                    'id': str(repo.id),
                    'created_at': starred_at.isoformat(),
                    'name': repo.name,
                    'full_name': repo.full_name,
                    'description': repo.description,
                    'url': repo.html_url,
                    'source': 'github',
                    'type': 'star',
                    'metadata': {
                        'language': repo.language,
                        'stars': repo.stargazers_count
                    }
                }
                new_stars.append(star_data)
            if new_stars:
                last_run['github_last_starred_at'] = new_stars[0]['created_at']
                logger.info(f"Fetched {len(new_stars)} new starred repositories.")
                self.save_to_staging('github', 'stars', new_stars)
                self.save_last_run_data(last_run)
            else:
                logger.info("No new starred repositories to fetch.")
        except Exception as e:
            logger.error(f"Error fetching GitHub data: {e}")

    def fetch_raindrop_data(self):
        logger.info("Fetching Raindrop.io data...")
        last_run = self.get_last_run_data()
        last_bookmark_id = last_run.get('raindrop_last_bookmark_id')
        new_bookmarks = []
        page = 0
        try:
            while True:
                url = 'https://api.raindrop.io/rest/v1/raindrops/0'
                params = {
                    'page': page,
                    'perpage': 50,
                    'sort': '-created'
                }
                logger.debug(f"Fetching Raindrop.io bookmarks with params: {params}")
                response = requests.get(url, headers=self.raindrop_headers, params=params)
                response.raise_for_status()
                data = response.json()
                items = data.get('items', [])
                if not items:
                    logger.debug("No more bookmarks to fetch.")
                    break
                for item in items:
                    if last_bookmark_id and str(item['_id']) == last_bookmark_id:
                        logger.debug("Reached last fetched bookmark.")
                        break
                    bookmark_data = {
                        'id': str(item['_id']),
                        'created_at': item['created'],
                        'title': item['title'],
                        'excerpt': item.get('excerpt', ''),
                        'url': item['link'],
                        'source': 'raindrop',
                        'type': 'bookmark',
                        'metadata': {
                            'tags': item.get('tags', []),
                            'collection': item.get('collection', {}).get('title', '')
                        }
                    }
                    new_bookmarks.append(bookmark_data)
                if items and str(items[0]['_id']) != last_bookmark_id:
                    last_run['raindrop_last_bookmark_id'] = str(items[0]['_id'])
                    logger.debug(f"Updated last bookmark ID to {items[0]['_id']}")
                else:
                    break
                page += 1
            if new_bookmarks:
                logger.info(f"Fetched {len(new_bookmarks)} new bookmarks.")
                self.save_to_staging('raindrop', 'bookmarks', new_bookmarks)
                self.save_last_run_data(last_run)
            else:
                logger.info("No new bookmarks to fetch.")
        except Exception as e:
            logger.error(f"Error fetching Raindrop.io data: {e}")

    def transform_data(self):
        logger.info("Transforming data...")
        staged_files = list(self.staging_dir.glob("*.json"))
        unified_data = []
        for file_path in staged_files:
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                logger.debug(f"Loaded {len(data)} items from {file_path.name}")
                unified_data.extend(data)
                # Move file to archived folder
                archive_dir = self.staging_dir / "archived"
                archive_dir.mkdir(exist_ok=True)
                archived_file_path = archive_dir / file_path.name
                file_path.rename(archived_file_path)
                logger.debug(f"Moved {file_path.name} to archive.")
            except Exception as e:
                logger.error(f"Error processing file {file_path.name}: {e}")
        if unified_data:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.processed_dir / f"unified_data_{timestamp}.json"
            try:
                with open(output_file, 'w') as f:
                    json.dump(unified_data, f, ensure_ascii=False, indent=2)
                logger.info(f"Transformed data saved to {output_file}")
            except Exception as e:
                logger.error(f"Error saving transformed data: {e}")
        else:
            logger.info("No new data to transform.")

    def check_recent_entries(self, jsonl_file_path):
        """Check the most recent entries for each source in the JSONL file."""
        # Load the JSONL file
        with open(jsonl_file_path, 'r') as file:
            lines = file.readlines()

        # Parse JSONL entries
        json_objects = [json.loads(line) for line in lines]

        # Group entries by source
        entries_by_source = defaultdict(list)
        for obj in json_objects:
            source = obj.get('source')
            if source:
                entries_by_source[source].append(obj)

        # Function to parse datetime strings
        parse_datetime = lambda dt_str: datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%S')

        # Check recent entries by source
        for source, entries in entries_by_source.items():
            # Sort entries by created_at, assuming 'created_at' is the field name
            try:
                entries.sort(key=lambda x: parse_datetime(x.get('created_at', '')), reverse=True)

                # Get the most recent entry
                most_recent_entry = entries[0] if entries else None

                if most_recent_entry:
                    # Extract relevant fields for comparison
                    most_recent_url = most_recent_entry.get('url')
                    most_recent_datetime = most_recent_entry.get('created_at')

                    logger.debug(f"Source: {source}")
                    logger.debug(f"Most Recent URL: {most_recent_url}")
                    logger.debug(f"Most Recent Datetime: {most_recent_datetime}")

                    # Implement logic to decide if processing should continue
                    # For example, check if the current entry matches the most recent one
                    # if current_entry['url'] == most_recent_url:
                    #     logger.info("Duplicate entry found, stopping further processing.")
                    # else:
                    #     logger.info("Continue processing.")
            except (ValueError, KeyError) as e:
                logger.error(f"Error processing entries for source {source}: {e}")
                continue

    def run(self):
        """Main ETL pipeline execution method."""
        logger.info("Starting Deltaload ETL pipeline...")
        
        # Fetch data from various sources
        twitter_data = self.fetch_twitter_data()
        self.fetch_github_data()
        self.fetch_raindrop_data()
        self.transform_data()
        jsonl_file_path = 'data-bookmark.jsonl'  # Adjust the path as needed
        self.check_recent_entries(jsonl_file_path)
        
        logger.info("Deltaload ETL pipeline completed.")

if __name__ == "__main__":
    try:
        etl = DeltaLoadETL()
        etl.run()
    except Exception as e:
        logger.error(f"Critical error in ETL pipeline: {e}")
        logger.error(f"Full exception details: {traceback.format_exc()}")