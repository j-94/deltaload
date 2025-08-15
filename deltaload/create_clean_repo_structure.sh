#!/bin/bash
set -e  # Exit on any error

# Script to create a clean, well-structured repository with both code and essential cache data
# This script doesn't execute any git commands automatically
# It just outputs commands for you to review and execute

echo "===== Clean ETL Repository Structure Creator ====="
echo "This script will show you the commands to create a clean repository structure"
echo "that includes both code and essential cache data."
echo ""
echo "NOTHING WILL BE EXECUTED AUTOMATICALLY - you will need to run these commands yourself."
echo "Review each command before executing it."
echo ""

# New branch name
NEW_BRANCH="feature/etl-pipeline-with-data"

# Directory structure 
echo "===== REPOSITORY STRUCTURE ====="
echo "
deltaload/ (Root)
├── .github/
│   └── workflows/
│       └── etl-pipeline.yml       # Hourly ETL workflow
├── pipeline/                      # Core ETL pipeline code
│   ├── etl_pipeline.py
│   ├── test_enrichment.py
│   ├── test_twitter_processor.py
│   └── README.md
├── tools/                         # Processing tools
│   ├── bookmark_enrichment.py
│   ├── github_scraper.py
│   ├── twitter_processor.py
│   ├── tweet_processor.py
│   ├── twitter_thread_fetcher.py
│   └── web_scraper.py
├── fixers/                        # Content fixers
│   ├── fix_twitter_content.py
│   ├── fix_retweets.py
│   ├── fix_truncated_tweets.py
│   └── fix_truncated_tweets_cached.py
├── scripts/                       # Utility scripts
│   ├── process_in_batches.py
│   ├── check_progress.py
│   ├── run_tweet_fixes.sh
│   └── update_twitter_full_text.py
├── huggingface/                   # HuggingFace integration
│   ├── upload_hf.py
│   ├── upload_dataset_card.py
│   └── dataset_card.md
├── data/                          # Primary data
│   ├── bookmarks/                 # Main bookmark files
│   │   ├── data-bookmark.jsonl
│   │   ├── data-bookmark-final.jsonl
│   │   └── data-bookmark-twitter-fixed.jsonl
│   ├── twitter_cache/             # Essential Twitter cache
│   │   ├── current/               # Latest cache files (to keep)
│   │   │   ├── UserTweetsAndReplies.json
│   │   │   └── Likes.json
│   │   └── backup/                # Historical cache files (to keep)
│   │       ├── UserTweetsAndReplies.json 
│   │       └── Likes.json
│   └── processed/                 # Processed data directory (keep structure, not files)
├── deltaload.py                   # Core application
├── .gitignore                     # Improved .gitignore
└── README.md                      # Documentation
"
echo ""
echo "===== COMMANDS TO RUN ====="
echo ""
echo "# 1. Create and switch to a new branch"
echo "git checkout -b $NEW_BRANCH"
echo ""

echo "# 2. Create the directory structure"
echo "mkdir -p .github/workflows"
echo "mkdir -p pipeline"
echo "mkdir -p tools"
echo "mkdir -p fixers"
echo "mkdir -p scripts"
echo "mkdir -p huggingface"
echo "mkdir -p data/bookmarks"
echo "mkdir -p data/twitter_cache/current"
echo "mkdir -p data/twitter_cache/backup"
echo "mkdir -p data/processed"
echo ""

echo "# 3. Copy essential files to their new locations"
echo ""
echo "# 3.1 Core files"
echo "cp deltaload.py ."
echo "cp README.md ."
echo "cp PR_README.md ."
echo "cp data-bookmark.jsonl data/bookmarks/"
echo "cp data-bookmark-final.jsonl data/bookmarks/"
echo "cp data-bookmark-twitter-fixed.jsonl data/bookmarks/"
echo ""

echo "# 3.2 Pipeline files"
echo "cp pipeline/etl_pipeline.py pipeline/"
echo "cp pipeline/test_enrichment.py pipeline/"
echo "cp pipeline/test_twitter_processor.py pipeline/"
echo "cp pipeline/README.md pipeline/"
echo ""

echo "# 3.3 Tool files"
echo "cp tools/bookmark_enrichment.py tools/"
echo "cp tools/github_scraper.py tools/"
echo "cp tools/twitter_processor.py tools/"
echo "cp tools/tweet_processor.py tools/"
echo "cp tools/web_scraper.py tools/"
echo "cp tools/__init__.py tools/"
echo ""

