"""
Script to fetch latest Twitter data and update local cache files.

Enhanced to support multiple cache directories and backup operations to ensure
continuous data availability across time periods. This script fetches tweet and like
data from the Twitter API and saves it for later processing by the deltaload ETL pipeline.
"""

import os
import json
import logging
import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv
from twitter.scraper import Scraper

# --- Configuration ---
CACHE_BASE_DIR = Path("data")
BACKUP_DIR = Path("data/backup")
# Set the number of tweets/likes to fetch per call (adjustable via command line)
DEFAULT_FETCH_LIMIT = 500 

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("fetch_twitter.log")
    ]
)
logger = logging.getLogger(__name__)

# --- Helper Functions ---
def save_to_cache(user_id: str, data_type: str, raw_data: any, directory=None):
    """
    Saves the raw fetched data (list/dict/etc.) to a timestamped JSON file.
    
    Args:
        user_id (str): Twitter user ID for directory naming
        data_type (str): Type of data being saved ('Likes', 'UserTweetsAndReplies', etc.)
        raw_data (any): The JSON-serializable data to save
        directory (Path, optional): Override the default cache directory
    
    Returns:
        Path: Path to the saved file, or None if save failed
    """
    try:
        # Basic check if data seems empty or problematic
        if not raw_data:
            logger.warning(f"Received empty or None data for {data_type}. Not creating cache file.")
            return None
        
        # Determine where to save the file
        if directory:
            user_cache_dir = directory
        else:
            user_cache_dir = CACHE_BASE_DIR / str(user_id)
            
        user_cache_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{data_type}.json"
        filepath = user_cache_dir / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            # Attempt to dump whatever the scraper returned
            json.dump(raw_data, f, ensure_ascii=False, indent=2) 
        logger.info(f"Successfully saved raw {data_type} data to {filepath}")
        logger.info(f"Raw data type saved was: {type(raw_data)}")
        
        return filepath
        
    except TypeError as te:
         logger.error(f"TypeError saving {data_type} data to cache: {te}. Data might not be JSON serializable.")
         # Log sample if possible
         try:
             logger.debug(f"Problematic data sample (first 500 chars): {str(raw_data)[:500]}")
         except: pass
         return None
    except Exception as e:
        logger.error(f"Error saving raw {data_type} data to cache: {e}")
        return None

def backup_cache_files(user_id: str, backup_dir=BACKUP_DIR):
    """
    Copies the most recent cache files to a backup directory.
    
    Args:
        user_id (str): Twitter user ID for directory naming
        backup_dir (Path): Backup directory path
    """
    try:
        source_dir = CACHE_BASE_DIR / str(user_id)
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        if not source_dir.exists():
            logger.warning(f"Source directory {source_dir} does not exist. Nothing to backup.")
            return
            
        # Find the most recent tweet and like files
        tweet_files = sorted(source_dir.glob("*_UserTweetsAndReplies.json"), reverse=True)
        like_files = sorted(source_dir.glob("*_Likes.json"), reverse=True)
        
        files_to_backup = []
        if tweet_files:
            files_to_backup.append(tweet_files[0])  # Most recent
        if like_files:
            files_to_backup.append(like_files[0])  # Most recent
            
        if not files_to_backup:
            logger.warning(f"No files found to backup in {source_dir}")
            return
            
        # Copy the files to the backup directory
        for src_file in files_to_backup:
            dest_file = backup_dir / src_file.name
            shutil.copy2(src_file, dest_file)
            logger.info(f"Backed up {src_file} to {dest_file}")
            
        logger.info(f"Successfully backed up {len(files_to_backup)} files to {backup_dir}")
        
    except Exception as e:
        logger.error(f"Error backing up cache files: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Fetch and cache Twitter data.")
    parser.add_argument("--limit", "-l", type=int, default=DEFAULT_FETCH_LIMIT,
                       help=f"Number of items to fetch (default: {DEFAULT_FETCH_LIMIT})")
    parser.add_argument("--backup", "-b", action="store_true",
                       help="Create backup copies of the most recent cache files")
    parser.add_argument("--backup-only", action="store_true",
                       help="Only create backups, don't fetch new data")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Enable verbose logging")
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
        
    fetch_limit = args.limit
    
    logger.info(f"Starting Twitter cache update script (fetch_limit={fetch_limit}, backup={args.backup})")
    
    # 1. Load Environment Variables
    try:
        load_dotenv()
        twitter_user_id = os.getenv('TWITTER_USER_ID')
        twitter_ct0 = os.getenv('TWITTER_CT0')
        twitter_auth_token = os.getenv('TWITTER_AUTH_TOKEN')

        if not all([twitter_user_id, twitter_ct0, twitter_auth_token]):
            raise ValueError("Missing required Twitter environment variables (TWITTER_USER_ID, TWITTER_CT0, TWITTER_AUTH_TOKEN)")
        logger.info(f"Loaded environment variables for user ID: {twitter_user_id}")
    except Exception as e:
        logger.error(f"Failed to load environment variables: {e}")
        exit(1)
    
    # If backup-only flag is set, just backup and exit
    if args.backup_only:
        logger.info("Running in backup-only mode")
        backup_cache_files(twitter_user_id)
        logger.info("Backup-only operation completed")
        exit(0)

    # 2. Initialize Scraper
    try:
        twitter_api = Scraper(
            cookies={
                'ct0': twitter_ct0,
                'auth_token': twitter_auth_token
            }
        )
        logger.info("Twitter scraper initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize Twitter scraper: {e}")
        exit(1)

    # 3. Fetch Tweets and Replies
    try:
        logger.info(f"Fetching latest {fetch_limit} tweets and replies for user {twitter_user_id}...")
        # Get the raw output from the scraper
        tweets_raw_data = twitter_api.tweets_and_replies([twitter_user_id], limit=fetch_limit)
        
        # Pass the raw data directly to the saver
        save_to_cache(twitter_user_id, "UserTweetsAndReplies", tweets_raw_data) 
            
    except Exception as e:
        logger.error(f"Failed to fetch tweets and replies: {e}")
        # Continue to likes even if tweets fail

    # 4. Fetch Likes
    try:
        logger.info(f"Fetching latest {fetch_limit} likes for user {twitter_user_id}...")
        # Get the raw output from the scraper
        likes_raw_data = twitter_api.likes([twitter_user_id], limit=fetch_limit)
        
        # Pass the raw data directly to the saver
        save_to_cache(twitter_user_id, "Likes", likes_raw_data)

    except Exception as e:
        logger.error(f"Failed to fetch likes: {e}")
    
    # 5. Create backup if requested
    if args.backup:
        logger.info("Creating backup of cache files...")
        backup_cache_files(twitter_user_id)

    logger.info("Twitter cache update script finished.")