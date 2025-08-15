#!/usr/bin/env python3
"""
Enhanced script to reconstruct Twitter threads from bookmark data
This version uses more advanced thread detection techniques
"""

import pandas as pd
import json
import re
import os
import sys
from datetime import datetime, timedelta
from collections import defaultdict

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

def clean_text(text):
    """Clean and normalize text for better matching."""
    if not isinstance(text, str):
        return ""
    # Remove URLs
    text = re.sub(r'https?://\S+', '', text)
    # Remove RT prefix
    text = re.sub(r'^RT\s+@\w+:\s*', '', text)
    # Convert to lowercase and remove extra whitespace
    text = ' '.join(text.lower().split())
    return text

def has_thread_marker(content):
    """Check if content has explicit thread markers."""
    if not isinstance(content, str):
        return False
    
    # Markers that indicate a thread
    thread_markers = [
        r'\d+\/', r'\d+\\', r'\(\d+\/\d+\)', r'\d+ of \d+',
        r'🧵', r'thread', r'\(cont', r'continues', r'continuing',
        r'part \d+', r'\d+\) ', r'^\d+\.', r'cont\.', r'…',
        r'more 👇', r'more👇', r'forthcoming', r'keep going'
    ]
    
    content_lower = content.lower()
    for marker in thread_markers:
        if re.search(marker, content_lower):
            return True
    return False

