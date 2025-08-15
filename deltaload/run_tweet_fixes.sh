#!/bin/bash

# This script runs all Twitter fixes sequentially for the bookmark dataset

# Define files
INPUT_FILE="data-bookmark.jsonl"
CONTENT_FIXED_FILE="data-bookmark-twitter-fixed.jsonl"
RETWEETS_FIXED_FILE="data-bookmark-retweets-fixed.jsonl"
CACHED_FIXED_FILE="data-bookmark-cached-fixed.jsonl"
TRUNCATED_FIXED_FILE="data-bookmark-truncated-fixed.jsonl"
FINAL_OUTPUT="data-bookmark-fixed-all.jsonl"

# Create backup of original
echo "Creating backup of original data file..."
cp "$INPUT_FILE" "$INPUT_FILE.bak"

# Step 1: Fix Twitter content
echo "Step 1: Fixing Twitter content mismatches..."
python fix_twitter_content.py --input "$INPUT_FILE" --output "$CONTENT_FIXED_FILE"

# Step 2: Fix retweets
echo "Step 2: Fixing Twitter retweet formatting..."
python fix_retweets.py --input "$CONTENT_FIXED_FILE" --output "$RETWEETS_FIXED_FILE"

# Step 3a: Fix truncated tweets using cache data
echo "Step 3a: Fixing truncated tweets using cached data (faster)..."
python fix_truncated_tweets_cached.py --input "$RETWEETS_FIXED_FILE" --output "$CACHED_FIXED_FILE" --batch-size 50

# Step 3b: Fix remaining truncated tweets using Twitter API
echo "Step 3b: Fixing remaining truncated tweets using Twitter API (this may take a while due to API rate limits)..."
python fix_truncated_tweets.py --input "$CACHED_FIXED_FILE" --output "$TRUNCATED_FIXED_FILE" --batch-size 10

# Final step: Copy to final output
echo "Final step: Creating final output file..."
cp "$TRUNCATED_FIXED_FILE" "$FINAL_OUTPUT"

echo "All Twitter fixes complete!"
echo "Final output file: $FINAL_OUTPUT"
echo ""
echo "Summary of fixes:"
echo "1. Content mismatches fixed (see fix_twitter_content.log for details)"
echo "2. Retweets properly formatted (see fix_retweets.log for details)"
echo "3a. Truncated tweets fixed using cache (see fix_truncated_tweets_cached.log for details)"
echo "3b. Remaining truncated tweets fixed using API (see fix_truncated_tweets.log for details)"