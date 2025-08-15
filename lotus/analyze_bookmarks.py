#!/usr/bin/env python3
"""
Script to analyze bookmark data from deltaload
"""

import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from datetime import datetime, timezone
import os

# Configure plots
plt.style.use('ggplot')
sns.set_palette('viridis')

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
print("\nData columns:")
print(df.columns.tolist())

# Data preprocessing
print("\nPreprocessing data...")
# Convert dates to datetime
if 'created_at' in df.columns:
    # Handle various date formats
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce', format='mixed')

# Parse metadata
def parse_metadata(metadata_str):
    try:
        return json.loads(metadata_str) if metadata_str else {}
    except (json.JSONDecodeError, TypeError):
        return {}

if 'metadata' in df.columns:
    df['parsed_metadata'] = df['metadata'].apply(parse_metadata)

# Extract domain from URL
def extract_domain(url):
    if not isinstance(url, str):
        return 'unknown'
    
    match = re.search(r'https?://([^/]+)', url)
    if match:
        return match.group(1)
    return 'unknown'

if 'url' in df.columns:
    df['domain'] = df['url'].apply(extract_domain)

# Basic statistics
print("\nData summary:")
print(df.describe(include='all').to_string())

# Source distribution
if 'source' in df.columns:
    source_counts = df['source'].value_counts()
    print("\nBookmark sources:")
    print(source_counts.to_string())
    
    # Plot source distribution
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=source_counts.index, y=source_counts.values)
    plt.title('Distribution of Bookmark Sources')
    plt.xlabel('Source')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    
    # Add count labels on top of bars
    for i, count in enumerate(source_counts.values):
        ax.text(i, count + 10, f'{count:,}', ha='center')
    
    plt.tight_layout()
    plt.savefig('bookmark_sources.png')
    print(f"Plot saved as bookmark_sources.png")

# Timeline analysis
if 'created_at' in df.columns:
    # Add date column
    df['date'] = df['created_at'].dt.date
    
    # Monthly aggregation
    df['year_month'] = df['created_at'].dt.to_period('M')
    monthly_counts = df.groupby(['year_month', 'source']).size().unstack().fillna(0)
    
    # Plot monthly counts
    plt.figure(figsize=(16, 8))
    monthly_counts.plot(kind='line', ax=plt.gca())
    plt.title('Bookmarks by Source Over Time')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.grid(True, alpha=0.3)
    plt.legend(title='Source')
    plt.tight_layout()
    plt.savefig('bookmark_timeline.png')
    print(f"Plot saved as bookmark_timeline.png")

# Domain analysis
if 'domain' in df.columns:
    top_domains = df['domain'].value_counts().head(20)
    print("\nTop 20 domains:")
    print(top_domains.to_string())
    
    # Plot top domains
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x=top_domains.values, y=top_domains.index)
    plt.title('Top 20 Domains in Bookmarks')
    plt.xlabel('Count')
    plt.ylabel('Domain')
    
    # Add count labels
    for i, count in enumerate(top_domains.values):
        ax.text(count + 1, i, f'{count:,}', va='center')
    
    plt.tight_layout()
    plt.savefig('top_domains.png')
    print(f"Plot saved as top_domains.png")

# GitHub-specific analysis
if 'source' in df.columns:
    github_df = df[df['source'] == 'github'].copy()
    
    # Extract language and stars
    def extract_language(metadata):
        if isinstance(metadata, dict):
            return metadata.get('language', 'Unknown')
        return 'Unknown'
    
    def extract_stars(metadata):
        if isinstance(metadata, dict):
            return metadata.get('stars', 0)
        return 0
    
    if len(github_df) > 0:
        github_df['language'] = github_df['parsed_metadata'].apply(extract_language)
        github_df['stars'] = github_df['parsed_metadata'].apply(extract_stars)
        
        # Language distribution
        lang_counts = github_df['language'].value_counts().head(15)
        print("\nTop 15 languages in GitHub repositories:")
        print(lang_counts.to_string())
        
        # Plot languages
        plt.figure(figsize=(12, 8))
        ax = sns.barplot(x=lang_counts.values, y=lang_counts.index)
        plt.title('Top 15 Languages in GitHub Repositories')
        plt.xlabel('Count')
        plt.ylabel('Language')
        
        # Add count labels
        for i, count in enumerate(lang_counts.values):
            ax.text(count + 1, i, f'{count:,}', va='center')
        
        plt.tight_layout()
        plt.savefig('github_languages.png')
        print(f"Plot saved as github_languages.png")

# Twitter-specific analysis
if 'source' in df.columns:
    twitter_df = df[df['source'].isin(['twitter', 'twitter_like'])].copy()
    
    if len(twitter_df) > 0:
        # Engagement metrics
        def extract_retweet_count(metadata):
            if isinstance(metadata, dict):
                return metadata.get('retweet_count', 0)
            return 0
        
        def extract_favorite_count(metadata):
            if isinstance(metadata, dict):
                return metadata.get('favorite_count', 0)
            return 0
        
        twitter_df['retweet_count'] = twitter_df['parsed_metadata'].apply(extract_retweet_count)
        twitter_df['favorite_count'] = twitter_df['parsed_metadata'].apply(extract_favorite_count)
        
        print("\nTwitter engagement metrics:")
        print(twitter_df[['retweet_count', 'favorite_count']].describe().to_string())
        
        # Activity over time
        if 'created_at' in twitter_df.columns:
            twitter_df['hour'] = twitter_df['created_at'].dt.hour
            twitter_df['day_of_week'] = twitter_df['created_at'].dt.day_name()
            
            # Plot activity heatmap
            day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            tweet_heatmap = pd.crosstab(twitter_df['day_of_week'], twitter_df['hour'])
            # Reorder the index
            tweet_heatmap = tweet_heatmap.reindex(day_order)
            
            plt.figure(figsize=(12, 8))
            sns.heatmap(tweet_heatmap, cmap='viridis', annot=True, fmt='d')
            plt.title('Tweet Activity by Hour and Day of Week')
            plt.xlabel('Hour of Day (UTC)')
            plt.ylabel('Day of Week')
            plt.tight_layout()
            plt.savefig('twitter_activity_heatmap.png')
            print(f"Plot saved as twitter_activity_heatmap.png")

print("\nAnalysis complete!")