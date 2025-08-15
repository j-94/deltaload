# Deltaload ETL Pipeline

A comprehensive ETL pipeline for managing the deltaload data processing workflow.

## Overview

This pipeline automates the process of:

1. Fetching latest social media data (Twitter, GitHub, Raindrop) using deltaload
2. Processing Twitter data to fix content issues:
   - Fixing content mismatches between content and markdown fields
   - Improving retweet formatting to emphasize original authors
   - Fixing truncated tweets using cache data and API
3. Enriching bookmarks with additional content from their sources
4. Performing quality checks on the dataset
5. Finalizing the dataset for use
6. Updating documentation with latest run information

## Components

- `etl_pipeline.py` - Main pipeline script that orchestrates the entire process
- `test_enrichment.py` - Testing script to verify enrichment functionality
- `test_twitter_processor.py` - Testing script for Twitter processing functionality
- `logs/` - Directory for pipeline logs
- `stats.json` - Pipeline run statistics

## Usage

### Running the Full Pipeline

```bash
python pipeline/etl_pipeline.py
```

### Selective Execution

Skip specific steps:

```bash
# Skip the deltaload step (use existing data)
python pipeline/etl_pipeline.py --skip-deltaload

# Skip Twitter processing
python pipeline/etl_pipeline.py --skip-twitter-processing

# Skip only truncated tweets fixing (still process other Twitter content)
python pipeline/etl_pipeline.py --skip-truncated-tweets

# Skip enrichment step
python pipeline/etl_pipeline.py --skip-enrichment

# Skip quality checks
python pipeline/etl_pipeline.py --skip-quality-check

# Skip documentation updates
python pipeline/etl_pipeline.py --skip-docs
```

### Controlling Enrichment

```bash
# Force refresh of cached content
python pipeline/etl_pipeline.py --force-refresh

# Limit enrichment to a specific number of bookmarks
python pipeline/etl_pipeline.py --enrichment-limit 100
```

## Testing

### Testing Enrichment

Test the enrichment functionality:

```bash
python pipeline/test_enrichment.py

# Test with larger sample
python pipeline/test_enrichment.py --sample-size 5

# Force fresh enrichment
python pipeline/test_enrichment.py --force-refresh
```

### Testing Twitter Processing

Test the Twitter processing functionality:

```bash
# Test with a small sample of bookmarks
python pipeline/test_twitter_processor.py --limit 10

# Test with Twitter bookmarks only
python pipeline/test_twitter_processor.py --twitter-only

# Specify input and output files
python pipeline/test_twitter_processor.py --input data-bookmark.jsonl --output test-twitter-processed.jsonl
```

## Results

After running the pipeline:

- Updated data is saved to `data-bookmark-final.jsonl`
- Pipeline statistics are saved to `pipeline/stats.json`
- README.md is updated with latest run info
- PR_README.md is updated with pipeline context

## Troubleshooting

If you encounter issues:

1. Check `pipeline/logs/etl_pipeline.log` for detailed error messages
2. Try running individual components separately
3. Limit enrichment to a smaller number of bookmarks if API rate limits are encountered