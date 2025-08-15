"""
Script to fix inconsistent data types in the JSONL file and enhance content
with structured representations of Twitter threads, GitHub READMEs, and web content.
"""

import json
import pandas as pd
import numpy as np
from pathlib import Path
import logging
from datetime import datetime
import re
import os
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def convert_tweet_thread_to_markdown(thread_data):
    """
    Convert Twitter thread data to a Markdown representation with embedded images.
    
    Args:
        thread_data: Dictionary containing tweets in the thread
        
    Returns:
        Markdown string representation of the thread
    """
    if not thread_data:
        return ""
    
    # Handle both thread data and single tweet data
    tweets = thread_data.get('tweets', [])
    
    # If no tweets list but we have tweet data, treat it as a single tweet
    if not tweets and 'text' in thread_data:
        tweets = [thread_data]
    elif not tweets:
        return ""
    
    author = thread_data.get('author', {})
    author_name = author.get('name', 'Unknown')
    author_username = author.get('screen_name', 'unknown')
    
    # Determine if this is a thread or single tweet
    is_thread = len(tweets) > 1
    
    # Build the markdown content
    if is_thread:
        markdown = f"# Thread by [{author_name} (@{author_username})](https://twitter.com/{author_username})\n\n"
    else:
        markdown = f"# Tweet by [{author_name} (@{author_username})](https://twitter.com/{author_username})\n\n"
    
    for i, tweet in enumerate(tweets):
        created_at = tweet.get('created_at', '')
        try:
            # Format the created_at field if it's in the Twitter format
            if created_at and not created_at.endswith('Z'):
                created_time = datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")
                created_at = created_time.strftime("%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            pass
        
        # Add tweet header (only show numbers if it's a thread)
        if is_thread:
            markdown += f"## Tweet {i+1} • {created_at}\n\n"
        else:
            markdown += f"## {created_at}\n\n"
        
        # Add tweet text
        text = tweet.get('text', '')
        markdown += f"{text}\n\n"
        
        # Add media if available
        media_urls = tweet.get('media', [])
        for url in media_urls:
            if url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                markdown += f"![image]({url})\n\n"
            elif url.endswith(('.mp4', '.mov')):
                markdown += f"[Video]({url})\n\n"
            else:
                markdown += f"[Media]({url})\n\n"
        
        # Add engagement metrics
        likes = tweet.get('favorite_count', 0)
        retweets = tweet.get('retweet_count', 0)
        replies = tweet.get('reply_count', 0)
        
        markdown += f"*💬 {replies} replies • 🔄 {retweets} retweets • ❤️ {likes} likes*\n\n"
        
        if is_thread and i < len(tweets) - 1:
            markdown += "---\n\n"
    
    return markdown

def convert_github_readme_to_markdown(readme_content, repo_data=None):
    """
    Format GitHub README content as Markdown with metadata.
    
    Args:
        readme_content: Raw README content
        repo_data: Repository metadata if available
        
    Returns:
        Markdown string with metadata and content
    """
    if not readme_content:
        return ""
    
    markdown = ""
    
    # Add repo metadata if available
    if repo_data:
        repo_name = repo_data.get('name', '')
        owner = repo_data.get('owner', '')
        full_name = repo_data.get('full_name', f"{owner}/{repo_name}" if owner and repo_name else "")
        description = repo_data.get('description', '')
        language = repo_data.get('language', '')
        stars = repo_data.get('stars', 0)
        forks = repo_data.get('forks', 0)
        
        markdown += f"# [{full_name}](https://github.com/{full_name})\n\n"
        
        if description:
            markdown += f"{description}\n\n"
            
        markdown += f"**Language:** {language} • **Stars:** {stars} • **Forks:** {forks}\n\n"
        markdown += "---\n\n"
    
    # Add README content
    markdown += readme_content
    
    return markdown

def convert_web_content_to_markdown(content, metadata=None):
    """
    Format web content as Markdown using the existing content.
    
    Args:
        content: Existing content from bookmark data
        metadata: Web page metadata if available
        
    Returns:
        Markdown representation of the web content
    """
    if not content:
        return ""
    
    # Simply use existing content since we're not re-scraping
    # Just add formatting for title and metadata if available
    markdown = ""
    
    # Add metadata if available
    if metadata:
        title = metadata.get('title', '')
        description = metadata.get('description', '')
        
        if title:
            markdown += f"# {title}\n\n"
            
        if description:
            markdown += f"*{description}*\n\n"
            
        markdown += "---\n\n"
    
    # Add the content that was already captured
    markdown += content
    
    return markdown

def extract_twitter_thread_data(record, thread_data_path='thread_data.jsonl'):
    """
    Extract Twitter thread data from a record's metadata or from thread_data.jsonl.
    
    Args:
        record: Dictionary containing bookmark data
        thread_data_path: Path to thread_data.jsonl file
        
    Returns:
        Extracted thread data or None
    """
    # First try to get thread data from record's metadata
    metadata = record.get('metadata', {})
    
    # Parse metadata if it's a string
    if isinstance(metadata, str):
        try:
            metadata = json.loads(metadata)
        except json.JSONDecodeError:
            metadata = {}
    
    # Check if we have thread data in the metadata
    if metadata and 'tweets' in metadata:
        return metadata
    
    # If not found in metadata, try to find it in thread_data.jsonl
    tweet_url = record.get('url', '')
    
    # Only continue if we have a Twitter URL
    if 'twitter.com' not in tweet_url and 'x.com' not in tweet_url:
        return None
        
    # Try to extract tweet ID from URL
    tweet_id = None
    if '/status/' in tweet_url:
        try:
            tweet_id = tweet_url.split('/status/')[1].split('/')[0].split('?')[0]
        except IndexError:
            return None
    
    if not tweet_id:
        return None
        
    # Check if thread_data.jsonl exists
    if not os.path.exists(thread_data_path):
        return None
        
    # Look for this tweet ID in thread_data.jsonl
    try:
        with open(thread_data_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    thread_record = json.loads(line)
                    thread_metadata = thread_record.get('metadata', {})
                    
                    # Check if this is the right thread
                    if thread_metadata.get('thread_id') == tweet_id:
                        return thread_metadata
                        
                    # Also check if this tweet ID is in the tweets list
                    tweets = thread_metadata.get('tweets', [])
                    for tweet in tweets:
                        if tweet.get('id') == tweet_id:
                            return thread_metadata
                except json.JSONDecodeError:
                    continue
    except Exception as e:
        logger.error(f"Error reading thread_data.jsonl: {str(e)}")
        
    return None

def fix_data_types(input_path, output_path):
    """
    Fix inconsistent data types in the JSONL file and enhance content.
    
    Args:
        input_path: Path to the input JSONL file
        output_path: Path to the output JSONL file
    """
    logger.info(f"Loading data from {input_path}")
    
    # Load the data
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                logger.error(f"Error parsing line: {e}")
    
    logger.info(f"Loaded {len(data)} records")
    
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(data)
    
    # Define numeric columns that need type conversion
    numeric_columns = [
        'id', 'content_length', 'year', 'month',
        'twitter_followers', 'twitter_likes', 'twitter_retweets', 'twitter_replies',
        'github_stars', 'github_forks'
    ]
    
    # Convert columns to appropriate types
    for col in numeric_columns:
        if col in df.columns:
            logger.info(f"Converting {col} to numeric type")
            # Convert to numeric, setting errors to 'coerce' will convert non-numeric values to NaN
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Convert date columns to proper datetime format
    if 'created_at' in df.columns:
        logger.info("Converting created_at to datetime")
        # First save the original date strings in case we need them
        df['original_created_at'] = df['created_at']
        # Then convert to datetime
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    
    # Fix list columns (specifically raindrop_tags)
    if 'raindrop_tags' in df.columns:
        logger.info("Fixing raindrop_tags format")
        df['raindrop_tags'] = df['raindrop_tags'].apply(
            lambda x: [] if pd.isna(x) else (x if isinstance(x, list) else [])
        )
    
    # Process and enhance Twitter thread data
    logger.info("Processing Twitter thread data")
    twitter_records = [record for record in data if record.get('source') == 'twitter']
    logger.info(f"Found {len(twitter_records)} Twitter records")
    
    # Process Twitter content (both threads and single tweets) and create markdown representation
    for record in twitter_records:
        # First try to get thread data
        thread_data = extract_twitter_thread_data(record)
        
        if thread_data:
            # It's a thread or we found thread data
            record['twitter_thread'] = thread_data.get('tweets', [])
            record['twitter_thread_markdown'] = convert_tweet_thread_to_markdown(thread_data)
        else:
            # Try to create a single tweet representation if we have enough data
            metadata = record.get('metadata', {})
            if isinstance(metadata, str):
                try:
                    metadata = json.loads(metadata)
                except json.JSONDecodeError:
                    metadata = {}
                    
            # Check if we have text and other basic tweet info
            text = record.get('content', '')
            
            # If there's a description in metadata, use that for content
            if isinstance(metadata, dict) and metadata.get('description') and len(metadata.get('description', '')) > len(text):
                text = metadata.get('description', '')
                
            username = metadata.get('username') or record.get('twitter_username')
            name = metadata.get('name') or record.get('twitter_name')
            likes = metadata.get('likes') or record.get('twitter_likes', 0)
            retweets = metadata.get('retweets') or record.get('twitter_retweets', 0)
            replies = metadata.get('replies') or record.get('twitter_replies', 0)
            
            # Use original date string if available, otherwise use the parsed datetime
            created_at = record.get('original_created_at', '') or record.get('created_at', '')
            
            # Try to extract media URLs
            media_urls = []
            if isinstance(metadata, dict):
                # Check for media_urls or similar fields in metadata
                if 'media' in metadata:
                    if isinstance(metadata['media'], list):
                        media_urls = metadata['media']
                    elif isinstance(metadata['media'], str):
                        media_urls = [metadata['media']]
                elif 'images' in metadata:
                    if isinstance(metadata['images'], list):
                        media_urls = metadata['images']
                    elif isinstance(metadata['images'], str):
                        media_urls = [metadata['images']]
                    
            # If no media found, try to look for image URLs in content
            if not media_urls and text:
                # Simple regex to find image URLs in text
                image_url_pattern = r'https?://[^\s]+\.(jpg|jpeg|png|gif)(?:\?[^\s]*)?(?=\s|$)'
                image_urls = re.findall(image_url_pattern, text)
                # Convert from tuples to full URLs
                if image_urls:
                    full_urls = []
                    for url_match in re.finditer(image_url_pattern, text):
                        full_urls.append(url_match.group(0))
                    media_urls = full_urls
            
            # Only proceed if we have at least text and username
            if text and username:
                # Create tweet data structure
                tweet_data = {
                    'text': text,
                    'created_at': created_at,
                    'favorite_count': likes,
                    'retweet_count': retweets,
                    'reply_count': replies,
                    'media': media_urls
                }
                
                # Create author data
                author_data = {
                    'name': name or username,
                    'screen_name': username,
                    'followers_count': metadata.get('followers') if isinstance(metadata, dict) else 0
                }
                
                # Create simplified thread data with single tweet
                single_tweet_data = {
                    'author': author_data,
                    'tweets': [tweet_data]
                }
                
                # Add to record
                record['twitter_thread'] = [tweet_data]
                record['twitter_thread_markdown'] = convert_tweet_thread_to_markdown(single_tweet_data)
    
    # Process GitHub repositories
    logger.info("Processing GitHub repository data")
    github_records = [record for record in data if record.get('source') == 'github']
    logger.info(f"Found {len(github_records)} GitHub records")
    
    # Process GitHub READMEs
    for record in github_records:
        metadata = record.get('metadata', {})
        if isinstance(metadata, str):
            try:
                metadata = json.loads(metadata)
            except json.JSONDecodeError:
                metadata = {}
        
        # Get the best content - either from content field or metadata
        content = record.get('content', '')
        if isinstance(metadata, dict) and metadata.get('description') and len(metadata.get('description', '')) > len(content):
            content = metadata.get('description', '')
        
        if content:
            record['github_readme'] = content
            record['github_readme_markdown'] = convert_github_readme_to_markdown(content, metadata)
    
    # Process web content using existing data
    logger.info("Processing web content (using existing data)")
    web_records = [record for record in data if record.get('source') not in ['twitter', 'github']]
    logger.info(f"Found {len(web_records)} web records")
    
    # Process web content from existing data
    for record in web_records:
        content = record.get('content', '')
        metadata = record.get('metadata', {})
        
        # Parse metadata if it's a string
        if isinstance(metadata, str):
            try:
                metadata = json.loads(metadata)
            except json.JSONDecodeError:
                metadata = {}
        
        # Extract title and description if available
        title = None
        description = None
        
        if isinstance(metadata, dict):
            title = metadata.get('title')
            description = metadata.get('description')
            
            # Try to extract from cached HTML if available
            if not title and 'html' in metadata:
                # Very simple regex extraction (lightweight approach)
                title_match = re.search(r'<title>(.*?)</title>', metadata.get('html', ''), re.IGNORECASE)
                if title_match:
                    title = title_match.group(1).strip()
            
            # Add basic metadata fields
            record['web_title'] = title
            record['web_description'] = description
            
            # Check if metadata has better content
            if description and len(description) > len(content):
                content = description
            
            # Add the HTML content if available
            if 'html' in metadata:
                record['web_content_html'] = metadata.get('html', '')
            
            # Add images if available
            if 'media' in metadata:
                if isinstance(metadata['media'], list):
                    record['web_images'] = metadata['media']
                elif isinstance(metadata['media'], str):
                    record['web_images'] = [metadata['media']]
        
        # Create markdown version
        if content:
            record['web_content_markdown'] = convert_web_content_to_markdown(content, 
                                                                            {'title': title, 'description': description})
    
    # Update the DataFrame
    df = pd.DataFrame(data)
    
    # Save the fixed and enhanced data
    logger.info(f"Saving {len(df)} records to {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        for record in df.to_dict(orient='records'):
            # Convert any non-JSON serializable objects to their string representation
            serialized_record = {}
            for k, v in record.items():
                # Skip the original_created_at field
                if k == 'original_created_at':
                    continue
                
                try:
                    if k == 'created_at' and not pd.isna(record.get('original_created_at')):
                        # Use the original date string
                        serialized_record[k] = record.get('original_created_at')
                    elif isinstance(v, (pd.Timestamp, datetime)):
                        serialized_record[k] = v.isoformat()
                    elif isinstance(v, (pd.Series, np.ndarray)):
                        # Convert pandas or numpy arrays to lists
                        serialized_record[k] = v.tolist() if hasattr(v, 'tolist') else list(v)
                    elif pd.isna(v):
                        serialized_record[k] = None
                    else:
                        serialized_record[k] = v
                except (ValueError, TypeError):
                    # If we can't determine truth value, assume it's not NA
                    serialized_record[k] = v
            
            json.dump(serialized_record, f, ensure_ascii=False)
            f.write('\n')
    
    logger.info("Fixed and enhanced data has been saved")
    
    return len(df)

def create_updated_metadata(output_path):
    """Create updated metadata.json file with consistent types and enhanced content."""
    metadata = {
        "dataset_info": {
            "description": "Bookmarks collected from various sources including Twitter, GitHub, and Raindrop.io",
            "citation": "",
            "homepage": "",
            "license": "",
            "features": {
                "id": {"dtype": "int64", "description": "Unique identifier for the bookmark"},
                "source": {"dtype": "string", "description": "Source of the bookmark (twitter, github, raindrop, etc.)"},
                "title": {"dtype": "string", "description": "Title of the bookmark"},
                "url": {"dtype": "string", "description": "URL of the bookmark"},
                "content": {"dtype": "string", "description": "Content of the bookmark"},
                "created_at": {"dtype": "string", "description": "Creation date of the bookmark"},
                "domain": {"dtype": "string", "description": "Domain of the URL"},
                "content_length": {"dtype": "int64", "description": "Length of the content in characters"},
                "year": {"dtype": "int64", "description": "Year the bookmark was created"},
                "month": {"dtype": "int64", "description": "Month the bookmark was created"},
                
                # Twitter-specific fields
                "twitter_username": {"dtype": "string", "description": "Twitter username"},
                "twitter_name": {"dtype": "string", "description": "Twitter display name"},
                "twitter_followers": {"dtype": "int64", "description": "Number of Twitter followers"},
                "twitter_likes": {"dtype": "int64", "description": "Number of likes on the tweet"},
                "twitter_retweets": {"dtype": "int64", "description": "Number of retweets"},
                "twitter_replies": {"dtype": "int64", "description": "Number of replies to the tweet"},
                "twitter_thread": {
                    "dtype": "list", 
                    "description": "Full thread of tweets (including the original tweet)",
                    "sequence": {
                        "dtype": "dict",
                        "dict": {
                            "id": {"dtype": "string", "description": "Tweet ID"},
                            "text": {"dtype": "string", "description": "Tweet text content"},
                            "created_at": {"dtype": "string", "description": "Tweet creation time"},
                            "media": {
                                "dtype": "list", 
                                "description": "Media URLs in the tweet",
                                "sequence": {"dtype": "string"}
                            },
                            "favorite_count": {"dtype": "int64", "description": "Number of likes"},
                            "retweet_count": {"dtype": "int64", "description": "Number of retweets"},
                            "reply_count": {"dtype": "int64", "description": "Number of replies"}
                        }
                    }
                },
                "twitter_thread_markdown": {"dtype": "string", "description": "Markdown representation of the full thread with embedded media"},
                
                # GitHub-specific fields
                "github_repo": {"dtype": "string", "description": "GitHub repository name"},
                "github_stars": {"dtype": "int64", "description": "Number of stars on the GitHub repository"},
                "github_forks": {"dtype": "int64", "description": "Number of forks of the GitHub repository"},
                "github_owner": {"dtype": "string", "description": "Owner of the GitHub repository"},
                "github_language": {"dtype": "string", "description": "Primary language of the GitHub repository"},
                "github_readme": {"dtype": "string", "description": "Full README content of the repository"},
                "github_readme_markdown": {"dtype": "string", "description": "README content formatted as Markdown"},
                
                # Web-specific fields
                "web_title": {"dtype": "string", "description": "Page title"},
                "web_description": {"dtype": "string", "description": "Page meta description"},
                "web_content_html": {"dtype": "string", "description": "Full HTML content of the webpage"},
                "web_content_markdown": {"dtype": "string", "description": "Converted markdown content of the webpage"},
                "web_images": {
                    "dtype": "list", 
                    "description": "Images found on the webpage",
                    "sequence": {"dtype": "string"}
                },
                
                # Raindrop-specific fields
                "raindrop_domain": {"dtype": "string", "description": "Domain saved in Raindrop.io"},
                "raindrop_tags": {
                    "dtype": "list", 
                    "description": "Tags associated with the Raindrop bookmark",
                    "sequence": {"dtype": "string"}
                }
            }
        }
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Updated metadata saved to {output_path}")

if __name__ == "__main__":
    # Input and output paths
    input_path = "/Users/imac/Desktop/ETL/deltaload/data-bookmark.jsonl"
    output_dir = "/Users/imac/Desktop/ETL/deltaload/hf_bookmarks_dataset_fixed"
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Output paths
    output_jsonl = Path(output_dir) / "data.jsonl"
    output_metadata = Path(output_dir) / "metadata.json"
    
    # Fix data types and save
    record_count = fix_data_types(input_path, output_jsonl)
    
    # Create updated metadata.json
    create_updated_metadata(output_metadata)
    
    # Copy the README
    import shutil
    readme_path = Path("/Users/imac/Desktop/ETL/deltaload/dataset_card.md")
    shutil.copy(readme_path, Path(output_dir) / "README.md")
    
    logger.info(f"\nFixed dataset created at {output_dir}")
    logger.info(f"Total records: {record_count}")
    logger.info(f"\nTo upload the fixed dataset to Hugging Face:")
    logger.info(f"python3 -c \"from huggingface_hub import HfApi; api = HfApi(); api.upload_folder(folder_path='{output_dir}', repo_id='J94/bookmarks-dataset', repo_type='dataset')\"")