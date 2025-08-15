#!/usr/bin/env python3
"""
Script to analyze the structure of Twitter data in bookmarks
"""

import pandas as pd
import json
import os
from datetime import datetime
from pprint import pprint

# Path to the bookmark data
bookmarks_path = '/Users/imac/Desktop/ETL/deltaload/data-bookmark.jsonl'

# Function to load JSONL file
def load_jsonl(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"Error parsing line: {line[:100]}...")
    return data

# Load the data
print(f"Loading bookmarks from {bookmarks_path}...")
bookmarks = load_jsonl(bookmarks_path)
print(f"Loaded {len(bookmarks)} bookmarks")

# Convert to DataFrame
df = pd.DataFrame(bookmarks)

# Filter only Twitter data
twitter_df = df[df['source'].isin(['twitter', 'twitter_like'])].copy()
print(f"Total Twitter bookmarks: {len(twitter_df)}")

# Convert dates to datetime
if 'created_at' in twitter_df.columns:
    twitter_df['created_at'] = pd.to_datetime(twitter_df['created_at'], errors='coerce')

# Sort by created_at in descending order
twitter_df = twitter_df.sort_values('created_at', ascending=False)

# Parse metadata to analyze structure
def parse_metadata(metadata_str):
    try:
        if isinstance(metadata_str, str):
            return json.loads(metadata_str)
        elif isinstance(metadata_str, dict):
            return metadata_str
        else:
            return {}
    except (json.JSONDecodeError, TypeError):
        return {}

twitter_df['parsed_metadata'] = twitter_df['metadata'].apply(parse_metadata)

# Examine the first few metadata structures
print("\nExamining metadata structure in recent Twitter posts:")
print("=" * 80)
for i, row in twitter_df.head(3).iterrows():
    print(f"\nTweet ID: {i}")
    print(f"Created at: {row['created_at']}")
    print(f"URL: {row['url']}")
    print(f"Content snippet: {str(row['content'])[:100]}...")
    
    # Analyze metadata structure
    metadata = row['parsed_metadata']
    if metadata:
        print(f"\nMetadata keys: {list(metadata.keys())}")
        
        # Check if we have thread information
        has_thread_info = False
        thread_keys = ['in_reply_to_status_id', 'conversation_id', 'reply_count']
        thread_values = {}
        
        for key in thread_keys:
            if key in metadata:
                has_thread_info = True
                thread_values[key] = metadata.get(key)
        
        if has_thread_info:
            print("\nThread information found:")
            for k, v in thread_values.items():
                print(f"  {k}: {v}")
        else:
            print("\nNo thread information found in metadata")
        
        # Check for user information
        if 'user' in metadata and isinstance(metadata['user'], dict):
            print("\nUser information:")
            user_info = metadata['user']
            user_keys = list(user_info.keys())
            print(f"  User keys: {user_keys}")
            if 'screen_name' in user_info:
                print(f"  Screen name: {user_info['screen_name']}")
            if 'name' in user_info:
                print(f"  Name: {user_info['name']}")
    else:
        print("\nNo metadata available or could not be parsed")

# Check for thread structure patterns
print("\n" + "=" * 80)
print("Analyzing thread patterns in the data:")

# Check for common thread indicators
thread_indicators = ['conversation_id', 'in_reply_to_status_id', 'in_reply_to_user_id']
has_indicators = twitter_df['parsed_metadata'].apply(lambda x: any(indicator in x for indicator in thread_indicators) if isinstance(x, dict) else False)
print(f"Tweets with thread indicators: {has_indicators.sum()} ({has_indicators.mean()*100:.2f}%)")

# Check for reply structure
is_reply = twitter_df['parsed_metadata'].apply(lambda x: x.get('in_reply_to_status_id') is not None if isinstance(x, dict) else False)
print(f"Tweets that are replies: {is_reply.sum()} ({is_reply.mean()*100:.2f}%)")

