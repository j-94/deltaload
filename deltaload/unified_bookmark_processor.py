#!/usr/bin/env python3
"""
Unified Bookmark Processor

This script processes bookmarks from various sources and standardizes them
according to a common schema, with rich full_text fields and metadata.

It integrates:
- TweetProcessor for Twitter content
- GitHubScraper for GitHub repositories
- WebScraper for general web content
"""

import os
import json
import logging
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union

# Import processors
from tools.tweet_processor import TweetProcessor
from tools.github_scraper import GitHubScraper
from tools.web_scraper import WebScraper

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("unified_processor.log")
    ]
)
logger = logging.getLogger(__name__)

class UnifiedBookmarkProcessor:
    """
    Unified processor for bookmarks from various sources.
    
    This class provides a standardized way to process bookmarks from:
    - Twitter/X
    - GitHub
    - Web content
    
    It standardizes metadata and generates rich full_text fields.
    """
    
    def __init__(self, cache_dir: str = './data'):
        """
        Initialize the unified processor.
        
        Args:
            cache_dir: Directory for cached data
        """
        self.cache_dir = Path(cache_dir)
        
        # Initialize individual processors
        self.tweet_processor = TweetProcessor(cache_dir=cache_dir)
        self.github_scraper = GitHubScraper()
        self.web_scraper = WebScraper(cache_dir=str(self.cache_dir / 'web_cache'))
        
        logger.info(f"UnifiedBookmarkProcessor initialized with cache_dir={cache_dir}")
    
    def process_bookmark(self, bookmark: Dict) -> Dict:
        """
        Process a bookmark and enrich it with standardized data.
        
        Args:
            bookmark: The bookmark to process
            
        Returns:
            The processed bookmark with enriched data
        """
        url = bookmark.get('url', '')
        source = bookmark.get('source', '')
        
        logger.info(f"Processing bookmark: {url} (source: {source})")
        
        # Skip if no URL
        if not url:
            logger.warning(f"Skipping bookmark with no URL")
            bookmark['processing_error'] = "No URL provided"
            return bookmark
        
        try:
            # Determine the source if not specified or refine it
            if not source:
                source = self._detect_source(url)
                bookmark['source'] = source
                logger.info(f"Detected source: {source}")
            
            # Process according to source
            if 'twitter' in source or 'x.com' in url:
                self._process_twitter_bookmark(bookmark)
            elif 'github' in source or 'github.com' in url:
                self._process_github_bookmark(bookmark)
            else:
                self._process_web_bookmark(bookmark)
            
            # Add processing timestamp
            bookmark['processed_at'] = datetime.now().isoformat()
            
            return bookmark
            
        except Exception as e:
            logger.error(f"Error processing bookmark {url}: {str(e)}")
            bookmark['processing_error'] = str(e)
            return bookmark
    
    def _detect_source(self, url: str) -> str:
        """
        Detect the source type from a URL.
        
        Args:
            url: The URL to analyze
            
        Returns:
            The detected source type
        """
        url_lower = url.lower()
        
        if 'twitter.com' in url_lower or 'x.com' in url_lower:
            return 'twitter'
        elif 'github.com' in url_lower:
            return 'github'
        else:
            return 'web'
    
    def _process_twitter_bookmark(self, bookmark: Dict) -> None:
        """
        Process a Twitter bookmark.
        
        Args:
            bookmark: The bookmark to process
        """
        url = bookmark.get('url', '')
        
        # Process the URL with TweetProcessor
        result = self.tweet_processor.process_tweet_url(url)
        
        if result['status'] == 'success':
            # Update the bookmark with processed data
            bookmark['full_text'] = result['full_text']
            bookmark['markdown'] = result['markdown']
            
            # Update content if not present
            if not bookmark.get('content') and result.get('content'):
                bookmark['content'] = result['content']
            
            # Update or add metadata
            if 'metadata' not in bookmark:
                bookmark['metadata'] = {}
                
            # Add tweet-specific metadata
            bookmark['metadata']['processed_with'] = 'TweetProcessor'
            bookmark['metadata']['tweet_processed_at'] = datetime.now().isoformat()
            
            # Add author info if available
            if 'author' in result.get('metadata', {}):
                bookmark['metadata']['author'] = result['metadata']['author']
            
            # Add metrics if available
            if 'metrics' in result.get('metadata', {}):
                bookmark['metadata']['tweet_metrics'] = result['metadata']['metrics']
            
            # Add thread info if it's a thread
            if result.get('is_thread', False):
                bookmark['metadata']['is_thread'] = True
                bookmark['metadata']['thread_size'] = result.get('metadata', {}).get('thread', {}).get('total_tweets', 0)
                
            logger.info(f"Successfully processed Twitter bookmark: {url}")
        else:
            logger.error(f"Failed to process Twitter bookmark {url}: {result.get('error', 'Unknown error')}")
            bookmark['processing_error'] = result.get('error', 'Failed to process Twitter content')
    
    def _process_github_bookmark(self, bookmark: Dict) -> None:
        """
        Process a GitHub bookmark.
        
        Args:
            bookmark: The bookmark to process
        """
        url = bookmark.get('url', '')
        
        # Process the URL with GitHubScraper
        result = self.github_scraper.process_url(url)
        
        if result['status'] == 'success':
            # Update the bookmark with processed data
            bookmark['full_text'] = result['content']
            bookmark['markdown'] = result['content']
            
            # Update content if not present
            if not bookmark.get('content') and result.get('content'):
                bookmark['content'] = result['content']
                
            # Update or add metadata
            if 'metadata' not in bookmark:
                bookmark['metadata'] = {}
                
            # Add GitHub-specific metadata
            bookmark['metadata'].update(result.get('metadata', {}))
            bookmark['metadata']['processed_with'] = 'GitHubScraper'
            bookmark['metadata']['github_processed_at'] = datetime.now().isoformat()
            
            # Store raw README separately if available
            if result.get('github_readme'):
                bookmark['metadata']['github_readme'] = result['github_readme']
                
            logger.info(f"Successfully processed GitHub bookmark: {url}")
        else:
            logger.error(f"Failed to process GitHub bookmark {url}: {result.get('error', 'Unknown error')}")
            bookmark['processing_error'] = result.get('error', 'Failed to process GitHub content')
    
    def _process_web_bookmark(self, bookmark: Dict) -> None:
        """
        Process a general web bookmark.
        
        Args:
            bookmark: The bookmark to process
        """
        url = bookmark.get('url', '')
        
        # Process the URL with WebScraper
        result = self.web_scraper.scrape_url(url)
        
        if result['status'] == 'success':
            # Update the bookmark with processed data
            bookmark['full_text'] = result.get('markdown', result.get('content', ''))
            bookmark['markdown'] = result.get('markdown', '')
            
            # Update content if not present
            if not bookmark.get('content') and result.get('content'):
                bookmark['content'] = result['content']
                
            # Update or add metadata
            if 'metadata' not in bookmark:
                bookmark['metadata'] = {}
                
            # Add web-specific metadata
            bookmark['metadata'].update(result.get('metadata', {}))
            bookmark['metadata']['processed_with'] = 'WebScraper'
            bookmark['metadata']['web_processed_at'] = datetime.now().isoformat()
            
            logger.info(f"Successfully processed web bookmark: {url}")
        else:
            logger.error(f"Failed to process web bookmark {url}: {result.get('error', 'Unknown error')}")
            bookmark['processing_error'] = result.get('error', 'Failed to process web content')

