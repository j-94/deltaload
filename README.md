# Bookmark Delta ETL Pipeline
Quickstart (single command)
- Run from repo root: npm run dev:viewer
  - Starts a local Convex dev server at http://127.0.0.1:3210
  - Starts the Next.js viewer at http://localhost:3050 with NEXT_PUBLIC_CONVEX_URL wired automatically

If you see a Convex warning the first time, it's initializing the local project; the viewer will still start.


A comprehensive ETL pipeline for bookmark data that implements delta load functionality inspired by [j-94/deltaload](https://github.com/j-94/deltaload), with AI enrichment using Vercel AI SDK.

## Features

### 🔄 Delta Load ETL
- **Change Detection**: Tracks changes using content hashing
- **Incremental Processing**: Only processes new or modified bookmarks
- **State Management**: Maintains processing state between runs
- **Snapshot Recovery**: Creates snapshots for data recovery
- **Change History**: Logs all additions, modifications, and deletions

### 🤖 AI Enrichment
- **Content Analysis**: Deep analysis of webpage content
- **Topic Extraction**: Identifies main topics and entities
- **Social Signals**: Analyzes virality and engagement potential
- **Temporal Analysis**: Tracks content lifecycle and relevance
- **Quality Scoring**: Rates content quality and uniqueness
- **Clustering**: Groups similar bookmarks automatically

### 📊 DocETL Integration
- **Batch Processing**: Efficient processing of large datasets
- **Intelligence Reports**: Generates comprehensive insights
- **Pattern Recognition**: Identifies content patterns and gaps
- **Recommendation Engine**: Suggests curation actions

## Installation

```bash
cd bookmark-delta-etl
bun install
bun run check
```

## Usage

### Basic ETL Run
```bash
bun run etl bookmarks.json
```

### Full Enrichment
```bash
bun run etl:full bookmarks.json
```

### Options
- `--no-ai`: Disable AI enrichment
- `--no-docetl`: Disable DocETL processing
- `--output <dir>`: Output directory (default: ./bookmark-delta-data)
- `--content`: Include webpage content fetching
- `--social`: Include social signal analysis
- `--temporal`: Include temporal analysis
- `--batch <size>`: AI enrichment batch size (default: 10)

### Examples
```bash
# Process multiple files
bun run etl bookmarks.json raindrop-export.json

# AI-only enrichment with small batches
bun run etl --no-docetl --batch 5 *.json

# Full analysis with custom output
bun run etl --output ./my-data --content --social bookmarks.csv
```

## Data Sources & .env

Copy `.env.example` to `.env` and fill in what you have:

- `RAINDROP_API_KEY` (Raindrop.io REST)
- `GITHUB_TOKEN` (GitHub PAT for starred repos)
- `X_CT0`, `X_AUTH_TOKEN`, `X_KDT` (optional; X.com cookies for Grok scraping)
- `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` (optional; enrichment)
- `UNIFIED_CHAT_PATH` (optional; path to your unified chat JSON)

Then check credentials and guidance:

```bash
bun check-credentials.ts --setup --test
```

## Fetch + Ingest (Unified)

Fetch from APIs (Raindrop, GitHub) and ingest into the unified delta store:

```bash
# Fetch sources individually
bun bin/fetch-raindrop.ts
bun bin/fetch-github-stars.ts

# Or fetch everything available and ingest to unified
bun bin/fetch-all.ts

# Verify + report
bun unified/verify.ts ./unified
bun unified/report.ts ./unified
```

Raw API dumps will be written to `raw/`. Unified outputs land in `unified/`.

## Data Flow

1. **Extract**: Load bookmarks from JSON/CSV sources
2. **Transform**: Enrich with metadata and calculate metrics
3. **Delta Detection**: Compare with previous state
4. **AI Enrichment**: Analyze content and generate insights
5. **Load**: Store enriched data with change tracking
6. **Report**: Generate intelligence reports and statistics

## Output Structure

```
bookmark-delta-data/
├── bookmarks.json              # Current bookmark state
├── delta-state.json           # Delta load state
├── changes-*.json             # Change logs
├── bookmark-clusters.json     # AI-generated clusters
├── bookmark-insights.json     # AI insights
├── etl-report.md             # Summary report
└── snapshot-*.json           # Recovery snapshots
```

## Enhanced Bookmark Schema

The pipeline enriches bookmarks with:

- **Content Metrics**: Length, reading time, language
- **Technical Details**: Response time, SSL validity, mobile friendliness
- **AI Analysis**: Topics, sentiment, readability, quality scores
- **Social Signals**: Sharing potential, virality, engagement
- **Temporal Data**: Content lifespan, update frequency, stability
- **Delta Tracking**: Change frequency, content stability

## Integration with Search UI

The enriched data can be used with the search interface:

```typescript
// Load enriched bookmarks
const bookmarks = await fs.readFile('bookmark-delta-data/bookmarks.json');
const clusters = await fs.readFile('bookmark-delta-data/bookmark-clusters.json');

// Use in search API
app.get('/api/bookmarks/search', async (req, res) => {
  const { q } = req.query;
  // Search through enriched bookmarks
});
```

## Monitoring & Statistics

Get ETL statistics:
```typescript
const stats = await etl.getStatistics();
console.log(`Total bookmarks: ${stats.totalBookmarks}`);
console.log(`Recent changes: ${stats.changesLast24h}`);
```

## Best Practices

1. **Regular Runs**: Schedule daily/weekly runs to track changes
2. **Batch Sizes**: Use smaller batches (5-10) for better AI quality
3. **Snapshots**: Create snapshots before major operations
4. **Content Fetching**: Enable selectively to avoid rate limits
5. **Review Reports**: Check attention_required bookmarks regularly

## Troubleshooting

- **Rate Limits**: Reduce batch size or add delays
- **Memory Issues**: Process in smaller chunks
- **API Errors**: Check OpenAI API key and quota
- **DocETL Errors**: Ensure DocETL is installed (`pip install docetl`)

## Contributing

This pipeline follows the delta load patterns from [j-94/deltaload](https://github.com/j-94/deltaload). Contributions welcome!

## Unified Format + Delta Loading (New)

In addition to bookmark-specific ETL, the repo includes a source-agnostic unified schema and delta loader under `unified/` to normalize multiple data types (bookmarks and unified chat to start).

- Unified schema: `unified/unified-schema.ts` (Zod)
- Normalizers: `unified/normalize.ts` (bookmarks, unified chat)
- Delta engine: `unified/unified-delta.ts` (snapshot/append modes)
- CLI: `unified/cli.ts`
- Verification: `unified/verify.ts`

Usage examples:

```
# Normalize bookmarks JSONL and write unified outputs to ./unified
bun unified/cli.ts bookmark:more-bookmarks.jsonl

# Process unified chat (conversations[]) and bookmarks together in snapshot mode
bun unified/cli.ts --out ./unified --mode snapshot \
  bookmark:/Users/imac/Desktop/Donkeyv1/context/bookmark/docetl_bookmarkv0/processed_bookmarks_for_docetl.jsonl \
  chat_unified:/Users/imac/Desktop/Donkeyv1/context/chat_history/unified_data/unified_chat_properly_separated_20250613_150354.json

# Verify unified outputs
bun unified/verify.ts ./unified

# Generate a report and markdown snapshot
bun unified/report.ts ./unified
```

Outputs:
- `unified/run-<timestamp>.jsonl` — normalized records
- `unified/changes-<timestamp>.json` — delta summary (added/modified/deleted/unchanged)
- `unified/unified-manifest.json` — persistent hashes for delta detection
- `unified/REPORT.md` — human-friendly summary written by report tool
## Convex Seed + Reactive Viewer (WIP)

Quickstart
- Audit and seed preview:
  - bun scripts/data_audit.ts
  - Outputs in ./reports/: inventory.json, duplicates-within.json, duplicates-cross.json, schema-diff.json, seed_preview.jsonl, SUMMARY.md
- Import to Convex (dry run by default):
  - bun apps/ingest/import_to_convex.ts --preview reports/seed_preview.jsonl --dry-run
  - Use CONVEX_URL to point at your Convex dev project; remove --dry-run to upsert.
- Viewer: a minimal Next.js + Convex UI lives under apps/viewer/ (set NEXT_PUBLIC_CONVEX_URL and run npm run dev).
