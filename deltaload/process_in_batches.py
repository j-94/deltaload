#!/usr/bin/env python3
"""
Batch processor for the unified bookmark processor.

This script processes bookmarks in batches to handle large datasets,
saving intermediate results and providing progress updates.
"""

import os
import sys
import json
import logging
import argparse
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("batch_processing.log")
    ]
)
logger = logging.getLogger(__name__)

def load_bookmark_batch(file_path: str, start_index: int, batch_size: int) -> Tuple[List[Dict], int]:
    """
    Load a batch of bookmarks from a JSONL file.
    
    Args:
        file_path: Path to the JSONL file
        start_index: Starting line index (0-based)
        batch_size: Number of bookmarks to load
        
    Returns:
        Tuple of (bookmarks, total_lines)
    """
    bookmarks = []
    total_lines = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Count total lines first
            total_lines = sum(1 for _ in f)
            
        # Now load the specified batch
        with open(file_path, 'r', encoding='utf-8') as f:
            # Skip to start_index
            for i in range(start_index):
                next(f, None)
            
            # Read batch_size lines
            for i in range(batch_size):
                line = next(f, None)
                if line is None:
                    break
                    
                if line.strip():
                    try:
                        bookmark = json.loads(line.strip())
                        bookmarks.append(bookmark)
                    except json.JSONDecodeError as e:
                        logger.error(f"Error parsing JSON at line {start_index + i + 1}: {str(e)}")
        
        logger.info(f"Loaded {len(bookmarks)} bookmarks from {file_path} (starting at index {start_index})")
        return bookmarks, total_lines
    except Exception as e:
        logger.error(f"Error loading bookmarks from {file_path}: {str(e)}")
        return [], 0

def save_bookmark_batch(bookmarks: List[Dict], output_file: str, append: bool = False) -> bool:
    """
    Save a batch of bookmarks to a JSONL file.
    
    Args:
        bookmarks: List of bookmark dictionaries
        output_file: Path to the output file
        append: Whether to append to the file
        
    Returns:
        Success status
    """
    mode = 'a' if append else 'w'
    try:
        with open(output_file, mode, encoding='utf-8') as f:
            for bookmark in bookmarks:
                f.write(json.dumps(bookmark, ensure_ascii=False) + '\n')
        
        logger.info(f"Saved {len(bookmarks)} bookmarks to {output_file} (append={append})")
        return True
    except Exception as e:
        logger.error(f"Error saving bookmarks to {output_file}: {str(e)}")
        return False

def process_batch(bookmarks: List[Dict], source_filter: Optional[str] = None) -> Tuple[List[Dict], Dict]:
    """
    Process a batch of bookmarks using the unified processor.
    
    Args:
        bookmarks: List of bookmark dictionaries
        source_filter: Optional filter for specific source
        
    Returns:
        Tuple of (processed_bookmarks, batch_stats)
    """
    from unified_bookmark_processor import UnifiedBookmarkProcessor
    
    # Initialize the processor
    processor = UnifiedBookmarkProcessor(cache_dir='./data')
    
    # Process the bookmarks one by one
    processed_bookmarks = []
    for bookmark in bookmarks:
        # Apply source filter if provided
        if source_filter and bookmark.get('source', '') != source_filter:
            # Skip this bookmark but keep it in the results
            processed_bookmarks.append(bookmark)
            continue
            
        # Process the bookmark
        processed_bookmark = processor.process_bookmark(bookmark)
        processed_bookmarks.append(processed_bookmark)
    
    # Generate batch stats
    batch_stats = {
        'total': len(bookmarks),
        'processed': sum(1 for b in processed_bookmarks if 'processed_at' in b),
        'errors': sum(1 for b in processed_bookmarks if 'processing_error' in b),
        'full_text_coverage': sum(1 for b in processed_bookmarks if b.get('full_text')),
        'sources': {}
    }
    
    # Count by source
    for bookmark in bookmarks:
        source = bookmark.get('source', 'unknown')
        batch_stats['sources'][source] = batch_stats['sources'].get(source, 0) + 1
    
    # Calculate percentages
    if batch_stats['total'] > 0:
        batch_stats['processed_percent'] = (batch_stats['processed'] / batch_stats['total']) * 100
        batch_stats['errors_percent'] = (batch_stats['errors'] / batch_stats['total']) * 100
        batch_stats['full_text_coverage_percent'] = (batch_stats['full_text_coverage'] / batch_stats['total']) * 100
    
    return processed_bookmarks, batch_stats

