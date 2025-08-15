#!/usr/bin/env python3
"""
Twitter Processor Module

This module provides comprehensive Twitter data processing capabilities including:
1. Fixing content mismatches between full_text and original content
2. Improving retweet formatting to emphasize original authors
3. Fixing truncated tweets using cache data first, then API if needed
"""

import os
import json
import re
import logging
import glob
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

# Configure logging
logger = logging.getLogger(__name__)

class TwitterProcessor:
    """
    Processes Twitter bookmarks to fix various issues with content.
    """
    
    def __init__(self, cache_dir: str = "data", batch_size: int = 50):
        """
        Initialize the Twitter processor.
        
        Args:
            cache_dir: Directory containing Twitter cache files
            batch_size: Number of tweets to process in each batch
        """
        self.cache_dir = cache_dir
        self.batch_size = batch_size
        self.stats = {
            "twitter_count": 0,
            "content_fixed_count": 0,
            "retweet_fixed_count": 0,
            "truncated_count": 0,
            "truncated_fixed_count": 0,
            "truncated_fixed_from_cache": 0,
            "truncated_fixed_from_api": 0
        }
    
    def process_bookmarks(self, bookmarks: List[Dict], 
                          fix_content: bool = True, 
                          fix_retweets: bool = True,
                          fix_truncated: bool = True) -> List[Dict]:
        """
        Process all bookmarks, applying the requested fixes.
        
        Args:
            bookmarks: List of bookmark dictionaries
            fix_content: Whether to fix content mismatches
            fix_retweets: Whether to fix retweet formatting
            fix_truncated: Whether to fix truncated tweets
            
        Returns:
            Updated list of bookmarks with fixes applied
        """
        logger.info(f"Starting Twitter processing with {len(bookmarks)} bookmarks")
        logger.info(f"Enabled fixes: content={fix_content}, retweets={fix_retweets}, truncated={fix_truncated}")
        
        # Reset stats
        self.stats = {
            "twitter_count": 0,
            "content_fixed_count": 0,
            "retweet_fixed_count": 0,
            "truncated_count": 0,
            "truncated_fixed_count": 0,
            "truncated_fixed_from_cache": 0,
            "truncated_fixed_from_api": 0
        }
        
        # Identify all Twitter bookmarks
        twitter_bookmarks = []
        twitter_indices = []
        
        for i, bookmark in enumerate(bookmarks):
            source = bookmark.get('source', '')
            if 'twitter' in source.lower():
                self.stats["twitter_count"] += 1
                twitter_bookmarks.append(bookmark)
                twitter_indices.append(i)
        
        logger.info(f"Found {len(twitter_bookmarks)} Twitter bookmarks to process")
        
        # Process in batches
        for batch_start in range(0, len(twitter_bookmarks), self.batch_size):
            batch_end = min(batch_start + batch_size, len(twitter_bookmarks))
            current_batch = twitter_bookmarks[batch_start:batch_end]
            
            logger.info(f"Processing batch: items {batch_start}-{batch_end-1} of {len(twitter_bookmarks)}")
            
            # Process current batch
            for i, bookmark in enumerate(current_batch):
                idx = twitter_indices[batch_start + i]
                original = bookmark.copy()
                
                # Apply fixes in sequence
                if fix_content:
                    bookmark = self._fix_twitter_content(bookmark)
                
                if fix_retweets:
                    bookmark = self._fix_retweet(bookmark)
                
                if fix_truncated:
                    # First try to fix from cache (faster and avoids API calls)
                    bookmark = self._fix_truncated_tweet_from_cache(bookmark)
                    
                    # If still truncated, try API
                    if self._is_truncated(bookmark.get('content', '')):
                        bookmark = self._fix_truncated_tweet(bookmark)
                
                # Update the bookmark in place
                bookmarks[idx] = bookmark
        
        # Log final stats
        logger.info(f"Twitter processing complete.")
        logger.info(f"Processed {self.stats['twitter_count']} Twitter bookmarks")
        logger.info(f"Fixed {self.stats['content_fixed_count']} content mismatches")
        logger.info(f"Fixed {self.stats['retweet_fixed_count']} retweets")
        logger.info(f"Found {self.stats['truncated_count']} truncated tweets")
        logger.info(f"Fixed {self.stats['truncated_fixed_count']} truncated tweets")
        logger.info(f"  - {self.stats['truncated_fixed_from_cache']} from cache")
        logger.info(f"  - {self.stats['truncated_fixed_from_api']} from API")
        
        return bookmarks
    
    def get_stats(self) -> Dict:
        """Get statistics about the processing."""
        return self.stats
    
    def _is_truncated(self, content: str) -> bool:
        """
        Check if content appears to be truncated.
        
        Looks for indicators like "..." at the end, or other common truncation patterns.
        """
        if not content:
            return False
            
        # Common truncation patterns
        patterns = [
            r'\.{3}$',                 # Ends with ...
            r'\.{3}\s*$',              # Ends with ... and optional whitespace
            r'\.\.\.$',                # Ends with ...
            r'…$',                     # Ends with Unicode ellipsis
            r'https://t\.co/\w+$',     # Ends with a t.co URL (likely truncated)
            r'\w+…$'                   # Word followed by ellipsis
        ]
        
        # Check if content matches any truncation pattern
        return any(re.search(pattern, content.strip()) for pattern in patterns)
    
    def _extract_tweet_id(self, url: str) -> Optional[str]:
        """
        Extract tweet ID from a Twitter URL.
        
        Handles various Twitter URL formats:
        - https://twitter.com/username/status/1234567890
        - https://x.com/username/status/1234567890
        - twitter/username/status/1234567890
        - https://twitter.com/i/web/status/1234567890
        """
        if not url:
            return None
            
        # Handle twitter.com, x.com, and twitter URLs without domain prefix
        valid_domains = ['twitter.com', 'x.com']
        is_valid_domain = any(domain in url.lower() for domain in valid_domains) or url.lower().startswith('twitter/')
        
        if not is_valid_domain:
            return None
            
        # Extract tweet ID from URL pattern
        if '/status/' in url:
            # Split by /status/ and take everything after it
            parts = url.split('/status/')
            if len(parts) < 2:
                return None
                
            # Take the first segment after status (the ID)
            tweet_id = parts[1].split('/')[0]
            
            # Remove any query parameters
            tweet_id = tweet_id.split('?')[0]
            
            # Validate that we have a numeric ID
            if tweet_id.isdigit():
                return tweet_id
        
        return None
    
    def _extract_retweet_info(self, content: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Extract retweet information from content.
        
        Returns:
            Tuple of (is_retweet, original_author, original_content)
        """
        # Pattern to match "RT @username: content"
        rt_pattern = r'^RT @([a-zA-Z0-9_]+):\s+(.*)'
        match = re.match(rt_pattern, content, re.DOTALL)
        
        if match:
            original_author = match.group(1)
            original_content = match.group(2)
            return True, original_author, original_content
        
        return False, None, None
    
    def _fix_twitter_content(self, bookmark: Dict) -> Dict:
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
            
            # Update stats
            self.stats["content_fixed_count"] += 1
        
        return bookmark
    
    def _fix_retweet(self, bookmark: Dict) -> Dict:
        """
        Fix a retweet bookmark by extracting original content and reformatting.
        """
        # Only process Twitter bookmarks
        source = bookmark.get('source', '')
        if 'twitter' not in source.lower():
            return bookmark
        
        # Get the original content
        content = bookmark.get('content', '')
        
        # Skip if no content
        if not content:
            return bookmark
        
        # Check if this is a retweet
        is_retweet, original_author, original_content = self._extract_retweet_info(content)
        
        if not is_retweet:
            return bookmark
        
        try:
            # Get the current markdown
            current_markdown = bookmark.get('markdown', '')
            
            # Create new markdown that emphasizes the original tweet
            # Extract header and footer from current markdown
            lines = current_markdown.split('\n')
            header_lines = []
            footer_lines = []
            content_start = False
            content_end = False
            
            for i, line in enumerate(lines):
                if '## Content' in line:
                    content_start = True
                    header_lines = lines[:i+2]  # Include the ## Content line and the blank line after it
                elif content_start and line.strip() and not content_end:
                    # This is part of the content - skip it
                    pass
                elif content_start and not line.strip() and not content_end:
                    # Empty line after content
                    content_end = True
                    footer_lines = lines[i:]
            
            # Update metadata to indicate this is a retweet
            if 'metadata' not in bookmark:
                bookmark['metadata'] = {}
            
            bookmark['metadata']['is_retweet'] = True
            bookmark['metadata']['original_author'] = original_author
            bookmark['metadata']['retweet_fixed'] = True
            
            # Create new markdown
            new_markdown = '\n'.join(header_lines)
            new_markdown += f"**Original Tweet by @{original_author}**\n\n{original_content}\n\n"
            new_markdown += "\n".join(footer_lines)
            
            # Update bookmark
            bookmark['markdown'] = new_markdown
            bookmark['full_text'] = new_markdown
            # Also update the content field to remove the RT prefix
            bookmark['content'] = f"Original Tweet by @{original_author}: {original_content}"
            bookmark['retweet_fixed_at'] = datetime.now().isoformat()
            
            logger.info(f"Fixed retweet for {bookmark.get('url', 'No URL')}, original author: @{original_author}")
            
            # Update stats
            self.stats["retweet_fixed_count"] += 1
            
        except Exception as e:
            logger.error(f"Error fixing retweet: {str(e)}")
        
        return bookmark
    
    def _find_tweet_in_cache_files(self, tweet_id: str) -> Optional[Dict]:
        """
        Search through all cache files for the given tweet ID.
        
        Args:
            tweet_id: The tweet ID to search for
            
        Returns:
            Dict containing tweet data if found, None otherwise
        """
        try:
            # First check the standard cache directory
            standard_cache_pattern = f"{self.cache_dir}/*/UserTweetsAndReplies.json"
            cache_files = glob.glob(standard_cache_pattern, recursive=False)
            
            # Also check the likes directory
            likes_pattern = f"{self.cache_dir}/*/Likes.json"
            cache_files.extend(glob.glob(likes_pattern, recursive=False))
            
            # Check the legacy cache directory
            legacy_cache_pattern = f"cache/twitter_*.json"
            cache_files.extend(glob.glob(legacy_cache_pattern, recursive=False))
            
            # Also check the test_cache directory
            test_cache_pattern = f"test_cache/twitter_*.json"
            cache_files.extend(glob.glob(test_cache_pattern, recursive=False))
            
            logger.info(f"Scanning {len(cache_files)} cache files for tweet {tweet_id}")
            
            # Search through each cache file
            for cache_file in cache_files:
                try:
                    with open(cache_file, 'r', encoding='utf-8') as f:
                        try:
                            cache_data = json.load(f)
                            
                            # Check if this file contains the tweet directly
                            # This is for legacy cache files
                            if 'thread_id' in cache_data.get('metadata', {}) and cache_data['metadata']['thread_id'] == tweet_id:
                                logger.info(f"Found direct match for tweet {tweet_id} in {cache_file}")
                                return cache_data
                            
                            # Check if this tweet is in the 'tweets' array in metadata
                            if 'tweets' in cache_data.get('metadata', {}):
                                for tweet in cache_data['metadata']['tweets']:
                                    if tweet.get('id') == tweet_id:
                                        logger.info(f"Found tweet {tweet_id} in metadata.tweets array in {cache_file}")
                                        return cache_data
                            
                            # For newer Twitter API format (UserTweetsAndReplies.json, Likes.json)
                            if isinstance(cache_data, list):
                                # This might be a list of API responses
                                for item in cache_data:
                                    # Look for tweet entries
                                    if 'data' in item and 'user' in item['data']:
                                        try:
                                            timeline = item['data']['user']['result']['timeline_v2']['timeline']
                                            for instruction in timeline.get('instructions', []):
                                                if instruction['type'] == 'TimelineAddEntries':
                                                    for entry in instruction.get('entries', []):
                                                        if 'entryId' in entry and f"tweet-{tweet_id}" in entry['entryId']:
                                                            logger.info(f"Found tweet {tweet_id} in entries array in {cache_file}")
                                                            return self._extract_tweet_from_entry(entry, tweet_id)
                                        except (KeyError, TypeError):
                                            pass
                                            
                            # Check if this is a direct Twitter API response and contains the tweet
                            if 'data' in cache_data and 'user' in cache_data['data']:
                                try:
                                    timeline = cache_data['data']['user']['result']['timeline_v2']['timeline']
                                    for instruction in timeline.get('instructions', []):
                                        if instruction['type'] == 'TimelineAddEntries':
                                            for entry in instruction.get('entries', []):
                                                if 'entryId' in entry and f"tweet-{tweet_id}" in entry['entryId']:
                                                    logger.info(f"Found tweet {tweet_id} in entries array in {cache_file}")
                                                    return self._extract_tweet_from_entry(entry, tweet_id)
                                except (KeyError, TypeError):
                                    pass
                                
                        except json.JSONDecodeError:
                            logger.warning(f"Error parsing JSON in {cache_file}")
                            continue
                except Exception as e:
                    logger.warning(f"Error reading cache file {cache_file}: {str(e)}")
                    continue
                    
            logger.info(f"Tweet {tweet_id} not found in any cache file")
            return None
            
        except Exception as e:
            logger.error(f"Error searching for tweet {tweet_id} in cache files: {str(e)}")
            return None
    
    def _extract_tweet_from_entry(self, entry: Dict, tweet_id: str) -> Optional[Dict]:
        """
        Extract tweet data from a Twitter API entry.
        
        Args:
            entry: Entry data from Twitter API response
            tweet_id: The ID of the tweet to extract
            
        Returns:
            Dict with extracted tweet data or None if extraction fails
        """
        try:
            # Navigate to the tweet result
            if 'content' in entry and 'itemContent' in entry['content']:
                item_content = entry['content']['itemContent']
                if 'tweet_results' in item_content and 'result' in item_content['tweet_results']:
                    tweet_result = item_content['tweet_results']['result']
                    
                    # Extract text content
                    text = ""
                    if 'legacy' in tweet_result and 'full_text' in tweet_result['legacy']:
                        text = tweet_result['legacy']['full_text']
                    elif 'note_tweet' in tweet_result:
                        note_tweet = tweet_result['note_tweet']['note_tweet_results']['result']
                        text = note_tweet.get('text', '')
                    
                    # If no text was found, we can't proceed
                    if not text:
                        return None
                    
                    # Extract media if available
                    media = []
                    if 'legacy' in tweet_result and 'extended_entities' in tweet_result['legacy']:
                        extended_entities = tweet_result['legacy']['extended_entities']
                        if 'media' in extended_entities:
                            for media_item in extended_entities['media']:
                                media_url = media_item.get('media_url_https', '')
                                if media_url:
                                    media.append(f"{media_url}?format=jpg&name=large")
                    
                    # Extract author info
                    author = {}
                    if 'core' in tweet_result and 'user_results' in tweet_result['core']:
                        user = tweet_result['core']['user_results']['result']['legacy']
                        author = {
                            'name': user.get('name', ''),
                            'screen_name': user.get('screen_name', ''),
                            'followers_count': user.get('followers_count', 0)
                        }
                    
                    # Extract metrics
                    metrics = {}
                    if 'legacy' in tweet_result:
                        legacy = tweet_result['legacy']
                        metrics = {
                            'favorite_count': legacy.get('favorite_count', 0),
                            'retweet_count': legacy.get('retweet_count', 0),
                            'reply_count': legacy.get('reply_count', 0)
                        }
                    
                    # Create result in format similar to TwitterThreadFetcher output
                    result = {
                        'status': 'success',
                        'content': text,
                        'metadata': {
                            'thread_id': tweet_id,
                            'author': author,
                            'tweet_count': 1,
                            'type': 'thread',
                            'tweets': [
                                {
                                    'id': tweet_id,
                                    'text': text,
                                    'media': media,
                                    'created_at': tweet_result['legacy'].get('created_at', '') if 'legacy' in tweet_result else '',
                                    'favorite_count': metrics.get('favorite_count', 0),
                                    'retweet_count': metrics.get('retweet_count', 0),
                                    'reply_count': metrics.get('reply_count', 0)
                                }
                            ]
                        }
                    }
                    
                    return result
        
        except Exception as e:
            logger.error(f"Error extracting tweet {tweet_id} from entry: {str(e)}")
        
        return None
    
    def _fix_truncated_tweet_from_cache(self, bookmark: Dict) -> Dict:
        """
        Fix a truncated tweet by searching for its complete content in cache files.
        """
        # Only process Twitter bookmarks
        source = bookmark.get('source', '')
        if 'twitter' not in source.lower():
            return bookmark
        
        # Get the content
        content = bookmark.get('content', '')
        
        # Skip if no content
        if not content:
            return bookmark
        
        # Check if content is truncated
        if not self._is_truncated(content):
            return bookmark
        
        # Update stats
        self.stats["truncated_count"] += 1
        
        try:
            # Get tweet URL
            url = bookmark.get('url', '')
            if not url:
                logger.warning(f"No URL found for bookmark with truncated content: {content[:50]}...")
                return bookmark
            
            # Extract tweet ID
            tweet_id = self._extract_tweet_id(url)
            if not tweet_id:
                logger.warning(f"Could not extract tweet ID from URL: {url}")
                return bookmark
            
            # Search for tweet in cache files
            logger.info(f"Searching cache for tweet ID: {tweet_id}")
            tweet_data = self._find_tweet_in_cache_files(tweet_id)
            
            # Check if we found tweet data
            if not tweet_data or tweet_data.get('status') != 'success':
                logger.warning(f"Could not find tweet {tweet_id} in cache files")
                return bookmark
            
            # Extract full content from the result
            full_content = tweet_data.get('content', '')
            
            if not full_content:
                logger.warning(f"No content found in cached data for tweet {tweet_id}")
                return bookmark
            
            # Update the bookmark with the full content
            logger.info(f"Updating truncated content for tweet {tweet_id} from cache")
            
            # Update content field
            bookmark['content'] = full_content
            
            # Update markdown to include the full content
            current_markdown = bookmark.get('markdown', '')
            new_markdown = current_markdown
            
            # Find the content section in the markdown
            content_start_marker = "## Content"
            content_start = current_markdown.find(content_start_marker)
            
            if content_start != -1:
                # Extract header (everything before content)
                header = current_markdown[:content_start + len(content_start_marker) + 1]
                
                # Find content end (first blank line after content)
                content_end = current_markdown.find("\n\n", content_start + len(content_start_marker))
                
                # If no blank line, assume rest of text is content
                if content_end == -1:
                    footer = ""
                else:
                    footer = current_markdown[content_end:]
                
                # Create new markdown with full content
                new_markdown = f"{header}\n{full_content}\n{footer}"
            
            # Update bookmark
            bookmark['markdown'] = new_markdown
            bookmark['full_text'] = new_markdown
            bookmark['truncated_fixed_at'] = datetime.now().isoformat()
            
            # Update metadata
            if 'metadata' not in bookmark:
                bookmark['metadata'] = {}
            
            bookmark['metadata']['truncated_fixed'] = True
            bookmark['metadata']['cached_fix'] = True
            
            # Update with any additional metadata from the fetched result
            if 'metadata' in tweet_data:
                # Only add new keys, don't overwrite existing ones
                for key, value in tweet_data['metadata'].items():
                    if key not in bookmark['metadata']:
                        bookmark['metadata'][key] = value
            
            logger.info(f"Successfully fixed truncated content for tweet {tweet_id} from cache")
            
            # Update stats
            self.stats["truncated_fixed_count"] += 1
            self.stats["truncated_fixed_from_cache"] += 1
        
        except Exception as e:
            logger.error(f"Error fixing truncated tweet: {str(e)}")
        
        return bookmark
    
    def _fix_truncated_tweet(self, bookmark: Dict) -> Dict:
        """
        Fix a truncated tweet by fetching the full content from Twitter API.
        """
        # Only process Twitter bookmarks
        source = bookmark.get('source', '')
        if 'twitter' not in source.lower():
            return bookmark
        
        # Get the content
        content = bookmark.get('content', '')
        
        # Skip if no content
        if not content:
            return bookmark
        
        # Check if content is truncated
        if not self._is_truncated(content):
            return bookmark
        
        # Skip if already fixed by cache
        if bookmark.get('metadata', {}).get('cached_fix', False):
            return bookmark
        
        try:
            # Import TwitterThreadFetcher
            from tools.twitter_thread_fetcher import TwitterThreadFetcher
            
            # Get tweet URL
            url = bookmark.get('url', '')
            if not url:
                logger.warning(f"No URL found for bookmark with truncated content: {content[:50]}...")
                return bookmark
            
            # Extract tweet ID
            tweet_id = self._extract_tweet_id(url)
            if not tweet_id:
                logger.warning(f"Could not extract tweet ID from URL: {url}")
                return bookmark
            
            # Initialize TwitterThreadFetcher
            fetcher = TwitterThreadFetcher()
            
            # Fetch complete thread/tweet
            logger.info(f"Fetching complete content for tweet ID: {tweet_id}")
            result = fetcher.process_url(url)
            
            # Check if fetch was successful
            if result.get('status') != 'success':
                logger.error(f"Failed to fetch tweet {tweet_id}: {result.get('error', 'Unknown error')}")
                return bookmark
            
            # Extract full content from the result
            full_content = result.get('content', '')
            
            if not full_content:
                logger.warning(f"No content returned for tweet {tweet_id}")
                return bookmark
            
            # Update the bookmark with the full content
            logger.info(f"Updating truncated content for tweet {tweet_id}")
            
            # Update content field
            bookmark['content'] = full_content
            
            # Update markdown to include the full content
            current_markdown = bookmark.get('markdown', '')
            new_markdown = current_markdown
            
            # Find the content section in the markdown
            content_start_marker = "## Content"
            content_start = current_markdown.find(content_start_marker)
            
            if content_start != -1:
                # Extract header (everything before content)
                header = current_markdown[:content_start + len(content_start_marker) + 1]
                
                # Find content end (first blank line after content)
                content_end = current_markdown.find("\n\n", content_start + len(content_start_marker))
                
                # If no blank line, assume rest of text is content
                if content_end == -1:
                    footer = ""
                else:
                    footer = current_markdown[content_end:]
                
                # Create new markdown with full content
                new_markdown = f"{header}\n{full_content}\n{footer}"
            
            # Update bookmark
            bookmark['markdown'] = new_markdown
            bookmark['full_text'] = new_markdown
            bookmark['truncated_fixed_at'] = datetime.now().isoformat()
            
            # Update metadata
            if 'metadata' not in bookmark:
                bookmark['metadata'] = {}
            
            bookmark['metadata']['truncated_fixed'] = True
            bookmark['metadata']['api_fix'] = True
            
            # Update with any additional metadata from the fetched result
            if 'metadata' in result:
                # Only add new keys, don't overwrite existing ones
                for key, value in result['metadata'].items():
                    if key not in bookmark['metadata']:
                        bookmark['metadata'][key] = value
            
            logger.info(f"Successfully fixed truncated content for tweet {tweet_id}")
            
            # Update stats
            self.stats["truncated_fixed_count"] += 1
            self.stats["truncated_fixed_from_api"] += 1
        
        except Exception as e:
            logger.error(f"Error fixing truncated tweet: {str(e)}")
        
        return bookmark


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

def main():
    """Main function when run as standalone script."""
    import argparse
    
    # Configure logging for command-line usage
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("twitter_processor.log")
        ]
    )
    
    parser = argparse.ArgumentParser(description="Process Twitter bookmarks to fix various issues")
    parser.add_argument('--input', '-i', required=True, help="Input JSONL file")
    parser.add_argument('--output', '-o', help="Output JSONL file (defaults to input-twitter-fixed.jsonl)")
    parser.add_argument('--cache-dir', '-c', default="data", help="Directory containing Twitter cache files")
    parser.add_argument('--batch-size', '-b', type=int, default=50, help="Number of bookmarks to process in each batch")
    parser.add_argument('--skip-content', action="store_true", help="Skip fixing content mismatches")
    parser.add_argument('--skip-retweets', action="store_true", help="Skip fixing retweet formatting")
    parser.add_argument('--skip-truncated', action="store_true", help="Skip fixing truncated tweets")
    parser.add_argument('--backup', action="store_true", help="Create a backup of the input file")
    
    args = parser.parse_args()
    
    # Set default output file if not provided
    if not args.output:
        input_path = Path(args.input)
        args.output = str(input_path.with_stem(f"{input_path.stem}-twitter-fixed"))
    
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
    
    # Initialize processor
    processor = TwitterProcessor(cache_dir=args.cache_dir, batch_size=args.batch_size)
    
    # Process bookmarks
    fixed_bookmarks = processor.process_bookmarks(
        bookmarks,
        fix_content=not args.skip_content,
        fix_retweets=not args.skip_retweets,
        fix_truncated=not args.skip_truncated
    )
    
    # Save processed bookmarks
    success = save_bookmarks(fixed_bookmarks, args.output)
    if not success:
        logger.error("Failed to save processed bookmarks. Exiting.")
        return 1
    
    # Print summary stats
    stats = processor.get_stats()
    print("\nTwitter Processing Summary:")
    print(f"Processed {stats['twitter_count']} Twitter bookmarks")
    if not args.skip_content:
        print(f"Fixed {stats['content_fixed_count']} content mismatches")
    if not args.skip_retweets:
        print(f"Fixed {stats['retweet_fixed_count']} retweets")
    if not args.skip_truncated:
        print(f"Found {stats['truncated_count']} truncated tweets")
        print(f"Fixed {stats['truncated_fixed_count']} truncated tweets")
        print(f"  - {stats['truncated_fixed_from_cache']} from cache")
        print(f"  - {stats['truncated_fixed_from_api']} from API")
    
    logger.info(f"Twitter processing complete. See {args.output} for the processed data.")
    return 0

if __name__ == "__main__":
    exit(main())