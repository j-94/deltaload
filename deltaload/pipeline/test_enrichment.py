#!/usr/bin/env python3
"""
Test script to verify the enrichment functionality works correctly.
This script tests enrichment on a small sample of bookmarks.
"""

import os
import json
import logging
import argparse
import tempfile
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Path to the main data file
BASE_DIR = Path(__file__).parent.parent
DATA_PATH = BASE_DIR / "data-bookmark.jsonl"

def create_sample_data(sample_size=5):
    """Create a sample file with a few bookmarks from each source."""
    if not DATA_PATH.exists():
        logger.error(f"Data file not found: {DATA_PATH}")
        return None
        
    # Read the original data
    bookmarks = []
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                bookmark = json.loads(line.strip())
                bookmarks.append(bookmark)
            except json.JSONDecodeError:
                continue
                
    logger.info(f"Read {len(bookmarks)} bookmarks from {DATA_PATH}")
    
    # Group by source
    sources = {}
    for bookmark in bookmarks:
        source = bookmark.get('source', 'unknown')
        if source not in sources:
            sources[source] = []
        sources[source].append(bookmark)
        
    logger.info(f"Found sources: {list(sources.keys())}")
    
    # Create a sample with a few bookmarks from each source
    sample = []
    for source, items in sources.items():
        count = min(sample_size, len(items))
        sample.extend(items[:count])
        logger.info(f"Added {count} bookmarks from '{source}'")
        
    # Create a temporary file for the sample
    fd, sample_path = tempfile.mkstemp(suffix='.jsonl', prefix='sample_')
    os.close(fd)
    
    # Write the sample data
    with open(sample_path, 'w', encoding='utf-8') as f:
        for bookmark in sample:
            json.dump(bookmark, f, ensure_ascii=False)
            f.write('\n')
            
    logger.info(f"Created sample data file with {len(sample)} bookmarks: {sample_path}")
    return sample_path
    
def run_enrichment_test(sample_path, args):
    """Run the enrichment script on the sample data."""
    import subprocess
    
    # Create output path
    output_path = sample_path.replace('.jsonl', '_enriched.jsonl')
    
    # Build command
    cmd = [
        'python', str(BASE_DIR / "enrich_bookmarks.py"),
        sample_path,
        "--output-file", output_path,
        "--cache-dir", str(BASE_DIR / "test_cache")
    ]
    
    # Add optional arguments
    if args.force_refresh:
        cmd.append("--force-refresh")
        
    logger.info(f"Running enrichment command: {' '.join(cmd)}")
    
    # Run the command
    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        
        logger.info(f"Enrichment command output: {result.stdout}")
        
        # Check if enriched file exists
        if not os.path.exists(output_path):
            logger.error(f"Enriched file not created: {output_path}")
            return False
            
        # Compare the original and enriched data
        compare_results(sample_path, output_path)
        
        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f"Enrichment command failed with exit code {e.returncode}")
        logger.error(f"Stdout: {e.stdout}")
        logger.error(f"Stderr: {e.stderr}")
        return False
        
def compare_results(original_path, enriched_path):
    """Compare the original and enriched data to verify enrichment."""
    # Read original data
    original = []
    with open(original_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                bookmark = json.loads(line.strip())
                original.append(bookmark)
            except json.JSONDecodeError:
                continue
                
    # Read enriched data
    enriched = []
    with open(enriched_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                bookmark = json.loads(line.strip())
                enriched.append(bookmark)
            except json.JSONDecodeError:
                continue
                
    logger.info(f"Comparing {len(original)} original bookmarks with {len(enriched)} enriched bookmarks")
    
    # Check if counts match
    if len(original) != len(enriched):
        logger.warning(f"Count mismatch: {len(original)} original vs {len(enriched)} enriched")
        
    # Check each bookmark
    enriched_by_url = {b.get('url'): b for b in enriched if 'url' in b}
    
    for i, bookmark in enumerate(original):
        url = bookmark.get('url')
        if not url:
            logger.warning(f"Original bookmark at position {i} has no URL")
            continue
            
        if url not in enriched_by_url:
            logger.warning(f"URL not found in enriched data: {url}")
            continue
            
        enriched_bookmark = enriched_by_url[url]
        
        # Check if metadata was enhanced
        original_metadata = bookmark.get('metadata', {})
        if isinstance(original_metadata, str):
            try:
                original_metadata = json.loads(original_metadata)
            except json.JSONDecodeError:
                original_metadata = {}
                
        enriched_metadata = enriched_bookmark.get('metadata', {})
        if isinstance(enriched_metadata, str):
            try:
                enriched_metadata = json.loads(enriched_metadata)
            except json.JSONDecodeError:
                enriched_metadata = {}
                
        # Check for enrichment markers
        if 'enriched_at' in enriched_metadata:
            logger.info(f"Bookmark enriched: {url} at {enriched_metadata['enriched_at']}")
        else:
            logger.warning(f"No enrichment marker for: {url}")
            
        # Compare content
        original_content = bookmark.get('content', '')
        enriched_content = enriched_bookmark.get('content', '')
        
        if enriched_content and enriched_content != original_content:
            logger.info(f"Content enriched for {url}: {len(original_content)} chars -> {len(enriched_content)} chars")
        elif not enriched_content and not original_content:
            logger.warning(f"Both original and enriched have empty content: {url}")
        elif not enriched_content:
            logger.warning(f"Enriched content is empty but original had content: {url}")
            
    logger.info(f"Results saved to {enriched_path}")

def main():
    parser = argparse.ArgumentParser(description="Test the enrichment functionality")
    parser.add_argument("--sample-size", type=int, default=2,
                       help="Number of bookmarks to sample from each source")
    parser.add_argument("--force-refresh", action="store_true",
                       help="Force refresh cached content during enrichment")
    parser.add_argument("--keep-files", action="store_true",
                       help="Keep temporary files after testing")
    
    args = parser.parse_args()
    
    # Create sample data
    sample_path = create_sample_data(args.sample_size)
    if not sample_path:
        return 1
        
    try:
        # Run enrichment test
        success = run_enrichment_test(sample_path, args)
        
        if success:
            logger.info("Enrichment test completed successfully")
        else:
            logger.error("Enrichment test failed")
            
        return 0 if success else 1
        
    finally:
        # Clean up temporary files
        if not args.keep_files:
            try:
                output_path = sample_path.replace('.jsonl', '_enriched.jsonl')
                if os.path.exists(sample_path):
                    os.unlink(sample_path)
                if os.path.exists(output_path):
                    os.unlink(output_path)
            except Exception as e:
                logger.error(f"Error cleaning up temporary files: {e}")

if __name__ == "__main__":
    import sys
    sys.exit(main())