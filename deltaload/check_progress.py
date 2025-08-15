#!/usr/bin/env python3
"""
Script to check the progress of batch processing.
"""

import os
import sys
import glob
import json
from datetime import datetime

def count_lines(file_path):
    """Count the number of lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"Error counting lines in {file_path}: {str(e)}")
        return 0

def check_checkpoint_files(output_prefix):
    """Find and analyze checkpoint files."""
    pattern = f"{output_prefix}.batch_*.jsonl"
    checkpoint_files = glob.glob(pattern)
    
    if not checkpoint_files:
        print(f"No checkpoint files found matching pattern: {pattern}")
        return None
    
    # Sort by batch number
    checkpoint_files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
    
    total_processed = 0
    for file in checkpoint_files:
        lines = count_lines(file)
        total_processed += lines
        batch_num = int(file.split('_')[-1].split('.')[0])
        print(f"Batch {batch_num}: {lines} bookmarks")
    
    return {
        'latest_batch': int(checkpoint_files[-1].split('_')[-1].split('.')[0]),
        'total_processed': total_processed,
        'checkpoint_files': len(checkpoint_files)
    }

def check_output_file(output_file):
    """Check the output file status."""
    if not os.path.exists(output_file):
        print(f"Output file not found: {output_file}")
        return None
    
    lines = count_lines(output_file)
    print(f"Output file contains {lines} bookmarks")
    return {'lines': lines}

def check_stats_file(stats_file):
    """Check the stats file if it exists."""
    if not os.path.exists(stats_file):
        print(f"Stats file not found: {stats_file}")
        return None
    
    try:
        with open(stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)
        
        print(f"Processing stats:")
        print(f"  Total bookmarks: {stats.get('total', 'N/A')}")
        print(f"  Processed: {stats.get('processed', 'N/A')} ({stats.get('processed_percent', 'N/A')}%)")
        print(f"  Full text coverage: {stats.get('full_text_coverage', 'N/A')} ({stats.get('full_text_coverage_percent', 'N/A')}%)")
        print(f"  Errors: {stats.get('errors', 'N/A')} ({stats.get('errors_percent', 'N/A')}%)")
        
        if 'elapsed_seconds' in stats:
            elapsed = stats['elapsed_seconds']
            print(f"  Time elapsed: {elapsed:.1f} seconds ({elapsed/60:.1f} minutes)")
        
        return stats
    except Exception as e:
        print(f"Error reading stats file {stats_file}: {str(e)}")
        return None

def check_process_running():
    """Check if the batch processing is still running."""
    try:
        import subprocess
        result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
        return "process_in_batches.py" in result.stdout
    except Exception as e:
        print(f"Error checking process status: {str(e)}")
        return None

def check_log_file(log_file):
    """Check the last few lines of the log file."""
    if not os.path.exists(log_file):
        print(f"Log file not found: {log_file}")
        return None
    
    try:
        import subprocess
        result = subprocess.run(["tail", "-n", "20", log_file], capture_output=True, text=True)
        print(f"Recent log entries:")
        print(result.stdout)
        return True
    except Exception as e:
        print(f"Error reading log file {log_file}: {str(e)}")
        return None

def main():
    """Main function."""
    # Default files
    output_file = "data-bookmark-enriched-full.jsonl"
    stats_file = "processing_stats.json"
    log_file = "processing_output.log"
    
    # Allow command line override
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    if len(sys.argv) > 2:
        stats_file = sys.argv[2]
    if len(sys.argv) > 3:
        log_file = sys.argv[3]
    
    print(f"=== Batch Processing Progress Check ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ===")
    
    # Check if process is running
    is_running = check_process_running()
    if is_running is not None:
        print(f"Process status: {'Running' if is_running else 'Not running'}")
    
    # Check output file
    output_prefix = output_file.split('.jsonl')[0]
    output_stats = check_output_file(output_file)
    
    # Check checkpoint files
    checkpoint_stats = check_checkpoint_files(output_prefix)
    
    # Check stats file
    stats = check_stats_file(stats_file)
    
    # Check log file
    check_log_file(log_file)
    
    # Calculate estimated completion
    if is_running and stats and 'total' in stats and 'processed' in stats and 'elapsed_seconds' in stats:
        total = stats['total']
        processed = stats['processed']
        elapsed_seconds = stats['elapsed_seconds']
        
        if processed > 0 and elapsed_seconds > 0:
            seconds_per_record = elapsed_seconds / processed
            remaining_records = total - processed
            estimated_remaining_seconds = remaining_records * seconds_per_record
            
            from datetime import timedelta
            estimated_completion_time = datetime.now() + timedelta(seconds=estimated_remaining_seconds)
            
            print(f"\nEstimated completion:")
            print(f"  Progress: {processed}/{total} ({processed/total*100:.1f}%)")
            print(f"  Processing rate: {3600/seconds_per_record:.1f} records/hour")
            print(f"  Estimated time remaining: {timedelta(seconds=estimated_remaining_seconds)}")
            print(f"  Estimated completion time: {estimated_completion_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()