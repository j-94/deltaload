#!/usr/bin/env python3
"""
Script to fetch complete threads from our bookmark data.
This script identifies potential tweet threads in our bookmarks and fetches
the complete threads using the TwitterThreadFetcher.
"""

import os
import sys
import json
import pandas as pd
from datetime import datetime, timedelta
from collections import defaultdict
import logging

# Add deltaload directory to path so we can import TwitterThreadFetcher
sys.path.append('/Users/imac/Desktop/ETL/deltaload')
from tools.twitter_thread_fetcher import TwitterThreadFetcher

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("thread_fetching.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Path to the bookmark data
bookmarks_path = '/Users/imac/Desktop/ETL/deltaload/data-bookmark.jsonl'
output_dir = 'fetched_threads'

def load_jsonl(filename):
    """Load data from JSONL file."""
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                logger.error(f"Error parsing line: {line[:100]}...")
    return data

def parse_metadata(metadata_str):
    """Parse metadata from string or dict."""
    try:
        if isinstance(metadata_str, str):
            return json.loads(metadata_str)
        elif isinstance(metadata_str, dict):
            return metadata_str
        else:
            return {}
    except (json.JSONDecodeError, TypeError):
        return {}

def find_potential_threads(df):
    """Find potential threads in our bookmark data.
    
    Strategy:
    1. Group tweets by author
    2. Find tweets that are close in time (within 60 minutes)
    3. Return groups of 2+ tweets that might be threads
    """
    # Group tweets by author
    author_tweets = defaultdict(list)
    
    for idx, row in df.iterrows():
        # Get author from metadata
        metadata = row.get('parsed_metadata', {})
        author = metadata.get('username', None)
        
        if author:
            author_tweets[author].append(idx)
    
    # Find potential threads
    potential_threads = []
    
    for author, tweet_ids in author_tweets.items():
        if len(tweet_ids) < 2:
            continue
            
        # Get tweets for this author
        author_df = df.loc[tweet_ids].copy()
        
        # Sort by time
        author_df = author_df.sort_values('created_at')
        
        # Find sequences of tweets that are close in time
        current_thread = []
        
        for i, (idx, row) in enumerate(author_df.iterrows()):
            if not current_thread:
                current_thread = [idx]
                continue
                
            last_tweet = df.loc[current_thread[-1]]
            time_diff = (row['created_at'] - last_tweet['created_at']).total_seconds() / 60
            
            if time_diff <= 60:  # 60 minutes threshold
                current_thread.append(idx)
            else:
                # If this group has at least 2 tweets, save it
                if len(current_thread) >= 2:
                    potential_threads.append(current_thread)
                current_thread = [idx]
        
        # Don't forget the last group
        if len(current_thread) >= 2:
            potential_threads.append(current_thread)
    
    return potential_threads

def fetch_complete_threads(df, potential_threads, fetcher):
    """Fetch complete threads using the TwitterThreadFetcher."""
    complete_threads = []
    
    for thread_indices in potential_threads:
        try:
            # Get the first tweet in the thread
            first_tweet = df.loc[thread_indices[0]]
            
            # Extract tweet ID from URL
            tweet_id = fetcher.extract_tweet_id_from_url(first_tweet['url'])
            
            if not tweet_id:
                logger.warning(f"Could not extract tweet ID from URL: {first_tweet['url']}")
                continue
            
            # Fetch complete thread
            logger.info(f"Fetching complete thread for tweet ID: {tweet_id} (mock mode)")
            thread_data = fetcher.process_url(first_tweet['url'], mock_data=True)
            
            if thread_data.get('status') != 'success':
                logger.warning(f"Failed to fetch thread for tweet ID: {tweet_id}")
                continue
            
            complete_threads.append(thread_data)
            
            # Save thread to file
            output_file = os.path.join(output_dir, f"thread_{tweet_id}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(thread_data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Saved thread with {thread_data['metadata']['tweet_count']} tweets to {output_file}")
        except Exception as e:
            logger.error(f"Error processing thread: {str(e)}")
    
    return complete_threads

def create_thread_summary(complete_threads):
    """Create a summary markdown file of all fetched threads."""
    output_file = os.path.join(output_dir, "thread_summary.md")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Twitter Thread Summary\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total threads: {len(complete_threads)}\n\n")
        
        # Sort threads by length (largest first)
        sorted_threads = sorted(complete_threads, 
                               key=lambda t: t['metadata']['tweet_count'],
                               reverse=True)
        
        for i, thread in enumerate(sorted_threads):
            metadata = thread['metadata']
            f.write(f"## Thread #{i+1}: {metadata['tweet_count']} tweets by @{metadata['author']['screen_name']}\n\n")
            
            # Write thread information
            f.write(f"**First tweet time:** {thread['created_at']}\n")
            f.write(f"**Thread ID:** {metadata['thread_id']}\n")
            f.write(f"**URL:** {thread['url']}\n")
            f.write(f"**Author followers:** {metadata['author']['followers_count']}\n\n")
            
            # Write thread content
            f.write(f"### Content\n\n")
            f.write(f"```\n{thread['content']}\n```\n\n")
            f.write(f"---\n\n")
    
    logger.info(f"Created thread summary at {output_file}")

def main():
    """Main function."""
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Initialize TwitterThreadFetcher in mock mode
    logger.info("Initializing TwitterThreadFetcher in mock mode...")
    fetcher = TwitterThreadFetcher(use_env=False)
    
    # Load bookmarks
    logger.info(f"Loading bookmarks from {bookmarks_path}...")
    bookmarks = load_jsonl(bookmarks_path)
    logger.info(f"Loaded {len(bookmarks)} bookmarks")
    
    # Convert to DataFrame
    df = pd.DataFrame(bookmarks)
    
    # Filter to Twitter data
    twitter_df = df[df['source'].isin(['twitter', 'twitter_like'])].copy()
    logger.info(f"Found {len(twitter_df)} Twitter bookmarks")
    
    # Parse metadata
    twitter_df['parsed_metadata'] = twitter_df['metadata'].apply(parse_metadata)
    
    # Convert dates to datetime
    twitter_df['created_at'] = pd.to_datetime(twitter_df['created_at'], errors='coerce')
    
    # Remove any rows with null created_at (they can't be part of a thread)
    twitter_df = twitter_df.dropna(subset=['created_at'])
    logger.info(f"Found {len(twitter_df)} Twitter bookmarks with valid dates")
    
    # Find potential threads
    logger.info("Finding potential threads...")
    potential_threads = find_potential_threads(twitter_df)
    logger.info(f"Found {len(potential_threads)} potential threads")
    
    # Fetch complete threads
    logger.info("Fetching complete threads...")
    complete_threads = fetch_complete_threads(twitter_df, potential_threads, fetcher)
    logger.info(f"Successfully fetched {len(complete_threads)} complete threads")
    
    # Create thread summary
    create_thread_summary(complete_threads)
    
    logger.info("Done!")

if __name__ == "__main__":
    main()