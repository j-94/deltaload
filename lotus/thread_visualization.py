#!/usr/bin/env python3
"""
Script to visualize thread statistics from enhanced thread reconstruction
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
import re
from datetime import datetime

# Configuration
output_dir = "."  # Current directory
threads_md_file = "enhanced_threads.md"

def extract_thread_stats(md_file):
    """Extract thread statistics from the markdown file."""
    threads = []
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract total threads count
    total_match = re.search(r'Total reconstructed threads: (\d+)', content)
    total_threads = int(total_match.group(1)) if total_match else 0
    
    # Extract thread headers
    thread_sections = re.findall(r'## Thread #(\d+) \((\d+) tweets\)(?: by @(.+?))?', content)
    
    for thread_id, thread_length, author in thread_sections:
        threads.append({
            'thread_id': int(thread_id),
            'length': int(thread_length),
            'author': author if author else 'Unknown'
        })
    
    return pd.DataFrame(threads), total_threads

def plot_thread_length_distribution(df, total_threads):
    """Create a bar chart of thread length distribution."""
    plt.figure(figsize=(10, 6))
    
    # Count threads by length
    length_counts = df['length'].value_counts().sort_index()
    
    # Create bar chart
    ax = sns.barplot(x=length_counts.index, y=length_counts.values)
    
    # Add value labels on top of each bar
    for i, v in enumerate(length_counts.values):
        percentage = (v / total_threads) * 100
        ax.text(i, v + 0.5, f"{v}\n({percentage:.1f}%)", 
                horizontalalignment='center', fontsize=10)
    
    plt.title('Twitter Thread Length Distribution')
    plt.xlabel('Number of Tweets in Thread')
    plt.ylabel('Number of Threads')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Save figure
    plt.savefig(os.path.join(output_dir, 'thread_length_distribution.png'), dpi=300)
    plt.close()

def plot_author_distribution(df):
    """Create a pie chart of top thread authors."""
    plt.figure(figsize=(10, 8))
    
    # Count threads by author
    author_counts = df['author'].value_counts()
    
    # Keep top 10 authors, group others
    if len(author_counts) > 10:
        top_authors = author_counts.iloc[:10]
        others_count = author_counts.iloc[10:].sum()
        
        # Create a new series with the top 10 and "Others"
        plot_data = pd.Series({**top_authors.to_dict(), 'Others': others_count})
    else:
        plot_data = author_counts
    
    # Create pie chart
    plt.pie(plot_data, labels=plot_data.index, autopct='%1.1f%%', 
            textprops={'fontsize': 9}, startangle=90)
    plt.axis('equal')
    plt.title('Thread Distribution by Author')
    
    # Save figure
    plt.savefig(os.path.join(output_dir, 'thread_author_distribution.png'), dpi=300)
    plt.close()

def plot_thread_length_histogram(df):
    """Create a histogram of thread lengths."""
    plt.figure(figsize=(10, 6))
    
    sns.histplot(df['length'], bins=range(2, df['length'].max() + 2), 
                 kde=False, discrete=True)
    
    plt.title('Histogram of Thread Lengths')
    plt.xlabel('Number of Tweets in Thread')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(range(2, df['length'].max() + 1))
    plt.tight_layout()
    
    # Save figure
    plt.savefig(os.path.join(output_dir, 'thread_length_histogram.png'), dpi=300)
    plt.close()

def main():
    """Main function to generate visualizations."""
    print(f"Analyzing thread data from {threads_md_file}...")
    
    # Extract statistics
    df, total_threads = extract_thread_stats(threads_md_file)
    print(f"Extracted data for {len(df)} threads out of {total_threads} total")
    
    # Generate visualizations
    print("Generating thread length distribution chart...")
    plot_thread_length_distribution(df, total_threads)
    
    print("Generating author distribution pie chart...")
    plot_author_distribution(df)
    
    print("Generating thread length histogram...")
    plot_thread_length_histogram(df)
    
    print("Visualizations saved to output directory")

if __name__ == "__main__":
    main()