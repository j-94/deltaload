# DeltaLoad

A data pipeline for collecting and consolidating social media activity across multiple platforms (Twitter, GitHub, Raindrop.io) into a unified JSONL format.

```
┌─────────────────┐     ┌──────────────┐     ┌──────────────┐
│  Data Sources   │     │   DeltaLoad  │     │    Output    │
│  ─────────────  │     │  ──────────  │     │  ──────────  │
│  • Twitter      │ ──► │  Extract     │     │  Unified     │
│  • GitHub       │     │  Transform   │ ──► │  JSONL       │
│  • Raindrop.io  │     │  Load        │     │  Format      │
└─────────────────┘     └──────────────┘     └──────────────┘
```

## Features

* Delta loading (only fetches new data since last run)
* Unified data format across platforms
* Error handling and logging
* Rate limit awareness
* Configurable through environment variables

## Data Structure

The system uses a unified bookmark format with the following fields:

* `id`: Unique identifier
* `created_at`: Timestamp of creation
* `url`: Source URL
* `source`: Platform identifier (twitter|github|raindrop)
* `content`: Title or excerpt
* `full_text`: Complete content with the following structure:
  * For tweets: Full thread text with metadata
  * For GitHub: Complete README content with repo info
  * For webpages: Parsed article content with metadata
  * For Raindrop: Bookmark data with tags and notes

## Setup


1. Clone the repository
2. Create a `.env` file with required tokens:

```
GH_TOKEN=your_github_token
RAINDROP_TOKEN=your_raindrop_token
TWITTER_USER_ID=your_twitter_user_id
TWITTER_CT0=your_twitter_ct0
TWITTER_AUTH_TOKEN=your_twitter_auth_token
```


3. Install dependencies:

```bash
# Python dependencies
pip install -r requirements.txt

# Node dependencies (for TypeScript components)
npm install
```

## Usage

Run the main pipeline:

```bash
python deltaload.py
```

Data will be saved to `data-bookmark.jsonl` in the following format:

```json
{
  "id": 123,
  "created_at": "2024-01-20T00:00:00Z",
  "url": "https://example.com",
  "source": "twitter|github|raindrop",
  "content": "content text",
  "metadata": {}
}
```

## Project Structure

* `deltaload.py`: Main ETL pipeline
* `jinaparse.ts`: TypeScript parser for data processing
* `test scrapers/`: Various scraper implementations
* `*_cache/`: Cache directories for different data sources

## Operations

### Content Fetching


1. Tweet Thread Operations:
   * Fetch complete thread context
   * Extract thread participants
   * Preserve thread hierarchy
   * Store media attachments
   * Track engagement metrics
2. GitHub README Operations:
   * Fetch repository README files
   * Extract repository metadata
   * Track stars and forks
   * Monitor README updates
   * Store commit history
3. Web Content Operations:
   * Raw HTML archival
   * Content extraction with readability
   * Metadata parsing (OpenGraph, Schema.org)
   * Image and asset preservation
   * Link validation
4. Enhanced Tweet Capture:
   * Use tweet-snap for visual preservation
   * Store tweet cards and embeds
   * Track tweet edit history
   * Preserve thread context
   * Archive referenced content

## Database Operations

The system follows a monolithic architecture for simplicity and maintainability:


1. Core Operations:
   * Create: Insert new bookmarks
   * Read: Query by source, date, content
   * Update: Modify existing entries
   * Delete: Remove outdated content
   * Merge: Combine duplicate entries
2. Advanced Operations:
   * Full-text search
   * Tag management
   * Content deduplication
   * Version tracking
   * Backup and restore

## Data Formats

The system supports multiple data formats for flexibility:


1. Primary Format (JSONL):
   * Line-delimited JSON
   * Efficient for streaming
   * Easy to parse and generate
   * Supports incremental updates
2. Export Formats:
   * CSV for spreadsheet analysis
   * Markdown for documentation
   * HTML for web viewing
   * PDF for archival
   * SQLite for local querying

## CRON Job

The system runs hourly checks for:

* New tweets and threads
* README updates
* Bookmark changes
* Content updates

## Improvements Roadmap


1. Database Enhancements:
   * Implement SQLite for indexed queries
   * Add PostgreSQL option for scaling
   * Support distributed operations
   * Implement caching layer
2. Content Processing:
   * Add NLP for content summarization
   * Implement topic clustering
   * Support content translation
   * Add semantic search
3. Data Format Extensions:
   * Support ActivityPub format
   * Add RSS/Atom feeds
   * Implement WebMention
   * Support IPFS storage

