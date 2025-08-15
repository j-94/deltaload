"""Twitter thread fetcher module."""

import os
import json
import logging
import requests
from typing import List, Dict, Optional
from datetime import datetime, timezone
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class TwitterThreadFetcher:
    """Twitter thread fetcher using Twitter API.
    
    This class handles retrieving Twitter thread contents by using the Twitter/X.com internal API.
    It requires authentication with valid Twitter cookies (ct0 and auth_token).
    """
    
    def _generate_mock_data(self, url: str, tweet_id: str) -> Dict:
        """Generate mock data for testing purposes."""
        mock_date = datetime.now(timezone.utc).isoformat()
        
        return {
            'url': url,
            'source': 'twitter',
            'status': 'success',
            'content': 'This is a mock tweet thread for testing.\n\nIt contains multiple mock tweets.',
            'created_at': mock_date,
            'metadata': {
                'thread_id': tweet_id,
                'author': {
                    'name': 'Test User',
                    'screen_name': 'testuser',
                    'followers_count': 1000
                },
                'tweet_count': 2,
                'type': 'thread',
                'tweets': [
                    {
                        'id': tweet_id,
                        'text': 'This is a mock tweet thread for testing.',
                        'media': [],
                        'created_at': mock_date,
                        'favorite_count': 42,
                        'retweet_count': 10,
                        'reply_count': 5
                    },
                    {
                        'id': str(int(tweet_id) + 1),
                        'text': 'It contains multiple mock tweets.',
                        'media': [],
                        'created_at': mock_date,
                        'favorite_count': 21,
                        'retweet_count': 5,
                        'reply_count': 2
                    }
                ]
            }
        }
    
    def __init__(self, use_env=True, user_id=None, ct0=None, auth_token=None):
        """Initialize with Twitter API credentials.
        
        Args:
            use_env: Whether to use environment variables (default: True)
            user_id: Optional Twitter user ID to override environment variable
            ct0: Optional ct0 cookie value to override environment variable
            auth_token: Optional auth token to override environment variable
        """
        # Load environment variables
        load_dotenv()
        
        # Get credentials from parameters or environment variables
        self.user_id = user_id or os.getenv("TWITTER_USER_ID")
        self.ct0 = ct0 or os.getenv("TWITTER_CT0")
        self.auth_token = auth_token or os.getenv("TWITTER_AUTH_TOKEN")
        
        # Validate required tokens if not in test mode
        if use_env and not all([self.user_id, self.ct0, self.auth_token]):
            logger.warning("Missing required environment variables. API calls will likely fail.")
            
        logger.info(f"Initializing TwitterThreadFetcher with user_id: {self.user_id or 'not set'}")
        if self.auth_token and self.ct0:
            logger.debug(f"Using auth_token: {self.auth_token[:5]}*** ct0: {self.ct0[:5]}***")
        else:
            logger.debug("No credentials provided, only mock mode will work")
        
        # Initialize headers with default values
        self.headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            'x-client-transaction-id': 'twitter-web',
            'Referer': 'https://twitter.com/',
            'Origin': 'https://twitter.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Connection': 'keep-alive',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en',
            'x-twitter-active-user': 'yes'
        }
        
        # Add auth-related headers if credentials are provided
        if self.auth_token and self.ct0:
            self.headers['cookie'] = f'auth_token={self.auth_token}; ct0={self.ct0}'
            self.headers['x-csrf-token'] = self.ct0
        
        # Set up cookies with default empty values
        self.cookies = {}
        
        # Add auth-related cookies if credentials are provided
        if self.auth_token:
            self.cookies['auth_token'] = self.auth_token
        if self.ct0:
            self.cookies['ct0'] = self.ct0
        if self.user_id:
            self.cookies['twid'] = f'u%3D{self.user_id}'
        
        logger.info("TwitterThreadFetcher initialized successfully")
        logger.debug(f"Using cookies: {self.cookies}")

    def extract_tweet_id_from_url(self, url: str) -> Optional[str]:
        """Extract tweet ID from Twitter URL.
        
        Handles various Twitter URL formats:
        - https://twitter.com/username/status/1234567890
        - https://x.com/username/status/1234567890
        - twitter/username/status/1234567890
        - https://twitter.com/i/web/status/1234567890
        - https://twitter.com/username/status/1234567890?s=20
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
        
    def _extract_media_urls(self, tweet_result: Dict) -> List[str]:
        """Extract media URLs from tweet."""
        media_urls = []
        
        try:
            if 'legacy' in tweet_result:
                if 'extended_entities' in tweet_result['legacy']:
                    for media in tweet_result['legacy']['extended_entities'].get('media', []):
                        if media['type'] == 'video' or media['type'] == 'animated_gif':
                            # Get highest quality video
                            variants = media['video_info']['variants']
                            video_variants = [v for v in variants if 'bitrate' in v]
                            if video_variants:
                                best_video = max(video_variants, key=lambda x: x['bitrate'])
                                media_urls.append(best_video['url'])
                        elif media['type'] == 'photo':
                            # Get highest quality photo
                            media_urls.append(f"{media['media_url_https']}?format=jpg&name=4096x4096")
        except Exception as e:
            logger.error(f"Error extracting media URLs: {str(e)}")
            
        return media_urls

    def _extract_tweet_content(self, tweet_result: Dict) -> Dict:
        """Extract tweet content from the tweet result object."""
        tweet_data = {}
        
        # Get basic tweet info
        tweet_data['id'] = tweet_result.get('rest_id')
        legacy = tweet_result.get('legacy', {})
        tweet_data['created_at'] = legacy.get('created_at')
        
        # Handle both regular tweets and note tweets
        if 'note_tweet' in tweet_result:
            note_tweet = tweet_result['note_tweet']['note_tweet_results']['result']
            tweet_data['text'] = note_tweet.get('text', '')
        else:
            tweet_data['text'] = legacy.get('full_text', '')
        
        # Get media URLs
        tweet_data['media'] = self._extract_media_urls(tweet_result)
        
        # Get engagement metrics
        tweet_data['favorite_count'] = legacy.get('favorite_count', 0)
        tweet_data['retweet_count'] = legacy.get('retweet_count', 0)
        tweet_data['reply_count'] = legacy.get('reply_count', 0)
        
        # Get user info from core
        if 'core' in tweet_result:
            user = tweet_result['core']['user_results']['result']['legacy']
            tweet_data['author'] = {
                'name': user.get('name'),
                'screen_name': user.get('screen_name'),
                'followers_count': user.get('followers_count')
            }
        
        return tweet_data
        
    def fetch_tweet_detail(self, tweet_id: str, max_retries=3, initial_backoff=5) -> Dict:
        """Fetch details for a specific tweet using GraphQL.
        
        Args:
            tweet_id: The ID of the tweet to fetch
            max_retries: Maximum number of retry attempts for rate limits
            initial_backoff: Initial backoff time in seconds (will increase exponentially)
            
        Returns:
            Dict containing tweet details or None if fetching failed
        """
        variables = {
            "focalTweetId": tweet_id,
            "with_rux_injections": False,
            "includePromotedContent": False,
            "withCommunity": True,
            "withQuickPromoteEligibilityTweetFields": True,
            "withBirdwatchNotes": True,
            "withVoice": True,
            "withV2Timeline": True
        }
        
        features = {
            "responsive_web_twitter_blue_verified_badge_is_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "tweetypie_unmention_optimization_enabled": True,
            "vibe_api_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "tweet_awards_web_tipping_enabled": False,
            "freedom_of_speech_not_reach_fetch_enabled": False,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
            "responsive_web_enhance_cards_enabled": False,
            "responsive_web_twitter_article_tweet_consumption_enabled": False,
            "responsive_web_media_download_video_enabled": True,
            "rweb_lists_timeline_redesign_enabled": True,
            "creator_subscriptions_tweet_preview_api_enabled": True
        }

        params = {
            'variables': json.dumps(variables),
            'features': json.dumps(features)
        }
        
        url = "https://twitter.com/i/api/graphql/NmCeCgkVlsRGS1cAwqtgmw/TweetDetail"
        
        logger.info(f"Fetching tweet details for tweet_id: {tweet_id}")
        
        for attempt in range(max_retries + 1):
            try:
                response = requests.get(
                    url, 
                    headers=self.headers, 
                    params=params,
                    cookies=self.cookies,
                    timeout=10
                )
                
                # Handle success case
                if response.status_code == 200:
                    return response.json()
                
                # Handle rate limiting
                if response.status_code == 429:
                    # If this is our last retry, give up
                    if attempt == max_retries:
                        logger.error(f"Rate limit exceeded after {max_retries} retries. Giving up on tweet_id: {tweet_id}")
                        logger.error(f"Response: {response.text}")
                        return None
                    
                    # Calculate backoff time with exponential increase
                    backoff_time = initial_backoff * (2 ** attempt)
                    
                    # Parse rate limit headers if available
                    reset_time = None
                    if 'x-rate-limit-reset' in response.headers:
                        try:
                            reset_time = int(response.headers['x-rate-limit-reset'])
                            reset_dt = datetime.fromtimestamp(reset_time)
                            now = datetime.now()
                            wait_seconds = (reset_dt - now).total_seconds()
                            if wait_seconds > 0:
                                backoff_time = max(backoff_time, wait_seconds + 1)  # Add 1 second buffer
                        except (ValueError, TypeError):
                            pass
                    
                    logger.warning(f"Rate limit hit. Waiting {backoff_time:.1f} seconds before retry {attempt+1}/{max_retries}")
                    import time
                    time.sleep(backoff_time)
                    continue  # Retry after backoff
                
                # Handle other errors
                logger.error(f"Failed to fetch tweet. Status code: {response.status_code}")
                logger.error(f"Response: {response.text}")
                logger.debug(f"Request headers: {response.request.headers}")
                
                # Don't retry for client errors other than rate limiting
                if 400 <= response.status_code < 500 and response.status_code != 429:
                    return None
                
                # For server errors, retry with backoff
                if attempt < max_retries:
                    backoff_time = initial_backoff * (2 ** attempt)
                    logger.warning(f"Server error. Retrying in {backoff_time} seconds. Attempt {attempt+1}/{max_retries}")
                    import time
                    time.sleep(backoff_time)
                else:
                    return None
                    
            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {str(e)}")
                
                # Retry network errors with backoff
                if attempt < max_retries:
                    backoff_time = initial_backoff * (2 ** attempt)
                    logger.warning(f"Network error. Retrying in {backoff_time} seconds. Attempt {attempt+1}/{max_retries}")
                    import time
                    time.sleep(backoff_time)
                else:
                    return None
        
        return None

    def get_conversation_thread(self, tweet_id: str) -> List[Dict]:
        """Get the full conversation thread for a tweet."""
        thread = []
        original_author = None
        
        tweet_data = self.fetch_tweet_detail(tweet_id)
        if not tweet_data:
            return thread
            
        try:
            instructions = tweet_data['data']['threaded_conversation_with_injections_v2']['instructions']
            entries = next(i['entries'] for i in instructions if i['type'] == 'TimelineAddEntries')
            
            # Process main tweet and its replies
            for entry in entries:
                try:
                    if 'tweet_results' in entry.get('content', {}).get('itemContent', {}):
                        tweet_result = entry['content']['itemContent']['tweet_results']['result']
                        tweet = self._extract_tweet_content(tweet_result)
                        
                        # Set original author from the first tweet
                        if not original_author:
                            original_author = tweet['author']['screen_name']
                            
                        # Only include tweets from the original author
                        if tweet['author']['screen_name'] == original_author:
                            thread.append(tweet)
                            
                    elif 'items' in entry.get('content', {}):
                        # Handle conversation thread items
                        for item in entry['content']['items']:
                            if 'tweet_results' in item.get('item', {}).get('itemContent', {}):
                                tweet_result = item['item']['itemContent']['tweet_results']['result']
                                tweet = self._extract_tweet_content(tweet_result)
                                
                                # Only include tweets from the original author
                                if tweet['author']['screen_name'] == original_author:
                                    thread.append(tweet)
                                    
                except Exception as e:
                    logger.error(f"Skipping entry due to structure mismatch: {str(e)}")
                    continue
                    
            logger.info(f"Successfully fetched thread with {len(thread)} tweets")
            
            # Sort thread by tweet ID to ensure proper ordering
            thread.sort(key=lambda t: int(t['id']))
            
            return thread
            
        except Exception as e:
            logger.error(f"Error parsing tweet data: {str(e)}")
            import traceback
            logger.error(f"Full traceback: {traceback.format_exc()}")
            return thread

    def process_url(self, url: str, mock_data=False) -> Dict:
        """Process a Twitter URL to extract thread data.
        
        Args:
            url: The Twitter URL to process
            mock_data: Whether to return mock data for testing purposes
        """
        result = {
            'url': url,
            'source': 'twitter',
            'status': 'error',
            'content': '',
            'metadata': {}
        }
        
        tweet_id = self.extract_tweet_id_from_url(url)
        if not tweet_id:
            result['error'] = 'Not a valid Twitter URL or could not extract tweet ID'
            return result
            
        # Return mock data for testing if requested
        if mock_data:
            return self._generate_mock_data(url, tweet_id)
            
        thread = self.get_conversation_thread(tweet_id)
        if not thread:
            result['error'] = 'Failed to fetch thread or thread is empty'
            return result
            
        # Combine text from all tweets in thread
        thread_text = '\n\n'.join(tweet['text'] for tweet in thread)
        
        # Get first tweet's date as ISO format
        created_at = None
        if thread[0]['created_at']:
            try:
                dt = datetime.strptime(thread[0]['created_at'], "%a %b %d %H:%M:%S %z %Y")
                created_at = dt.isoformat()
            except ValueError:
                logger.error(f"Could not parse created_at: {thread[0]['created_at']}")
        
        # Build result
        result.update({
            'status': 'success',
            'content': thread_text,
            'created_at': created_at,
            'metadata': {
                'thread_id': tweet_id,
                'author': thread[0]['author'],
                'tweet_count': len(thread),
                'type': 'thread',
                'tweets': [
                    {
                        'id': tweet['id'],
                        'text': tweet['text'],
                        'media': tweet['media'],
                        'created_at': tweet['created_at'],
                        'favorite_count': tweet['favorite_count'],
                        'retweet_count': tweet['retweet_count'],
                        'reply_count': tweet['reply_count']
                    }
                    for tweet in thread
                ]
            }
        })
        
        return result

def format_tweet_text(text: str, width: int = 80) -> str:
    """Format tweet text for display"""
    lines = []
    words = text.split()
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + 1 <= width:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
            
    if current_line:
        lines.append(' '.join(current_line))
        
    return '\n'.join(lines)

if __name__ == "__main__":
    import sys
    import argparse
    
    # Configure logging for command-line use
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        handlers=[
            logging.FileHandler("twitter_thread.log"),
            logging.StreamHandler()
        ]
    )
    
    parser = argparse.ArgumentParser(description="Fetch Twitter thread content")
    parser.add_argument("url", nargs="?", help="Twitter URL to process")
    parser.add_argument("--tweet-id", help="Tweet ID to process directly")
    parser.add_argument("--mock", action="store_true", help="Use mock data for testing")
    parser.add_argument("--no-env", action="store_true", help="Don't use environment variables")
    
    args = parser.parse_args()
    
    if not args.url and not args.tweet_id:
        parser.error("Either a URL or tweet ID must be provided")
    
    try:
        fetcher = TwitterThreadFetcher(use_env=not args.no_env)
        
        if args.url:
            result = fetcher.process_url(args.url, mock_data=args.mock)
            print("\n=== URL Processing Result ===")
            print(json.dumps(result, indent=2))
        else:
            # Direct thread fetching
            thread = fetcher.get_conversation_thread(args.tweet_id)
            
            if thread:
                print("\n=== Thread Summary ===")
                print(f"Author: @{thread[0]['author']['screen_name']}")
                print(f"Total tweets: {len(thread)}")
                
                try:
                    print(f"Total engagement: {sum(t.get('favorite_count', 0) for t in thread)} likes, "
                           f"{sum(t.get('retweet_count', 0) for t in thread)} retweets, "
                           f"{sum(t.get('reply_count', 0) for t in thread)} replies")
                except Exception as e:
                    print(f"Error calculating engagement: {str(e)}")
                
                print("\n=== Thread Contents ===")
                for i, tweet in enumerate(thread, 1):
                    print(f"\n[Tweet {i}/{len(thread)}]")
                    print(f"Time: {tweet.get('created_at', 'unknown')}")
                    print(f"Text:\n{format_tweet_text(tweet.get('text', ''))}")
                    try:
                        print(f"Engagement: {tweet.get('favorite_count', 0)} likes, "
                              f"{tweet.get('retweet_count', 0)} retweets, "
                              f"{tweet.get('reply_count', 0)} replies")
                    except Exception as e:
                        print(f"Error showing engagement: {str(e)}")
                
                # Save to file
                output_file = f"thread_{thread[0]['id']}.json"
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(thread, f, ensure_ascii=False, indent=2)
                print(f"\nThread saved to {output_file}")
            else:
                print("Failed to fetch thread")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        import traceback
        print(traceback.format_exc(), file=sys.stderr)
        sys.exit(1)