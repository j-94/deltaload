#!/usr/bin/env python3
"""
Script to analyze the most recent bookmarks from deltaload
"""

import pandas as pd
import json
import os
from datetime import datetime

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

# Convert dates to datetime
if 'created_at' in df.columns:
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')

# Sort by created_at in descending order
df = df.sort_values('created_at', ascending=False)

# Display the 20 most recent bookmarks
print("\n20 most recent bookmarks:")
for i, row in df.head(20).iterrows():
    created = row['created_at'].strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(row['created_at']) else 'Unknown date'
    source = row['source']
    url = row['url']
    content = row['content'][:100] + '...' if len(str(row['content'])) > 100 else row['content']
    
    print(f"\n[{created}] [{source}]")
    print(f"URL: {url}")
    print(f"Content: {content}")

# Print distribution by source for recently added bookmarks (last 100)
recent_100 = df.head(100)
source_counts = recent_100['source'].value_counts()
print("\nSource distribution in 100 most recent bookmarks:")
for source, count in source_counts.items():
    print(f"{source}: {count} ({count}%)")

# Analyze Twitter content from the most recent ones
twitter_recent = df[df['source'].isin(['twitter', 'twitter_like'])].head(10)
print("\n10 most recent Twitter bookmarks:")
for i, row in twitter_recent.iterrows():
    created = row['created_at'].strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(row['created_at']) else 'Unknown date'
    source = row['source']
    content = row['content'][:100] + '...' if len(str(row['content'])) > 100 else row['content']
    
    print(f"\n[{created}] [{source}]")
    print(f"Content: {content}")