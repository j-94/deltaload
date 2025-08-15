#!/usr/bin/env python3
"""
Test script for the TweetProcessor class.

This script tests the new TweetProcessor with real tweet data and validates its output.
"""

import os
import json
import logging
import argparse
from pathlib import Path
from tools.tweet_processor import TweetProcessor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def test_with_url(processor, url, output_dir=None):
    """Test processing a tweet URL."""
    logger.info(f"Testing tweet processor with URL: {url}")
    
    # Process the URL
    result = processor.process_tweet_url(url)
    
    # Log the result status
    if result['status'] == 'success':
        logger.info(f"Successfully processed tweet: {url}")
        logger.info(f"Tweet text: {result['content'][:100]}...")
        logger.info(f"Markdown length: {len(result['markdown'])} characters")
    else:
        logger.error(f"Failed to process tweet: {result.get('error', 'Unknown error')}")
        return False
    
    # Save output if requested
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Extract tweet ID for filename
        tweet_id = processor._extract_tweet_id(url) or "unknown"
        output_file = output_path / f"processed_tweet_{tweet_id}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        logger.info(f"Saved processed result to {output_file}")
        
        # Also save markdown separately for easy inspection
        markdown_file = output_path / f"processed_tweet_{tweet_id}.md"
        with open(markdown_file, 'w', encoding='utf-8') as f:
            f.write(result['markdown'])
        logger.info(f"Saved markdown to {markdown_file}")
    
    return True

def test_with_cache_file(processor, cache_file, output_dir=None):
    """Test processing a cached tweet file."""
    logger.info(f"Testing tweet processor with cache file: {cache_file}")
    
    try:
        # Load the cache file
        with open(cache_file, 'r', encoding='utf-8') as f:
            cache_data = json.load(f)
        
        logger.info(f"Loaded cache file with {len(cache_data) if isinstance(cache_data, list) else 1} entries")
        
        # If it's a list, process the first item
        if isinstance(cache_data, list) and len(cache_data) > 0:
            tweet_data = cache_data[0]
            logger.info(f"Processing first tweet from list in cache file")
        else:
            tweet_data = cache_data
        
        # Process the tweet data
        result = processor.process_tweet_data(tweet_data)
        
        # Log the result status
        if result['status'] == 'success':
            logger.info(f"Successfully processed tweet from cache")
            logger.info(f"Tweet text: {result['content'][:100]}...")
            logger.info(f"Markdown length: {len(result['markdown'])} characters")
        else:
            logger.error(f"Failed to process tweet from cache: {result.get('error', 'Unknown error')}")
            return False
        
        # Save output if requested
        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Extract filename from cache path
            cache_filename = Path(cache_file).stem
            output_file = output_path / f"processed_{cache_filename}.json"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved processed result to {output_file}")
            
            # Also save markdown separately for easy inspection
            markdown_file = output_path / f"processed_{cache_filename}.md"
            with open(markdown_file, 'w', encoding='utf-8') as f:
                f.write(result['markdown'])
            logger.info(f"Saved markdown to {markdown_file}")
        
        return True
    
    except Exception as e:
        logger.error(f"Error processing cache file: {str(e)}")
        return False

def main():
    """Main test function."""
    parser = argparse.ArgumentParser(description="Test the TweetProcessor class.")
    parser.add_argument("--url", "-u", help="Twitter URL to test")
    parser.add_argument("--cache-file", "-c", help="Cache file to test")
    parser.add_argument("--output-dir", "-o", default="./test_output", help="Output directory for processed results")
    
    args = parser.parse_args()
    
    if not args.url and not args.cache_file:
        parser.error("Either --url or --cache-file must be provided")
    
    # Initialize the processor
    processor = TweetProcessor(cache_dir='./data')
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Test with URL if provided
    if args.url:
        success = test_with_url(processor, args.url, args.output_dir)
        if success:
            logger.info("URL processing test completed successfully")
        else:
            logger.error("URL processing test failed")
    
    # Test with cache file if provided
    if args.cache_file:
        success = test_with_cache_file(processor, args.cache_file, args.output_dir)
        if success:
            logger.info("Cache file processing test completed successfully")
        else:
            logger.error("Cache file processing test failed")

if __name__ == "__main__":
    main() 