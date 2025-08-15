#!/usr/bin/env python3
"""
Fix retweets in enriched dataset by directly extracting original content.

This script:
1. Identifies retweets in the enriched dataset
2. Extracts the original tweet text directly from the "RT @username: text" pattern
3. Updates the content field to contain "Original Tweet by @username: [original text]"
"""

import os
import json
import re
import logging
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("direct_retweet_fix.log")
    ]
)
logger = logging.getLogger(__name__)

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

def fix_retweet_content(bookmark: Dict) -> Dict:
    """
    Fix a retweet bookmark by extracting original content directly.
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
    is_retweet, original_author, original_content = extract_retweet_info(content)
    
    if not is_retweet or not original_author or not original_content:
        return bookmark
    
    try:
        # Update content field with original content
        bookmark['content'] = f"Original Tweet by @{original_author}: {original_content}"
        
        # Add metadata
        if 'metadata' not in bookmark:
            bookmark['metadata'] = {}
        
        bookmark['metadata']['retweet_fixed'] = True
        bookmark['metadata']['original_author'] = original_author
        bookmark['metadata']['retweet_fixed_at'] = datetime.now().isoformat()
        
        return bookmark
        
    except Exception as e:
        logger.error(f"Error fixing retweet: {str(e)}")
    
    return bookmark

def process_enriched_dataset(input_file: str, output_file: str):
    """Process the enriched dataset to update retweet content."""
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
                        is_retweet, _, _ = extract_retweet_info(content)
                        
                        if is_retweet:
                            retweets += 1
                            
                            # Fix the retweet content
                            original_bookmark = bookmark.copy()
                            fixed_bookmark = fix_retweet_content(bookmark)
                            
                            # Check if fixing was successful
                            if fixed_bookmark.get('metadata', {}).get('retweet_fixed', False):
                                fixed_retweets += 1
                                bookmark = fixed_bookmark
                                logger.info(f"Fixed retweet {total_bookmarks}: {bookmark.get('url', 'No URL')}")
                
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
    
    parser = argparse.ArgumentParser(description="Fix retweets in enriched dataset by extracting original content")
    parser.add_argument('--input', '-i', default="enriched/data-bookmark-enriched-full.jsonl",
                      help="Input JSONL file (default: enriched/data-bookmark-enriched-full.jsonl)")
    parser.add_argument('--output', '-o', default="enriched/data-bookmark-enriched-fixed-direct.jsonl",
                      help="Output JSONL file (default: enriched/data-bookmark-enriched-fixed-direct.jsonl)")
    
    args = parser.parse_args()
    
    # Create backup of input file
    if os.path.exists(args.input):
        import shutil
        backup_file = f"{args.input}.bak"
        if not os.path.exists(backup_file):
            shutil.copy2(args.input, backup_file)
            logger.info(f"Created backup of input file at {backup_file}")
    
    # Process the enriched dataset
    success = process_enriched_dataset(args.input, args.output)
    
    if success:
        logger.info(f"Successfully processed enriched dataset")
        logger.info(f"Output file: {args.output}")
    else:
        logger.error(f"Failed to process enriched dataset")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())