#!/usr/bin/env python3
"""
Script to reconstruct Twitter threads from bookmark data
"""

import pandas as pd
import json
import re
import os
from datetime import datetime, timedelta
from collections import defaultdict
import sys

# Path to the bookmark data
bookmarks_path = '/Users/imac/Desktop/ETL/deltaload/data-bookmark.jsonl'

def load_jsonl(filename):
    """Load data from JSONL file."""
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"Error parsing line: {line[:100]}...")
    return data

def parse_metadata(metadata_str):
    """Parse metadata from string or dict."""
    try:
        if isinstance(metadata_str, str):
            return json.loads(metadata_str)
        elif isinstance(metadata_str, dict):
            return metadata_str
        else:
            return {}
    except (json.JSONDecodeError, TypeError):
        return {}

def has_thread_marker(content):
    """Check if content has explicit thread markers."""
    if not isinstance(content, str):
        return False
    
    # Markers that indicate a thread
    thread_markers = [
        r'\d+\/', r'\d+\\', r'\(\d+\/\d+\)', 
        r'🧵', r'thread', r'\(cont', r'continues', 
        r'continuing', r'part \d+', r'\d+\) ', r'^\d+\.'
    ]
    
    content_lower = content.lower()
    for marker in thread_markers:
        if re.search(marker, content_lower):
            return True
    return False

