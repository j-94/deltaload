#!/usr/bin/env python3
"""
Test script for GitHub README extraction improvements.
Tests the enhanced GitHub scraper and full_text generation.
"""

import json
import logging
import os
import sys
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Add the parent directory to the Python path so we can import from tools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the GitHubScraper
from tools.github_scraper import GitHubScraper

# Import the enhance_github_bookmark function
from add_full_text import enhance_github_bookmark

def test_github_readme_extraction(url):
    """
    Test GitHub README extraction and enhancement.
    
    Args:
        url: GitHub repository URL to test
    """
    logger.info(f"Testing GitHub README extraction for: {url}")
    
    # Initialize the GitHub scraper
    scraper = GitHubScraper()
    
    # Process the GitHub URL
    result = scraper.process_url(url)
    
    # Check if successful
    if result['status'] != 'success':
        logger.error(f"Failed to extract GitHub data: {result.get('error', 'Unknown error')}")
        return
    
    # Log metadata
    logger.info(f"Extracted metadata: {json.dumps(result['metadata'], indent=2)}")
    
    # Check if README was extracted
    if 'github_readme' in result and result['github_readme']:
        readme_preview = result['github_readme'][:200] + "..." if len(result['github_readme']) > 200 else result['github_readme']
        logger.info(f"Extracted README (first 200 chars): {readme_preview}")
    else:
        logger.warning("No README content extracted")
    
    # Create a bookmark object
    bookmark = {
        'url': url,
        'source': 'github',
        'content': result.get('content', ''),
        'metadata': result.get('metadata', {}),
        'github_readme': result.get('github_readme', ''),
        'created_at': result.get('created_at', datetime.now().isoformat())
    }
    
    # Enhance the bookmark with full_text
    enhanced = enhance_github_bookmark(bookmark)
    
    # Write the results to a file
    output_file = "test_github_enhance_output.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(enhanced, indent=2))
    
    logger.info(f"Enhanced bookmark saved to {output_file}")
    
    # Preview the full_text
    full_text_preview = enhanced.get('full_text', '')[:300] + "..." if len(enhanced.get('full_text', '')) > 300 else enhanced.get('full_text', '')
    logger.info(f"Generated full_text preview: {full_text_preview}")

def main():
    """Main function."""
    # Test URLs
    urls = [
        # Popular repositories with good README files
        "https://github.com/expressjs/express",
        "https://github.com/sindresorhus/awesome",
        "https://github.com/facebook/react",
        # Add your own repositories to test
    ]
    
    # Test each URL
    for url in urls:
        test_github_readme_extraction(url)
        print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main() 