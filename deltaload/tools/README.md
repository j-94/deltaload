# Twitter Thread Fetcher

A module for fetching and processing Twitter/X.com thread content using their API.

## Features

- Extract thread content from Twitter/X URLs
- Handle various URL formats (twitter.com, x.com)
- Extract media URLs (videos, images)
- Format and structure thread data
- Extract thread metadata (engagement stats, author info)
- Command-line interface for direct usage

## Usage

```python
from tools.twitter_thread_fetcher import TwitterThreadFetcher

# Initialize with Twitter API credentials
fetcher = TwitterThreadFetcher()

# Process a Twitter URL
result = fetcher.process_url("https://twitter.com/username/status/123456789")
print(result['content'])  # Thread text content
print(result['metadata'])  # Thread metadata

# Directly fetch a thread by tweet ID
thread = fetcher.get_conversation_thread("123456789")
```

## Command-line usage

```bash
# Process a Twitter URL
python tools/twitter_thread_fetcher.py https://twitter.com/username/status/123456789

# Fetch a thread by tweet ID
python tools/twitter_thread_fetcher.py --tweet-id 123456789

# Use mock data for testing (no API credentials needed)
python tools/twitter_thread_fetcher.py --mock https://twitter.com/username/status/123456789
```

## Environment Variables

The following environment variables are required:

- `TWITTER_USER_ID`: Your Twitter user ID
- `TWITTER_CT0`: Your ct0 cookie value
- `TWITTER_AUTH_TOKEN`: Your auth_token cookie value