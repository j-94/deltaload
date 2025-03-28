"""Delta Load Pipeline for social media data."""

import os
import json
import logging
import traceback
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv
import requests
from github import Github
from twitter.scraper import Scraper

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class DeltaLoadETL:
    def __init__(self):
        self.jsonl_file = Path("data-bookmark.jsonl")
        self.setup_logging()
        
        try:
            self.load_env_variables()
            self.init_api_clients()
        except Exception as e:
            logger.error(f"Initialization failed: {e}")
            logger.error(traceback.format_exc())
            raise

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[logging.StreamHandler()]
        )
        
        global logger
        logger = logging.getLogger(__name__)

    def load_env_variables(self):
        """Load environment variables."""
        try:
            # Load environment variables from .env file
            load_dotenv()
            
            # Required environment variables
            self.github_token = os.getenv('GH_TOKEN')
            self.raindrop_token = os.getenv('RAINDROP_TOKEN')
            self.twitter_user_id = os.getenv('TWITTER_USER_ID')
            self.twitter_ct0 = os.getenv('TWITTER_CT0')
            self.twitter_auth_token = os.getenv('TWITTER_AUTH_TOKEN')
            
            # Validate required environment variables
            required_vars = {
                'GH_TOKEN': self.github_token,
                'RAINDROP_TOKEN': self.raindrop_token,
                'TWITTER_USER_ID': self.twitter_user_id,
                'TWITTER_CT0': self.twitter_ct0,
                'TWITTER_AUTH_TOKEN': self.twitter_auth_token
            }
            
            for var_name, var_value in required_vars.items():
                if not var_value:
                    raise ValueError(f"{var_name} environment variable is required")
                    
            logger.info("Environment variables loaded successfully.")
            
        except Exception as e:
            logger.error(f"Error loading environment variables: {e}")
            raise

    def init_api_clients(self):
        """Initialize API clients."""
        # Initialize GitHub API client
        try:
            logger.info("Initializing GitHub API client...")
            self.github_api = Github(self.github_token)
            # Test connection by getting user
            user = self.github_api.get_user()
            logger.info(f"GitHub API client initialized. Logged in as: {user.login}")
        except Exception as e:
            logger.error(f"Failed to initialize GitHub API: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")
            self.github_api = None

        # Initialize Twitter API client
        try:
            logger.info("Initializing Twitter API client...")
            self.twitter_api = Scraper(
                cookies={
                    'ct0': self.twitter_ct0,
                    'auth_token': self.twitter_auth_token
                }
            )
            logger.info("Twitter API client initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize Twitter API: {e}")
            logger.error(f"Full exception details: {traceback.format_exc()}")
            self.twitter_api = None

        # Initialize Raindrop.io API headers
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

    def read_jsonl(self):
        """Read existing JSONL data and get latest timestamps."""
        data = []
        latest_timestamps = {
            'twitter': datetime.min.replace(tzinfo=timezone.utc),
            'twitter_like': datetime.min.replace(tzinfo=timezone.utc),
            'github': datetime.min.replace(tzinfo=timezone.utc),
            'raindrop': datetime.min.replace(tzinfo=timezone.utc)
        }
        latest_id = 0
        
        try:
            if self.jsonl_file.exists():
                with open(self.jsonl_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        try:
                            record = json.loads(line.strip())
                            data.append(record)
                            
                            # Track latest ID
                            if 'id' in record:
                                latest_id = max(latest_id, int(record['id']))
                            
                            # Track latest timestamps by source
                            if 'created_at' in record and 'source' in record:
                                created_at = datetime.fromisoformat(record['created_at'])
                                source = record['source']
                                if source == 'twitter_like':
                                    latest_timestamps['twitter_like'] = max(latest_timestamps['twitter_like'], created_at)
                                elif source == 'twitter':
                                    latest_timestamps['twitter'] = max(latest_timestamps['twitter'], created_at)
                                elif source == 'github':
                                    latest_timestamps['github'] = max(latest_timestamps['github'], created_at)
                                elif source == 'raindrop':
                                    latest_timestamps['raindrop'] = max(latest_timestamps['raindrop'], created_at)
                            
                        except json.JSONDecodeError:
                            logger.error(f"Error decoding JSON line: {line}")
                            continue
                        except Exception as e:
                            logger.error(f"Error processing line: {e}")
                            continue
                
                logger.info(f"Read {len(data)} records from JSONL file")
                logger.info(f"Latest timestamps: {latest_timestamps}")
                
            return data, latest_timestamps, latest_id
            
        except Exception as e:
            logger.error(f"Error reading JSONL file: {e}")
            return [], latest_timestamps, latest_id

    def write_jsonl(self, data):
        """Write data to JSONL file."""
        try:
            with open(self.jsonl_file, 'w', encoding='utf-8') as f:
                for record in data:
                    # Ensure created_at is in ISO format
                    if isinstance(record.get('created_at'), datetime):
                        record['created_at'] = record['created_at'].isoformat()
                    # Ensure ID is an integer
                    if 'id' in record:
                        record['id'] = int(record['id'])
                    json.dump(record, f, ensure_ascii=False)
                    f.write('\n')
            logger.info(f"Wrote {len(data)} records to JSONL file")
        except Exception as e:
            logger.error(f"Error writing to JSONL file: {e}")
            raise

    def fetch_twitter_data(self, latest_timestamps):
        """Fetch tweets and likes from cached files."""
        processed_items = []
        if not self.twitter_user_id:
            logger.error("Twitter user ID not set")
            return processed_items

        try:
            # Get the latest timestamps for tweets and likes
            since_time_tweets = latest_timestamps['twitter']
            since_time_likes = latest_timestamps['twitter_like']
            
            logger.info(f"Fetching Twitter tweets since {since_time_tweets.isoformat()}")
            logger.info(f"Fetching Twitter likes since {since_time_likes.isoformat()}")
            
            # Path to cached data directory
            cache_dir = Path(f"data/{self.twitter_user_id}")
            
            # Get latest cached files
            tweet_files = sorted(cache_dir.glob("*_UserTweetsAndReplies.json"), reverse=True)
            like_files = sorted(cache_dir.glob("*_Likes.json"), reverse=True)
            
            # Process tweets
            if tweet_files:
                latest_tweet_file = tweet_files[0]
                logger.info(f"Reading tweets from {latest_tweet_file}")
                with open(latest_tweet_file, 'r', encoding='utf-8') as f:
                    tweet_data = json.load(f)
                    logger.debug(f"Raw tweet data structure: {list(tweet_data.keys())}")
                    
                    if 'data' in tweet_data:
                        for entry in tweet_data['data'].get('user', {}).get('result', {}).get('timeline_v2', {}).get('timeline', {}).get('instructions', []):
                            if entry.get('type') == 'TimelineAddEntries':
                                for tweet_entry in entry.get('entries', []):
                                    try:
                                        logger.debug(f"Processing tweet entry: {json.dumps(tweet_entry.get('content', {}))[:200]}")
                                        
                                        # Extract tweet from the result structure
                                        tweet = None
                                        if 'content' in tweet_entry:
                                            tweet_result = tweet_entry['content'].get('itemContent', {}).get('tweet_results', {}).get('result', {})
                                            if 'legacy' in tweet_result:
                                                tweet = tweet_result['legacy']
                                            elif 'tweet' in tweet_result:
                                                tweet = tweet_result['tweet'].get('legacy', {})
                                        
                                        if not tweet:
                                            logger.warning(f"Could not extract tweet data from entry: {json.dumps(tweet_entry)[:200]}")
                                            continue
                                            
                                        # Extract user info
                                        user_info = tweet.get('user', {})
                                        
                                        # Convert Twitter's timestamp format to datetime
                                        created_at = datetime.strptime(tweet.get('created_at'), '%a %b %d %H:%M:%S %z %Y')
                                        
                                        if created_at > since_time_tweets:
                                            processed_tweet = {
                                                'created_at': created_at.isoformat(),
                                                'url': f"https://twitter.com/i/web/status/{tweet.get('id_str')}",
                                                'source': 'twitter',
                                                'content': tweet.get('full_text', ''),
                                                'metadata': json.dumps({
                                                    'retweet_count': tweet.get('retweet_count'),
                                                    'favorite_count': tweet.get('favorite_count'),
                                                    'reply_count': tweet.get('reply_count'),
                                                    'quote_count': tweet.get('quote_count'),
                                                    'lang': tweet.get('lang'),
                                                    'user': {
                                                        'id': user_info.get('id_str'),
                                                        'screen_name': user_info.get('screen_name'),
                                                        'name': user_info.get('name'),
                                                        'followers_count': user_info.get('followers_count'),
                                                        'following_count': user_info.get('friends_count'),
                                                        'statuses_count': user_info.get('statuses_count'),
                                                        'verified': user_info.get('verified', False)
                                                    }
                                                })
                                            }
                                            processed_items.append(processed_tweet)
                                            logger.info(f"Added tweet: {processed_tweet['content'][:100]}")
                                        else:
                                            logger.info(f"Tweet too old: {created_at.isoformat()} <= {since_time_tweets.isoformat()}")
                                            
                                    except Exception as e:
                                        logger.error(f"Error processing individual tweet: {str(e)}")
                                        logger.error(f"Tweet entry: {json.dumps(tweet_entry)[:200]}")
                                        continue

            # Process likes
            if like_files:
                latest_like_file = like_files[0]
                logger.info(f"Reading likes from {latest_like_file}")
                with open(latest_like_file, 'r', encoding='utf-8') as f:
                    like_data = json.load(f)
                    logger.debug(f"Raw like data structure: {list(like_data.keys())}")
                    
                    if 'data' in like_data:
                        for entry in like_data['data'].get('user', {}).get('result', {}).get('timeline_v2', {}).get('timeline', {}).get('instructions', []):
                            if entry.get('type') == 'TimelineAddEntries':
                                for like_entry in entry.get('entries', []):
                                    try:
                                        logger.debug(f"Processing like entry: {json.dumps(like_entry.get('content', {}))[:200]}")
                                        
                                        # Extract tweet from the result structure
                                        tweet = None
                                        if 'content' in like_entry:
                                            tweet_result = like_entry['content'].get('itemContent', {}).get('tweet_results', {}).get('result', {})
                                            if 'legacy' in tweet_result:
                                                tweet = tweet_result['legacy']
                                            elif 'tweet' in tweet_result:
                                                tweet = tweet_result['tweet'].get('legacy', {})
                                        
                                        if not tweet:
                                            logger.warning(f"Could not extract like data from entry: {json.dumps(like_entry)[:200]}")
                                            continue
                                            
                                        # Extract user info
                                        user_info = tweet.get('user', {})
                                        
                                        # Convert Twitter's timestamp format to datetime
                                        created_at = datetime.strptime(tweet.get('created_at'), '%a %b %d %H:%M:%S %z %Y')
                                        
                                        if created_at > since_time_likes:
                                            processed_like = {
                                                'created_at': created_at.isoformat(),
                                                'url': f"https://twitter.com/i/web/status/{tweet.get('id_str')}",
                                                'source': 'twitter_like',
                                                'content': tweet.get('full_text', ''),
                                                'metadata': json.dumps({
                                                    'retweet_count': tweet.get('retweet_count'),
                                                    'favorite_count': tweet.get('favorite_count'),
                                                    'reply_count': tweet.get('reply_count'),
                                                    'quote_count': tweet.get('quote_count'),
                                                    'lang': tweet.get('lang'),
                                                    'user': {
                                                        'id': user_info.get('id_str'),
                                                        'screen_name': user_info.get('screen_name'),
                                                        'name': user_info.get('name'),
                                                        'followers_count': user_info.get('followers_count'),
                                                        'following_count': user_info.get('friends_count'),
                                                        'statuses_count': user_info.get('statuses_count'),
                                                        'verified': user_info.get('verified', False)
                                                    }
                                                })
                                            }
                                            processed_items.append(processed_like)
                                            logger.info(f"Added like: {processed_like['content'][:100]}")
                                        else:
                                            logger.info(f"Like too old: {created_at.isoformat()} <= {since_time_likes.isoformat()}")
                                            
                                    except Exception as e:
                                        logger.error(f"Error processing individual like: {str(e)}")
                                        logger.error(f"Like entry: {json.dumps(like_entry)[:200]}")
                                        continue
 
            logger.info(f"Processed {len(processed_items)} total items from Twitter")
            return processed_items
            
        except Exception as e:
            logger.error(f"Error processing Twitter data: {e}")
            logger.error(traceback.format_exc())
            return processed_items

    def fetch_github_data(self, since_time):
        """Fetch starred repositories from GitHub API."""
        if not self.github_api:
            return []

        try:
            logger.info("Fetching GitHub data...")
            stars = []
            
            # Get starred repositories with starred_at timestamps
            response = requests.get(
                'https://api.github.com/user/starred',
                headers={
                    'Authorization': f'token {self.github_token}',
                    'Accept': 'application/vnd.github.v3.star+json'  # Required for starred_at field
                },
                params={'sort': 'created', 'direction': 'desc', 'per_page': 100}
            )
            response.raise_for_status()
            starred_data = response.json()
            
            logger.info(f"Found {len(starred_data)} starred repositories")
            
            for item in starred_data:
                try:
                    # Extract repository data and starred_at timestamp
                    repo = item.get('repo')  # The repository data is under 'repo' key
                    starred_at = datetime.strptime(item.get('starred_at'), '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
                    
                    if not repo:
                        logger.warning(f"No repository data found in item: {json.dumps(item)[:200]}")
                        continue
                        
                    # Only include stars newer than the last processed
                    if starred_at > since_time:
                        star_data = {
                            'created_at': starred_at.isoformat(),
                            'url': repo['html_url'],
                            'source': 'github',
                            'content': f"{repo['full_name']}: {repo['description']}" if repo.get('description') else repo['full_name'],
                            'metadata': json.dumps({
                                'language': repo.get('language'),
                                'stars': repo.get('stargazers_count'),
                                'forks': repo.get('forks_count'),
                                'repo_created_at': repo.get('created_at'),
                                'repo_updated_at': repo.get('updated_at'),
                                'repo_pushed_at': repo.get('pushed_at'),
                                'owner': {
                                    'login': repo['owner']['login'],
                                    'type': repo['owner']['type'],
                                    'avatar_url': repo['owner']['avatar_url']
                                }
                            })
                        }
                        stars.append(star_data)
                        logger.info(f"Added star: {star_data['content'][:100]}")
                    else:
                        logger.info(f"Star too old: {starred_at.isoformat()} <= {since_time.isoformat()}")
                        break  # GitHub stars are in chronological order
                        
                except Exception as e:
                    logger.error(f"Error processing starred repo: {str(e)}")
                    logger.error(f"Raw item: {json.dumps(item)}")
                    continue
            
            if not stars:
                logger.info("No new starred repositories to fetch.")
            else:
                logger.info(f"Fetched {len(stars)} new starred repositories")
            
            return stars
            
        except Exception as e:
            logger.error(f"Error fetching GitHub data: {e}")
            logger.error(traceback.format_exc())
            return []

    def fetch_raindrop_data(self, since_time):
        """Fetch bookmarks from Raindrop.io API."""
        if not self.raindrop_headers:
            return []

        try:
            logger.info("Fetching Raindrop.io data...")
            bookmarks = []
            page = 0
            per_page = 50

            while True:
                url = f'https://api.raindrop.io/rest/v1/raindrops/0'
                params = {
                    'page': page,
                    'perpage': per_page,
                    'sort': '-created'
                }

                response = requests.get(url, headers=self.raindrop_headers, params=params)
                response.raise_for_status()
                data = response.json()

                if not data.get('items'):
                    break

                for bookmark in data['items']:
                    # Convert the Z timezone to +00:00 format
                    created_str = bookmark['created'].replace('Z', '+00:00')
                    created_at = datetime.fromisoformat(created_str)
                    
                    # Only include bookmarks newer than the last processed
                    if created_at > since_time:
                        bookmark_data = {
                            'created_at': created_at.isoformat(),
                            'url': bookmark['link'],
                            'source': 'raindrop',
                            'content': bookmark.get('title', ''),
                            'metadata': json.dumps({
                                'folder': bookmark.get('collection', {}).get('title', 'Unsorted'),
                                'tags': bookmark.get('tags', []),
                                'cover': bookmark.get('cover'),
                                'highlights': bookmark.get('highlights', []),
                                'favorite': bookmark.get('favorite', False)
                            })
                        }
                        bookmarks.append(bookmark_data)
                    else:
                        return bookmarks  # We've reached older bookmarks

                if len(data['items']) < per_page:
                    break

                page += 1

            if not bookmarks:
                logger.info("No new bookmarks to fetch.")
            else:
                logger.info(f"Fetched {len(bookmarks)} new bookmarks")
            
            return bookmarks
            
        except Exception as e:
            logger.error(f"Error fetching Raindrop.io data: {e}")
            logger.error(traceback.format_exc())
            return []

    def transform_data(self, new_data, latest_id):
        """Transform and combine data from all sources."""
        transformed_data = []
        current_id = latest_id
        
        for item in new_data:
            current_id += 1
            item['id'] = current_id
            
            # Ensure created_at is in ISO format
            if isinstance(item.get('created_at'), str):
                try:
                    # Parse the string to datetime first
                    dt = datetime.fromisoformat(item['created_at'].replace('Z', '+00:00'))
                    # Convert back to ISO format string
                    item['created_at'] = dt.isoformat()
                except ValueError as e:
                    logger.error(f"Error parsing datetime: {e}")
                    continue
            
            # Normalize metadata
            if 'metadata' in item:
                if isinstance(item['metadata'], str):
                    try:
                        metadata = json.loads(item['metadata'])
                    except json.JSONDecodeError:
                        metadata = {}
                else:
                    metadata = item['metadata']
                
                # Convert numeric values to integers where appropriate
                for key in metadata:
                    if isinstance(metadata[key], float) and metadata[key].is_integer():
                        metadata[key] = int(metadata[key])
                
                # Replace NaN with appropriate empty values
                for key in metadata:
                    if str(metadata[key]) == 'NaN':
                        if key in ['tags', 'highlights']:
                            metadata[key] = []
                        elif key in ['user_id']:
                            metadata[key] = None
                        else:
                            metadata[key] = None
                
                item['metadata'] = json.dumps(metadata)
            
            transformed_data.append(item)
        
        return transformed_data

    def process_twitter_threads(self, data):
        """Process Twitter threads from the fetched data.
        
        This method identifies potential Twitter threads in the data and fetches
        the complete thread data using the TwitterThreadFetcher.
        
        Args:
            data: List of processed bookmark records
            
        Returns:
            List of complete thread records
        """
        try:
            # Import the ThreadProcessor
            from tools.thread_processor import ThreadProcessor
            
            # Initialize the thread processor
            thread_processor = ThreadProcessor(
                twitter_user_id=self.twitter_user_id,
                ct0=self.twitter_ct0,
                auth_token=self.twitter_auth_token
            )
            
            # Process threads
            logger.info("Processing Twitter threads...")
            threads = thread_processor.process_threads(data)
            
            # Add thread records to the data
            if threads:
                logger.info(f"Adding {len(threads)} thread records to data")
                next_id = max([record.get('id', 0) for record in data]) + 1
                
                for thread in threads:
                    # Set the ID for the thread record
                    thread['id'] = next_id
                    next_id += 1
                    
                    # Add the thread record to the data
                    data.append(thread)
            
            return data
        except Exception as e:
            logger.error(f"Error processing Twitter threads: {e}")
            logger.error(traceback.format_exc())
            return data
            
    def process_data(self):
        """Main data processing pipeline."""
        try:
            # Read existing data
            existing_data, latest_timestamps, latest_id = self.read_jsonl()
            
            # Fetch new data from all sources
            new_data = []
            
            # Fetch Twitter data
            twitter_data = self.fetch_twitter_data(latest_timestamps)
            if twitter_data:
                new_data.extend(twitter_data)
            
            # Fetch GitHub data
            github_data = self.fetch_github_data(latest_timestamps['github'])
            if github_data:
                new_data.extend(github_data)
            
            # Fetch Raindrop data
            raindrop_data = self.fetch_raindrop_data(latest_timestamps['raindrop'])
            if raindrop_data:
                new_data.extend(raindrop_data)
            
            if new_data:
                logger.info(f"Found {len(new_data)} new records")
                
                # Transform new data
                logger.info("Transforming data...")
                transformed_data = self.transform_data(new_data, latest_id)
                
                # Combine with existing data
                all_data = existing_data + transformed_data
                
                # Process Twitter threads
                logger.info("Processing Twitter threads...")
                all_data = self.process_twitter_threads(all_data)
                
                # Write combined data
                self.write_jsonl(all_data)
                logger.info(f"Total records after update: {len(all_data)}")
            else:
                logger.info("No new data to transform.")
        except Exception as e:
            logger.error(f"Error processing data: {e}")
            logger.error(traceback.format_exc())
            raise

    def run(self):
        """Main ETL pipeline execution method."""
        try:
            logger.info("Starting Deltaload ETL pipeline...")
            
            # Process data
            self.process_data()
            
            logger.info("Deltaload ETL pipeline completed.")
        except Exception as e:
            logger.error(f"Error in ETL pipeline: {e}")
            logger.error(traceback.format_exc())
            raise

    def save_data(self, data):
        """Save transformed data to JSONL file."""
        try:
            # Create directories if they don't exist
            self.jsonl_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Append new data to JSONL file
            with open(self.jsonl_file, 'a', encoding='utf-8') as f:
                for item in data:
                    f.write(json.dumps(item) + '\n')
            
            logger.info(f"Appended {len(data)} new items to {self.jsonl_file}")
            
        except Exception as e:
            logger.error(f"Error saving data: {e}")
            logger.error(traceback.format_exc())

if __name__ == "__main__":
    etl = DeltaLoadETL()
    etl.run()