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

class DeltaLoadETL:
    def __init__(self):
        self.staging_dir = Path("data/staging")
        self.processed_dir = Path("data/processed")
        self.last_run_file = self.processed_dir / "last_run.json"
        self.staging_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        
        self.setup_logging()
        
        try:
            self.load_env_variables()
            self.init_api_clients()
        except Exception as e:
            logger.error(f"Initialization failed: {e}")
            logger.error(traceback.format_exc())
            raise

    def setup_logging(self):
        # Create a logger with a unique filename based on timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f'logs/deltaload_{timestamp}.log'
        
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        
        # Configure logging to write to file and console
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                logging.FileHandler(log_filename, mode='w'),
                logging.StreamHandler()
            ]
        )
        
        global logger
        logger = logging.getLogger(__name__)

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

    def get_last_processed_tweet(self):
        """Retrieve the last processed tweet from previous run data."""
        try:
            # Try to read from last_run.json
            with open(self.processed_dir / 'last_run.json', 'r') as f:
                last_run_data = json.load(f)
                
            # Extract last processed tweet information
            last_processed_tweet = {
                "id": last_run_data.get('last_processed_tweet_id', 0),
                "created_at": last_run_data.get('last_processed_time', '2000-01-01T00:00:00+00:00'),
                "url": last_run_data.get('last_processed_tweet_url', '')
            }
            
            logger.info(f"Retrieved last processed tweet from file: {last_processed_tweet}")
            return last_processed_tweet
        
        except FileNotFoundError:
            # Hardcoded default tweet when no previous run data exists
            default_tweet = {
                "id": 1859499631282913423,  # Specific tweet ID from a known tweet
                "created_at": "2024-11-21 07:30:34+00:00",  # Specific timestamp
                "url": "https://twitter.com/i/web/status/1859499631282913423"  # Corresponding tweet URL
            }
            
            logger.warning("No last_run.json found. Using hardcoded default tweet.")
            logger.info(f"Default tweet: {default_tweet}")
            return default_tweet
        
        except Exception as e:
            # Fallback to hardcoded default if any other error occurs
            logger.error(f"Error reading last processed tweet: {e}")
            
            default_tweet = {
                "id": 1859499631282913423,  # Specific tweet ID from a known tweet
                "created_at": "2024-11-21 07:30:34+00:00",  # Specific timestamp
                "url": "https://twitter.com/i/web/status/1859499631282913423"  # Corresponding tweet URL
            }
            
            logger.warning("Using hardcoded default tweet due to error.")
            logger.info(f"Default tweet: {default_tweet}")
            return default_tweet

    def fetch_twitter_data(self):
        if not self.twitter_api:
            logger.error("Twitter API client not initialized.")
            return None

        try:
            logger.info("Fetching Twitter tweets and likes...")
            
            # Get tweets
            tweets = []
            tweet_iterator = self.twitter_api.tweets_and_replies(
                user_ids=[self.twitter_user_id],
                limit=50
            )
            for tweet in tweet_iterator:
                if tweet and 'tweet' in tweet:
                    tweets.append(tweet['tweet'])
            logger.info(f"Fetched {len(tweets)} tweets")

            # Get likes
            likes = []
            like_iterator = self.twitter_api.likes(
                user_ids=[self.twitter_user_id],
                limit=30
            )
            for like in like_iterator:
                if like and 'tweet' in like:
                    likes.append(like['tweet'])
            logger.info(f"Fetched {len(likes)} likes")

            # Return the data
            twitter_data = {
                'tweets': tweets,
                'likes': likes
            }

            return twitter_data

        except Exception as e:
            logger.error(f"Error fetching Twitter data: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")
            return None

    def test_twitter_batch_scraping(self):
        """Test Twitter batch scraping methods."""
        if not self.twitter_api:
            logger.error("Twitter API client not initialized.")
            return None

        try:
            # Test batch tweet retrieval
            test_tweet_ids = [
                1859499631282913423,  # Last processed tweet ID
                1850000000000000000,  # Example additional tweet ID
            ]
            
            logger.info("Testing batch tweet retrieval...")
            batch_tweets = self.twitter_api.tweets(test_tweet_ids)
            logger.info(f"Retrieved {len(batch_tweets)} tweets in batch.")
            
            for tweet in batch_tweets:
                logger.info(f"Batch Tweet Details: {tweet.get('id', 'N/A')}, Created at: {tweet.get('created_at', 'N/A')}")
            
            # Test batch user retrieval (if applicable)
            try:
                test_user_ids = [self.twitter_user_id]  # Use the authenticated user's ID
                batch_users = self.twitter_api.users([test_user_ids])
                logger.info(f"Retrieved {len(batch_users)} users in batch.")
                
                for user in batch_users:
                    logger.info(f"Batch User Details: {user.get('id', 'N/A')}, Username: {user.get('username', 'N/A')}")
            except Exception as user_error:
                logger.warning(f"User batch retrieval failed: {user_error}")
            
            return {
                'batch_tweets': batch_tweets,
                'batch_users': batch_users if 'batch_users' in locals() else []
            }
        
        except Exception as e:
            logger.error(f"Error in batch Twitter scraping test: {e}")
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
            url = 'https://api.github.com/user/starred'
            params = {
                'per_page': 10,  # Limit to 10 starred repositories
                'sort': 'created',
                'direction': 'desc'
            }
            logger.debug(f"Fetching GitHub starred repositories with params: {params}")
            response = requests.get(url, params=params, headers={'Authorization': f'token {self.github_token}'})
            response.raise_for_status()
            for star in response.json():
                # Stop if we've reached the last starred repository
                if last_starred_at and star['created_at'] <= last_starred_at:
                    break
                
                star_data = {
                    'id': str(star['id']),
                    'name': star['full_name'],
                    'description': star.get('description', ''),
                    'url': star['html_url'],
                    'created_at': star['created_at'],
                    'language': star.get('language'),
                    'source': 'github',
                    'type': 'star'
                }
                new_stars.append(star_data)
            
            if new_stars:
                # Update last starred at to the most recent star
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
        try:
            url = 'https://api.raindrop.io/rest/v1/raindrops/0'
            params = {
                'page': 0,  # Always fetch first page
                'perpage': 50,  # Limit to 50 bookmarks
                'sort': '-created'
            }
            logger.debug(f"Fetching Raindrop.io bookmarks with params: {params}")
            response = requests.get(url, headers=self.raindrop_headers, params=params)
            response.raise_for_status()
            data = response.json()
            items = data.get('items', [])
            
            for item in items:
                # Stop if we've reached the last fetched bookmark
                if last_bookmark_id and str(item['_id']) == last_bookmark_id:
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
            
            if new_bookmarks:
                # Update last bookmark ID to the most recent one
                last_run['raindrop_last_bookmark_id'] = str(items[0]['_id'])
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
        def parse_datetime(dt_str):
            if not dt_str:
                return None
            
            try:
                from dateutil.parser import parse
                # Use dateutil to parse various datetime formats
                parsed_dt = parse(dt_str)
                
                # Normalize to UTC if timezone is not specified
                if parsed_dt.tzinfo is None:
                    from dateutil.tz import tzutc
                    parsed_dt = parsed_dt.replace(tzinfo=tzutc())
                
                return parsed_dt
            except ImportError:
                logger.error("dateutil not installed. Falling back to basic parsing.")
                raise
            except Exception as e:
                logger.error(f"Failed to parse datetime '{dt_str}': {e}")
                return None

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