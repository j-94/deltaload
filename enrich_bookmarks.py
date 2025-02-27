#!/usr/bin/env python3
"""
Command-line script to enrich bookmarks with content from their sources.
"""

import os
import sys
import json
import logging
import argparse
from typing import List, Dict
from dotenv import load_dotenv
from tools.bookmark_enrichment import BookmarkEnrichment

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("enrich_bookmarks.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def read_jsonl_file(file_path: str) -> List[Dict]:
    """Read bookmarks from JSONL file."""
    bookmarks = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    bookmark = json.loads(line.strip())
                    bookmarks.append(bookmark)
                except json.JSONDecodeError:
                    logger.error(f"Error parsing JSON line: {line}")
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
        
    return bookmarks

def write_jsonl_file(file_path: str, bookmarks: List[Dict]):
    """Write bookmarks to JSONL file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for bookmark in bookmarks:
                json.dump(bookmark, f, ensure_ascii=False)
                f.write('\n')
        logger.info(f"Successfully wrote {len(bookmarks)} bookmarks to {file_path}")
    except Exception as e:
        logger.error(f"Error writing file {file_path}: {str(e)}")

def main():
    """Main function to run bookmark enrichment."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Enrich bookmarks with external content')
    parser.add_argument('input_file', help='Input JSONL file with bookmarks')
    parser.add_argument('--output-file', '-o', help='Output JSONL file (default: input file with .enriched suffix)')
    parser.add_argument('--cache-dir', '-c', default='./cache', help='Cache directory for enriched content')
    parser.add_argument('--force-refresh', '-f', action='store_true', help='Force refresh cached content')
    parser.add_argument('--skip-existing', '-s', action='store_true', help='Skip bookmarks that already have content')
    parser.add_argument('--limit', '-l', type=int, help='Limit processing to specified number of bookmarks')
    parser.add_argument('--filter-source', choices=['twitter', 'github', 'web'], help='Only process bookmarks from specified source')
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    
    # Set output file if not specified
    if not args.output_file:
        base, ext = os.path.splitext(args.input_file)
        args.output_file = f"{base}.enriched{ext}"
    
    # Read input file
    logger.info(f"Reading bookmarks from {args.input_file}")
    bookmarks = read_jsonl_file(args.input_file)
    logger.info(f"Read {len(bookmarks)} bookmarks")
    
    # Filter bookmarks if needed
    if args.skip_existing:
        bookmarks = [b for b in bookmarks if not b.get('content')]
        logger.info(f"Filtered to {len(bookmarks)} bookmarks without existing content")
        
    if args.filter_source:
        # Initialize enrichment to use determine_source
        enrichment = BookmarkEnrichment(cache_dir=args.cache_dir)
        bookmarks = [b for b in bookmarks if enrichment.determine_source(b.get('url', '')) == args.filter_source]
        logger.info(f"Filtered to {len(bookmarks)} bookmarks from {args.filter_source}")
        
    if args.limit and args.limit > 0:
        bookmarks = bookmarks[:args.limit]
        logger.info(f"Limited to {len(bookmarks)} bookmarks")
    
    # Process bookmarks
    if not bookmarks:
        logger.info("No bookmarks to process")
        return
        
    logger.info(f"Enriching {len(bookmarks)} bookmarks")
    enrichment = BookmarkEnrichment(cache_dir=args.cache_dir)
    enriched_bookmarks = enrichment.enrich_bookmarks(bookmarks, force_refresh=args.force_refresh)
    
    # Write output file
    logger.info(f"Writing enriched bookmarks to {args.output_file}")
    write_jsonl_file(args.output_file, enriched_bookmarks)
    logger.info("Bookmark enrichment completed")

if __name__ == '__main__':
    main()