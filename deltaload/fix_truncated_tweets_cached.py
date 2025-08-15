#!/usr/bin/env python3
"""
Fix truncated tweets by using existing Twitter data from the cache directory.
This script is an alternative to fix_truncated_tweets.py that doesn't rely on API calls.
"""

import os
import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import glob

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("fix_truncated_tweets_cached.log")
    ]
)
logger = logging.getLogger(__name__)

def is_truncated(content: str) -> bool:
    """
    Check if content appears to be truncated.
    
    Looks for indicators like "..." at the end, or other common truncation patterns.
    """
    if not content:
        return False
        
    # Common truncation patterns
    patterns = [
        r'\.{3}$',                 # Ends with ...
        r'\.{3}\s*$',              # Ends with ... and optional whitespace
        r'\.\.\.$',                # Ends with ...
        r'…$',                     # Ends with Unicode ellipsis
        r'https://t\.co/\w+$',     # Ends with a t.co URL (likely truncated)
        r'\w+…$'                   # Word followed by ellipsis
    ]
    
    # Check if content matches any truncation pattern
    return any(re.search(pattern, content.strip()) for pattern in patterns)

def load_bookmarks(file_path: str) -> List[Dict]:
    """Load bookmarks from a JSONL file."""
    bookmarks = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    try:
                        bookmark = json.loads(line.strip())
                        bookmarks.append(bookmark)
                    except json.JSONDecodeError as e:
                        logger.error(f"Error parsing JSON line: {str(e)}")
        
        logger.info(f"Loaded {len(bookmarks)} bookmarks from {file_path}")
        return bookmarks
    except Exception as e:
        logger.error(f"Error loading bookmarks from {file_path}: {str(e)}")
        return []

