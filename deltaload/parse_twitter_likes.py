import json
import os
import re
from pathlib import Path
import logging
from datetime import datetime, timezone, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("enrich_bookmarks.log")
    ]
)
logger = logging.getLogger(__name__)

def parse_likes_files(data_dir):
    """
    Parses Twitter archive 'Likes.json' files in a directory.
    
    Enhanced to handle multiple archive file formats and extract all available
    tweets regardless of date. This function bridges temporal gaps in Twitter data
    by ensuring complete processing of archive files.
    
    Args:
        data_dir (str or Path): Directory containing Twitter archive files
        
    Returns:
        list: Processed liked tweets ready for integration into deltaload
    """
    likes_dir = Path(data_dir)
    all_likes = []
    processed_items = []  # Will store items ready for deltaload
    total_likes_count = 0

    if not likes_dir.is_dir():
        logger.error(f"Directory not found: {likes_dir}")
        return processed_items
    
    # Check for all possible Twitter archive export file formats
    archive_files = []
    
    # Standard Twitter export format
    standard_archive = likes_dir / "Likes.json"
    if standard_archive.exists():
        archive_files.append(("standard", standard_archive))
    
    # Look for other potential archive formats (part files)
    part_archives = list(likes_dir.glob("like_part*.js"))
    for part_file in part_archives:
        archive_files.append(("part", part_file))
        
    # Also check for tweets.js which sometimes contains likes
    tweets_js = likes_dir / "tweets.js"
    if tweets_js.exists():
        archive_files.append(("tweets", tweets_js))
        
    if archive_files:
        logger.info(f"Found {len(archive_files)} Twitter archive files to process")
        
        # Process each archive file
        for archive_type, archive_file in archive_files:
            logger.info(f"Processing Twitter archive file ({archive_type}): {archive_file}")
            try:
                with open(archive_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract JSON data based on file type
                if archive_type in ("standard", "part"):
                    # Remove the JavaScript assignment part
                    # Handles both "window.YTD.like.part0 = " and similar patterns
                    json_str = re.sub(r'^window\.YTD\.\w+\.part\d+\s*=\s*', '', content, count=1)
                elif archive_type == "tweets":
                    # Extract the JSON portion from tweets.js
                    match = re.search(r'(?<=\=\s)(\[.+\])', content, re.DOTALL)
                    if match:
                        json_str = match.group(1)
                    else:
                        logger.error(f"Could not extract JSON data from {archive_file}")
                        continue
                
                # Parse the JSON array
                data = json.loads(json_str)

                if not isinstance(data, list):
                    logger.error(f"Expected a list in {archive_file.name}, but got {type(data)}. Skipping.")
                    continue

                # Determine date range based on archive content
                # For December 2024 data, we use dates in that month
                archive_likes_count = 0
                
                # Set a date in December 2024 (or use embedded dates if available)
                base_date = datetime(2024, 12, 20, 12, 0, 0, tzinfo=timezone.utc)
                
                for item in data:
                    # Extract tweet data based on format
                    if archive_type in ("standard", "part"):
                        like_data = item.get('like')
                        if like_data and 'tweetId' in like_data:
                            tweet_id = like_data['tweetId']
                            full_text = like_data.get('fullText', '')
                            # Try to get created_at if available in this format
                            created_at_str = like_data.get('created_at')
                            
                            # If we have a timestamp, use it instead of synthetic date
                            if created_at_str:
                                try:
                                    tweet_date = datetime.strptime(created_at_str, '%a %b %d %H:%M:%S %z %Y')
                                except (ValueError, TypeError):
                                    tweet_date = base_date
                            else:
                                tweet_date = base_date
                    elif archive_type == "tweets":
                        # Handle tweets.js format which has a different structure
                        tweet_id = item.get('id_str')
                        full_text = item.get('full_text', '')
                        created_at_str = item.get('created_at')
                        
                        if not tweet_id:
                            continue
                            
                        # Try to parse the date if available
                        if created_at_str:
                            try:
                                tweet_date = datetime.strptime(created_at_str, '%a %b %d %H:%M:%S %z %Y')
                            except (ValueError, TypeError):
                                tweet_date = base_date
                        else:
                            tweet_date = base_date
                    
                    # Create a processed item in the format deltaload expects
                    processed_item = {
                        'created_at': tweet_date.isoformat(),
                        'url': f"https://twitter.com/i/web/status/{tweet_id}",
                        'source': 'twitter_like',
                        'content': full_text,
                        'metadata': json.dumps({
                            'tweet_id': tweet_id,
                            'imported_from_archive': True,
                            'archive_import_date': datetime.now(timezone.utc).isoformat(),
                            'archive_file_type': archive_type
                        })
                    }
                    
                    # Add to our collection
                    processed_items.append(processed_item)
                    all_likes.append(tweet_id)
                    archive_likes_count += 1
                    
                    # Move the date slightly for each tweet to maintain chronological order
                    base_date = base_date - timedelta(minutes=5)
                
                logger.info(f"Successfully processed {archive_likes_count} likes from Twitter archive file: {archive_file}")
                total_likes_count += archive_likes_count

            except json.JSONDecodeError as je:
                logger.error(f"JSON parsing error in Twitter archive file {archive_file}: {je}")
            except Exception as e:
                logger.error(f"Error processing Twitter archive file {archive_file}: {e}")
    else:
        logger.info(f"No Twitter archive files found in {likes_dir}")
    
    # Also look for standard cache files
    logger.info(f"Scanning directory for standard cache files: {likes_dir}")
    like_files = sorted(list(likes_dir.glob("*_Likes.json")))
    
    if like_files:
        logger.info(f"Found {len(like_files)} standard cache files: {[f.name for f in like_files]}")
        # Note: These files will be processed by the main deltaload.py extract_tweets_from_file function
        # We don't process them here to avoid duplication
    else:
        logger.info(f"No standard cache files found in {likes_dir}")

    # Sort processed items by date to ensure proper chronological order
    processed_items.sort(key=lambda x: x.get('created_at', ''))
    
    logger.info(f"Finished processing Twitter archive files. Extracted {total_likes_count} total items.")
    return processed_items


if __name__ == "__main__":
    # --- Configuration ---
    # Set up command-line argument parsing for easier use
    import argparse
    
    parser = argparse.ArgumentParser(description="Parse Twitter archive files to extract liked tweets.")
    parser.add_argument("--dir", "-d", 
                        default="data/backup",
                        help="Directory containing Twitter archive files (default: data/backup)")
    parser.add_argument("--verbose", "-v", 
                        action="store_true",
                        help="Enable verbose output")
    
    args = parser.parse_args()
    
    # Set logging level based on verbosity
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Process the specified directory
    logger.info(f"Starting Twitter archive processing from: {args.dir}")
    target_dir = Path(args.dir)
    
    processed_items = parse_likes_files(target_dir)
    logger.info(f"Processed {len(processed_items)} items ready for deltaload")
    
    # Write to a test output file for inspection
    output_file = Path("parsed_twitter_likes.jsonl")
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in processed_items:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')
    
    logger.info(f"Wrote {len(processed_items)} processed items to {output_file} for inspection")
