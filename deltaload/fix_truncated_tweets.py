#!/usr/bin/env python3
"""
Fix truncated tweets by using TwitterThreadFetcher to retrieve the full content.
This script specifically targets tweets that end with "..." or are otherwise truncated.
"""

import os
import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("fix_truncated_tweets.log")
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
        r'\w+…$'                   # Word followed by ellipsis$',                 # Ends with ...
        r'\.{3}\s*$',              # Ends with ... and optional whitespace
        r'\.\.\.$',                # Ends with ...
        r'…$',                     # Ends with Unicode ellipsis
        r'https://t\.co/\w+$',     # Ends with a t.co URL (likely truncated)
        r'\w+…$',                  # Word followed by ellipsis
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

def fix_truncated_tweet(bookmark: Dict) -> Dict:
    """
    Fix a truncated tweet by fetching the full content from Twitter API.
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
        # Import TwitterThreadFetcher
        from tools.twitter_thread_fetcher import TwitterThreadFetcher
        
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
        
        # Initialize TwitterThreadFetcher
        fetcher = TwitterThreadFetcher()
        
        # Fetch complete thread/tweet
        logger.info(f"Fetching complete content for tweet ID: {tweet_id}")
        result = fetcher.process_url(url)
        
        # Check if fetch was successful
        if result.get('status') != 'success':
            logger.error(f"Failed to fetch tweet {tweet_id}: {result.get('error', 'Unknown error')}")
            return bookmark
        
        # Extract full content from the result
        full_content = result.get('content', '')
        
        if not full_content:
            logger.warning(f"No content returned for tweet {tweet_id}")
            return bookmark
        
        # Update the bookmark with the full content
        logger.info(f"Updating truncated content for tweet {tweet_id}")
        
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
        
        # Update with any additional metadata from the fetched result
        if 'metadata' in result:
            # Only add new keys, don't overwrite existing ones
            for key, value in result['metadata'].items():
                if key not in bookmark['metadata']:
                    bookmark['metadata'][key] = value
        
        logger.info(f"Successfully fixed truncated content for tweet {tweet_id}")
    
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
            fixed = fix_truncated_tweet(bookmark)
            
            # Check if a fix was actually applied
            if 'truncated_fixed_at' in fixed:
                fixed_count += 1
                logger.info(f"Fixed truncated tweet {i+1}/{len(bookmarks)}: {fixed.get('url', 'No URL')}")
            
            # Update the bookmark in place
            bookmarks[i] = fixed
    
    logger.info(f"Processed {twitter_count} Twitter bookmarks")
    logger.info(f"Found {truncated_count} truncated tweets")
    logger.info(f"Fixed {fixed_count} truncated tweets")
    
    return bookmarks

def main():
    """Main function to fix truncated tweets in bookmarks."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Fix truncated tweets in processed bookmarks")
    parser.add_argument('--input', '-i', required=True, help="Input JSONL file")
    parser.add_argument('--output', '-o', help="Output JSONL file (defaults to input-truncated-fixed.jsonl)")
    parser.add_argument('--backup', '-b', action="store_true", help="Create a backup of the input file")
    parser.add_argument('--batch-size', '-s', type=int, default=100, help="Number of bookmarks to process in each batch")
    parser.add_argument('--start-index', type=int, default=0, help="Index to start processing from")
    parser.add_argument('--max-items', type=int, default=None, help="Maximum number of items to process (useful for testing)")
    
    args = parser.parse_args()
    
    # Set default output file if not provided
    if not args.output:
        input_path = Path(args.input)
        args.output = str(input_path.with_stem(f"{input_path.stem}-truncated-fixed"))
    
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
                fixed = fix_truncated_tweet(bookmark)
                
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