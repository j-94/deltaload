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
        logging.FileHandler('debug.log'),
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
        self.load_env_variables()
        self.init_api_clients()

    def load_env_variables(self):
        from dotenv import load_dotenv
        load_dotenv()
        # Twitter auth using cookies
        self.twitter_ct0 = os.getenv('TWITTER_CT0')
        self.twitter_auth_token = os.getenv('TWITTER_AUTH_TOKEN')
        self.twitter_user_id = os.getenv('TWITTER_USER_ID')
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.github_username = os.getenv('GITHUB_USERNAME')
        self.raindrop_token = os.getenv('RAINDROP_TOKEN')
        logger.debug("Environment variables loaded.")

    def init_api_clients(self):
        # Initialize Twitter scraper using cookies
        try:
            self.twitter_api = Scraper(cookies={
                "ct0": self.twitter_ct0,
                "auth_token": self.twitter_auth_token
            })
            logger.debug("Twitter scraper initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize Twitter scraper: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")
            self.twitter_api = None

        # Initialize GitHub API client
        try:
            self.github_api = Github(self.github_token)
            logger.debug("GitHub API client initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize GitHub API client: {e}")
            self.github_api = None

        # Initialize Raindrop.io headers
        self.raindrop_headers = {'Authorization': f'Bearer {self.raindrop_token}'}
        logger.debug("Raindrop.io API headers initialized.")

    def get_last_run_data(self):
        if self.last_run_file.exists():
            with open(self.last_run_file, 'r') as f:
                data = json.load(f)
                logger.debug(f"Last run data loaded: {data}")
                return data
        logger.debug("No last run data found.")
        return {}

    def save_last_run_data(self, data):
        with open(self.last_run_file, 'w') as f:
            json.dump(data, f)
        logger.debug(f"Last run data saved: {data}")

    def save_to_staging(self, source, data_type, data):
        if not data:
            logger.debug(f"No new data to save for {source} {data_type}.")
            return
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.staging_dir / f"{source}_{data_type}_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.debug(f"Saved {len(data)} items to {filename}")

    def fetch_twitter_data(self):
        logger.info("Fetching Twitter data...")
        last_run = self.get_last_run_data()
        last_tweet_id = last_run.get('twitter_last_tweet_id')
        last_like_id = last_run.get('twitter_last_like_id')
        new_tweets = []
        new_likes = []

        # Fetch tweets using batch endpoint
        try:
            # Get user's tweets (we'll use tweets_and_replies for comprehensive data)
            logger.debug(f"Attempting to fetch tweets for user ID: {self.twitter_user_id}")
            tweets = self.twitter_api.tweets_and_replies([self.twitter_user_id])
            logger.info(f"Fetched {len(tweets)} tweets.")
            
            # Filter tweets newer than last_tweet_id
            if last_tweet_id:
                tweets = [t for t in tweets if int(t['id']) > int(last_tweet_id)]
            
            for tweet in tweets:
                try:
                    tweet_data = {
                        'id': str(tweet['id']),
                        'created_at': tweet['created_at'],
                        'text': tweet['text'],
                        'source': 'twitter',
                        'type': 'tweet',
                        'url': f"https://twitter.com/i/web/status/{tweet['id']}",
                        'metadata': {
                            'retweet_count': tweet.get('retweet_count', 0),
                            'favorite_count': tweet.get('favorite_count', 0),
                            'reply_count': tweet.get('reply_count', 0),
                            'quote_count': tweet.get('quote_count', 0)
                        }
                    }
                    new_tweets.append(tweet_data)
                except Exception as tweet_error:
                    logger.error(f"Error processing individual tweet: {tweet_error}")
                    logger.error(f"Problematic tweet data: {tweet}")
            
            if tweets:
                last_run['twitter_last_tweet_id'] = str(max(int(t['id']) for t in tweets))
                logger.debug(f"Updated last tweet ID to {last_run['twitter_last_tweet_id']}")
        except Exception as e:
            logger.error(f"Error fetching tweets: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")

        # Fetch likes
        try:
            logger.debug(f"Attempting to fetch likes for user ID: {self.twitter_user_id}")
            likes = self.twitter_api.likes([self.twitter_user_id])
            logger.info(f"Fetched {len(likes)} likes.")
            
            # Filter likes newer than last_like_id
            if last_like_id:
                likes = [l for l in likes if int(l['id']) > int(last_like_id)]
            
            for like in likes:
                try:
                    like_data = {
                        'id': str(like['id']),
                        'created_at': like['created_at'],
                        'text': like['text'],
                        'source': 'twitter',
                        'type': 'like',
                        'url': f"https://twitter.com/i/web/status/{like['id']}",
                        'metadata': {
                            'author': like['user']['screen_name'],
                            'user_id': like['user']['id_str']
                        }
                    }
                    new_likes.append(like_data)
                except Exception as like_error:
                    logger.error(f"Error processing individual like: {like_error}")
                    logger.error(f"Problematic like data: {like}")
            
            if likes:
                last_run['twitter_last_like_id'] = str(max(int(l['id']) for l in likes))
                logger.debug(f"Updated last like ID to {last_run['twitter_last_like_id']}")
        except Exception as e:
            logger.error(f"Error fetching likes: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")

        self.save_to_staging('twitter', 'tweets', new_tweets)
        self.save_to_staging('twitter', 'likes', new_likes)
        self.save_last_run_data(last_run)

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
        logger.info("Starting ETL process...")
        self.fetch_twitter_data()
        self.fetch_github_data()
        self.fetch_raindrop_data()
        self.transform_data()
        jsonl_file_path = 'data-bookmark.jsonl'  # Adjust the path as needed
        self.check_recent_entries(jsonl_file_path)
        logger.info("ETL process completed.")

if __name__ == "__main__":
    etl = DeltaLoadETL()
    etl.run()