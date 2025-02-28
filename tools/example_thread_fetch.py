#!/usr/bin/env python
"""Example script showing how to use the TwitterThreadFetcher."""

import json
from twitter_thread_fetcher import TwitterThreadFetcher

def main():
    """Demonstrate TwitterThreadFetcher usage."""
    # Initialize fetcher
    fetcher = TwitterThreadFetcher()
    
    # Example Twitter URL
    twitter_url = "https://twitter.com/elonmusk/status/1668027458457051137"
    
    # Process URL (use mock data in this example to avoid requiring credentials)
    result = fetcher.process_url(twitter_url, mock_data=True)
    
    # Print results
    print("\n=== Thread Content ===")
    print(result['content'])
    
    print("\n=== Thread Metadata ===")
    print(f"Author: @{result['metadata']['author']['screen_name']}")
    print(f"Tweet count: {result['metadata']['tweet_count']}")
    
    # Print formatted JSON
    print("\n=== Full Result ===")
    print(json.dumps(result, indent=2))
    
if __name__ == "__main__":
    main()