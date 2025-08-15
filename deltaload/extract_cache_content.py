#!/usr/bin/env python3
"""
Extract original tweet content from cache for retweets.

This script:
1. Identifies retweets in the enriched dataset
2. Searches for the original tweet content in the processed_tweets cache directory
3. Updates the content field with the original tweet text without any added text
"""

import os
import json
import re
import glob
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("extract_cache_content.log")
    ]
)
logger = logging.getLogger(__name__)

def extract_tweet_id(url: str) -> Optional[str]:
    """Extract the tweet ID from a Twitter URL."""
    if not url:
        return None
        
    # Handle twitter.com, x.com URLs
    if '/status/' in url:
        parts = url.split('/status/')
        if len(parts) < 2:
            return None
            
        # Take the first segment after status (the ID)
        tweet_id = parts[1].split('/')[0]
        
        # Remove any query parameters
        tweet_id = tweet_id.split('?')[0]
        
        # Validate that we have a numeric ID
        if tweet_id.isdigit():
            return tweet_id
    
    return None

def is_retweet(content: str) -> bool:
    """Check if content is a retweet based on RT @username pattern."""
    return content.strip().startswith("RT @")

def extract_retweet_info(content: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """
    Extract retweet information from content.
    
    Returns:
        Tuple of (is_retweet, original_author, original_content)
    """
    # Pattern to match "RT @username: content"
    rt_pattern = r'^RT @([a-zA-Z0-9_]+):\s+(.*)'
    match = re.match(rt_pattern, content, re.DOTALL)
    
    if match:
        original_author = match.group(1)
        original_content = match.group(2)
        return True, original_author, original_content
    
    return False, None, None

def find_processed_tweet(tweet_id: str, processed_dir: str = "data/processed_tweets") -> Optional[Dict]:
    """Find a processed tweet by ID in the processed_tweets directory."""
    try:
        # Look for matching filename patterns
        matching_files = glob.glob(f"{processed_dir}/{tweet_id}_*.json")
        
        if matching_files:
            with open(matching_files[0], 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
                
        # If no direct match, search through all files
        for file_path in Path(processed_dir).glob("*.json"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Check metadata for the tweet ID
                    if data.get('metadata', {}).get('thread_id') == tweet_id:
                        return data
                    # Check tweets array for the ID
                    for tweet in data.get('metadata', {}).get('tweets', []):
                        if tweet.get('id') == tweet_id:
                            return data
            except Exception as e:
                logger.warning(f"Error reading file {file_path}: {str(e)}")
                continue
    except Exception as e:
        logger.error(f"Error searching for processed tweet: {str(e)}")
    
    return None

def extract_content_from_processed_tweet(data: Dict, is_original_retweet: bool = False) -> Optional[str]:
    """
    Extract the content from a processed tweet.
    
    Args:
        data: The processed tweet data
        is_original_retweet: Whether this is originally a retweet
        
    Returns:
        The content from the processed tweet or None
    """
    if not data:
        return None
    
    # First try to get content directly
    content = data.get('content')
    
    # If it's originally a retweet and we have content, extract the original content
    if is_original_retweet and content and content.strip().startswith("RT @"):
        _, _, original_content = extract_retweet_info(content)
        if original_content:
            return original_content
    elif content:
        return content
    
    # If no content, try to get from tweets array
    for tweet in data.get('metadata', {}).get('tweets', []):
        if 'text' in tweet:
            text = tweet.get('text')
            # If the text is a retweet, extract the original content
            if is_original_retweet and text and text.strip().startswith("RT @"):
                _, _, original_content = extract_retweet_info(text)
                if original_content:
                    return original_content
            else:
                return text
    
    return None

def process_enriched_dataset(input_file: str, output_file: str, processed_dir: str = "data/processed_tweets"):
    """Process the enriched dataset to update retweet content from cache."""
    try:
        # Count statistics
        total_bookmarks = 0
        twitter_bookmarks = 0
        retweets = 0
        fixed_retweets = 0
        skipped_retweets = 0
        
        # Process the input file
        with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                total_bookmarks += 1
                try:
                    bookmark = json.loads(line.strip())
                    
                    # Only process Twitter bookmarks
                    if 'twitter' in bookmark.get('source', '').lower():
                        twitter_bookmarks += 1
                        content = bookmark.get('content', '')
                        
                        # Check if this is a retweet
                        if is_retweet(content):
                            retweets += 1
                            
                            # Try to extract the tweet ID from the URL
                            url = bookmark.get('url', '')
                            tweet_id = extract_tweet_id(url)
                            
                            if tweet_id:
                                # Try to find the processed tweet in cache
                                processed_tweet = find_processed_tweet(tweet_id, processed_dir)
                                
                                if processed_tweet:
                                    # Extract content from the processed tweet
                                    original_content = extract_content_from_processed_tweet(processed_tweet, is_original_retweet=True)
                                    
                                    if original_content:
                                        # Update the bookmark content with just the original content
                                        bookmark['content'] = original_content
                                        
                                        # Update metadata to track the fix
                                        if 'metadata' not in bookmark:
                                            bookmark['metadata'] = {}
                                        bookmark['metadata']['retweet_fixed'] = True
                                        bookmark['metadata']['retweet_fixed_at'] = datetime.now().isoformat()
                                        
                                        fixed_retweets += 1
                                        logger.info(f"Fixed retweet {total_bookmarks}: {url}")
                                    else:
                                        skipped_retweets += 1
                                        logger.warning(f"Could not extract content from processed tweet: {url}")
                                else:
                                    skipped_retweets += 1
                                    logger.warning(f"Could not find processed tweet in cache: {url}")
                            else:
                                skipped_retweets += 1
                                logger.warning(f"Could not extract tweet ID from URL: {url}")
                
                    # Write the bookmark to output file
                    f_out.write(json.dumps(bookmark, ensure_ascii=False) + '\n')
                    
                except json.JSONDecodeError as e:
                    logger.error(f"Error parsing JSON: {str(e)}")
                    # Write the original line to output file
                    f_out.write(line)
                except Exception as e:
                    logger.error(f"Error processing bookmark: {str(e)}")
                    # Write the original line to output file
                    f_out.write(line)
        
        # Log statistics
        logger.info(f"Processing complete:")
        logger.info(f"Total bookmarks: {total_bookmarks}")
        logger.info(f"Twitter bookmarks: {twitter_bookmarks}")
        logger.info(f"Retweets: {retweets}")
        logger.info(f"Fixed retweets: {fixed_retweets}")
        logger.info(f"Skipped retweets: {skipped_retweets}")
        
        return True
    except Exception as e:
        logger.error(f"Error processing enriched dataset: {str(e)}")
        return False

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract original tweet content from cache for retweets")
    parser.add_argument('--input', '-i', default="enriched/data-bookmark-enriched-full.jsonl",
                      help="Input JSONL file (default: enriched/data-bookmark-enriched-full.jsonl)")
    parser.add_argument('--output', '-o', default="enriched/data-bookmark-enriched-fixed-cache.jsonl",
                      help="Output JSONL file (default: enriched/data-bookmark-enriched-fixed-cache.jsonl)")
    parser.add_argument('--processed-dir', '-p', default="data/processed_tweets",
                      help="Directory containing processed tweets (default: data/processed_tweets)")
    
    args = parser.parse_args()
    
    # Create backup of input file
    if os.path.exists(args.input):
        import shutil
        backup_file = f"{args.input}.bak"
        if not os.path.exists(backup_file):
            shutil.copy2(args.input, backup_file)
            logger.info(f"Created backup of input file at {backup_file}")
    
    # Process the enriched dataset
    success = process_enriched_dataset(args.input, args.output, args.processed_dir)
    
    if success:
        logger.info(f"Successfully processed enriched dataset")
        logger.info(f"Output file: {args.output}")
    else:
        logger.error(f"Failed to process enriched dataset")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())