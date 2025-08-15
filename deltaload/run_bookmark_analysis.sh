#!/bin/bash

# Script to prepare bookmark data for HuggingFace Data Studio

echo "==============================================="
echo "Bookmark Data Preparation for HuggingFace"
echo "==============================================="

# Set working directory
cd "$(dirname "$0")"
WORKING_DIR=$(pwd)
echo "Working directory: $WORKING_DIR"

# Check if bookmark data exists
BOOKMARK_DATA="$WORKING_DIR/data-bookmark.jsonl"
if [ ! -f "$BOOKMARK_DATA" ]; then
    echo "Error: $BOOKMARK_DATA not found!"
    echo "Please run the deltaload ETL pipeline first."
    exit 1
fi

# Install required Python packages
echo "Installing required Python packages..."
pip install pandas matplotlib huggingface_hub seaborn urllib3

# Run the HuggingFace data preparation script
echo "Preparing data for HuggingFace..."
python "$WORKING_DIR/hf_bookmark_analysis.py"

echo "Done!"
echo ""
echo "To view your data in HuggingFace Data Studio:"
echo "1. Follow the instructions to upload your data"
echo "2. Go to https://huggingface.co/datasets/YOUR_USERNAME/bookmarks-dataset"
echo "3. Click on 'Explore in Data Studio'"
echo ""
echo "For more information, refer to: https://huggingface.co/docs/hub/en/datasets-viewer"
echo ""