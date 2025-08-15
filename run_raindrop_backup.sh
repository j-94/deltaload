#!/bin/bash
# Script to run Raindrop.io backup using UV for fast package installation

# Create a backup directory
BACKUP_DIR="/Users/imac/Desktop/raindrop_backup"
mkdir -p "$BACKUP_DIR"

# Use UV to install required packages if they're not already installed
echo "Installing required packages with UV..."
uv pip install jupyter aiohttp pandas tqdm

# Choose your preferred method:
# 1. Run the Python script directly
# 2. Start Jupyter and open the notebook

echo "How do you want to run the backup?"
echo "1) Run Python script directly (faster, no UI)"
echo "2) Open Jupyter notebook (interactive with UI)"
read -p "Enter your choice (1 or 2): " choice

if [ "$choice" = "1" ]; then
    # Run the backup script directly
    echo "Starting Raindrop.io backup..."
    python3 /Users/imac/Desktop/raindrop_backup.py
    echo "Backup completed! Check the $BACKUP_DIR directory for your files."
else
    # Start Jupyter notebook
    echo "Starting Jupyter notebook..."
    cd /Users/imac/Desktop
    jupyter notebook raindrop_backup.ipynb
fi