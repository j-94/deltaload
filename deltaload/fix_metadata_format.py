#!/usr/bin/env python3
"""
Script to fix incorrectly formatted JSON metadata in bookmark files.
This script converts metadata using Python single quotes ('') to valid JSON double quotes ("").
"""

import json
import ast
import logging
import argparse
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def fix_metadata_in_file(input_file, output_file=None, create_backup=True):
    """
    Fix metadata format in a JSONL file.
    
    Args:
        input_file: Path to input JSONL file
        output_file: Path to output JSONL file (default: overwrite input file)
        create_backup: Whether to create a backup of the input file
        
    Returns:
        Tuple of (success, records_processed, records_fixed)
    """
    # Set output file if not specified
    if not output_file:
        output_file = input_file
        
    # Create backup if requested and we're overwriting the input file
    if create_backup and input_file == output_file:
        backup_file = f"{input_file}.bak"
        logger.info(f"Creating backup of {input_file} to {backup_file}")
        import shutil
        try:
            shutil.copy2(input_file, backup_file)
        except Exception as e:
            logger.error(f"Error creating backup: {str(e)}")
            return False, 0, 0
    
    # Process the file
    total_records = 0
    fixed_records = 0
    
    try:
        # Read all records first
        records = []
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    record = json.loads(line.strip())
                    
                    # Check if metadata needs fixing
                    metadata = record.get('metadata', {})
                    if isinstance(metadata, str):
                        try:
                            # Try to parse with JSON first
                            record['metadata'] = json.loads(metadata)
                        except json.JSONDecodeError:
                            try:
                                # Try to parse with ast.literal_eval
                                record['metadata'] = ast.literal_eval(metadata)
                                fixed_records += 1
                            except (SyntaxError, ValueError) as e:
                                logger.warning(f"Couldn't parse metadata string: {metadata}")
                                # Keep as string if we can't parse it
                                pass
                    
                    records.append(record)
                    total_records += 1
                except json.JSONDecodeError as e:
                    logger.error(f"Error parsing JSON line: {str(e)}")
        
        # Write out the fixed records
        with open(output_file, 'w', encoding='utf-8') as f:
            for record in records:
                json.dump(record, f, ensure_ascii=False)
                f.write('\n')
                
        logger.info(f"Processed {total_records} records, fixed {fixed_records} metadata entries")
        return True, total_records, fixed_records
        
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        return False, total_records, fixed_records

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Fix metadata format in bookmark files")
    parser.add_argument('input_file', help='Input JSONL file')
    parser.add_argument('--output', '-o', help='Output JSONL file (default: overwrite input file)')
    parser.add_argument('--no-backup', action='store_true', help='Do not create backup of input file')
    
    args = parser.parse_args()
    
    # Verify the input file exists
    if not Path(args.input_file).exists():
        logger.error(f"Input file not found: {args.input_file}")
        return 1
        
    # Fix metadata in the file
    success, total, fixed = fix_metadata_in_file(
        args.input_file, 
        args.output, 
        not args.no_backup
    )
    
    if success:
        logger.info(f"Successfully fixed metadata in {fixed}/{total} records")
        return 0
    else:
        logger.error("Failed to fix metadata")
        return 1

if __name__ == "__main__":
    sys.exit(main())