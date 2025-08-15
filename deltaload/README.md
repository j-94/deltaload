# DeltaLoad: Comprehensive ETL Pipeline

A complete ETL (Extract, Transform, Load) pipeline for collecting, enriching, and consolidating social media content from multiple platforms (Twitter, GitHub, Raindrop.io) into a unified dataset with rich full-text content, metadata, and HuggingFace integration.

```
┌─────────────────┐     ┌──────────────────────┐     ┌──────────────────┐
│  Data Sources   │     │     ETL Pipeline     │     │    Output        │
│  ─────────────  │     │  ──────────────────  │     │  ──────────────  │
│  • Twitter      │     │  1. Extract          │     │  • Enriched JSONL│
│  • GitHub       │ ──► │  2. Fix & Clean      │ ──► │  • HuggingFace   │
│  • Raindrop.io  │     │  3. Enrich Content   │     │    Dataset       │
└─────────────────┘     │  4. Quality Check    │     └──────────────────┘
                        └──────────────────────┘
```

## Core Features

* **Complete ETL Pipeline**: Orchestrated workflow from data extraction to publishing
* **Twitter Content Enhancement**: Fixes truncated tweets, content mismatches, and retweet formatting
* **GitHub README Enrichment**: Retrieves and formats repository metadata and README content
* **Web Content Processing**: Extracts and formats content from web bookmarks
* **Batch Processing**: Handles large datasets in manageable chunks
* **Full-Text Generation**: Creates rich markdown content for all sources
* **Quality Control**: Validates and reports on dataset quality
* **HuggingFace Integration**: Publishes datasets to HuggingFace Hub
* **Scheduled Execution**: Runs hourly via GitHub Actions workflow

## Data Structure

The system uses a unified bookmark format:

* `id`: Unique identifier
* `created_at`: Timestamp of creation
* `url`: Source URL
* `source`: Platform identifier (twitter|github|raindrop)
* `content`: Text content
* `full_text`: Rich markdown-formatted content
* `metadata`: Source-specific metadata

## Setup

1. Clone the repository
2. Create a `.env` file with required tokens:

```
GH_TOKEN=your_github_token
RAINDROP_TOKEN=your_raindrop_token
TWITTER_USER_ID=your_twitter_user_id
TWITTER_CT0=your_twitter_ct0
TWITTER_AUTH_TOKEN=your_twitter_auth_token
HUGGINGFACE_TOKEN=your_huggingface_token
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## ETL Pipeline Usage

### Running the Full Pipeline

```bash
# Run the complete pipeline
python pipeline/etl_pipeline.py

# Skip specific steps
python pipeline/etl_pipeline.py --skip-deltaload
python pipeline/etl_pipeline.py --skip-twitter-processing
python pipeline/etl_pipeline.py --skip-enrichment

# Process limited number of bookmarks (for testing)
python pipeline/etl_pipeline.py --enrichment-limit 100
```

### Running Individual Components

```bash
# Run deltaload to fetch latest data
python deltaload.py

# Fix Twitter content
./run_tweet_fixes.sh

# Enrich bookmarks
python enrich_bookmarks.py data-bookmark.jsonl -o data-bookmark-enriched.jsonl

# Enhance with full text
python add_full_text.py data-bookmark-enriched.jsonl -o data-bookmark-final.jsonl

# Upload to HuggingFace
python upload_hf.py
```

## Key Components

### 1. Core ETL Pipeline
- `pipeline/etl_pipeline.py`: Main orchestration script
- `deltaload.py`: Data extraction from sources
- `enrich_bookmarks.py`: Bookmark enrichment
- `add_full_text.py`: Rich content generation

### 2. Twitter Processing
- `tools/twitter_processor.py`: Twitter-specific processing
- `fix_twitter_content.py`: Fixes content mismatches
- `fix_retweets.py`: Improves retweet formatting
- `fix_truncated_tweets.py`: Fixes truncated tweets

### 3. Content Enrichment
- `tools/bookmark_enrichment.py`: Generic enrichment system
- `tools/github_scraper.py`: GitHub-specific enrichment
- `tools/twitter_thread_fetcher.py`: Twitter thread handling
- `tools/web_scraper.py`: Web content extraction

### 4. HuggingFace Integration
- `upload_hf.py`: Dataset upload
- `dataset_card.md`: Dataset documentation

### 5. Batch Processing
- `process_in_batches.py`: Chunk-based processing
- `check_progress.py`: Monitoring and reporting

## Automated Scheduling

The repository includes a GitHub Actions workflow (`.github/workflows/twitter-process.yml`) that runs the ETL pipeline hourly:

1. Fetches latest data with deltaload
2. Fixes and enhances Twitter content
3. Enriches all bookmarks
4. Performs quality checks
5. Updates documentation
6. Uploads to HuggingFace when significant changes occur

## Dataset Statistics

Current dataset (`data-bookmark-final.jsonl`):
- Total bookmarks: 11,213
- Source distribution:
  - GitHub: 4,562 (40.7%)
  - Twitter: 3,879 (34.6%)
  - Web: 2,772 (24.7%)

## Architecture

The system follows a modular architecture:
- Source-specific processors for different content types
- Extensive caching to minimize API calls
- Batch processing for large datasets
- Error handling with detailed logging
- Comprehensive statistical reporting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.

## Last Updated

Last pipeline run: 2025-04-15 12:46:21

### Dataset Statistics

- Total bookmarks: 11,213
- Source distribution:
  - GitHub: 4,562 (40.7%)
  - Twitter: 3,879 (34.6%)
  - Web: 2,772 (24.7%)