echo "# 3.4 Fixer scripts"
echo "cp fix_twitter_content.py fixers/"
echo "cp fix_retweets.py fixers/"
echo "cp fix_truncated_tweets.py fixers/"
echo "cp fix_truncated_tweets_cached.py fixers/"
echo ""

echo "# 3.5 Utility scripts"
echo "cp process_in_batches.py scripts/"
echo "cp check_progress.py scripts/"
echo "cp run_tweet_fixes.sh scripts/"
echo "cp add_full_text.py scripts/"
echo "cp update_twitter_full_text.py scripts/"
echo ""

echo "# 3.6 HuggingFace integration"
echo "cp upload_hf.py huggingface/"
echo "cp upload_dataset_card.py huggingface/"
echo "cp dataset_card.md huggingface/"
echo ""

echo "# 3.7 GitHub workflow"
echo "cp .github/workflows/twitter-process.yml .github/workflows/etl-pipeline.yml"
echo ""

echo "# 3.8 Copy essential Twitter cache data (only the files from March 28 that bridge the gap)"
echo "# This is critical for fixing the 3-month data loss issue"
echo "cp 'data/backup/UserTweetsAndReplies.json' data/twitter_cache/backup/"
echo "cp 'data/backup/Likes.json' data/twitter_cache/backup/"
echo ""
echo "# Also copy the most recent Twitter API responses"
echo "cp 'data/1169726235817185281/20250414_193611_UserTweetsAndReplies.json' data/twitter_cache/current/"
echo "cp 'data/1169726235817185281/20250414_193615_Likes.json' data/twitter_cache/current/"
echo ""

echo "# 4. Create a good .gitignore file that includes cache data"
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

# Logs and temp data
*.log
logs/
tmp/
temp/
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

# Data files - ignore by default
data/processed/*
*.batch_*.jsonl
*-enriched-full.jsonl*
*-cached-fixed.jsonl*
*-retweets-fixed.jsonl*
*-truncated-fixed.jsonl*
*-sample*.jsonl

# Explicitly include essential data
!data/bookmarks/data-bookmark.jsonl
!data/bookmarks/data-bookmark-final.jsonl
!data/bookmarks/data-bookmark-twitter-fixed.jsonl
!data/twitter_cache/backup/UserTweetsAndReplies.json
!data/twitter_cache/backup/Likes.json
!data/twitter_cache/current/20250414_193611_UserTweetsAndReplies.json
!data/twitter_cache/current/20250414_193615_Likes.json

# macOS system files
.DS_Store
EOF

echo "# 5. Replace the .gitignore file"
echo "cp gitignore_new.txt .gitignore"
echo ""

echo "# 6. Update import paths in files to reflect new structure"
echo "# This will require examining import statements in files"
echo "# For example in pipeline/etl_pipeline.py:"
echo "sed -i '' 's/from tools.twitter_processor import/from ..tools.twitter_processor import/g' pipeline/etl_pipeline.py"
echo "# Add similar commands for other imports"
echo ""

echo "# 7. Update path references in scripts"
echo "# For example in scripts/run_tweet_fixes.sh:"
echo "sed -i '' 's/python fix_twitter_content.py/python fixers\\/fix_twitter_content.py/g' scripts/run_tweet_fixes.sh"
echo "# Add similar commands for other path references"
echo ""

echo "# 8. Add all files to git"
echo "git add ."
echo ""

echo "# 9. Commit the changes"
echo "git commit -m \"Create clean repository structure with essential code and cache data\""
echo ""

echo "===== IMPORTANT NOTES ====="
echo "1. The commands above organize files but don't update imports or paths within files."
echo "2. You will need to manually update import statements and file paths before running the code."
echo "3. The cache files included are only the essential ones for bridging the data gap."
echo "4. The .gitignore is set to include these specific cache files while excluding others."
echo ""

echo "After executing these commands, test the repository structure by running the pipeline to ensure:"
echo "1. The Twitter data gap is fixed"
echo "2. All components can find their dependencies"
echo "3. Cache files are correctly accessed"
echo ""

echo "This approach gives you a clean, well-structured repository while keeping the essential data"
echo "files needed to fix the Twitter data gap issue."

# Make this script executable
chmod +x "$0"