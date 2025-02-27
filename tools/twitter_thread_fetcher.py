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
    """Twitter thread fetcher using Twitter API."""
    
    def __init__(self):
        """Initialize with Twitter API credentials."""
        # Load environment variables
        load_dotenv()
        
        # Get and validate environment variables
        self.user_id = os.getenv("TWITTER_USER_ID")
        self.ct0 = os.getenv("TWITTER_CT0")
        self.auth_token = os.getenv("TWITTER_AUTH_TOKEN")
        
        # Validate required tokens
        if not all([self.user_id, self.ct0, self.auth_token]):
            raise ValueError("Missing required environment variables. Please check TWITTER_USER_ID, TWITTER_CT0, and TWITTER_AUTH_TOKEN")
            
        logger.info(f"Initializing TwitterThreadFetcher with user_id: {self.user_id}")
        
        self.headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'cookie': f'auth_token={self.auth_token}; ct0={self.ct0}',
            'x-csrf-token': self.ct0,
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en',
            'x-twitter-active-user': 'yes',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            'Referer': 'https://twitter.com/',
            'Origin': 'https://twitter.com',
            'Connection': 'keep-alive'
        }
        
        # Set up cookies
        self.cookies = {
            'auth_token': self.auth_token,
            'ct0': self.ct0,
            'twid': f'u%3D{self.user_id}'
        }
        
        logger.info("TwitterThreadFetcher initialized successfully")

    def extract_tweet_id_from_url(self, url: str) -> Optional[str]:
        """Extract tweet ID from Twitter URL."""
        if not url:
            return None
            
        # Handle both twitter.com and x.com URLs
        if not any(domain in url.lower() for domain in ['twitter.com', 'x.com']):
            return None
            
        # Extract tweet ID from URL pattern
        if '/status/' in url:
            tweet_id = url.split('/status/')[1].split('/')[0].split('?')[0]
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
        
    def fetch_tweet_detail(self, tweet_id: str) -> Dict:
        """Fetch details for a specific tweet using GraphQL."""
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
            "longform_notetweets_consumption_enabled": True,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
            "responsive_web_media_download_video_enabled": True
        }

        params = {
            'variables': json.dumps(variables),
            'features': json.dumps(features)
        }
        
        url = "https://twitter.com/i/api/graphql/NmCeCgkVlsRGS1cAwqtgmw/TweetDetail"
        
        logger.info(f"Fetching tweet details for tweet_id: {tweet_id}")
        
        try:
            response = requests.get(
                url, 
                headers=self.headers, 
                params=params,
                cookies=self.cookies,
                timeout=10
            )
            
            if response.status_code != 200:
                logger.error(f"Failed to fetch tweet. Status code: {response.status_code}")
                logger.error(f"Response: {response.text}")
                return None
                
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
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

    def process_url(self, url: str) -> Dict:
        """Process a Twitter URL to extract thread data."""
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