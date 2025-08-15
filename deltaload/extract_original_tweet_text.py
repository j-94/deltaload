#!/usr/bin/env python3
"""
Extract original tweet text from retweets in processed tweets
and update content field in enriched dataset.

This script:
1. Identifies retweets in the enriched dataset
2. Extracts the original tweet text from processed_tweets cache
3. Updates the content field to contain the original tweet text instead of "RT @username: ..."
"""

import os
import json
import re
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
        logging.FileHandler("extract_original_tweet_text.log")
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
    return content.startswith("RT @")

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
    for file_path in Path(processed_dir).glob("*_*.json"):
        try:
            if tweet_id in file_path.name:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data
            else:
                # Try to load the file and check if it contains the tweet
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data.get('metadata', {}).get('thread_id') == tweet_id:
                        return data
                    # Check tweets array
                    for tweet in data.get('metadata', {}).get('tweets', []):
                        if tweet.get('id') == tweet_id:
                            return data
        except Exception as e:
            logger.warning(f"Error reading file {file_path}: {str(e)}")
    return None

def extract_original_text_from_processed_tweet(data: Dict) -> Optional[str]:
    """Extract the original text from a processed tweet."""
    if not data:
        return None
    
    # Get the original text from the retweet
    # First try to get it from the tweets array in metadata
    for tweet in data.get('metadata', {}).get('tweets', []):
        if 'text' in tweet:
            # Check if this is a retweet
            if is_retweet(tweet['text']):
                _, _, original_content = extract_retweet_info(tweet['text'])
                return original_content
            return tweet['text']
    
    # Fallback to content field
    content = data.get('content')
    if content:
        if is_retweet(content):
            _, _, original_content = extract_retweet_info(content)
            return original_content
        return content
    
    return None

def process_enriched_dataset(input_file: str, output_file: str, processed_dir: str = "data/processed_tweets"):
    """Process the enriched dataset to update retweet content with original text."""
    try:
        # Count statistics
        total_bookmarks = 0
        twitter_bookmarks = 0
        retweets = 0
        fixed_retweets = 0
        
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
                            # Extract tweet ID from URL
                            url = bookmark.get('url', '')
                            tweet_id = extract_tweet_id(url)
                            
                            if tweet_id:
                                # Find processed tweet
                                processed_tweet = find_processed_tweet(tweet_id, processed_dir)
                                
                                if processed_tweet:
                                    # Extract original text
                                    original_text = extract_original_text_from_processed_tweet(processed_tweet)
                                    
                                    if original_text:
                                        # Extract original author for better formatting
                                        _, original_author, _ = extract_retweet_info(content)
                                        
                                        # Update content field with better formatting
                                        if original_author:
                                            bookmark['content'] = f"Original Tweet by @{original_author}: {original_text}"
                                        else:
                                            bookmark['content'] = original_text
                                        
                                        # Add metadata
                                        if 'metadata' not in bookmark:
                                            bookmark['metadata'] = {}
                                        bookmark['metadata']['retweet_fixed'] = True
                                        bookmark['metadata']['retweet_fixed_at'] = datetime.now().isoformat()
                                        
                                        fixed_retweets += 1
                                        logger.info(f"Fixed retweet: {tweet_id}")
                
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
        
        return True
    except Exception as e:
        logger.error(f"Error processing enriched dataset: {str(e)}")
        return False

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract original tweet text from retweets")
    parser.add_argument('--input', '-i', default="enriched/data-bookmark-enriched-full.jsonl",
                      help="Input JSONL file (default: enriched/data-bookmark-enriched-full.jsonl)")
    parser.add_argument('--output', '-o', default="enriched/data-bookmark-enriched-fixed.jsonl",
                      help="Output JSONL file (default: enriched/data-bookmark-enriched-fixed.jsonl)")
    parser.add_argument('--processed-dir', '-p', default="data/processed_tweets",
                      help="Directory containing processed tweets (default: data/processed_tweets)")
    
    args = parser.parse_args()
    
    # Create backup of input file
    if os.path.exists(args.input):
        import shutil
        backup_file = f"{args.input}.bak"
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