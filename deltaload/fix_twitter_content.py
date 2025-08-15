#!/usr/bin/env python3
"""
Fix Twitter content in processed bookmarks by ensuring that the text content
in the full_text field matches the original tweet content.
"""

import os
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("fix_twitter_content.log")
    ]
)
logger = logging.getLogger(__name__)

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

def fix_twitter_bookmark(bookmark: Dict) -> Dict:
    """
    Fix Twitter bookmark by ensuring the original content is properly reflected
    in the full_text and markdown fields.
    """
    # Only process Twitter bookmarks
    source = bookmark.get('source', '')
    if 'twitter' not in source.lower():
        return bookmark
    
    # Get the original content
    original_content = bookmark.get('content', '')
    
    # Skip if no original content
    if not original_content:
        logger.warning(f"Skipping bookmark with no original content: {bookmark.get('url', 'No URL')}")
        return bookmark
    
    # Get the current markdown and full_text
    current_markdown = bookmark.get('markdown', '')
    
    # Check if the original content is in the markdown
    # If not, we need to fix it
    if original_content not in current_markdown:
        logger.info(f"Fixing content mismatch for {bookmark.get('url', 'No URL')}")
        
        # Extract metadata from current markdown
        header_lines = []
        content_start = False
        
        for line in current_markdown.split('\n'):
            if '## Content' in line:
                content_start = True
                header_lines.append(line)
                continue
            
            if not content_start:
                header_lines.append(line)
            elif content_start and not line.strip():
                # Keep empty lines after content marker
                header_lines.append(line)
            else:
                # Stop at first non-empty line after content marker
                break
        
        # Generate new markdown with original content
        new_markdown = '\n'.join(header_lines) + '\n'
        new_markdown += original_content + '\n\n'
        
        # Add source link if present in original markdown
        if '*Source:' in current_markdown:
            source_line = [line for line in current_markdown.split('\n') if '*Source:' in line]
            if source_line:
                new_markdown += '\n' + source_line[0] + '\n'
        
        # Update bookmark
        bookmark['markdown'] = new_markdown
        bookmark['full_text'] = new_markdown
        bookmark['fixed_at'] = datetime.now().isoformat()
        
        # Add a flag to indicate this was fixed
        if 'metadata' not in bookmark:
            bookmark['metadata'] = {}
        bookmark['metadata']['content_fixed'] = True
    
    return bookmark

def process_bookmarks(bookmarks: List[Dict]) -> List[Dict]:
    """Process all bookmarks, fixing Twitter content as needed."""
    fixed_count = 0
    twitter_count = 0
    
    for i, bookmark in enumerate(bookmarks):
        source = bookmark.get('source', '')
        if 'twitter' in source.lower():
            twitter_count += 1
            
            # Check if content needs fixing
            original = bookmark.copy()
            fixed = fix_twitter_bookmark(bookmark)
            
            # Count if we actually made a change
            if fixed.get('metadata', {}).get('content_fixed', False):
                fixed_count += 1
                logger.info(f"Fixed bookmark {i+1}/{len(bookmarks)}: {fixed.get('url', 'No URL')}")
            
            # Update the bookmark in place
            bookmarks[i] = fixed
    
    logger.info(f"Processed {twitter_count} Twitter bookmarks")
    logger.info(f"Fixed content for {fixed_count} bookmarks")
    
    return bookmarks

def main():
    """Main function to fix Twitter content in bookmarks."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Fix Twitter content in processed bookmarks")
    parser.add_argument('--input', '-i', required=True, help="Input JSONL file")
    parser.add_argument('--output', '-o', help="Output JSONL file (defaults to input-fixed.jsonl)")
    parser.add_argument('--backup', '-b', action="store_true", help="Create a backup of the input file")
    
    args = parser.parse_args()
    
    # Set default output file if not provided
    if not args.output:
        input_path = Path(args.input)
        args.output = str(input_path.with_stem(f"{input_path.stem}-fixed"))
    
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
    
    # Process bookmarks
    fixed_bookmarks = process_bookmarks(bookmarks)
    
    # Save fixed bookmarks
    success = save_bookmarks(fixed_bookmarks, args.output)
    if not success:
        logger.error("Failed to save fixed bookmarks. Exiting.")
        return 1
    
    logger.info(f"Twitter content fix complete. See {args.output} for the fixed data.")
    return 0

if __name__ == "__main__":
    exit(main())