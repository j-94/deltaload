# Bookmark Delta ETL Pipeline

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