def extract_thread_position(content):
    """Extract thread position information from content."""
    if not isinstance(content, str):
        return None
    
    # Try to extract position markers like "1/5", "1 of 5", etc.
    patterns = [
        r'(\d+)\/(\d+)', # 1/5
        r'(\d+)\s*of\s*(\d+)', # 1 of 5
        r'^(\d+)\)', # 1)
        r'^(\d+)\.', # 1.
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            try:
                position = int(match.group(1))
                total = int(match.group(2)) if len(match.groups()) > 1 else None
                return {"position": position, "total": total}
            except (ValueError, IndexError):
                pass
    
    # Check for positions that aren't labeled with a total
    if re.match(r'^(\d+)\/', content) or re.match(r'^(\d+)\\', content):
        try:
            position = int(re.match(r'^(\d+)[\/\\]', content).group(1))
            return {"position": position, "total": None}
        except (ValueError, AttributeError):
            pass
            
    return None

def extract_username_from_rt(content):
    """Extract the original username from a retweet."""
    if not isinstance(content, str):
        return None
    
    match = re.match(r'^RT\s+@([A-Za-z0-9_]+):', content)
    if match:
        return match.group(1)
    return None

def identify_related_tweets(df):
    """Identify tweets that may be related to each other."""
    # Group tweets by username to find potential threads
    related_tweets = defaultdict(list)
    
    for i, row in df.iterrows():
        username = None
        # Try to get username from metadata
        if 'parsed_metadata' in row and isinstance(row['parsed_metadata'], dict):
            username = row['parsed_metadata'].get('username')
        
        # If no username in metadata, try to extract from RT
        if not username:
            username = extract_username_from_rt(row['content'])
        
        # If we found a username, add to related tweets
        if username:
            related_tweets[username].append(i)
    
    return related_tweets

def find_potential_threads(df, related_tweets):
    """Find potential thread sequences."""
    potential_threads = []
    
    # For each user with multiple tweets
    for username, tweet_ids in related_tweets.items():
        if len(tweet_ids) < 2:
            continue
        
        # Get the tweets and sort by created_at
        user_tweets = df.loc[tweet_ids].copy()
        user_tweets['thread_position'] = user_tweets['content'].apply(extract_thread_position)
        user_tweets = user_tweets.sort_values('created_at', ascending=True)
        
        # Check for thread markers
        marked_tweets = user_tweets[user_tweets['content'].apply(has_thread_marker)]
        
        # If we have marked tweets, check for a sequential thread
        if len(marked_tweets) >= 2:
            # If the tweets have position info, try to order by position
            if any(user_tweets['thread_position'].notna()):
                user_tweets_with_pos = user_tweets[user_tweets['thread_position'].notna()].copy()
                
                if len(user_tweets_with_pos) >= 2:
                    # Extract position number for sorting
                    user_tweets_with_pos['position_num'] = user_tweets_with_pos['thread_position'].apply(
                        lambda x: x['position'] if x and 'position' in x else 999
                    )
                    
                    # Sort by position
                    user_tweets_with_pos = user_tweets_with_pos.sort_values('position_num')
                    
                    if len(user_tweets_with_pos) >= 2:
                        potential_threads.append(user_tweets_with_pos.index.tolist())
            
            # If not enough positional tweets, try time-based approach
            # Find tweets posted within a short timeframe (max 30 minutes between tweets)
            time_windows = []
            current_window = []
            
            for i in range(len(marked_tweets) - 1):
                tweet1 = marked_tweets.iloc[i]
                tweet2 = marked_tweets.iloc[i + 1]
                
                if current_window == []:
                    current_window.append(tweet1.name)
                
                time_diff = (tweet2['created_at'] - tweet1['created_at']).total_seconds() / 60
                
                if time_diff <= 30:
                    current_window.append(tweet2.name)
                else:
                    if len(current_window) >= 2:
                        time_windows.append(current_window)
                    current_window = [tweet2.name]
            
            # Add the last window if it has at least 2 tweets
            if len(current_window) >= 2:
                time_windows.append(current_window)
            
            # Add all time windows as potential threads
            potential_threads.extend(time_windows)
    
    return potential_threads

def format_thread_content(thread_tweets, df):
    """Format thread contents for display."""
    formatted_thread = []
    
    for tweet_id in thread_tweets:
        tweet = df.loc[tweet_id]
        created_at = tweet['created_at'].strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(tweet['created_at']) else 'Unknown'
        
        # Format position info if available
        position_str = ""
        if pd.notnull(tweet.get('thread_position')) and tweet['thread_position']:
            pos = tweet['thread_position']
            if pos.get('total'):
                position_str = f" [{pos['position']}/{pos['total']}]"
            else:
                position_str = f" [{pos['position']}/?]"
        
        # Format the tweet content
        formatted_tweet = f"[{created_at}]{position_str}\n{tweet['content']}\n"
        formatted_thread.append(formatted_tweet)
    
    return "\n".join(formatted_thread)

def save_reconstructed_threads(potential_threads, df, output_file):
    """Save reconstructed threads to a file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Reconstructed Twitter Threads\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total reconstructed threads: {len(potential_threads)}\n\n")
        
        for i, thread in enumerate(potential_threads, 1):
            # Get the first tweet to use as thread title
            first_tweet = df.loc[thread[0]]
            username = None
            
            # Try to get username from metadata
            if isinstance(first_tweet.get('parsed_metadata'), dict):
                username = first_tweet['parsed_metadata'].get('username')
            
            # If no username in metadata, try to extract from RT
            if not username:
                username = extract_username_from_rt(first_tweet['content'])
            
            # Thread title
            thread_title = f"Thread #{i}"
            if username:
                thread_title += f" by @{username}"
                
            f.write(f"## {thread_title}\n")
            f.write(f"*Thread contains {len(thread)} tweets*\n\n")
            
            # Format the thread
            formatted_thread = format_thread_content(thread, df)
            f.write(formatted_thread)
            f.write("\n\n" + "-" * 80 + "\n\n")

def main():
    """Main function."""
    # Define output file
    output_file = "reconstructed_threads.md"
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    
    print(f"Loading bookmarks from {bookmarks_path}...")
    bookmarks = load_jsonl(bookmarks_path)
    print(f"Loaded {len(bookmarks)} bookmarks")
    
    # Convert to DataFrame
    df = pd.DataFrame(bookmarks)
    
    # Filter to Twitter data
    twitter_df = df[df['source'].isin(['twitter', 'twitter_like'])].copy()
    print(f"Found {len(twitter_df)} Twitter bookmarks")
    
    # Parse metadata
    twitter_df['parsed_metadata'] = twitter_df['metadata'].apply(parse_metadata)
    
    # Convert dates to datetime
    twitter_df['created_at'] = pd.to_datetime(twitter_df['created_at'], errors='coerce')
    
    # Check for thread markers
    twitter_df['has_thread_marker'] = twitter_df['content'].apply(has_thread_marker)
    marked_count = twitter_df['has_thread_marker'].sum()
    print(f"Found {marked_count} tweets with thread markers ({marked_count/len(twitter_df)*100:.2f}%)")
    
    # Identify related tweets
    print("Identifying related tweets...")
    related_tweets = identify_related_tweets(twitter_df)
    print(f"Found {len(related_tweets)} unique Twitter users")
    
    # Find potential threads
    print("Finding potential threads...")
    potential_threads = find_potential_threads(twitter_df, related_tweets)
    print(f"Found {len(potential_threads)} potential threads")
    
    # Save reconstructed threads
    print(f"Saving reconstructed threads to {output_file}...")
    save_reconstructed_threads(potential_threads, twitter_df, output_file)
    print("Done!")
    
    # Print summary of longest threads
    thread_lengths = [len(thread) for thread in potential_threads]
    if thread_lengths:
        longest_thread_idx = thread_lengths.index(max(thread_lengths))
        longest_thread = potential_threads[longest_thread_idx]
        print(f"\nLongest thread has {len(longest_thread)} tweets")
        
        # Sample of the longest thread
        first_tweet = twitter_df.loc[longest_thread[0]]
        if 'parsed_metadata' in first_tweet and isinstance(first_tweet['parsed_metadata'], dict):
            username = first_tweet['parsed_metadata'].get('username')
            if username:
                print(f"By user: @{username}")
        
        # Show the beginning of the thread
        print("\nSample of longest thread:")
        for i, tweet_id in enumerate(longest_thread[:3]):
            tweet = twitter_df.loc[tweet_id]
            created_at = tweet['created_at'].strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(tweet['created_at']) else 'Unknown'
            content = tweet['content'][:100] + "..." if len(str(tweet['content'])) > 100 else tweet['content']
            print(f"\n[{created_at}] Tweet {i+1}/{len(longest_thread)}")
            print(f"{content}")
    else:
        print("No threads found.")

if __name__ == "__main__":
    main()