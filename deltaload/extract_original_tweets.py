#!/usr/bin/env python3
"""
Extract original tweet text directly from retweets.

This script:
1. Reads the user's Twitter cache files to find tweet data
2. For each retweet, extracts the actual retweeted content
3. Replaces "RT @username: text" with just the original text
"""

import os
import json
import re
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("extract_original_tweets.log")
    ]
)
logger = logging.getLogger(__name__)

def load_jsonl(file_path: str) -> List[Dict]:
    """Load a JSONL file and return a list of dictionaries."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line.strip()))
            except json.JSONDecodeError as e:
                logger.error(f"Error parsing JSON line in {file_path}: {e}")
    return data

def save_jsonl(data: List[Dict], file_path: str) -> None:
    """Save a list of dictionaries to a JSONL file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

def load_twitter_cache(cache_path: str) -> Dict[str, Any]:
    """Load a Twitter cache file and return the JSON data."""
    try:
        with open(cache_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
        logger.error(f"Error loading Twitter cache file {cache_path}: {e}")
        return {}

def extract_retweet_id_from_content(content: str) -> Optional[str]:
    """Extract the retweet ID if the content is a retweet."""
    if content.startswith("RT @"):
        return None  # We can't extract the original tweet ID from just the content
    return None

def extract_tweet_id_from_url(url: str) -> Optional[str]:
    """Extract the tweet ID from a Twitter URL."""
    match = re.search(r'/status/(\d+)', url)
    if match:
        return match.group(1)
    return None

def is_retweet(content: str) -> bool:
    """Check if the content is a retweet."""
    return content.strip().startswith("RT @")

def extract_original_tweet_from_user_cache(tweet_id: str, cache_files: List[str]) -> Optional[Dict]:
    """
    Extract the original tweet data from the user's cache files.
    
    Args:
        tweet_id: The ID of the tweet to extract.
        cache_files: List of cache file paths to search.
        
    Returns:
        The original tweet data if found, or None.
    """
    for cache_file in cache_files:
        if not os.path.exists(cache_file):
            logger.warning(f"Cache file does not exist: {cache_file}")
            continue
            
        try:
            logger.info(f"Searching cache file: {cache_file}")
            data = load_twitter_cache(cache_file)
            
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
                                        entry_id = entry.get('entryId', '')
                                        if f"tweet-{tweet_id}" in entry_id:
                                            # Found the tweet
                                            logger.info(f"Found tweet {tweet_id} in {cache_file}")
                                            try:
                                                item_content = entry.get('content', {}).get('itemContent', {})
                                                tweet_results = item_content.get('tweet_results', {})
                                                tweet_result = tweet_results.get('result', {})
                                                
                                                if tweet_result:
                                                    # First try to get the retweeted content
                                                    retweeted_status = None
                                                    if 'legacy' in tweet_result and 'retweeted_status_result' in tweet_result['legacy']:
                                                        retweeted_status = tweet_result['legacy']['retweeted_status_result']['result']
                                                        logger.info(f"Found retweeted status for {tweet_id}")
                                                    
                                                    # If we found retweeted content, extract the text
                                                    if retweeted_status:
                                                        if 'legacy' in retweeted_status:
                                                            return {
                                                                'text': retweeted_status['legacy'].get('full_text', ''),
                                                                'source': 'user_cache_retweeted'
                                                            }
                                                        elif 'note_tweet' in retweeted_status:
                                                            note_tweet = retweeted_status['note_tweet']['note_tweet_results']['result']
                                                            return {
                                                                'text': note_tweet.get('text', ''),
                                                                'source': 'user_cache_retweeted_note'
                                                            }
                                                    
                                                    # If we couldn't find retweeted content, just return the original tweet
                                                    # (which will contain the "RT @username: text" format)
                                                    if 'legacy' in tweet_result:
                                                        tweet_text = tweet_result['legacy'].get('full_text', '')
                                                        # Extract the original text from the RT format
                                                        if tweet_text and is_retweet(tweet_text):
                                                            match = re.match(r'^RT @[^:]+:\s+(.*)', tweet_text, re.DOTALL)
                                                            if match:
                                                                return {
                                                                    'text': match.group(1),
                                                                    'source': 'user_cache_extracted'
                                                                }
                                                        return {
                                                            'text': tweet_text,
                                                            'source': 'user_cache_original'
                                                        }
                                                    elif 'note_tweet' in tweet_result:
                                                        note_tweet = tweet_result['note_tweet']['note_tweet_results']['result']
                                                        return {
                                                            'text': note_tweet.get('text', ''),
                                                            'source': 'user_cache_note'
                                                        }
                                            except Exception as e:
                                                logger.error(f"Error extracting tweet data from {cache_file}: {e}")
                        except Exception as e:
                            logger.error(f"Error processing timeline in {cache_file}: {e}")
                            
        except Exception as e:
            logger.error(f"Error processing cache file {cache_file}: {e}")
    
    return None

def process_retweets(bookmarks: List[Dict], cache_files: List[str]) -> List[Dict]:
    """
    Process retweets in the bookmarks list and update them with original content.
    
    Args:
        bookmarks: The list of bookmark dictionaries.
        cache_files: The list of Twitter cache files to search.
        
    Returns:
        The updated list of bookmarks.
    """
    processed_ids: Set[str] = set()  # Track processed tweet IDs to avoid duplicates
    fixed_count = 0
    retweet_count = 0
    methods = {'user_cache_retweeted': 0, 'user_cache_extracted': 0, 'user_cache_original': 0, 
              'user_cache_retweeted_note': 0, 'user_cache_note': 0, 'direct_extraction': 0}
    
    for i, bookmark in enumerate(bookmarks):
        content = bookmark.get('content', '')
        
        # Skip if not Twitter or not a retweet
        if 'twitter' not in bookmark.get('source', '').lower() or not is_retweet(content):
            continue
            
        retweet_count += 1
        url = bookmark.get('url', '')
        tweet_id = extract_tweet_id_from_url(url)
        
        if tweet_id in processed_ids:
            logger.info(f"Skipping duplicate tweet ID: {tweet_id}")
            continue
            
        processed_ids.add(tweet_id)
        
        if tweet_id:
            # Try to find the original content in the cache
            original_data = extract_original_tweet_from_user_cache(tweet_id, cache_files)
            
            if original_data and original_data['text']:
                # Update the bookmark with the original content
                bookmark['content'] = original_data['text']
                
                # Update full_text and markdown if they exist
                if 'full_text' in bookmark:
                    # Extract the header and footer from the full_text
                    parts = bookmark['full_text'].split("## Content\n\n")
                    if len(parts) > 1:
                        header = parts[0] + "## Content\n\n"
                        # Update the content portion only
                        bookmark['full_text'] = header + original_data['text'] + "\n\n\n\n*Source: [" + url + "](" + url + ")*\n"
                
                if 'markdown' in bookmark:
                    # Extract the header and footer from the markdown
                    parts = bookmark['markdown'].split("## Content\n\n")
                    if len(parts) > 1:
                        header = parts[0] + "## Content\n\n"
                        # Update the content portion only
                        bookmark['markdown'] = header + original_data['text'] + "\n\n\n\n*Source: [" + url + "](" + url + ")*\n"
                
                # Add metadata
                if 'metadata' not in bookmark:
                    bookmark['metadata'] = {}
                    
                bookmark['metadata']['retweet_fixed'] = True
                bookmark['metadata']['retweet_fixed_method'] = original_data['source']
                
                methods[original_data['source']] = methods.get(original_data['source'], 0) + 1
                fixed_count += 1
                logger.info(f"Fixed retweet {i+1} using {original_data['source']}: {url}")
            else:
                # Fallback to direct extraction
                match = re.match(r'^RT @([^:]+):\s+(.*)', content, re.DOTALL)
                if match:
                    original_author = match.group(1)
                    original_content = match.group(2)
                    
                    # Update the bookmark
                    bookmark['content'] = original_content
                    
                    # Update full_text and markdown if they exist
                    if 'full_text' in bookmark:
                        # Extract the header and footer from the full_text
                        parts = bookmark['full_text'].split("## Content\n\n")
                        if len(parts) > 1:
                            header = parts[0] + "## Content\n\n"
                            # Update the content portion only
                            bookmark['full_text'] = header + original_content + "\n\n\n\n*Source: [" + url + "](" + url + ")*\n"
                    
                    if 'markdown' in bookmark:
                        # Extract the header and footer from the markdown
                        parts = bookmark['markdown'].split("## Content\n\n")
                        if len(parts) > 1:
                            header = parts[0] + "## Content\n\n"
                            # Update the content portion only
                            bookmark['markdown'] = header + original_content + "\n\n\n\n*Source: [" + url + "](" + url + ")*\n"
                    
                    # Add metadata
                    if 'metadata' not in bookmark:
                        bookmark['metadata'] = {}
                        
                    bookmark['metadata']['retweet_fixed'] = True
                    bookmark['metadata']['retweet_fixed_method'] = 'direct_extraction'
                    bookmark['metadata']['original_author'] = original_author
                    
                    methods['direct_extraction'] = methods.get('direct_extraction', 0) + 1
                    fixed_count += 1
                    logger.info(f"Fixed retweet {i+1} using direct extraction: {url}")
        else:
            # If we can't get the tweet ID, try direct extraction
            match = re.match(r'^RT @([^:]+):\s+(.*)', content, re.DOTALL)
            if match:
                original_author = match.group(1)
                original_content = match.group(2)
                
                # Update the bookmark
                bookmark['content'] = original_content
                
                # Update full_text and markdown if they exist
                if 'full_text' in bookmark:
                    # Extract the header and footer from the full_text
                    parts = bookmark['full_text'].split("## Content\n\n")
                    if len(parts) > 1:
                        header = parts[0] + "## Content\n\n"
                        # Update the content portion only
                        bookmark['full_text'] = header + original_content + "\n\n\n\n*Source: [" + url + "](" + url + ")*\n"
                
                if 'markdown' in bookmark:
                    # Extract the header and footer from the markdown
                    parts = bookmark['markdown'].split("## Content\n\n")
                    if len(parts) > 1:
                        header = parts[0] + "## Content\n\n"
                        # Update the content portion only
                        bookmark['markdown'] = header + original_content + "\n\n\n\n*Source: [" + url + "](" + url + ")*\n"
                
                # Add metadata
                if 'metadata' not in bookmark:
                    bookmark['metadata'] = {}
                    
                bookmark['metadata']['retweet_fixed'] = True
                bookmark['metadata']['retweet_fixed_method'] = 'direct_extraction'
                bookmark['metadata']['original_author'] = original_author
                
                methods['direct_extraction'] = methods.get('direct_extraction', 0) + 1
                fixed_count += 1
                logger.info(f"Fixed retweet {i+1} using direct extraction (no ID): {url}")
    
    # Log statistics
    logger.info(f"Total retweets: {retweet_count}")
    logger.info(f"Fixed retweets: {fixed_count}")
    logger.info(f"Methods used:")
    for method, count in methods.items():
        logger.info(f"  - {method}: {count}")
        
    return bookmarks

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract original tweet content from retweets")
    parser.add_argument('--input', '-i', default="enriched/data-bookmark-enriched-full.jsonl",
                      help="Input JSONL file")
    parser.add_argument('--output', '-o', default="enriched/data-bookmark-original-tweets-fixed.jsonl",
                      help="Output JSONL file")
    parser.add_argument('--cache-dir', '-c', default="data/1169726235817185281",
                      help="Directory containing Twitter cache files")
    
    args = parser.parse_args()
    
    # Find cache files
    cache_files = [
        f"{args.cache_dir}/20250414_193611_UserTweetsAndReplies.json",
        f"{args.cache_dir}/20250414_193615_Likes.json"
    ]
    
    # Check if cache files exist
    for cache_file in cache_files:
        if not os.path.exists(cache_file):
            logger.warning(f"Cache file does not exist: {cache_file}")
    
    # Load bookmarks
    logger.info(f"Loading bookmarks from {args.input}")
    bookmarks = load_jsonl(args.input)
    logger.info(f"Loaded {len(bookmarks)} bookmarks")
    
    # Process retweets
    processed_bookmarks = process_retweets(bookmarks, cache_files)
    
    # Save processed bookmarks
    logger.info(f"Saving processed bookmarks to {args.output}")
    save_jsonl(processed_bookmarks, args.output)
    logger.info(f"Done")
    
    return 0

if __name__ == "__main__":
    exit(main())