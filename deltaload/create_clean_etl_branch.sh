#!/bin/bash
set -e  # Exit on any error

# Script to create a clean ETL pipeline branch with all necessary files
# This script doesn't execute any git commands automatically
# It just outputs commands for you to review and execute

echo "===== ETL Pipeline Clean Branch Creator ====="
echo "This script will show you the commands to run to create a clean branch"
echo "with all the necessary files for the complete ETL pipeline."
echo ""
echo "NOTHING WILL BE EXECUTED AUTOMATICALLY - you will need to run these commands yourself."
echo "Review each command before executing it."
echo ""

# New branch name
NEW_BRANCH="feature/complete-etl-pipeline-clean"

# List of essential files to include
ESSENTIAL_FILES=(
  # Core ETL files
  "deltaload.py"
  "pipeline/etl_pipeline.py"
  "pipeline/README.md"
  "pipeline/test_twitter_processor.py"
  "pipeline/test_enrichment.py"
  
  # Twitter processing
  "fix_twitter_content.py"
  "fix_retweets.py"
  "fix_truncated_tweets.py"
  "fix_truncated_tweets_cached.py"
  "run_tweet_fixes.sh"
  "tools/twitter_processor.py"
  
  # Content enrichment
  "enrich_bookmarks.py"
  "add_full_text.py"
  "fix_data_types.py"
  "tools/bookmark_enrichment.py"
  "tools/github_scraper.py"
  "tools/tweet_processor.py"
  "tools/web_scraper.py"
  "tools/__init__.py"
  
  # Batch processing
  "process_in_batches.py"
  "unified_bookmark_processor.py"
  "check_progress.py"
  "update_twitter_full_text.py"
  
  # HuggingFace integration
  "upload_hf.py"
  "upload_dataset_card.py"
  "dataset_card.md"
  "run_bookmark_analysis.sh"
  
  # Data files
  "data-bookmark.jsonl"
  "data-bookmark-final.jsonl"
  "data-bookmark-twitter-fixed.jsonl"
  
  # Documentation
  "README.md"
  "PR_README.md"
  "PR_DESCRIPTION.txt"
  "TWITTER_PROCESSING_REPORT.md"
  
  # GitHub Actions workflow
  ".github/workflows/twitter-process.yml"
  
  # Configuration
  ".gitignore"
)

# Generate commands
echo "===== COMMANDS TO RUN ====="
echo ""
echo "# 1. Create and switch to a new branch"
echo "git checkout -b $NEW_BRANCH"
echo ""

echo "# 2. Clean the staging area (in case you have staged files)"
echo "git reset"
echo ""

echo "# 3. Add each essential file to staging"
for file in "${ESSENTIAL_FILES[@]}"; do
  echo "git add \"$file\" 2>/dev/null || echo \"Warning: Could not add $file - file may not exist\""
done
echo ""

echo "# 4. Create a good .gitignore file"
cat << 'EOF' > gitignore_new.txt
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Logs and cache
*.log
cache/
logs/
test_cache/
temp/
tmp/
test_output/
pipeline/logs/

# Environment
.env
.venv
venv/
ENV/
odr_env/
.venv/
env_files/

# IDEs
.idea/
.vscode/
*.swp
*.swo

# Backup files
*.bak
*.backup
*-backup*

# Claude related
.claude/
CLAUDE.md
claude-prompt.md

# Data files
data/
enriched/
*.jsonl
*.json
*.batch_*.jsonl
*-enriched-full.jsonl*
*-cached-fixed.jsonl*
*-retweets-fixed.jsonl*
*-truncated-fixed.jsonl*
*-sample*.jsonl

# Keep only these essential data files
!data-bookmark.jsonl
!data-bookmark-final.jsonl
!data-bookmark-twitter-fixed.jsonl

# macOS system files
.DS_Store
EOF

echo "# 5. Replace the .gitignore file with an improved version"
echo "cp gitignore_new.txt .gitignore && git add .gitignore"
echo ""

echo "# 6. Commit all the essential files"
echo "git commit -m \"Create clean comprehensive ETL pipeline with Twitter fixes and HuggingFace integration\""
echo ""

echo "# 7. Verify that only the essential files are included"
echo "git ls-files"
echo ""

echo "===== END OF COMMANDS ====="
echo ""
echo "Review the commands above, then copy and paste them into your terminal to execute."
echo "You can also save these commands to a file for future reference."
echo ""
echo "After executing these commands, you'll have a clean branch with only the essential files."
echo "This branch will be ready for review and can be pushed to the remote repository."

# Make this script executable
chmod +x "$0"