def save_bookmarks(bookmarks: List[Dict], file_path: str) -> bool:
    """Save bookmarks to a JSONL file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for bookmark in bookmarks:
                f.write(json.dumps(bookmark, ensure_ascii=False) + '\n')
        
        logger.info(f"Saved {len(bookmarks)} bookmarks to {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error saving bookmarks to {file_path}: {str(e)}")
        return False

def extract_tweet_id(url: str) -> Optional[str]:
    """
    Extract tweet ID from a Twitter URL.
    
    Handles various Twitter URL formats:
    - https://twitter.com/username/status/1234567890
    - https://x.com/username/status/1234567890
    - twitter/username/status/1234567890
    - https://twitter.com/i/web/status/1234567890
    """
    if not url:
        return None
        
    # Handle twitter.com, x.com, and twitter URLs without domain prefix
    valid_domains = ['twitter.com', 'x.com']
    is_valid_domain = any(domain in url.lower() for domain in valid_domains) or url.lower().startswith('twitter/')
    
    if not is_valid_domain:
        return None
        
    # Extract tweet ID from URL pattern
    if '/status/' in url:
        # Split by /status/ and take everything after it
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

def find_tweet_in_cache_files(tweet_id: str, cache_dir: str = "data") -> Optional[Dict]:
    """
    Search through all cache files for the given tweet ID.
    
    Args:
        tweet_id: The tweet ID to search for
        cache_dir: Base directory for cache files
        
    Returns:
        Dict containing tweet data if found, None otherwise
    """
    try:
        # First check the standard cache directory
        standard_cache_pattern = f"{cache_dir}/*/UserTweetsAndReplies.json"
        cache_files = glob.glob(standard_cache_pattern, recursive=False)
        
        # Also check the likes directory
        likes_pattern = f"{cache_dir}/*/Likes.json"
        cache_files.extend(glob.glob(likes_pattern, recursive=False))
        
        # Check the legacy cache directory
        legacy_cache_pattern = f"cache/twitter_*.json"
        cache_files.extend(glob.glob(legacy_cache_pattern, recursive=False))
        
        # Also check the test_cache directory
        test_cache_pattern = f"test_cache/twitter_*.json"
        cache_files.extend(glob.glob(test_cache_pattern, recursive=False))
        
        logger.info(f"Scanning {len(cache_files)} cache files for tweet {tweet_id}")
        
        # Search through each cache file
        for cache_file in cache_files:
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    try:
                        cache_data = json.load(f)
                        
                        # Check if this file contains the tweet directly
                        # This is for legacy cache files
                        if 'thread_id' in cache_data.get('metadata', {}) and cache_data['metadata']['thread_id'] == tweet_id:
                            logger.info(f"Found direct match for tweet {tweet_id} in {cache_file}")
                            return cache_data
                        
                        # Check if this tweet is in the 'tweets' array in metadata
                        if 'tweets' in cache_data.get('metadata', {}):
                            for tweet in cache_data['metadata']['tweets']:
                                if tweet.get('id') == tweet_id:
                                    logger.info(f"Found tweet {tweet_id} in metadata.tweets array in {cache_file}")
                                    return cache_data
                        
                        # For newer Twitter API format (UserTweetsAndReplies.json, Likes.json)
                        if isinstance(cache_data, list):
                            # This might be a list of API responses
                            for item in cache_data:
                                # Look for tweet entries
                                if 'data' in item and 'user' in item['data']:
                                    try:
                                        timeline = item['data']['user']['result']['timeline_v2']['timeline']
                                        for instruction in timeline.get('instructions', []):
                                            if instruction['type'] == 'TimelineAddEntries':
                                                for entry in instruction.get('entries', []):
                                                    if 'entryId' in entry and f"tweet-{tweet_id}" in entry['entryId']:
                                                        logger.info(f"Found tweet {tweet_id} in entries array in {cache_file}")
                                                        return extract_tweet_from_entry(entry, tweet_id)
                                    except (KeyError, TypeError):
                                        pass
                                        
                        # Check if this is a direct Twitter API response and contains the tweet
                        if 'data' in cache_data and 'user' in cache_data['data']:
                            try:
                                timeline = cache_data['data']['user']['result']['timeline_v2']['timeline']
                                for instruction in timeline.get('instructions', []):
                                    if instruction['type'] == 'TimelineAddEntries':
                                        for entry in instruction.get('entries', []):
                                            if 'entryId' in entry and f"tweet-{tweet_id}" in entry['entryId']:
                                                logger.info(f"Found tweet {tweet_id} in entries array in {cache_file}")
                                                return extract_tweet_from_entry(entry, tweet_id)
                            except (KeyError, TypeError):
                                pass
                            
                    except json.JSONDecodeError:
                        logger.warning(f"Error parsing JSON in {cache_file}")
                        continue
            except Exception as e:
                logger.warning(f"Error reading cache file {cache_file}: {str(e)}")
                continue
                
        logger.info(f"Tweet {tweet_id} not found in any cache file")
        return None
        
    except Exception as e:
        logger.error(f"Error searching for tweet {tweet_id} in cache files: {str(e)}")
        return None

def extract_tweet_from_entry(entry: Dict, tweet_id: str) -> Optional[Dict]:
    """
    Extract tweet data from a Twitter API entry.
    
    Args:
        entry: Entry data from Twitter API response
        tweet_id: The ID of the tweet to extract
        
    Returns:
        Dict with extracted tweet data or None if extraction fails
    """
    try:
        # Navigate to the tweet result
        if 'content' in entry and 'itemContent' in entry['content']:
            item_content = entry['content']['itemContent']
            if 'tweet_results' in item_content and 'result' in item_content['tweet_results']:
                tweet_result = item_content['tweet_results']['result']
                
                # Extract text content
                text = ""
                if 'legacy' in tweet_result and 'full_text' in tweet_result['legacy']:
                    text = tweet_result['legacy']['full_text']
                elif 'note_tweet' in tweet_result:
                    note_tweet = tweet_result['note_tweet']['note_tweet_results']['result']
                    text = note_tweet.get('text', '')
                
                # If no text was found, we can't proceed
                if not text:
                    return None
                
                # Extract media if available
                media = []
                if 'legacy' in tweet_result and 'extended_entities' in tweet_result['legacy']:
                    extended_entities = tweet_result['legacy']['extended_entities']
                    if 'media' in extended_entities:
                        for media_item in extended_entities['media']:
                            media_url = media_item.get('media_url_https', '')
                            if media_url:
                                media.append(f"{media_url}?format=jpg&name=large")
                
                # Extract author info
                author = {}
                if 'core' in tweet_result and 'user_results' in tweet_result['core']:
                    user = tweet_result['core']['user_results']['result']['legacy']
                    author = {
                        'name': user.get('name', ''),
                        'screen_name': user.get('screen_name', ''),
                        'followers_count': user.get('followers_count', 0)
                    }
                
                # Extract metrics
                metrics = {}
                if 'legacy' in tweet_result:
                    legacy = tweet_result['legacy']
                    metrics = {
                        'favorite_count': legacy.get('favorite_count', 0),
                        'retweet_count': legacy.get('retweet_count', 0),
                        'reply_count': legacy.get('reply_count', 0)
                    }
                
                # Create result in format similar to TwitterThreadFetcher output
                result = {
                    'status': 'success',
                    'content': text,
                    'metadata': {
                        'thread_id': tweet_id,
                        'author': author,
                        'tweet_count': 1,
                        'type': 'thread',
                        'tweets': [
                            {
                                'id': tweet_id,
                                'text': text,
                                'media': media,
                                'created_at': tweet_result['legacy'].get('created_at', '') if 'legacy' in tweet_result else '',
                                'favorite_count': metrics.get('favorite_count', 0),
                                'retweet_count': metrics.get('retweet_count', 0),
                                'reply_count': metrics.get('reply_count', 0)
                            }
                        ]
                    }
                }
                
                return result
    
    except Exception as e:
        logger.error(f"Error extracting tweet {tweet_id} from entry: {str(e)}")
    
    return None

def fix_truncated_tweet_from_cache(bookmark: Dict) -> Dict:
    """
    Fix a truncated tweet by searching for its complete content in cache files.
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
    
    # Check if content is truncated
    if not is_truncated(content):
        return bookmark
    
    try:
        # Get tweet URL
        url = bookmark.get('url', '')
        if not url:
            logger.warning(f"No URL found for bookmark with truncated content: {content[:50]}...")
            return bookmark
        
        # Extract tweet ID
        tweet_id = extract_tweet_id(url)
        if not tweet_id:
            logger.warning(f"Could not extract tweet ID from URL: {url}")
            return bookmark
        
        # Search for tweet in cache files
        logger.info(f"Searching cache for tweet ID: {tweet_id}")
        tweet_data = find_tweet_in_cache_files(tweet_id)
        
        # Check if we found tweet data
        if not tweet_data or tweet_data.get('status') != 'success':
            logger.warning(f"Could not find tweet {tweet_id} in cache files")
            return bookmark
        
        # Extract full content from the result
        full_content = tweet_data.get('content', '')
        
        if not full_content:
            logger.warning(f"No content found in cached data for tweet {tweet_id}")
            return bookmark
        
        # Update the bookmark with the full content
        logger.info(f"Updating truncated content for tweet {tweet_id} from cache")
        
        # Update content field
        bookmark['content'] = full_content
        
        # Update markdown to include the full content
        current_markdown = bookmark.get('markdown', '')
        new_markdown = current_markdown
        
        # Find the content section in the markdown
        content_start_marker = "## Content"
        content_start = current_markdown.find(content_start_marker)
        
        if content_start != -1:
            # Extract header (everything before content)
            header = current_markdown[:content_start + len(content_start_marker) + 1]
            
            # Find content end (first blank line after content)
            content_end = current_markdown.find("\n\n", content_start + len(content_start_marker))
            
            # If no blank line, assume rest of text is content
            if content_end == -1:
                footer = ""
            else:
                footer = current_markdown[content_end:]
            
            # Create new markdown with full content
            new_markdown = f"{header}\n{full_content}\n{footer}"
        
        # Update bookmark
        bookmark['markdown'] = new_markdown
        bookmark['full_text'] = new_markdown
        bookmark['truncated_fixed_at'] = datetime.now().isoformat()
        
        # Update metadata
        if 'metadata' not in bookmark:
            bookmark['metadata'] = {}
        
        bookmark['metadata']['truncated_fixed'] = True
        bookmark['metadata']['cached_fix'] = True
        
        # Update with any additional metadata from the fetched result
        if 'metadata' in tweet_data:
            # Only add new keys, don't overwrite existing ones
            for key, value in tweet_data['metadata'].items():
                if key not in bookmark['metadata']:
                    bookmark['metadata'][key] = value
        
        logger.info(f"Successfully fixed truncated content for tweet {tweet_id} from cache")
    
    except Exception as e:
        logger.error(f"Error fixing truncated tweet: {str(e)}")
    
    return bookmark

