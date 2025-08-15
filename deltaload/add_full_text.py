#!/usr/bin/env python3
"""
Script to enhance the bookmarks dataset by adding full_text fields containing markdown-formatted
content for each source type (GitHub README, Twitter threads, Raindrop web content).
"""

import json
import logging
import os
import sys
import ast
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from collections import Counter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("full_text_enhancement.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Import functions from fix_data_types.py
try:
    from fix_data_types import (
        convert_tweet_thread_to_markdown,
        convert_github_readme_to_markdown,
        convert_web_content_to_markdown,
        extract_twitter_thread_data
    )
    logger.info("Successfully imported markdown conversion functions")
except ImportError as e:
    logger.error(f"Error importing from fix_data_types.py: {e}")
    # Define fallback functions if imports fail
    def convert_tweet_thread_to_markdown(thread_data):
        """Fallback function if import fails."""
        return f"Tweet thread content not available. Thread data keys: {list(thread_data.keys())}"
    
    def convert_github_readme_to_markdown(readme_content, repo_data=None):
        """Fallback function if import fails."""
        return readme_content
    
    def convert_web_content_to_markdown(content, metadata=None):
        """Fallback function if import fails."""
        return content
    
    def extract_twitter_thread_data(record, thread_data_path='thread_data.jsonl'):
        """Fallback function if import fails."""
        return None

def format_tweet_as_markdown(tweet_data):
    """Format a single tweet as markdown."""
    if not tweet_data:
        return ""
    
    # Extract tweet text
    text = tweet_data.get('text', '') or tweet_data.get('full_text', '') or tweet_data.get('content', '')
    
    # Extract user info
    user = tweet_data.get('user', {})
    if isinstance(user, str):
        try:
            user = json.loads(user)
        except:
            try:
                user = ast.literal_eval(user)
            except:
                user = {}
    
    username = user.get('screen_name') or tweet_data.get('username', 'unknown')
    name = user.get('name') or tweet_data.get('user_name', username)
    
    # Get metrics
    likes = tweet_data.get('favorite_count', 0)
    retweets = tweet_data.get('retweet_count', 0)
    replies = tweet_data.get('reply_count', 0)
    
    # Format created date
    created_at = tweet_data.get('created_at', '')
    
    # Build markdown
    markdown = f"# Tweet by [{name} (@{username})](https://twitter.com/{username})\n\n"
    markdown += f"## {created_at}\n\n"
    markdown += f"{text}\n\n"
    
    # Add media if available
    media = tweet_data.get('media', [])
    if media:
        for url in media:
            if isinstance(url, str) and url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                markdown += f"![image]({url})\n\n"
            elif isinstance(url, str) and url.endswith(('.mp4', '.mov')):
                markdown += f"[Video]({url})\n\n"
            elif isinstance(url, str):
                markdown += f"[Media]({url})\n\n"
    
    # Add metrics
    markdown += f"*💬 {replies} replies • 🔄 {retweets} retweets • ❤️ {likes} likes*\n\n"
    
    return markdown

def get_tweet_id_from_url(url):
    """Extract tweet ID from a Twitter URL."""
    if not url or ('twitter.com' not in url and 'x.com' not in url):
        return None
    
    # Pattern for status URLs
    if '/status/' in url:
        try:
            tweet_id = url.split('/status/')[1].split('/')[0].split('?')[0]
            return tweet_id
        except IndexError:
            return None
    
    return None

def enhance_github_bookmark(bookmark):
    """Add full_text to GitHub bookmarks with README content."""
    url = bookmark.get('url', '')
    content = bookmark.get('content', '')
    metadata = bookmark.get('metadata', {})
    
    # Get repo data
    owner = metadata.get('owner', '')
    repo = metadata.get('repo', '')
    language = metadata.get('language', '')
    stars = metadata.get('stars', 0)
    forks = metadata.get('forks', 0)
    
    # Create simplified repo data
    repo_data = {
        'name': repo,
        'owner': owner,
        'full_name': f"{owner}/{repo}" if owner and repo else "",
        'description': metadata.get('description', content),
        'language': language,
        'stars': stars,
        'forks': forks,
        'url': url,
        'watchers': metadata.get('watchers', 0),
        'license': metadata.get('license', '')
    }
    
    # Check if the content already includes formatted repository information
    # This happens when the GitHubScraper's format_repo_markdown has already been used
    if content and '## README' in content:
        # Content is already formatted with repository details
        bookmark['full_text'] = content
        logger.info(f"Using pre-formatted GitHub content for {owner}/{repo}")
        return bookmark
    
    # Get README content - prioritize the dedicated github_readme field 
    readme_content = ''
    if 'github_readme' in bookmark and bookmark['github_readme']:
        logger.info(f"Using github_readme field for {owner}/{repo}")
        readme_content = bookmark['github_readme']
    elif content and len(content) > 20 and "README" not in content.upper()[:40]:
        # Content might be the README but without proper formatting
        logger.info(f"Using content field as README for {owner}/{repo}")
        readme_content = content
    
    # Format markdown content with consistent structure
    full_text = ""
    
    # Add repository header and metadata
    full_text += f"# [{owner}/{repo}]({url})\n\n"
    
    if repo_data.get('description'):
        full_text += f"{repo_data['description']}\n\n"
        
    # Add metadata table
    full_text += "| | |\n"
    full_text += "|---|---|\n"
        
    if language:
        full_text += f"| Language | {language} |\n"
        
    if stars is not None:
        full_text += f"| Stars | {stars} |\n"
        
    if forks is not None:
        full_text += f"| Forks | {forks} |\n"
        
    if repo_data.get('watchers') is not None:
        full_text += f"| Watchers | {repo_data['watchers']} |\n"
        
    if repo_data.get('license'):
        full_text += f"| License | {repo_data['license']} |\n"
    
    full_text += "\n## README\n\n"
    
    # Add README content, avoiding duplicate headers
    if readme_content:
        content_lines = readme_content.split('\n')
        if content_lines and content_lines[0].startswith('# ') and repo in content_lines[0]:
            # Skip the first line and any empty lines that follow
            i = 1
            while i < len(content_lines) and not content_lines[i].strip():
                i += 1
            readme_content = '\n'.join(content_lines[i:])
            
        full_text += readme_content
    else:
        full_text += "(README content not available)"
    
    bookmark['full_text'] = full_text
    
    return bookmark

def enhance_twitter_bookmark(bookmark):
    """Add full_text to Twitter bookmarks with thread/tweet content."""
    url = bookmark.get('url', '')
    content = bookmark.get('content', '')
    metadata = bookmark.get('metadata', {})
    
    # Try to get thread data first
    thread_data = None
    if 'twitter_thread' in bookmark:
        # Already has thread data
        thread_data = {
            'author': {
                'name': metadata.get('user_name', 'Unknown'),
                'screen_name': metadata.get('username', 'unknown')
            },
            'tweets': bookmark['twitter_thread']
        }
    else:
        # Try to extract thread data
        thread_data = extract_twitter_thread_data(bookmark)
    
    # If we have thread data, convert to markdown
    if thread_data and (thread_data.get('tweets') or 'text' in thread_data):
        full_text = convert_tweet_thread_to_markdown(thread_data)
        bookmark['full_text'] = full_text
        if 'twitter_thread_markdown' not in bookmark:
            bookmark['twitter_thread_markdown'] = full_text
        return bookmark
    
    # Handle single tweet
    tweet_data = {
        'text': content,
        'user': {
            'name': metadata.get('user_name', 'Unknown'),
            'screen_name': metadata.get('username', 'unknown')
        },
        'created_at': bookmark.get('created_at', ''),
        'favorite_count': metadata.get('favorite_count', 0),
        'retweet_count': metadata.get('retweet_count', 0),
        'reply_count': metadata.get('reply_count', 0),
        'media': []
    }
    
    # Add tweet markdown
    full_text = format_tweet_as_markdown(tweet_data)
    bookmark['full_text'] = full_text
    
    return bookmark

def enhance_twitter_like_bookmark(bookmark):
    """Add full_text to Twitter like bookmarks."""
    url = bookmark.get('url', '')
    content = bookmark.get('content', '')
    metadata = bookmark.get('metadata', {})
    
    # Try to get user data
    user = metadata.get('user', {})
    if isinstance(user, str):
        try:
            user = json.loads(user)
        except:
            try:
                user = ast.literal_eval(user)
            except:
                user = {}
    
    # Create tweet data
    tweet_data = {
        'text': content,
        'user': user,
        'created_at': bookmark.get('created_at', ''),
        'favorite_count': metadata.get('favorite_count', 0),
        'retweet_count': metadata.get('retweet_count', 0),
        'reply_count': metadata.get('reply_count', 0),
        'media': []
    }
    
    # Add tweet markdown
    full_text = format_tweet_as_markdown(tweet_data)
    bookmark['full_text'] = full_text
    
    return bookmark

def enhance_raindrop_bookmark(bookmark):
    """Add full_text to Raindrop bookmarks with web content."""
    url = bookmark.get('url', '')
    content = bookmark.get('content', '')
    metadata = bookmark.get('metadata', {})
    
    # Create metadata for markdown formatting
    web_metadata = {
        'title': bookmark.get('title', url.split('/')[-1]),
        'description': metadata.get('description', '')
    }
    
    # Format content
    full_text = convert_web_content_to_markdown(content, web_metadata)
    bookmark['full_text'] = full_text
    
    return bookmark

def process_file(input_file, output_file=None, backup=True):
    """
    Process a JSONL file to add full_text fields.
    
    Args:
        input_file: Path to input JSONL file
        output_file: Path to output JSONL file (default: overwrite input file)
        backup: Whether to create a backup of the input file
        
    Returns:
        Tuple of (success, stats)
    """
    # Set output file if not specified
    if not output_file:
        output_file = input_file
        
    # Create backup if requested and we're overwriting
    if backup and input_file == output_file:
        backup_file = f"{input_file}.bak"
        logger.info(f"Creating backup of {input_file} to {backup_file}")
        import shutil
        try:
            shutil.copy2(input_file, backup_file)
        except Exception as e:
            logger.error(f"Error creating backup: {str(e)}")
            return False, {}
    
    # Process the file
    stats = {
        'total': 0,
        'with_full_text_before': 0,
        'with_full_text_after': 0,
        'by_source': Counter(),
        'enhanced': Counter()
    }
    
    try:
        # Read all records
        records = []
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    record = json.loads(line.strip())
                    stats['total'] += 1
                    
                    # Count by source
                    source = record.get('source', 'unknown')
                    stats['by_source'][source] += 1
                    
                    # Check if already has full_text
                    if 'full_text' in record:
                        stats['with_full_text_before'] += 1
                    
                    # Add full_text field based on source
                    if source == 'github':
                        record = enhance_github_bookmark(record)
                        stats['enhanced']['github'] += 1
                    elif source == 'twitter':
                        record = enhance_twitter_bookmark(record)
                        stats['enhanced']['twitter'] += 1
                    elif source == 'twitter_like':
                        record = enhance_twitter_like_bookmark(record)
                        stats['enhanced']['twitter_like'] += 1
                    elif source == 'raindrop':
                        record = enhance_raindrop_bookmark(record)
                        stats['enhanced']['raindrop'] += 1
                    else:
                        # Unknown source, use content as full_text
                        if 'full_text' not in record:
                            record['full_text'] = record.get('content', '')
                        stats['enhanced']['other'] += 1
                    
                    # Check if now has full_text
                    if 'full_text' in record:
                        stats['with_full_text_after'] += 1
                    
                    records.append(record)
                except json.JSONDecodeError as e:
                    logger.error(f"Error parsing JSON line: {str(e)}")
        
        # Write out the enhanced records
        with open(output_file, 'w', encoding='utf-8') as f:
            for record in records:
                json.dump(record, f, ensure_ascii=False)
                f.write('\n')
                
        logger.info(f"Processed {stats['total']} records, added full_text to {stats['with_full_text_after'] - stats['with_full_text_before']} records")
        return True, stats
        
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        return False, stats

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Add full_text field to bookmarks")
    parser.add_argument('input_file', help='Input JSONL file')
    parser.add_argument('--output', '-o', help='Output JSONL file (default: overwrite input file)')
    parser.add_argument('--no-backup', action='store_true', help='Do not create backup of input file')
    parser.add_argument('--report', '-r', help='Save statistics report to specified JSON file')
    
    args = parser.parse_args()
    
    # Verify the input file exists
    if not Path(args.input_file).exists():
        logger.error(f"Input file not found: {args.input_file}")
        return 1
        
    # Process the file
    success, stats = process_file(
        args.input_file, 
        args.output, 
        not args.no_backup
    )
    
    # Print statistics
    logger.info("Enhancement Statistics:")
    logger.info(f"Total records: {stats['total']}")
    logger.info(f"Records with full_text before: {stats['with_full_text_before']} ({stats['with_full_text_before']/stats['total']*100:.1f}%)")
    logger.info(f"Records with full_text after: {stats['with_full_text_after']} ({stats['with_full_text_after']/stats['total']*100:.1f}%)")
    logger.info("Source distribution:")
    for source, count in sorted(stats['by_source'].items(), key=lambda x: x[1], reverse=True):
        logger.info(f"  {source}: {count} ({count/stats['total']*100:.1f}%)")
    logger.info("Enhanced records by source:")
    for source, count in sorted(stats['enhanced'].items(), key=lambda x: x[1], reverse=True):
        logger.info(f"  {source}: {count}")
    
    # Save report if requested
    if args.report:
        try:
            with open(args.report, 'w', encoding='utf-8') as f:
                json.dump({
                    'timestamp': datetime.now().isoformat(),
                    'input_file': args.input_file,
                    'output_file': args.output or args.input_file,
                    'stats': {k: v if not isinstance(v, Counter) else dict(v) for k, v in stats.items()}
                }, f, indent=2)
            logger.info(f"Saved statistics report to {args.report}")
        except Exception as e:
            logger.error(f"Error saving report: {str(e)}")
    
    if success:
        logger.info("Successfully enhanced bookmarks with full_text fields")
        return 0
    else:
        logger.error("Failed to enhance bookmarks")
        return 1

if __name__ == "__main__":
    sys.exit(main())