def get_thread_number(content):
    """Extract thread number like '1/' or '(1/5)'."""
    if not isinstance(content, str):
        return None
    
    patterns = [
        r'^(\d+)\/\d*', # 1/ or 1/5
        r'^\(\s*(\d+)\s*\/\s*\d+\s*\)', # (1/5)
        r'^(\d+)\s*of\s*\d+', # 1 of 5
        r'^(\d+)\.\s', # 1. 
        r'^(\d+)\)\s', # 1) 
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            try:
                return int(match.group(1))
            except (ValueError, IndexError):
                pass
    return None

def extract_tweet_text(tweet_content):
    """Extract just the tweet text, removing RT prefix and username."""
    if not isinstance(tweet_content, str):
        return ""
    
    # If it's a retweet, extract just the content
    match = re.match(r'^RT\s+@[A-Za-z0-9_]+:\s*(.*)', tweet_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return tweet_content.strip()

def get_original_author(tweet_content):
    """Extract the original author from a retweet."""
    if not isinstance(tweet_content, str):
        return None
    
    match = re.match(r'^RT\s+@([A-Za-z0-9_]+):', tweet_content)
    if match:
        return match.group(1)
    return None

def build_tweet_graph(df):
    """
    Build a graph of related tweets.
    Each tweet can be:
    1. Part of a thread (indicated by markers)
    2. Reply to another tweet
    3. Retweet of a thread tweet
    """
    # Prepare dataframe
    df = df.copy()
    df['clean_text'] = df['content'].apply(clean_text)
    df['thread_number'] = df['content'].apply(get_thread_number)
    df['has_marker'] = df['content'].apply(has_thread_marker)
    df['original_author'] = df['content'].apply(get_original_author)
    
    # Group tweets by original author
    author_tweets = defaultdict(list)
    for idx, row in df.iterrows():
        if row['original_author']:
            author_tweets[row['original_author']].append(idx)
        
        # Also try to get author from metadata
        if isinstance(row.get('parsed_metadata'), dict) and row['parsed_metadata'].get('username'):
            author = row['parsed_metadata'].get('username')
            author_tweets[author].append(idx)
    
    # Find potential threads
    potential_threads = []
    processed_ids = set()
    
    # Method 1: Thread detection by numbering (1/, 2/, etc.)
    for author, tweet_ids in author_tweets.items():
        if len(tweet_ids) < 2:
            continue
            
        # Get tweets with thread markers and numbers
        author_df = df.loc[tweet_ids].copy()
        numbered_tweets = author_df[(author_df['thread_number'].notna()) & (author_df['has_marker'])]
        
        if len(numbered_tweets) >= 2:
            # Group by datetime proximity (tweets in same thread should be close in time)
            numbered_tweets = numbered_tweets.sort_values('created_at')
            thread_groups = []
            current_group = []
            
            for i, (idx, row) in enumerate(numbered_tweets.iterrows()):
                if not current_group:
                    current_group = [idx]
                    continue
                    
                last_tweet = df.loc[current_group[-1]]
                time_diff = (row['created_at'] - last_tweet['created_at']).total_seconds() / 60
                
                # If time difference is small enough, assume they're part of the same thread
                if time_diff <= 60:  # 60 minutes threshold
                    current_group.append(idx)
                else:
                    # If this group has at least 2 tweets, save it
                    if len(current_group) >= 2:
                        thread_groups.append(current_group)
                    current_group = [idx]
            
            # Don't forget the last group
            if len(current_group) >= 2:
                thread_groups.append(current_group)
            
            # For each group, sort by thread number
            for group in thread_groups:
                group_df = df.loc[group].copy()
                group_df = group_df.sort_values('thread_number')
                potential_threads.append(group_df.index.tolist())
                processed_ids.update(group)
    
    # Method 2: Text similarity and temporal proximity
    # For tweets that haven't been assigned to a thread yet
    for author, tweet_ids in author_tweets.items():
        unprocessed = [tid for tid in tweet_ids if tid not in processed_ids]
        if len(unprocessed) < 2:
            continue
        
        # Get tweets with thread markers
        author_df = df.loc[unprocessed].copy()
        marked_tweets = author_df[author_df['has_marker']]
        
        if len(marked_tweets) >= 2:
            # Sort by time
            marked_tweets = marked_tweets.sort_values('created_at')
            
            # Find sequences of tweets that are close in time
            time_threads = []
            current_thread = []
            
            for i, (idx, row) in enumerate(marked_tweets.iterrows()):
                if not current_thread:
                    current_thread = [idx]
                    continue
                
                last_tweet = df.loc[current_thread[-1]]
                time_diff = (row['created_at'] - last_tweet['created_at']).total_seconds() / 60
                
                if time_diff <= 60:  # 60 minutes
                    current_thread.append(idx)
                else:
                    if len(current_thread) >= 2:
                        time_threads.append(current_thread)
                    current_thread = [idx]
            
            # Don't forget the last group
            if len(current_thread) >= 2:
                time_threads.append(current_thread)
            
            potential_threads.extend(time_threads)
            for thread in time_threads:
                processed_ids.update(thread)
    
    # Method 3: Content-based thread detection
    # For threads without explicit markers but talking about same topic
    for author, tweet_ids in author_tweets.items():
        unprocessed = [tid for tid in tweet_ids if tid not in processed_ids]
        if len(unprocessed) < 2:
            continue
        
        author_df = df.loc[unprocessed].copy()
        
        # Sort by time
        author_df = author_df.sort_values('created_at')
        
        # If tweets are close in time, look for topic continuity
        content_threads = []
        current_thread = []
        
        for i, (idx, row) in enumerate(author_df.iterrows()):
            if not current_thread:
                current_thread = [idx]
                continue
            
            last_tweet = df.loc[current_thread[-1]]
            time_diff = (row['created_at'] - last_tweet['created_at']).total_seconds() / 60
            
            # If close in time, check for topic continuity
            if time_diff <= 30:  # 30 minutes
                # Simple heuristic: check if tweets share significant words
                last_words = set(last_tweet['clean_text'].split())
                curr_words = set(row['clean_text'].split())
                
                # Calculate Jaccard similarity
                if len(last_words) > 0 and len(curr_words) > 0:
                    similarity = len(last_words.intersection(curr_words)) / len(last_words.union(curr_words))
                    
                    # If similarity is high, assume they're part of same thread
                    if similarity > 0.15:  # Threshold can be adjusted
                        current_thread.append(idx)
                    else:
                        if len(current_thread) >= 2:
                            content_threads.append(current_thread)
                        current_thread = [idx]
                else:
                    if len(current_thread) >= 2:
                        content_threads.append(current_thread)
                    current_thread = [idx]
            else:
                if len(current_thread) >= 2:
                    content_threads.append(current_thread)
                current_thread = [idx]
        
        # Don't forget the last group
        if len(current_thread) >= 2:
            content_threads.append(current_thread)
        
        potential_threads.extend(content_threads)
    
    # De-duplicate threads
    seen = set()
    unique_threads = []
    
    for thread in potential_threads:
        thread_tuple = tuple(sorted(thread))
        if thread_tuple not in seen and len(thread_tuple) >= 2:
            seen.add(thread_tuple)
            unique_threads.append(list(thread_tuple))
    
    return unique_threads

def format_thread_content(thread_tweets, df):
    """Format thread contents for display."""
    formatted_thread = []
    
    for tweet_id in thread_tweets:
        tweet = df.loc[tweet_id]
        created_at = tweet['created_at'].strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(tweet['created_at']) else 'Unknown'
        
        # Format thread number if available
        thread_num = ""
        if pd.notnull(tweet.get('thread_number')):
            thread_num = f" [{int(tweet['thread_number'])}]"
        
        # Format the tweet content
        formatted_tweet = f"[{created_at}]{thread_num}\n{tweet['content']}\n"
        formatted_thread.append(formatted_tweet)
    
    return "\n".join(formatted_thread)

def save_reconstructed_threads(threads, df, output_file):
    """Save reconstructed threads to a file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Enhanced Reconstructed Twitter Threads\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total reconstructed threads: {len(threads)}\n\n")
        
        # Sort threads by length (longest first)
        threads_with_len = [(thread, len(thread)) for thread in threads]
        threads_with_len.sort(key=lambda x: x[1], reverse=True)
        
        for i, (thread, length) in enumerate(threads_with_len, 1):
            # Get the first tweet to use as thread title
            first_tweet = df.loc[thread[0]]
            
            # Get author information
            author = None
            if first_tweet.get('original_author'):
                author = first_tweet['original_author']
            elif isinstance(first_tweet.get('parsed_metadata'), dict) and first_tweet['parsed_metadata'].get('username'):
                author = first_tweet['parsed_metadata'].get('username')
            
            # Thread title
            thread_title = f"Thread #{i} ({length} tweets)"
            if author:
                thread_title += f" by @{author}"
            
            # Extract content of first tweet for title
            first_content = extract_tweet_text(first_tweet['content'])
            if len(first_content) > 100:
                first_content = first_content[:97] + "..."
            
            f.write(f"## {thread_title}\n")
            f.write(f"*{first_content}*\n\n")
            
            # Format the thread
            thread_df = df.loc[thread].copy()
            thread_df = thread_df.sort_values('created_at')
            formatted_thread = format_thread_content(thread_df.index.tolist(), df)
            f.write(formatted_thread)
            f.write("\n\n" + "-" * 80 + "\n\n")

def main():
    """Main function."""
    # Define output file
    output_file = "enhanced_threads.md"
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
    
    # Remove any rows with null created_at (they can't be part of a thread)
    twitter_df = twitter_df.dropna(subset=['created_at'])
    print(f"Found {len(twitter_df)} Twitter bookmarks with valid dates")
    
    # Build tweet graph and find threads
    print("Finding potential threads using enhanced methods...")
    threads = build_tweet_graph(twitter_df)
    print(f"Found {len(threads)} potential threads")
    
    # Sort threads by length
    thread_lens = [len(t) for t in threads]
    print(f"Thread statistics:")
    if thread_lens:
        print(f"  - Longest thread: {max(thread_lens)} tweets")
        print(f"  - Average thread length: {sum(thread_lens)/len(thread_lens):.1f} tweets")
        
        # Count threads of different lengths
        len_counts = {}
        for l in thread_lens:
            len_counts[l] = len_counts.get(l, 0) + 1
        
        print(f"  - Thread length distribution:")
        for l in sorted(len_counts.keys()):
            print(f"    - {l} tweets: {len_counts[l]} threads")
    
    # Save reconstructed threads
    print(f"Saving reconstructed threads to {output_file}...")
    save_reconstructed_threads(threads, twitter_df, output_file)
    print("Done!")
    
    # Display a sample of the longest thread
    if threads:
        # Sort by length
        threads.sort(key=len, reverse=True)
        longest_thread = threads[0]
        
        print(f"\nSample from longest thread ({len(longest_thread)} tweets):")
        thread_df = twitter_df.loc[longest_thread].copy()
        thread_df = thread_df.sort_values('created_at')
        
        # Show first 3 tweets
        for i, (idx, row) in enumerate(thread_df.head(3).iterrows()):
            created_at = row['created_at'].strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(row['created_at']) else 'Unknown'
            content = row['content'][:100] + "..." if len(str(row['content'])) > 100 else row['content']
            print(f"\n[{created_at}] Tweet {i+1}/{len(longest_thread)}")
            print(f"{content}")

if __name__ == "__main__":
    main()