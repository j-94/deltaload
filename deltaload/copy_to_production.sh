#!/bin/bash

# This script copies the Twitter processing implementation to the production environment
# Adjust PROD_DIR to point to your production repository

PROD_DIR="/path/to/production/repo"

# Create directories if they don't exist
mkdir -p "$PROD_DIR/tools"
mkdir -p "$PROD_DIR/pipeline"

# Copy core Twitter processing files
cp tools/twitter_processor.py "$PROD_DIR/tools/"
cp fix_twitter_content.py "$PROD_DIR/"
cp fix_retweets.py "$PROD_DIR/"
cp fix_truncated_tweets.py "$PROD_DIR/"
cp fix_truncated_tweets_cached.py "$PROD_DIR/"
cp run_tweet_fixes.sh "$PROD_DIR/"

# Copy pipeline integration files
cp -r pipeline/ "$PROD_DIR/"

# Copy documentation
cp PR_DESCRIPTION.txt "$PROD_DIR/"
cp TWITTER_PROCESSING_REPORT.md "$PROD_DIR/"

echo "Files copied to production environment at $PROD_DIR"
echo "Remember to review and commit the changes in your production repository"