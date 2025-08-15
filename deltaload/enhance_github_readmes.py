#!/usr/bin/env python3
"""
GitHub README Enhancement Script

This script processes all GitHub bookmarks in the dataset and enhances
them with improved README content using our updated GitHub scraper.
"""

import os
import sys
import json
import logging
import argparse
from datetime import datetime
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("github_enhancement.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Import our custom modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tools.github_scraper import GitHubScraper
from add_full_text import enhance_github_bookmark

def read_jsonl(file_path):
    """Read bookmarks from a JSONL file."""
    bookmarks = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    bookmark = json.loads(line.strip())
                    bookmarks.append(bookmark)
                except json.JSONDecodeError:
                    logger.warning(f"Error decoding JSON line: {line[:100]}...")
                    continue
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
        raise
    
    return bookmarks

def write_jsonl(file_path, bookmarks):
    """Write bookmarks to a JSONL file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for bookmark in bookmarks:
                f.write(json.dumps(bookmark) + '\n')
    except Exception as e:
        logger.error(f"Error writing file {file_path}: {str(e)}")
        raise

def process_github_bookmarks(input_file, output_file, limit=None, force_refresh=False):
    """Process all GitHub bookmarks in the dataset."""
    logger.info(f"Reading bookmarks from {input_file}")
    bookmarks = read_jsonl(input_file)
    logger.info(f"Read {len(bookmarks)} bookmarks")
    
    # Filter for GitHub bookmarks
    github_bookmarks = [b for b in bookmarks if b.get('source') == 'github']
    logger.info(f"Found {len(github_bookmarks)} GitHub bookmarks")
    
    # Apply limit if specified
    if limit:
        github_bookmarks = github_bookmarks[:limit]
        logger.info(f"Limited to {len(github_bookmarks)} GitHub bookmarks")
    
    # Initialize GitHub scraper
    github_scraper = GitHubScraper()
    
    # Process each GitHub bookmark
    enhanced_github = []
    enhanced_count = 0
    readme_count = 0
    
    for bookmark in tqdm(github_bookmarks, desc="Enhancing GitHub bookmarks"):
        try:
            # Only fetch new data if force_refresh is True or if the bookmark doesn't have github_readme
            if force_refresh or 'github_readme' not in bookmark:
                # Get the repository URL
                url = bookmark.get('url')
                if not url or 'github.com' not in url:
                    logger.warning(f"Invalid GitHub URL: {url}")
                    enhanced_github.append(bookmark)
                    continue
                
                # Process the URL with the GitHub scraper
                result = github_scraper.process_url(url)
                
                if result['status'] == 'success':
                    # Update the bookmark with the new data
                    bookmark['content'] = result['content']
                    bookmark['github_readme'] = result.get('github_readme', '')
                    bookmark['metadata'] = result['metadata']
                    bookmark['enriched_at'] = datetime.now().isoformat()
                    
                    if bookmark['github_readme']:
                        readme_count += 1
                
                else:
                    logger.warning(f"Failed to process GitHub URL: {url} - {result.get('error', 'Unknown error')}")
            
            # Enhance the bookmark with full_text
            enhanced = enhance_github_bookmark(bookmark)
            enhanced_github.append(enhanced)
            enhanced_count += 1
            
        except Exception as e:
            logger.error(f"Error processing bookmark {bookmark.get('url', 'Unknown URL')}: {str(e)}")
            enhanced_github.append(bookmark)
    
    # Update the github bookmarks in the original dataset
    github_urls = {b.get('url') for b in github_bookmarks}
    
    # Create new dataset with enhanced github bookmarks
    enhanced_bookmarks = []
    for bookmark in bookmarks:
        if bookmark.get('url') in github_urls:
            # This is a GitHub bookmark that we've enhanced
            # Find the enhanced version
            for enhanced in enhanced_github:
                if enhanced.get('url') == bookmark.get('url'):
                    enhanced_bookmarks.append(enhanced)
                    break
        else:
            # This is not a GitHub bookmark, keep it as is
            enhanced_bookmarks.append(bookmark)
    
    logger.info(f"Writing {len(enhanced_bookmarks)} bookmarks to {output_file}")
    write_jsonl(output_file, enhanced_bookmarks)
    
    logger.info(f"Enhanced {enhanced_count} GitHub bookmarks")
    logger.info(f"Added README content to {readme_count} GitHub bookmarks")
    
    return {
        'total': len(bookmarks),
        'github': len(github_bookmarks),
        'processed': len(github_bookmarks),
        'enhanced': enhanced_count,
        'with_readme': readme_count
    }

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Enhance GitHub bookmarks with README content")
    parser.add_argument("input_file", help="Input JSONL file with bookmarks")
    parser.add_argument("--output", "-o", help="Output JSONL file (default: input-file-github-enhanced.jsonl)")
    parser.add_argument("--limit", "-l", type=int, help="Limit processing to specified number of bookmarks")
    parser.add_argument("--force-refresh", "-f", action="store_true", help="Force refresh all GitHub data")
    
    args = parser.parse_args()
    
    # Set output file if not specified
    if not args.output:
        base, ext = os.path.splitext(args.input_file)
        args.output = f"{base}-github-enhanced{ext}"
    
    # Process GitHub bookmarks
    stats = process_github_bookmarks(
        args.input_file,
        args.output,
        limit=args.limit,
        force_refresh=args.force_refresh
    )
    
    logger.info("GitHub README enhancement completed")
    logger.info(f"Statistics: {json.dumps(stats, indent=2)}")

if __name__ == "__main__":
    main() 