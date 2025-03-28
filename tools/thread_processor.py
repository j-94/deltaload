"""Twitter Thread Processor module.

This module handles the processing of Twitter threads.
It integrates with the DeltaLoadETL pipeline to fetch and process complete
Twitter threads from bookmarked tweets.
"""

import os
import json
import logging
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from collections import defaultdict
import pandas as pd
from .twitter_thread_fetcher import TwitterThreadFetcher

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class ThreadProcessor:
    """A class for identifying and processing Twitter threads.
    
    This class handles the identification of potential Twitter threads in the
    bookmark data and the fetching of complete thread data using the 
    TwitterThreadFetcher.
    """
    
    def __init__(self, twitter_user_id=None, ct0=None, auth_token=None):
        """Initialize with Twitter API credentials.
        
        Args:
            twitter_user_id: Twitter user ID (from env variables if not provided)
            ct0: Twitter ct0 cookie (from env variables if not provided)
            auth_token: Twitter auth token (from env variables if not provided)
        """
        self.twitter_user_id = twitter_user_id or os.getenv("TWITTER_USER_ID")
        self.ct0 = ct0 or os.getenv("TWITTER_CT0")
        self.auth_token = auth_token or os.getenv("TWITTER_AUTH_TOKEN")
        
        # Initialize the thread fetcher
        self.thread_fetcher = TwitterThreadFetcher(
            user_id=self.twitter_user_id,
            ct0=self.ct0,
            auth_token=self.auth_token
        )
    
    def find_potential_threads(self, bookmarks: List[Dict]) -> List[List[Dict]]:
        """Find potential threads in bookmark data.
        
        Strategy:
        1. Group tweets by author
        2. Find tweets that are close in time (within 60 minutes)
        3. Return groups of 2+ tweets that might be threads
        
        Args:
            bookmarks: List of bookmark records
            
        Returns:
            List of potential thread groups (each group is a list of bookmark records)
        """
        logger.info("Finding potential Twitter threads...")
        
        # Convert to DataFrame for easier manipulation
        df = pd.DataFrame(bookmarks)
        
        # Filter to Twitter data only
        twitter_df = df[df['source'].isin(['twitter', 'twitter_like'])].copy()
        logger.info(f"Found {len(twitter_df)} Twitter bookmarks to process")
        
        # Parse metadata if it's a string
        def parse_metadata(metadata):
            if isinstance(metadata, str):
                try:
                    return json.loads(metadata)
                except json.JSONDecodeError:
                    return {}
            return metadata or {}
        
        twitter_df['parsed_metadata'] = twitter_df['metadata'].apply(parse_metadata)
        
        # Convert dates to datetime
        twitter_df['created_at'] = pd.to_datetime(twitter_df['created_at'], errors='coerce')
        
        # Remove any rows with null created_at (they can't be part of a thread)
        twitter_df = twitter_df.dropna(subset=['created_at'])
        logger.info(f"Found {len(twitter_df)} Twitter bookmarks with valid dates")
        
        # Group tweets by author
        author_tweets = defaultdict(list)
        
        for idx, row in twitter_df.iterrows():
            # Get author from metadata
            metadata = row.get('parsed_metadata', {})
            author = metadata.get('username')
            
            if author:
                author_tweets[author].append(idx)
        
        # Find potential threads
        potential_threads = []
        
        for author, tweet_indices in author_tweets.items():
            if len(tweet_indices) < 2:
                continue
                
            # Get tweets for this author
            author_df = twitter_df.loc[tweet_indices].copy()
            
            # Sort by time
            author_df = author_df.sort_values('created_at')
            
            # Find sequences of tweets that are close in time
            current_thread = []
            
            for i, (idx, row) in enumerate(author_df.iterrows()):
                if not current_thread:
                    current_thread = [row.to_dict()]
                    continue
                    
                last_tweet = current_thread[-1]
                last_tweet_time = pd.to_datetime(last_tweet['created_at'])
                current_tweet_time = pd.to_datetime(row['created_at'])
                time_diff = (current_tweet_time - last_tweet_time).total_seconds() / 60
                
                if time_diff <= 60:  # 60 minutes threshold
                    current_thread.append(row.to_dict())
                else:
                    # If this group has at least 2 tweets, save it
                    if len(current_thread) >= 2:
                        potential_threads.append(current_thread)
                    current_thread = [row.to_dict()]
            
            # Don't forget the last group
            if len(current_thread) >= 2:
                potential_threads.append(current_thread)
        
        logger.info(f"Found {len(potential_threads)} potential Twitter threads")
        return potential_threads
    
    def fetch_complete_threads(self, potential_threads: List[List[Dict]]) -> List[Dict]:
        """Fetch complete threads using the TwitterThreadFetcher.
        
        Args:
            potential_threads: List of potential thread groups
            
        Returns:
            List of complete thread data
        """
        logger.info(f"Fetching complete data for {len(potential_threads)} potential threads...")
        fetched_threads = []
        
        for thread_group in potential_threads:
            # Get the first tweet URL (which we'll use to fetch the complete thread)
            first_tweet = thread_group[0]
            tweet_url = first_tweet.get('url')
            
            if not tweet_url:
                logger.warning(f"No URL found for tweet: {first_tweet}")
                continue
            
            # Extract tweet ID from URL
            tweet_id = self.thread_fetcher.extract_tweet_id_from_url(tweet_url)
            
            if not tweet_id:
                logger.warning(f"Could not extract tweet ID from URL: {tweet_url}")
                continue
            
            # Fetch complete thread
            logger.info(f"Fetching complete thread for tweet ID: {tweet_id}")
            thread_data = self.thread_fetcher.process_url(tweet_url)
            
            if thread_data.get('status') != 'success':
                logger.warning(f"Failed to fetch thread for tweet ID: {tweet_id}")
                continue
            
            fetched_threads.append(thread_data)
            logger.info(f"Successfully fetched thread with {thread_data['metadata']['tweet_count']} tweets")
        
        logger.info(f"Successfully fetched {len(fetched_threads)} complete threads")
        return fetched_threads
    
    def process_threads(self, bookmarks: List[Dict]) -> List[Dict]:
        """Process Twitter threads in bookmark data.
        
        This method:
        1. Identifies potential threads
        2. Fetches complete thread data
        3. Returns the complete thread data
        
        Args:
            bookmarks: List of bookmark records
            
        Returns:
            List of complete thread records
        """
        # Find potential threads
        potential_threads = self.find_potential_threads(bookmarks)
        
        # Fetch complete threads
        threads = self.fetch_complete_threads(potential_threads)
        
        return threads

# Example usage if run as a script
if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    # Load bookmarks from JSONL file
    def load_jsonl(filename):
        data = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError:
                    logger.error(f"Error parsing line: {line[:100]}...")
        return data
    
    # Path to the bookmark data
    bookmarks_path = Path("../data-bookmark.jsonl")
    
    if not bookmarks_path.exists():
        logger.error(f"Bookmark data file not found: {bookmarks_path}")
        sys.exit(1)
    
    # Load bookmarks
    logger.info(f"Loading bookmarks from {bookmarks_path}...")
    bookmarks = load_jsonl(bookmarks_path)
    logger.info(f"Loaded {len(bookmarks)} bookmarks")
    
    # Process threads
    processor = ThreadProcessor()
    threads = processor.process_threads(bookmarks)
    
    # Output results
    output_file = Path("thread_data.jsonl")
    with open(output_file, 'w', encoding='utf-8') as f:
        for thread in threads:
            json.dump(thread, f, ensure_ascii=False)
            f.write('\n')
    
    logger.info(f"Saved {len(threads)} threads to {output_file}")