# Try to identify threaded conversations
if 'conversation_id' in thread_indicators:
    has_conversation_id = twitter_df['parsed_metadata'].apply(lambda x: 'conversation_id' in x and x['conversation_id'] is not None if isinstance(x, dict) else False)
    print(f"Tweets with conversation IDs: {has_conversation_id.sum()} ({has_conversation_id.mean()*100:.2f}%)")
    
    # Get sample conversation
    if has_conversation_id.sum() > 0:
        # Count conversation occurrences to find threads
        conversation_sample = twitter_df[has_conversation_id].copy()
        
        if len(conversation_sample) > 0:
            # Convert to string for counting
            conversation_sample['conv_id_str'] = conversation_sample['parsed_metadata'].apply(
                lambda x: str(x.get('conversation_id', ''))
            )
            
            # Count occurrences
            conv_counts = conversation_sample['conv_id_str'].value_counts()
            multi_tweet_threads = conv_counts[conv_counts > 1]
            
            print(f"Found {len(multi_tweet_threads)} potential multi-tweet threads")
            
            if len(multi_tweet_threads) > 0:
                # Examine the largest thread
                largest_thread_id = multi_tweet_threads.index[0]
                largest_thread = conversation_sample[conversation_sample['conv_id_str'] == largest_thread_id]
                
                print(f"\nExamining largest thread (conversation_id: {largest_thread_id}) with {len(largest_thread)} tweets:")
                
                for i, row in largest_thread.iterrows():
                    created = row['created_at'].strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(row['created_at']) else 'Unknown'
                    content = str(row['content'])[:100] + '...' if len(str(row['content'])) > 100 else row['content']
                    print(f"\n[{created}]")
                    print(f"Content: {content}")
                    
                    # Show thread position indicators if available
                    metadata = row['parsed_metadata']
                    if metadata.get('in_reply_to_status_id'):
                        print(f"Reply to: {metadata.get('in_reply_to_status_id')}")
                    if metadata.get('in_reply_to_screen_name'):
                        print(f"Reply to user: {metadata.get('in_reply_to_screen_name')}")

# Check content for manual thread indicators
print("\n" + "=" * 80)
print("Checking for manual thread indicators in content:")

# Look for patterns like "1/", "2/", "🧵", "thread", etc.
thread_markers = [
    r'\d+\/', r'🧵', r'thread', r'\(cont', r'continues', r'continuing'
]

import re
def has_thread_marker(content):
    if not isinstance(content, str):
        return False
    content_lower = content.lower()
    for marker in thread_markers:
        if re.search(marker, content_lower):
            return True
    return False

twitter_df['has_thread_marker'] = twitter_df['content'].apply(has_thread_marker)
print(f"Tweets with manual thread markers: {twitter_df['has_thread_marker'].sum()} ({twitter_df['has_thread_marker'].mean()*100:.2f}%)")

# Show examples of tweets with thread markers
thread_marker_examples = twitter_df[twitter_df['has_thread_marker']].head(5)
print("\nExamples of tweets with thread markers:")
for i, row in thread_marker_examples.iterrows():
    created = row['created_at'].strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(row['created_at']) else 'Unknown'
    content = str(row['content'])[:150] + '...' if len(str(row['content'])) > 150 else row['content']
    print(f"\n[{created}]")
    print(f"Content: {content}")

# Summary
print("\n" + "=" * 80)
print("SUMMARY OF TWITTER DATA STRUCTURE:")
print(f"1. Total Twitter bookmarks: {len(twitter_df)}")
print(f"2. Tweets with thread indicators: {has_indicators.sum()} ({has_indicators.mean()*100:.2f}%)")
print(f"3. Tweets that are replies: {is_reply.sum()} ({is_reply.mean()*100:.2f}%)")
print(f"4. Tweets with manual thread markers: {twitter_df['has_thread_marker'].sum()} ({twitter_df['has_thread_marker'].mean()*100:.2f}%)")

# Only print this if we found any multi-tweet threads
multi_tweet_threads_count = 0
if 'conversation_id' in thread_indicators and 'multi_tweet_threads' in locals():
    multi_tweet_threads_count = len(multi_tweet_threads)
    print(f"5. Potential multi-tweet threads: {multi_tweet_threads_count}")

# Examine full data structure of a few entries
print("\n" + "=" * 80)
print("FULL DATA STRUCTURE EXAMPLES:")

# Get a few representative examples
sample_tweets = twitter_df.head(2).to_dict('records')
for i, tweet in enumerate(sample_tweets):
    print(f"\nSample Tweet {i+1}:")
    # Convert datetime to string for pretty printing
    if isinstance(tweet['created_at'], pd.Timestamp):
        tweet['created_at'] = str(tweet['created_at'])
    
    # Pretty print the structure
    pprint(tweet)