def process_bookmarks(bookmarks: List[Dict]) -> List[Dict]:
    """Process all bookmarks, fixing truncated tweets as needed."""
    fixed_count = 0
    twitter_count = 0
    truncated_count = 0
    
    for i, bookmark in enumerate(bookmarks):
        source = bookmark.get('source', '')
        if 'twitter' not in source.lower():
            continue
            
        twitter_count += 1
        
        content = bookmark.get('content', '')
        if is_truncated(content):
            truncated_count += 1
            
            # Fix the truncated tweet
            original = bookmark.copy()
            fixed = fix_truncated_tweet_from_cache(bookmark)
            
            # Check if a fix was actually applied
            if 'truncated_fixed_at' in fixed:
                fixed_count += 1
                logger.info(f"Fixed truncated tweet {i+1}/{len(bookmarks)}: {fixed.get('url', 'No URL')}")
            
            # Update the bookmark in place
            bookmarks[i] = fixed
    
    logger.info(f"Processed {twitter_count} Twitter bookmarks")
    logger.info(f"Found {truncated_count} truncated tweets")
    logger.info(f"Fixed {fixed_count} truncated tweets using cache data")
    
    return bookmarks

def main():
    """Main function to fix truncated tweets in bookmarks."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Fix truncated tweets in processed bookmarks using cache data")
    parser.add_argument('--input', '-i', required=True, help="Input JSONL file")
    parser.add_argument('--output', '-o', help="Output JSONL file (defaults to input-cache-fixed.jsonl)")
    parser.add_argument('--backup', '-b', action="store_true", help="Create a backup of the input file")
    parser.add_argument('--batch-size', '-s', type=int, default=100, help="Number of bookmarks to process in each batch")
    parser.add_argument('--start-index', type=int, default=0, help="Index to start processing from")
    parser.add_argument('--max-items', type=int, default=None, help="Maximum number of items to process (useful for testing)")
    
    args = parser.parse_args()
    
    # Set default output file if not provided
    if not args.output:
        input_path = Path(args.input)
        args.output = str(input_path.with_stem(f"{input_path.stem}-cache-fixed"))
    
    # Create backup if requested
    if args.backup:
        import shutil
        backup_file = f"{args.input}.bak"
        shutil.copy2(args.input, backup_file)
        logger.info(f"Created backup of input file at {backup_file}")
    
    # Load bookmarks
    bookmarks = load_bookmarks(args.input)
    if not bookmarks:
        logger.error("Failed to load bookmarks. Exiting.")
        return 1
        
    # Apply max-items limit if specified
    if args.max_items is not None:
        bookmarks = bookmarks[:args.start_index + args.max_items]
        
    # Process bookmarks in batches
    batch_size = args.batch_size
    start_index = args.start_index
    total_bookmarks = len(bookmarks)
    
    logger.info(f"Processing {total_bookmarks} bookmarks in batches of {batch_size}, starting from index {start_index}")
    
    # Get the Twitter bookmarks that need processing
    twitter_bookmarks = []
    truncated_indices = []
    
    for i, bookmark in enumerate(bookmarks):
        if i < start_index:
            continue
            
        source = bookmark.get('source', '')
        if 'twitter' not in source.lower():
            continue
            
        content = bookmark.get('content', '')
        if is_truncated(content):
            twitter_bookmarks.append(bookmark)
            truncated_indices.append(i)
    
    logger.info(f"Found {len(twitter_bookmarks)} truncated Twitter bookmarks to process")
    
    # Process in batches
    fixed_count = 0
    batch_count = 0
    
    for batch_start in range(0, len(twitter_bookmarks), batch_size):
        batch_count += 1
        batch_end = min(batch_start + batch_size, len(twitter_bookmarks))
        current_batch = twitter_bookmarks[batch_start:batch_end]
        
        logger.info(f"Processing batch {batch_count}: items {batch_start}-{batch_end-1} of {len(twitter_bookmarks)}")
        
        # Process current batch
        for i, bookmark in enumerate(current_batch):
            try:
                idx = truncated_indices[batch_start + i]
                original = bookmark.copy()
                fixed = fix_truncated_tweet_from_cache(bookmark)
                
                # Check if a fix was actually applied
                if 'truncated_fixed_at' in fixed:
                    fixed_count += 1
                    logger.info(f"Fixed truncated tweet {idx+1}/{total_bookmarks}: {fixed.get('url', 'No URL')}")
                
                # Update the bookmark in place
                bookmarks[idx] = fixed
                
                # Save progress after each successful fix
                if fixed_count % 10 == 0:
                    logger.info(f"Saving intermediate progress ({fixed_count} tweets fixed so far)")
                    save_bookmarks(bookmarks, args.output)
            except Exception as e:
                logger.error(f"Error processing bookmark {batch_start + i}: {str(e)}")
        
        # Save after each batch
        logger.info(f"Saving batch {batch_count} results")
        success = save_bookmarks(bookmarks, args.output)
        if not success:
            logger.error(f"Failed to save batch {batch_count}. Continuing to next batch.")
    
    logger.info(f"Processed {len(twitter_bookmarks)} Twitter bookmarks")
    logger.info(f"Fixed {fixed_count} truncated tweets")
    logger.info(f"Truncated tweet fixing complete. See {args.output} for the fixed data.")
    return 0

if __name__ == "__main__":
    exit(main())