def merge_stats(stats_list: List[Dict]) -> Dict:
    """
    Merge multiple batch statistics into one.
    
    Args:
        stats_list: List of batch statistics dictionaries
        
    Returns:
        Merged statistics dictionary
    """
    merged = {
        'total': 0,
        'processed': 0,
        'errors': 0,
        'full_text_coverage': 0,
        'sources': {},
        'batches': len(stats_list),
        'processing_time': datetime.now().isoformat()
    }
    
    for stats in stats_list:
        merged['total'] += stats['total']
        merged['processed'] += stats['processed']
        merged['errors'] += stats['errors']
        merged['full_text_coverage'] += stats['full_text_coverage']
        
        # Merge sources
        for source, count in stats.get('sources', {}).items():
            merged['sources'][source] = merged['sources'].get(source, 0) + count
    
    # Calculate percentages
    if merged['total'] > 0:
        merged['processed_percent'] = (merged['processed'] / merged['total']) * 100
        merged['errors_percent'] = (merged['errors'] / merged['total']) * 100
        merged['full_text_coverage_percent'] = (merged['full_text_coverage'] / merged['total']) * 100
    
    return merged

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Process bookmarks in batches")
    parser.add_argument("--input", "-i", required=True, help="Input JSONL file")
    parser.add_argument("--output", "-o", help="Output JSONL file")
    parser.add_argument("--batch-size", "-b", type=int, default=100, help="Batch size")
    parser.add_argument("--start-index", "-s", type=int, default=0, help="Starting index")
    parser.add_argument("--num-batches", "-n", type=int, help="Number of batches to process (default: all)")
    parser.add_argument("--source-filter", "-f", help="Only process bookmarks from specific source")
    parser.add_argument("--stats-file", help="Statistics output file")
    parser.add_argument("--checkpoint", action="store_true", help="Create checkpoint files after each batch")
    
    args = parser.parse_args()
    
    # Set default output file if not specified
    if not args.output:
        base, ext = os.path.splitext(args.input)
        args.output = f"{base}.processed{ext}"
    
    # Set default stats file if not specified
    if not args.stats_file:
        args.stats_file = f"{args.output}.stats.json"
    
    # Initialize
    start_time = datetime.now()
    batch_stats_list = []
    total_processed = 0
    
    # Get the first batch to determine total size
    first_batch, total_lines = load_bookmark_batch(args.input, args.start_index, 1)
    logger.info(f"Total records in file: {total_lines}")
    
    # Calculate total batches
    total_batches = (total_lines - args.start_index + args.batch_size - 1) // args.batch_size
    if args.num_batches and args.num_batches < total_batches:
        total_batches = args.num_batches
    
    logger.info(f"Processing {total_batches} batches of size {args.batch_size}")
    
    # Process in batches
    for batch_num in range(total_batches):
        batch_start_index = args.start_index + (batch_num * args.batch_size)
        
        # Skip if beyond end of file
        if batch_start_index >= total_lines:
            break
        
        logger.info(f"Processing batch {batch_num + 1}/{total_batches} (lines {batch_start_index + 1}-{min(batch_start_index + args.batch_size, total_lines)})")
        
        # Load batch
        batch_bookmarks, _ = load_bookmark_batch(args.input, batch_start_index, args.batch_size)
        if not batch_bookmarks:
            logger.warning(f"No bookmarks loaded for batch {batch_num + 1}")
            continue
        
        # Process batch
        processed_batch, batch_stats = process_batch(batch_bookmarks, args.source_filter)
        batch_stats_list.append(batch_stats)
        total_processed += batch_stats['processed']
        
        # Save batch
        append = batch_num > 0
        if args.checkpoint:
            # Save checkpoint file
            checkpoint_file = f"{args.output}.batch_{batch_num + 1}.jsonl"
            save_bookmark_batch(processed_batch, checkpoint_file, False)
        
        # Save to main output file
        save_bookmark_batch(processed_batch, args.output, append)
        
        # Print progress
        elapsed = datetime.now() - start_time
        records_per_second = total_processed / elapsed.total_seconds() if elapsed.total_seconds() > 0 else 0
        estimated_total_time = timedelta(seconds=total_lines / records_per_second) if records_per_second > 0 else "unknown"
        estimated_remaining = timedelta(seconds=(total_lines - batch_start_index - len(batch_bookmarks)) / records_per_second) if records_per_second > 0 else "unknown"
        
        logger.info(f"Batch {batch_num + 1} complete: {batch_stats['processed']}/{batch_stats['total']} processed, {batch_stats['full_text_coverage']} with full text")
        logger.info(f"Progress: {total_processed}/{total_lines} records ({total_processed/total_lines*100:.1f}%)")
        logger.info(f"Speed: {records_per_second:.1f} records/second (estimated total time: {estimated_total_time}, remaining: {estimated_remaining})")
    
    # Merge statistics
    merged_stats = merge_stats(batch_stats_list)
    merged_stats['start_time'] = start_time.isoformat()
    merged_stats['end_time'] = datetime.now().isoformat()
    merged_stats['elapsed_seconds'] = (datetime.now() - start_time).total_seconds()
    
    # Save statistics
    try:
        with open(args.stats_file, 'w', encoding='utf-8') as f:
            json.dump(merged_stats, f, indent=2)
        logger.info(f"Saved statistics to {args.stats_file}")
    except Exception as e:
        logger.error(f"Error saving statistics: {str(e)}")
    
    # Print final summary
    logger.info(f"Processing complete: {merged_stats['processed']}/{merged_stats['total']} records processed")
    logger.info(f"Full text coverage: {merged_stats['full_text_coverage']}/{merged_stats['total']} ({merged_stats['full_text_coverage_percent']:.1f}%)")
    logger.info(f"Errors: {merged_stats['errors']}/{merged_stats['total']} ({merged_stats['errors_percent']:.1f}%)")
    logger.info(f"Total time: {datetime.now() - start_time}")

if __name__ == "__main__":
    main()