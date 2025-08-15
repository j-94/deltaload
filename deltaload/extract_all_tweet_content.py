#!/usr/bin/env python3
"""
Extract original tweet content using a hybrid approach:
1. First check specific user cache files for most recent tweets
2. Then look in processed_tweets cache for older tweets
3. Finally fall back to direct extraction from the RT pattern if needed

This script ensures we get the best quality content for all retweets.
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
        logging.FileHandler("extract_all_tweet_content.log")
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

def search_tweet_in_user_cache(tweet_id: str) -> Optional[str]:
    """
    Search for a tweet in the user's cache files.
    
    Args:
        tweet_id: The ID of the tweet to find
        
    Returns:
        The original content if found, None otherwise
    """
    user_cache_files = [
        "data/1169726235817185281/20250414_193611_UserTweetsAndReplies.json",
        "data/1169726235817185281/20250414_193615_Likes.json",
        "data/backup/UserTweetsAndReplies.json"
    ]
    
    for cache_file in user_cache_files:
        if not os.path.exists(cache_file):
            continue
            
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Handle different cache file formats
                if isinstance(data, list):
                    # UserTweetsAndReplies.json format
                    for item in data:
                        if 'data' in item and 'user' in item.get('data', {}):
                            try:
                                timeline = item['data']['user']['result']['timeline_v2']['timeline']
                                for instruction in timeline.get('instructions', []):
                                    if instruction['type'] == 'TimelineAddEntries':
                                        for entry in instruction.get('entries', []):
                                            if 'entryId' in entry and f"tweet-{tweet_id}" in entry.get('entryId', ''):
                                                # Found the tweet
                                                tweet_content = None
                                                try:
                                                    item_content = entry.get('content', {}).get('itemContent', {})
                                                    tweet_result = item_content.get('tweet_results', {}).get('result', {})
                                                    
                                                    # Try to get the text
                                                    if 'legacy' in tweet_result:
                                                        tweet_content = tweet_result['legacy'].get('full_text', '')
                                                    elif 'note_tweet' in tweet_result:
                                                        note_tweet = tweet_result['note_tweet']['note_tweet_results']['result']
                                                        tweet_content = note_tweet.get('text', '')
                                                        
                                                    # If it's a retweet, extract the original content
                                                    if tweet_content and is_retweet(tweet_content):
                                                        _, _, original_content = extract_retweet_info(tweet_content)
                                                        if original_content:
                                                            return original_content
                                                    elif tweet_content:
                                                        return tweet_content
                                                except Exception as e:
                                                    logger.warning(f"Error extracting content from entry: {e}")
                            except Exception as e:
                                logger.warning(f"Error processing timeline in {cache_file}: {e}")
                
                # Handle backup/UserTweetsAndReplies.json format
                elif 'window.YTD.tweets.part0' in cache_file:
                    try:
                        # This is a YTD data format
                        tweets = data
                        for tweet_data in tweets:
                            if 'tweet' in tweet_data and tweet_data['tweet'].get('id_str') == tweet_id:
                                full_text = tweet_data['tweet'].get('full_text', '')
                                if full_text and is_retweet(full_text):
                                    _, _, original_content = extract_retweet_info(full_text)
                                    if original_content:
                                        return original_content
                                elif full_text:
                                    return full_text
                    except Exception as e:
                        logger.warning(f"Error processing YTD data in {cache_file}: {e}")
        
        except Exception as e:
            logger.warning(f"Error reading {cache_file}: {e}")
            
    return None

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

def hybrid_fix_retweet_content(bookmark: Dict, processed_dir: str = "data/processed_tweets") -> Dict:
    """
    Fix a retweet using a hybrid approach:
    1. First check user cache files for most recent tweets
    2. Then check processed_tweets directory
    3. Finally fall back to direct extraction
    
    Args:
        bookmark: The bookmark to fix
        processed_dir: Directory containing processed tweets
        
    Returns:
        The fixed bookmark
    """
    # Only process Twitter bookmarks
    source = bookmark.get('source', '')
    if 'twitter' not in source.lower():
        return bookmark
    
    # Get the content
    content = bookmark.get('content', '')
    
    # Skip if no content
    if not content:
        return bookmark
    
    # Check if this is a retweet
    if not is_retweet(content):
        return bookmark
        
    original_content = None
    method = None
    
    # Extract tweet ID from URL
    url = bookmark.get('url', '')
    tweet_id = extract_tweet_id(url)
    
    if not tweet_id:
        # If we can't get the tweet ID, use direct extraction
        _, _, direct_content = extract_retweet_info(content)
        if direct_content:
            original_content = direct_content
            method = "direct"
    else:
        # First try the user's cache files (most recent tweets)
        user_cache_content = search_tweet_in_user_cache(tweet_id)
        if user_cache_content:
            original_content = user_cache_content
            method = "user_cache"
        else:
            # Try processed_tweets cache
            processed_tweet = find_processed_tweet(tweet_id, processed_dir)
            if processed_tweet:
                processed_content = extract_content_from_processed_tweet(processed_tweet, is_original_retweet=True)
                if processed_content:
                    original_content = processed_content
                    method = "processed_cache"
            
            # If still no content, fall back to direct extraction
            if not original_content:
                _, _, direct_content = extract_retweet_info(content)
                if direct_content:
                    original_content = direct_content
                    method = "direct"
    
    # Update the bookmark if we found original content
    if original_content:
        # Update content with the original content
        bookmark['content'] = original_content
        
        # Update metadata
        if 'metadata' not in bookmark:
            bookmark['metadata'] = {}
        
        bookmark['metadata']['retweet_fixed'] = True
        bookmark['metadata']['fix_method'] = method
        bookmark['metadata']['retweet_fixed_at'] = datetime.now().isoformat()
        
        # Extract original author for metadata
        _, original_author, _ = extract_retweet_info(content)
        if original_author:
            bookmark['metadata']['original_author'] = original_author
            
    return bookmark

def process_enriched_dataset(input_file: str, output_file: str, processed_dir: str = "data/processed_tweets"):
    """Process the enriched dataset to update retweet content using a hybrid approach."""
    try:
        # Count statistics
        total_bookmarks = 0
        twitter_bookmarks = 0
        retweets = 0
        fixed_retweets = 0
        fix_methods = {"user_cache": 0, "processed_cache": 0, "direct": 0}
        
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
                            
                            # Apply the hybrid fix
                            original_bookmark = bookmark.copy()
                            fixed_bookmark = hybrid_fix_retweet_content(bookmark, processed_dir)
                            
                            # Check if fixing was successful
                            if fixed_bookmark.get('metadata', {}).get('retweet_fixed', False):
                                fixed_retweets += 1
                                method = fixed_bookmark.get('metadata', {}).get('fix_method', 'unknown')
                                fix_methods[method] = fix_methods.get(method, 0) + 1
                                bookmark = fixed_bookmark
                                logger.info(f"Fixed retweet {total_bookmarks} using {method}: {bookmark.get('url', 'No URL')}")
                
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
        logger.info(f"Fix methods:")
        logger.info(f"  - User cache: {fix_methods.get('user_cache', 0)}")
        logger.info(f"  - Processed cache: {fix_methods.get('processed_cache', 0)}")
        logger.info(f"  - Direct extraction: {fix_methods.get('direct', 0)}")
        
        return True
    except Exception as e:
        logger.error(f"Error processing enriched dataset: {str(e)}")
        return False

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract original tweet content using a hybrid approach")
    parser.add_argument('--input', '-i', default="enriched/data-bookmark-enriched-full.jsonl",
                      help="Input JSONL file (default: enriched/data-bookmark-enriched-full.jsonl)")
    parser.add_argument('--output', '-o', default="enriched/data-bookmark-enriched-fixed-all.jsonl",
                      help="Output JSONL file (default: enriched/data-bookmark-enriched-fixed-all.jsonl)")
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