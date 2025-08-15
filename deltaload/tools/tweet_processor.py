"""
Unified Twitter processing module for tweet and thread processing.

This module provides a standardized way to process Twitter content:
- Handles both single tweets and threads
- Standardizes tweet metadata
- Provides consistent markdown formatting
- Supports media extraction and embedding
"""

import os
import json
import logging
import re
from typing import Dict, List, Optional, Union, Tuple
from datetime import datetime, timezone
from pathlib import Path

# Import existing fetcher for API access
from .twitter_thread_fetcher import TwitterThreadFetcher

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class TweetProcessor:
    """
    Unified processor for Twitter content.
    
    This class handles the processing of Twitter content from various sources,
    standardizing the metadata format and providing consistent markdown output.
    """
    
    def __init__(self, cache_dir: str = './data', use_api: bool = True):
        """
        Initialize the Tweet Processor.
        
        Args:
            cache_dir: Directory for cached tweet data
            use_api: Whether to use the Twitter API for fetching missing data
        """
        self.cache_dir = Path(cache_dir)
        self.use_api = use_api
        
        # Initialize Twitter API client if needed
        self.api_client = None
        if use_api:
            self.api_client = TwitterThreadFetcher()
            
        logger.info(f"TweetProcessor initialized with cache_dir={cache_dir}, use_api={use_api}")
    
    def process_tweet_url(self, url: str, force_refresh: bool = False) -> Dict:
        """
        Process a tweet URL and return standardized data.
        
        Args:
            url: Twitter/X.com URL to process
            force_refresh: Whether to force refresh data from API
            
        Returns:
            Dict containing processed tweet data
        """
        result = {
            'url': url,
            'source': 'twitter',
            'status': 'error',
            'content': '',
            'metadata': {},
            'processed_at': datetime.now(timezone.utc).isoformat()
        }
        
        try:
            # Extract tweet ID from URL
            tweet_id = self._extract_tweet_id(url)
            if not tweet_id:
                result['error'] = f"Could not extract tweet ID from URL: {url}"
                return result
                
            # Try to get from cache first
            tweet_data = self._get_from_cache(tweet_id)
            
            # If not in cache or force refresh, fetch from API
            if (not tweet_data or force_refresh) and self.use_api and self.api_client:
                logger.info(f"Fetching tweet {tweet_id} from API")
                api_result = self.api_client.process_url(url)
                
                if api_result and api_result.get('status') == 'success':
                    tweet_data = api_result
                    
                    # Cache the result
                    self._save_to_cache(tweet_id, tweet_data)
            
            # If we still don't have data, return error
            if not tweet_data:
                result['error'] = f"Could not retrieve data for tweet {tweet_id}"
                return result
                
            # Process and standardize the data
            processed_data = self._standardize_tweet_data(tweet_data)
            
            # Generate markdown
            markdown = self._generate_markdown(processed_data)
            
            # Update result
            result.update({
                'status': 'success',
                'content': processed_data.get('text', ''),
                'metadata': processed_data.get('metadata', {}),
                'markdown': markdown,
                'full_text': markdown,  # Use markdown as full_text
                'domain': 'twitter.com' if 'twitter.com' in url else 'x.com'
            })
            
            return result
            
        except Exception as e:
            logger.error(f"Error processing tweet URL {url}: {str(e)}")
            result['error'] = str(e)
            return result
    
    def process_tweet_data(self, tweet_data: Dict) -> Dict:
        """
        Process already fetched tweet data.
        
        Args:
            tweet_data: Raw tweet data to process
            
        Returns:
            Dict containing processed tweet data
        """
        try:
            # Standardize the data
            processed_data = self._standardize_tweet_data(tweet_data)
            
            # Generate markdown
            markdown = self._generate_markdown(processed_data)
            
            # Create result
            result = {
                'status': 'success',
                'content': processed_data.get('text', ''),
                'metadata': processed_data.get('metadata', {}),
                'markdown': markdown,
                'full_text': markdown,  # Use markdown as full_text
                'source': 'twitter',
                'processed_at': datetime.now(timezone.utc).isoformat()
            }
            
            # Add URL if available
            if 'url' in tweet_data:
                result['url'] = tweet_data['url']
                result['domain'] = 'twitter.com' if 'twitter.com' in tweet_data['url'] else 'x.com'
            
            return result
            
        except Exception as e:
            logger.error(f"Error processing tweet data: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'source': 'twitter',
                'processed_at': datetime.now(timezone.utc).isoformat()
            }
    
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
    
    def _get_from_cache(self, tweet_id: str) -> Optional[Dict]:
        """
        Try to get tweet data from cache.
        
        This method searches for cached tweet data in various formats.
        """
        try:
            # Look for thread cache files that might contain the tweet
            # Search through different user directories
            for user_dir in self.cache_dir.glob("*"):
                if not user_dir.is_dir():
                    continue
                    
                # Look for thread files
                for thread_file in user_dir.glob("*UserTweetsAndReplies.json"):
                    try:
                        with open(thread_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            
                            # Check if this file contains our tweet
                            # This depends on the structure of the cache files
                            # Determine if the tweet ID is in the data
                            if self._tweet_exists_in_data(data, tweet_id):
                                logger.info(f"Found tweet {tweet_id} in cache file {thread_file}")
                                return self._extract_tweet_from_data(data, tweet_id)
                    except Exception as e:
                        logger.warning(f"Error reading cache file {thread_file}: {str(e)}")
                
                # Look for like files
                for like_file in user_dir.glob("*Likes.json"):
                    try:
                        with open(like_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            
                            # Check if this file contains our tweet
                            if self._tweet_exists_in_data(data, tweet_id):
                                logger.info(f"Found tweet {tweet_id} in cache file {like_file}")
                                return self._extract_tweet_from_data(data, tweet_id)
                    except Exception as e:
                        logger.warning(f"Error reading cache file {like_file}: {str(e)}")
            
            logger.info(f"Tweet {tweet_id} not found in cache")
            return None
            
        except Exception as e:
            logger.error(f"Error accessing cache for tweet {tweet_id}: {str(e)}")
            return None
    
    def _tweet_exists_in_data(self, data: Union[List, Dict], tweet_id: str) -> bool:
        """
        Check if tweet exists in the data.
        
        This is a simplified implementation that needs to be adapted to
        the actual structure of the cache files.
        """
        try:
            # Handle different formats of cache data
            if isinstance(data, list):
                # For list of tweets
                for tweet in data:
                    if isinstance(tweet, dict):
                        # Direct ID match
                        if str(tweet.get('id')) == tweet_id or str(tweet.get('rest_id')) == tweet_id:
                            return True
                        
                        # Check nested Twitter API format
                        if 'data' in tweet and 'user' in tweet['data']:
                            try:
                                timeline = tweet['data']['user']['result']['timeline_v2']['timeline']
                                for instruction in timeline.get('instructions', []):
                                    if instruction['type'] == 'TimelineAddEntries':
                                        for entry in instruction.get('entries', []):
                                            if 'entryId' in entry and f"tweet-{tweet_id}" in entry['entryId']:
                                                return True
                                            
                                            if 'content' in entry and 'itemContent' in entry['content']:
                                                item_content = entry['content']['itemContent']
                                                if item_content.get('itemType') != 'TimelineTweet':
                                                    continue
                                                
                                                tweet_results = item_content.get('tweet_results', {})
                                                if not tweet_results or 'result' not in tweet_results:
                                                    continue
                                                
                                                result_tweet = tweet_results['result']
                                                if str(result_tweet.get('rest_id', '')) == tweet_id:
                                                    return True
                            except (KeyError, TypeError):
                                pass
                
                return False
                
            elif isinstance(data, dict):
                # Direct tweet
                if str(data.get('id')) == tweet_id or str(data.get('rest_id')) == tweet_id:
                    return True
                
                # Check in metadata tweets array
                if 'metadata' in data and 'tweets' in data['metadata']:
                    for tweet in data['metadata']['tweets']:
                        if str(tweet.get('id')) == tweet_id:
                            return True
                
                # Check nested Twitter API format
                if 'data' in data and 'user' in data['data']:
                    try:
                        timeline = data['data']['user']['result']['timeline_v2']['timeline']
                        for instruction in timeline.get('instructions', []):
                            if instruction['type'] == 'TimelineAddEntries':
                                for entry in instruction.get('entries', []):
                                    if 'entryId' in entry and f"tweet-{tweet_id}" in entry['entryId']:
                                        return True
                                    
                                    if 'content' in entry and 'itemContent' in entry['content']:
                                        item_content = entry['content']['itemContent']
                                        if item_content.get('itemType') != 'TimelineTweet':
                                            continue
                                        
                                        tweet_results = item_content.get('tweet_results', {})
                                        if not tweet_results or 'result' not in tweet_results:
                                            continue
                                        
                                        result_tweet = tweet_results['result']
                                        if str(result_tweet.get('rest_id', '')) == tweet_id:
                                            return True
                    except (KeyError, TypeError):
                        pass
                
                return False
            
            return False
            
        except Exception as e:
            logger.error(f"Error checking if tweet exists in data: {str(e)}")
            return False
    
    def _extract_tweet_from_data(self, data: Union[List, Dict], tweet_id: str) -> Optional[Dict]:
        """
        Extract a specific tweet from cached data.
        
        This is a simplified implementation that needs to be adapted to
        the actual structure of the cache files.
        """
        try:
            # Handle different formats of cache data
            if isinstance(data, list):
                # For list of tweets
                for tweet in data:
                    if isinstance(tweet, dict):
                        # Direct ID match
                        if str(tweet.get('id')) == tweet_id or str(tweet.get('rest_id')) == tweet_id:
                            return tweet
                        
                        # Check nested Twitter API format
                        if 'data' in tweet and 'user' in tweet['data']:
                            try:
                                timeline = tweet['data']['user']['result']['timeline_v2']['timeline']
                                for instruction in timeline.get('instructions', []):
                                    if instruction['type'] == 'TimelineAddEntries':
                                        for entry in instruction.get('entries', []):
                                            if 'entryId' in entry and f"tweet-{tweet_id}" in entry['entryId']:
                                                return tweet
                                            
                                            if 'content' in entry and 'itemContent' in entry['content']:
                                                item_content = entry['content']['itemContent']
                                                if item_content.get('itemType') != 'TimelineTweet':
                                                    continue
                                                
                                                tweet_results = item_content.get('tweet_results', {})
                                                if not tweet_results or 'result' not in tweet_results:
                                                    continue
                                                
                                                result_tweet = tweet_results['result']
                                                if str(result_tweet.get('rest_id', '')) == tweet_id:
                                                    return tweet
                            except (KeyError, TypeError):
                                pass
                
                # If we can't find the specific tweet, return the first one
                # This is useful for testing with random samples
                if data and isinstance(data[0], dict):
                    return data[0]
                    
                return None
                
            elif isinstance(data, dict):
                # Direct tweet
                if str(data.get('id')) == tweet_id or str(data.get('rest_id')) == tweet_id:
                    return data
                
                # Check in metadata tweets array
                if 'metadata' in data and 'tweets' in data['metadata']:
                    for tweet in data['metadata']['tweets']:
                        if str(tweet.get('id')) == tweet_id:
                            return data  # Return the whole thread data
                
                # Check nested Twitter API format
                if 'data' in data and 'user' in data['data']:
                    try:
                        timeline = data['data']['user']['result']['timeline_v2']['timeline']
                        for instruction in timeline.get('instructions', []):
                            if instruction['type'] == 'TimelineAddEntries':
                                for entry in instruction.get('entries', []):
                                    if 'entryId' in entry and f"tweet-{tweet_id}" in entry['entryId']:
                                        return data
                                    
                                    if 'content' in entry and 'itemContent' in entry['content']:
                                        item_content = entry['content']['itemContent']
                                        if item_content.get('itemType') != 'TimelineTweet':
                                            continue
                                        
                                        tweet_results = item_content.get('tweet_results', {})
                                        if not tweet_results or 'result' not in tweet_results:
                                            continue
                                        
                                        result_tweet = tweet_results['result']
                                        if str(result_tweet.get('rest_id', '')) == tweet_id:
                                            return data
                    except (KeyError, TypeError):
                        pass
                
                return None
            
            return None
            
        except Exception as e:
            logger.error(f"Error extracting tweet from data: {str(e)}")
            return None
    
    def _save_to_cache(self, tweet_id: str, data: Dict) -> bool:
        """
        Save tweet data to cache.
        
        Args:
            tweet_id: ID of the tweet
            data: Tweet data to cache
            
        Returns:
            bool: Whether the save was successful
        """
        try:
            # Create a special directory for cached tweets
            cache_dir = self.cache_dir / "processed_tweets"
            cache_dir.mkdir(parents=True, exist_ok=True)
            
            # Create a filename with timestamp
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            cache_file = cache_dir / f"{tweet_id}_{timestamp}.json"
            
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            logger.info(f"Saved tweet {tweet_id} to cache file {cache_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving tweet {tweet_id} to cache: {str(e)}")
            return False
    
    def _standardize_tweet_data(self, raw_data: Dict) -> Dict:
        """
        Standardize tweet data format.
        
        Args:
            raw_data: Raw tweet data from API or cache
            
        Returns:
            Dict with standardized structure
        """
        # Start with a basic structure
        result = {
            'id': '',
            'text': '',
            'created_at': '',
            'is_thread': False,
            'metadata': {
                'author': {
                    'name': '',
                    'screen_name': '',
                    'profile_image_url': ''
                },
                'metrics': {
                    'likes': 0,
                    'retweets': 0,
                    'replies': 0
                },
                'media': [],
                'urls': [],
                'hashtags': [],
                'mentions': [],
                'thread': {
                    'is_thread': False,
                    'position': 0,
                    'total_tweets': 0,
                    'tweets': []
                }
            }
        }
        
        try:
            # Handle different formats from different sources
            # This is where we need to map the input format to our standard format
            
            # If we have a full thread from TwitterThreadFetcher
            if 'metadata' in raw_data and 'tweets' in raw_data['metadata']:
                tweets = raw_data['metadata']['tweets']
                
                # Set thread info
                result['is_thread'] = len(tweets) > 1
                result['metadata']['thread']['is_thread'] = len(tweets) > 1
                result['metadata']['thread']['total_tweets'] = len(tweets)
                
                if tweets:
                    # Get the first tweet's data
                    first_tweet = tweets[0]
                    
                    # Basic tweet info
                    result['id'] = first_tweet.get('id', '')
                    result['text'] = first_tweet.get('text', '')
                    result['created_at'] = first_tweet.get('created_at', '')
                    
                    # Author info
                    if 'author' in first_tweet:
                        author = first_tweet['author']
                        result['metadata']['author'] = {
                            'name': author.get('name', ''),
                            'screen_name': author.get('screen_name', ''),
                            'profile_image_url': author.get('profile_image_url', '')
                        }
                    
                    # Metrics
                    result['metadata']['metrics'] = {
                        'likes': first_tweet.get('favorite_count', 0),
                        'retweets': first_tweet.get('retweet_count', 0),
                        'replies': first_tweet.get('reply_count', 0)
                    }
                    
                    # Media
                    result['metadata']['media'] = first_tweet.get('media', [])
                    
                    # All tweets in thread
                    result['metadata']['thread']['tweets'] = [
                        {
                            'id': t.get('id', ''),
                            'text': t.get('text', ''),
                            'created_at': t.get('created_at', ''),
                            'media': t.get('media', []),
                            'metrics': {
                                'likes': t.get('favorite_count', 0),
                                'retweets': t.get('retweet_count', 0),
                                'replies': t.get('reply_count', 0)
                            },
                            'position': i + 1
                        }
                        for i, t in enumerate(tweets)
                    ]
            
            # Handle individual tweet formats
            # This would need to be expanded based on the actual formats of the data
            elif 'legacy' in raw_data:
                # Handle Twitter API format
                legacy = raw_data['legacy']
                result['id'] = raw_data.get('rest_id', '')
                result['text'] = legacy.get('full_text', '')
                result['created_at'] = legacy.get('created_at', '')
                
                # Metrics
                result['metadata']['metrics'] = {
                    'likes': legacy.get('favorite_count', 0),
                    'retweets': legacy.get('retweet_count', 0),
                    'replies': legacy.get('reply_count', 0)
                }
                
                # Try to get user info
                if 'core' in raw_data and 'user_results' in raw_data['core']:
                    user = raw_data['core']['user_results']['result']['legacy']
                    result['metadata']['author'] = {
                        'name': user.get('name', ''),
                        'screen_name': user.get('screen_name', ''),
                        'profile_image_url': user.get('profile_image_url_https', '')
                    }
            
            # Handle Twitter API response format with nested tweet data
            elif 'data' in raw_data and 'user' in raw_data['data']:
                # This is the format from the Twitter likes cache
                entries = []
                
                # Navigate the nested structure to find tweet entries
                try:
                    timeline = raw_data['data']['user']['result']['timeline_v2']['timeline']
                    for instruction in timeline.get('instructions', []):
                        if instruction['type'] == 'TimelineAddEntries':
                            entries = instruction.get('entries', [])
                            break
                except (KeyError, TypeError):
                    pass
                
                # Process each entry to find tweet data
                for entry in entries:
                    if 'content' not in entry or 'itemContent' not in entry['content']:
                        continue
                    
                    item_content = entry['content']['itemContent']
                    if item_content.get('itemType') != 'TimelineTweet':
                        continue
                    
                    tweet_results = item_content.get('tweet_results', {})
                    if not tweet_results or 'result' not in tweet_results:
                        continue
                    
                    tweet = tweet_results['result']
                    
                    # Extract legacy data which contains the actual tweet content
                    if 'legacy' in tweet:
                        legacy = tweet['legacy']
                        result['id'] = tweet.get('rest_id', '')
                        result['text'] = legacy.get('full_text', '')
                        result['created_at'] = legacy.get('created_at', '')
                        
                        # Metrics
                        result['metadata']['metrics'] = {
                            'likes': legacy.get('favorite_count', 0),
                            'retweets': legacy.get('retweet_count', 0),
                            'replies': legacy.get('reply_count', 0)
                        }
                        
                        # Media extraction
                        if 'extended_entities' in legacy and 'media' in legacy['extended_entities']:
                            result['metadata']['media'] = []
                            for media in legacy['extended_entities']['media']:
                                media_url = media.get('media_url_https', '')
                                if media_url:
                                    media_obj = {
                                        'url': f"{media_url}?format=jpg&name=large",
                                        'type': media.get('type', 'photo'),
                                        'alt': media.get('ext_alt_text', 'Image')
                                    }
                                    result['metadata']['media'].append(media_obj)
                    
                    # Extract user info
                    if 'core' in tweet and 'user_results' in tweet['core']:
                        user = tweet['core']['user_results']['result']['legacy']
                        result['metadata']['author'] = {
                            'name': user.get('name', ''),
                            'screen_name': user.get('screen_name', ''),
                            'profile_image_url': user.get('profile_image_url_https', '')
                        }
                    
                    # We've found and processed one tweet, so break
                    break
            
            # Pass-through for fields we don't need to standardize
            if 'url' in raw_data:
                result['url'] = raw_data['url']
                
            # Extract hashtags, mentions, URLs using regex
            if result['text']:
                # Extract hashtags
                hashtags = re.findall(r'#(\w+)', result['text'])
                result['metadata']['hashtags'] = hashtags
                
                # Extract mentions
                mentions = re.findall(r'@(\w+)', result['text'])
                result['metadata']['mentions'] = mentions
                
                # Extract URLs (simplified regex)
                urls = re.findall(r'https?://[^\s]+', result['text'])
                result['metadata']['urls'] = urls
            
            return result
            
        except Exception as e:
            logger.error(f"Error standardizing tweet data: {str(e)}")
            # Return original data if standardization fails
            return {
                'id': raw_data.get('id', ''),
                'text': raw_data.get('text', ''),
                'created_at': raw_data.get('created_at', ''),
                'is_thread': False,
                'metadata': raw_data.get('metadata', {})
            }
    
    def _generate_markdown(self, tweet_data: Dict) -> str:
        """
        Generate markdown representation of a tweet.
        
        Args:
            tweet_data: Standardized tweet data
            
        Returns:
            Markdown string representation
        """
        try:
            markdown = ""
            
            # Get author info
            author = tweet_data.get('metadata', {}).get('author', {})
            author_name = author.get('name', 'Unknown')
            author_handle = author.get('screen_name', 'unknown')
            
            # Get tweet metrics
            metrics = tweet_data.get('metadata', {}).get('metrics', {})
            likes = metrics.get('likes', 0)
            retweets = metrics.get('retweets', 0)
            replies = metrics.get('replies', 0)
            
            # Add header
            markdown += f"# Tweet by {author_name} (@{author_handle})\n\n"
            
            # Add metadata
            created_at = tweet_data.get('created_at', '')
            if created_at:
                # Format the date if possible
                try:
                    date_obj = datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")
                    created_at = date_obj.strftime("%Y-%m-%d %H:%M:%S")
                except ValueError:
                    pass
                
                markdown += f"**Date:** {created_at}\n\n"
            
            markdown += f"**Likes:** {likes} | **Retweets:** {retweets} | **Replies:** {replies}\n\n"
            
            # Add divider
            markdown += "---\n\n"
            
            # Check if it's a thread
            is_thread = tweet_data.get('is_thread', False)
            thread_data = tweet_data.get('metadata', {}).get('thread', {})
            
            if is_thread and thread_data.get('is_thread', False):
                # It's a thread, add all tweets
                markdown += "## Thread\n\n"
                
                for tweet in thread_data.get('tweets', []):
                    # Add position indicator
                    position = tweet.get('position', 0)
                    markdown += f"### Tweet {position}/{thread_data.get('total_tweets', 0)}\n\n"
                    
                    # Add text
                    markdown += f"{tweet.get('text', '')}\n\n"
                    
                    # Add media
                    for media in tweet.get('media', []):
                        if 'url' in media:
                            alt = media.get('alt', 'Image')
                            markdown += f"![{alt}]({media['url']})\n\n"
                    
                    # Add metrics for each tweet
                    tweet_metrics = tweet.get('metrics', {})
                    likes = tweet_metrics.get('likes', 0)
                    retweets = tweet_metrics.get('retweets', 0)
                    replies = tweet_metrics.get('replies', 0)
                    
                    markdown += f"*Likes: {likes} | Retweets: {retweets} | Replies: {replies}*\n\n"
                    
                    # Add separator between tweets
                    if position < thread_data.get('total_tweets', 0):
                        markdown += "---\n\n"
            else:
                # Single tweet
                markdown += "## Content\n\n"
                markdown += f"{tweet_data.get('text', '')}\n\n"
                
                # Add media
                for media in tweet_data.get('metadata', {}).get('media', []):
                    if 'url' in media:
                        alt = media.get('alt', 'Image')
                        markdown += f"![{alt}]({media['url']})\n\n"
            
            # Add source link
            if 'url' in tweet_data:
                markdown += f"\n\n*Source: [{tweet_data['url']}]({tweet_data['url']})*\n"
            
            return markdown
            
        except Exception as e:
            logger.error(f"Error generating markdown: {str(e)}")
            return f"Error generating markdown: {str(e)}\n\nRaw content:\n{tweet_data.get('text', '')}" 