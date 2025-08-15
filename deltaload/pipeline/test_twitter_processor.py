#!/usr/bin/env python3
"""
Test script for the Twitter processor module.
This script loads a sample of bookmarks and runs the Twitter processor on them
to verify that it properly fixes content, retweets, and truncated tweets.
"""

import sys
import json
import logging
from pathlib import Path

# Add the parent directory to the path so we can import modules
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the TwitterProcessor
from tools.twitter_processor import TwitterProcessor, load_bookmarks, save_bookmarks

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def main():
    """Main function to test the Twitter processor."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test the Twitter processor module")
    parser.add_argument('--input', '-i', default="data-bookmark.jsonl", help="Input JSONL file")
    parser.add_argument('--output', '-o', default="data-bookmark-twitter-test.jsonl", help="Output JSONL file")
    parser.add_argument('--cache-dir', '-c', default="data", help="Directory containing Twitter cache files")
    parser.add_argument('--batch-size', '-b', type=int, default=50, help="Number of bookmarks to process in each batch")
    parser.add_argument('--limit', '-l', type=int, default=10, help="Limit to the first N bookmarks")
    parser.add_argument('--twitter-only', '-t', action="store_true", help="Only process Twitter bookmarks")
    
    args = parser.parse_args()
    
    # Load the bookmarks
    logger.info(f"Loading bookmarks from {args.input}")
    bookmarks = load_bookmarks(args.input)
    
    if not bookmarks:
        logger.error("No bookmarks loaded. Exiting.")
        return 1
    
    # Apply limit if provided
    if args.limit > 0 and args.limit < len(bookmarks):
        logger.info(f"Limiting to first {args.limit} bookmarks")
        bookmarks = bookmarks[:args.limit]
    
    # Filter for Twitter bookmarks if requested
    if args.twitter_only:
        logger.info("Filtering for Twitter bookmarks only")
        twitter_bookmarks = []
        for bookmark in bookmarks:
            source = bookmark.get('source', '')
            if 'twitter' in source.lower():
                twitter_bookmarks.append(bookmark)
        bookmarks = twitter_bookmarks
        logger.info(f"Found {len(bookmarks)} Twitter bookmarks")
    
    # Initialize the processor
    processor = TwitterProcessor(cache_dir=args.cache_dir, batch_size=args.batch_size)
    
    # Process the bookmarks
    logger.info("Processing bookmarks")
    processed_bookmarks = processor.process_bookmarks(
        bookmarks,
        fix_content=True,
        fix_retweets=True,
        fix_truncated=True
    )
    
    # Save the processed bookmarks
    logger.info(f"Saving processed bookmarks to {args.output}")
    save_bookmarks(processed_bookmarks, args.output)
    
    # Print statistics
    stats = processor.get_stats()
    print("\nTwitter Processing Statistics:")
    print(f"Total Twitter bookmarks: {stats['twitter_count']}")
    print(f"Content mismatches fixed: {stats['content_fixed_count']}")
    print(f"Retweets fixed: {stats['retweet_fixed_count']}")
    print(f"Truncated tweets found: {stats['truncated_count']}")
    print(f"Truncated tweets fixed: {stats['truncated_fixed_count']}")
    print(f"  - Fixed from cache: {stats['truncated_fixed_from_cache']}")
    print(f"  - Fixed from API: {stats['truncated_fixed_from_api']}")
    
    logger.info("Test completed successfully")
    return 0

if __name__ == "__main__":
    sys.exit(main())