## Bookmark Enrichment System

The repository now includes a powerful bookmark enrichment system that can extract content from various sources:

### Features

- **Twitter Thread Fetching**: Extract complete Twitter threads from URLs
- **GitHub Repository Scraping**: Fetch repository metadata and README content
- **General Web Scraping**: Extract content from any website
- **Content Caching**: Cache scraped content to avoid redundant API calls
- **JSONL Processing**: Read and write bookmark data in JSONL format

### Usage

Use the `enrich_bookmarks.py` script to enrich bookmark data:

```bash
python enrich_bookmarks.py data-bookmark.jsonl --output-file enriched.jsonl
```

#### Options

- `input_file`: Input JSONL file with bookmarks
- `--output-file`, `-o`: Output JSONL file (default: input file with .enriched suffix)
- `--cache-dir`, `-c`: Cache directory for enriched content (default: ./cache)
- `--force-refresh`, `-f`: Force refresh cached content
- `--skip-existing`, `-s`: Skip bookmarks that already have content
- `--limit`, `-l`: Limit processing to specified number of bookmarks
- `--filter-source`: Only process bookmarks from a specific source (twitter, github, or web)

### API Usage

You can also use the system programmatically:

```python
from tools.bookmark_enrichment import BookmarkEnrichment

# Initialize the enrichment system
enrichment = BookmarkEnrichment(cache_dir='./cache')

# Enrich a single bookmark
bookmark = {"url": "https://github.com/username/repo"}
enriched = enrichment.enrich_bookmark(bookmark)

# Enrich multiple bookmarks
bookmarks = [
    {"url": "https://github.com/username/repo"},
    {"url": "https://twitter.com/username/status/123456789"}
]
enriched_bookmarks = enrichment.enrich_bookmarks(bookmarks)
```

# Twitter Thread Fetcher and Markdown Formatter

This project provides tools to fetch Twitter threads and convert them into nicely formatted markdown files with collapsible blocks for better readability.

## Features

- Fetch complete Twitter threads using GraphQL API
- Extract media (images and videos) with highest quality
- Convert mentions and hashtags to clickable links
- Generate clean markdown output with collapsible sections
- Save raw data for future reference
- Comprehensive logging for debugging

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd deltaload
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your Twitter credentials:
```
TWITTER_USER_ID=your_user_id
TWITTER_CT0=your_ct0_cookie
TWITTER_AUTH_TOKEN=your_auth_token
```

To get these credentials:
1. Log in to Twitter in your browser
2. Open Developer Tools (F12)
3. Go to the Network tab
4. Make any request on Twitter
5. Look for the following in the request headers:
   - `ct0` cookie value for TWITTER_CT0
   - `auth_token` cookie value for TWITTER_AUTH_TOKEN
   - Your user ID can be found in the `twid` cookie (remove the 'u=' prefix)

## Usage

### Fetch a Twitter Thread

```python
from twitter.conversation_fetcher import TwitterThreadFetcher

# Initialize the fetcher
fetcher = TwitterThreadFetcher()

# Fetch a thread by its tweet ID
thread = fetcher.get_conversation_thread("TWEET_ID")

# Save to JSONL format
output_file = f"thread_{thread[0]['id']}.jsonl"
fetcher.save_thread_to_jsonl(thread, output_file)
```

### Convert JSONL to Markdown

```python
from twitter.markdown_formatter import process_thread

# Convert JSONL to markdown
jsonl_file = "thread_TWEET_ID.jsonl"
process_thread(jsonl_file, output_dir="output")
```

The markdown output will be saved in the specified output directory with the following structure:

```markdown
# Twitter Thread

## Main Tweet

[Tweet content with formatted links and mentions]

<details><summary>Metadata</summary>
- Date: [formatted date]
- Tweet ID: [link to tweet]
</details>

## Thread

### Tweet 1
[Tweet content]

**Media:**
[Images/Videos if present]

---

### Tweet 2
[Tweet content]
...

## Raw Data
<details><summary>Click to expand raw data</summary>
[JSON data]
</details>
```

## Logging

The scripts use the `loguru` library for logging. Logs are saved to:
- `twitter_thread.log` for the fetcher
- `markdown_formatter.log` for the formatter

Both scripts also output INFO level logs to the console.

## Error Handling

The scripts include comprehensive error handling and logging:
- Network request failures
- API response parsing errors
- File I/O errors
- Invalid credentials
- Missing environment variables

Check the log files for detailed error messages and debugging information.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.


