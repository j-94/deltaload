#!/usr/bin/env python3
"""
Test script to verify metadata parsing works correctly.
"""

import json
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def test_metadata_parsing(file_path, sample_size=5):
    """Test metadata parsing from the file."""
    logger.info(f"Testing metadata parsing from {file_path}")
    
    bookmarks = []
    invalid_json_count = 0
    
    # Read sample bookmarks
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= sample_size:
                    break
                try:
                    bookmark = json.loads(line)
                    bookmarks.append(bookmark)
                except json.JSONDecodeError:
                    logger.error(f"Error parsing JSON at line {i+1}")
                    invalid_json_count += 1
    except Exception as e:
        logger.error(f"Error reading file: {str(e)}")
        return False
        
    logger.info(f"Successfully read {len(bookmarks)} sample bookmarks")
    
    # Check metadata parsing
    json_issues = []
    ast_issues = []
    
    import ast
    
    for i, bookmark in enumerate(bookmarks):
        metadata = bookmark.get('metadata', {})
        
        if isinstance(metadata, str):
            # Test JSON parsing
            try:
                # Try parsing as JSON
                parsed = json.loads(metadata)
            except json.JSONDecodeError:
                json_issues.append(f"Bookmark {i+1}: Invalid JSON in metadata")
                
                # Try parsing with ast.literal_eval as a fallback
                try:
                    parsed = ast.literal_eval(metadata)
                    logger.info(f"Bookmark {i+1}: Successfully parsed with ast.literal_eval: {parsed}")
                except (SyntaxError, ValueError):
                    ast_issues.append(f"Bookmark {i+1}: Failed to parse with ast.literal_eval")
                
    if json_issues:
        logger.info("Found JSON parsing issues:")
        for issue in json_issues:
            logger.info(f"- {issue}")
    else:
        logger.info("No JSON parsing issues found!")
        
    if ast_issues:
        logger.info("Found ast.literal_eval parsing issues:")
        for issue in ast_issues:
            logger.info(f"- {issue}")
    else:
        if json_issues:
            logger.info("All metadata could be parsed with ast.literal_eval!")
        
    return len(ast_issues) == 0

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test metadata parsing in JSONL file")
    parser.add_argument('--file', default='data-bookmark-enriched.jsonl', help='JSONL file to test')
    parser.add_argument('--sample', type=int, default=5, help='Number of bookmarks to test')
    
    args = parser.parse_args()
    
    success = test_metadata_parsing(args.file, args.sample)
    sys.exit(0 if success else 1)