def load_bookmarks(bookmark_file: str) -> Optional[List[Dict]]:
    """Load bookmarks from JSONL file (each line is a JSON object)."""
    bookmarks = []
    try:
        with open(bookmark_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():  # Skip empty lines
                    try:
                        bookmark = json.loads(line.strip())
                        bookmarks.append(bookmark)
                    except json.JSONDecodeError as e:
                        logger.error(f"Error parsing JSON line: {str(e)}")
        
        logger.info(f"Loaded {len(bookmarks)} bookmarks from {bookmark_file}")
        return bookmarks
    except Exception as e:
        logger.error(f"Error loading bookmarks from {bookmark_file}: {str(e)}")
        return None

def save_bookmarks(bookmarks: List[Dict], output_file: str) -> bool:
    """Save bookmarks to JSONL file (each line is a JSON object)."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for bookmark in bookmarks:
                f.write(json.dumps(bookmark, ensure_ascii=False) + '\n')
        logger.info(f"Saved {len(bookmarks)} bookmarks to {output_file}")
        return True
    except Exception as e:
        logger.error(f"Error saving bookmarks to {output_file}: {str(e)}")
        return False

def generate_stats(bookmarks: List[Dict]) -> Dict:
    """Generate statistics for processed bookmarks."""
    stats = {
        'total': len(bookmarks),
        'sources': {},
        'processed': 0,
        'errors': 0,
        'full_text_coverage': 0,
        'processing_time': datetime.now().isoformat()
    }
    
    # Count by source
    for bookmark in bookmarks:
        source = bookmark.get('source', 'unknown')
        stats['sources'][source] = stats['sources'].get(source, 0) + 1
        
        # Check if processed
        if 'processed_at' in bookmark:
            stats['processed'] += 1
            
        # Check if error
        if 'processing_error' in bookmark:
            stats['errors'] += 1
            
        # Check if full_text exists
        if bookmark.get('full_text'):
            stats['full_text_coverage'] += 1
    
    # Calculate percentages
    if stats['total'] > 0:
        stats['processed_percent'] = round(stats['processed'] / stats['total'] * 100, 1)
        stats['errors_percent'] = round(stats['errors'] / stats['total'] * 100, 1)
        stats['full_text_coverage_percent'] = round(stats['full_text_coverage'] / stats['total'] * 100, 1)
    
    return stats

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Unified bookmark processor")
    parser.add_argument("--input", "-i", required=True, help="Input bookmarks JSON file")
    parser.add_argument("--output", "-o", help="Output bookmarks JSON file (defaults to input file with .processed suffix)")
    parser.add_argument("--stats", "-s", action="store_true", help="Generate statistics file")
    parser.add_argument("--cache-dir", "-c", default="./data", help="Cache directory path")
    parser.add_argument("--source-filter", "-f", help="Only process bookmarks from this source (twitter, github, web)")
    parser.add_argument("--limit", "-l", type=int, help="Limit processing to first N bookmarks")
    parser.add_argument("--backup", "-b", action="store_true", help="Create backup of input file before processing")
    
    args = parser.parse_args()
    
    # Set default output file if not provided
    if not args.output:
        output_path = Path(args.input)
        args.output = str(output_path.with_stem(f"{output_path.stem}.processed"))
    
    # Backup input file if requested
    if args.backup:
        backup_file = f"{args.input}.bak.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        try:
            import shutil
            shutil.copy2(args.input, backup_file)
            logger.info(f"Created backup of input file at {backup_file}")
        except Exception as e:
            logger.error(f"Failed to create backup: {str(e)}")
    
    # Load bookmarks
    bookmarks = load_bookmarks(args.input)
    if not bookmarks:
        logger.error("Failed to load bookmarks. Exiting.")
        return 1
    
    logger.info(f"Loaded {len(bookmarks)} bookmarks from {args.input}")
    
    # Initialize processor
    processor = UnifiedBookmarkProcessor(cache_dir=args.cache_dir)
    
    # Apply limit if provided
    if args.limit and args.limit > 0:
        bookmarks_to_process = bookmarks[:args.limit]
        logger.info(f"Limiting processing to first {args.limit} bookmarks")
    else:
        bookmarks_to_process = bookmarks
    
    # Process bookmarks
    processed_count = 0
    error_count = 0
    skipped_count = 0
    
    for i, bookmark in enumerate(bookmarks_to_process):
        # Apply source filter if provided
        if args.source_filter:
            source = bookmark.get('source', '')
            if source != args.source_filter:
                skipped_count += 1
                continue
        
        logger.info(f"Processing bookmark {i+1}/{len(bookmarks_to_process)}: {bookmark.get('url', 'No URL')}")
        
        try:
            # Process the bookmark
            processor.process_bookmark(bookmark)
            
            # Check if processing succeeded
            if 'processing_error' in bookmark:
                logger.error(f"Error processing bookmark {i+1}: {bookmark['processing_error']}")
                error_count += 1
            else:
                processed_count += 1
                
        except Exception as e:
            logger.error(f"Exception processing bookmark {i+1}: {str(e)}")
            bookmark['processing_error'] = str(e)
            error_count += 1
    
    logger.info(f"Processing completed: {processed_count} processed, {error_count} errors, {skipped_count} skipped")
    
    # Save processed bookmarks
    success = save_bookmarks(bookmarks, args.output)
    if not success:
        logger.error(f"Failed to save processed bookmarks to {args.output}")
        return 1
    
    # Generate statistics if requested
    if args.stats:
        stats = generate_stats(bookmarks)
        stats_file = f"{args.output}.stats.json"
        try:
            with open(stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved statistics to {stats_file}")
            
            # Also show summary in log
            logger.info(f"Processing summary:")
            logger.info(f"Total: {stats['total']} bookmarks")
            logger.info(f"Processed: {stats['processed']} ({stats.get('processed_percent', 0)}%)")
            logger.info(f"Errors: {stats['errors']} ({stats.get('errors_percent', 0)}%)")
            logger.info(f"Full text coverage: {stats['full_text_coverage']} ({stats.get('full_text_coverage_percent', 0)}%)")
            logger.info(f"Sources: {', '.join([f'{k}: {v}' for k, v in stats['sources'].items()])}")
            
        except Exception as e:
            logger.error(f"Failed to save statistics: {str(e)}")
    
    return 0

if __name__ == "__main__":
    exit(main()) 