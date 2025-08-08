# Delta Load Guide: Adding More Data

## Overview
The delta load system tracks changes using content hashing and only processes new or modified bookmarks. Here's how to add more data from various sources.

## Adding New Data Sources

### 1. From Raindrop.io Export
```bash
# Export from Raindrop.io as JSON
# Then run:
bun run etl raindrop-export-new.json

# Or combine with existing sources:
bun run etl bookmarks.json raindrop-export-new.json twitter-export.json
```

### 2. From Twitter/X Bookmarks
```bash
# Use a Twitter export tool or API
# Save as JSON format with tweet data
bun run etl twitter-bookmarks-2024.json
```

### 3. From GitHub Stars
```bash
# Use GitHub API to export starred repos
# Format as JSON with repo metadata
bun run etl github-stars-export.json
```

### 4. From Browser Bookmarks
```bash
# Export from Chrome/Firefox/Safari
# Convert to JSON format
bun run etl browser-bookmarks.json
```

## Delta Load Process

### How It Works
1. **Hash Generation**: Each bookmark gets a unique hash based on its content
2. **Change Detection**: Compares new hashes with stored hashes
3. **Incremental Processing**: Only processes new or changed bookmarks
4. **State Tracking**: Maintains processing history

### Running Delta Loads

#### Basic Delta Load
```bash
# First run - processes all bookmarks
bun run etl initial-bookmarks.json

# Second run - only processes changes
bun run etl initial-bookmarks.json new-bookmarks.json
```

#### Scheduled Delta Loads
```bash
# Create a cron job or scheduled task
# daily-delta.sh
#!/bin/bash
cd /path/to/bookmark-delta-etl

# Fetch latest exports
python fetch_raindrop_export.py > raindrop-latest.json
python fetch_twitter_bookmarks.py > twitter-latest.json

# Run delta ETL
bun run etl:full raindrop-latest.json twitter-latest.json

# Send notification
echo "Delta load complete: $(date)" | mail -s "Bookmark ETL" you@email.com
```

## Data Source Integration

### 1. Raindrop.io API Integration
```typescript
// raindrop-fetcher.ts
import { BookmarkDeltaETL } from './delta-load-pipeline';

async function fetchRaindropBookmarks(apiKey: string) {
  const response = await fetch('https://api.raindrop.io/rest/v1/raindrops/0', {
    headers: { 'Authorization': `Bearer ${apiKey}` }
  });
  
  const data = await response.json();
  return data.items.map(item => ({
    id: `raindrop-${item._id}`,
    url: item.link,
    title: item.title,
    description: item.excerpt,
    created_at: item.created,
    source: 'raindrop',
    metadata: {
      tags: item.tags,
      folder: item.collection?.$id,
      cover: item.cover,
      domain: item.domain,
      ...item
    }
  }));
}

// Run delta load with fresh data
const bookmarks = await fetchRaindropBookmarks(process.env.RAINDROP_API_KEY);
await fs.writeFile('raindrop-latest.json', JSON.stringify(bookmarks));

const etl = new BookmarkDeltaETL();
await etl.runETL(['raindrop-latest.json']);
```

### 2. Twitter Bookmarks Scraper
```typescript
// twitter-fetcher.ts
async function fetchTwitterBookmarks(session: string) {
  // Use Twitter API v2 or scraping tool
  const bookmarks = await twitterClient.getBookmarks();
  
  return bookmarks.map(tweet => ({
    id: `twitter-${tweet.id}`,
    url: `https://twitter.com/user/status/${tweet.id}`,
    full_text: tweet.full_text,
    created_at: tweet.created_at,
    source: 'twitter',
    metadata: {
      author: tweet.author,
      tweet_metrics: tweet.public_metrics,
      // ... other Twitter fields
    }
  }));
}
```

### 3. GitHub Stars Fetcher
```typescript
// github-fetcher.ts
async function fetchGitHubStars(token: string) {
  const octokit = new Octokit({ auth: token });
  const stars = await octokit.paginate(octokit.activity.listReposStarredByAuthenticatedUser);
  
  return stars.map(repo => ({
    id: `github-${repo.id}`,
    url: repo.html_url,
    title: repo.full_name,
    description: repo.description,
    created_at: repo.created_at,
    source: 'github',
    metadata: {
      stars: repo.stargazers_count,
      forks: repo.forks_count,
      language: repo.language,
      // ... other GitHub fields
    }
  }));
}
```

## Monitoring Delta Loads

### Check Delta State
```bash
# View current state
cat bookmark-delta-data/delta-state.json

# See recent changes
ls -la bookmark-delta-data/changes-*.json

# View statistics
bun run scripts/delta-stats.ts
```

### Delta Load Dashboard
```typescript
// delta-dashboard.ts
import { BookmarkDeltaETL } from './delta-load-pipeline';

async function getDeltaStats() {
  const etl = new BookmarkDeltaETL();
  const stats = await etl.getStatistics();
  
  console.log(`
📊 Delta Load Dashboard
======================
Total Bookmarks: ${stats.totalBookmarks}
Changes (24h): ${stats.changesLast24h}
Avg Change Rate: ${stats.averageChangeFrequency}/month

Most Active:
${stats.mostChanged.map(b => `- ${b.title}: ${b.change_frequency} changes`).join('\n')}

Most Stable:
${stats.mostStable.map(b => `- ${b.title}: ${b.content_stability} stability`).join('\n')}
  `);
}
```

## Handling Large Datasets

### Chunked Processing
```bash
# Split large files
split -l 1000 huge-bookmarks.json chunk-

# Process chunks
for chunk in chunk-*; do
  bun run etl $chunk
  sleep 5 # Rate limiting
done
```

### Parallel Processing
```typescript
// parallel-delta.ts
async function parallelDeltaLoad(sources: string[], workers = 4) {
  const chunks = chunkArray(sources, Math.ceil(sources.length / workers));
  
  await Promise.all(
    chunks.map(async (chunk, i) => {
      const etl = new BookmarkDeltaETL(`./delta-data-${i}`);
      return etl.runETL(chunk);
    })
  );
  
  // Merge results
  await mergeDeltaResults(workers);
}
```

## Best Practices

### 1. Regular Schedules
- Run delta loads daily/weekly
- Process during off-peak hours
- Monitor for failures

### 2. Data Validation
```typescript
// Validate before processing
const validateBookmark = (b: any) => {
  if (!b.url || !b.id) return false;
  if (!b.source) b.source = 'unknown';
  if (!b.created_at) b.created_at = new Date().toISOString();
  return true;
};

bookmarks = bookmarks.filter(validateBookmark);
```

### 3. Incremental Enrichment
```bash
# Only enrich new/changed bookmarks
bun run etl:simple new-data.json  # Delta load only
bun run enrich-new                # AI enrichment for new items
```

### 4. Backup Strategy
```bash
# Before major imports
bun run scripts/create-snapshot.ts

# Restore if needed
bun run scripts/restore-snapshot.ts snapshot-2024-01-15.json
```

## Example: Complete Delta Workflow

```bash
#!/bin/bash
# delta-workflow.sh

echo "🚀 Starting Delta Load Workflow"

# 1. Fetch new data
echo "📥 Fetching new bookmarks..."
node fetch-raindrop.js > data/raindrop-$(date +%Y%m%d).json
node fetch-twitter.js > data/twitter-$(date +%Y%m%d).json
node fetch-github.js > data/github-$(date +%Y%m%d).json

# 2. Run delta ETL
echo "🔄 Running delta ETL..."
bun run etl data/*.json

# 3. Enrich new bookmarks
echo "🤖 Enriching new bookmarks..."
bun run etl:full --batch 20 data/*.json

# 4. Generate reports
echo "📊 Generating reports..."
bun run scripts/generate-reports.ts

# 5. Cleanup old data
echo "🧹 Cleaning up..."
find data -name "*.json" -mtime +30 -delete

echo "✅ Delta load complete!"
```

## Troubleshooting

### Common Issues

1. **Duplicate Detection**
```typescript
// Handle same URL with different IDs
const deduped = bookmarks.reduce((acc, b) => {
  const key = b.url || b.id;
  if (!acc[key] || new Date(b.updated_at) > new Date(acc[key].updated_at)) {
    acc[key] = b;
  }
  return acc;
}, {});
```

2. **Memory Issues**
```bash
# Process in smaller batches
bun run etl --batch-size 100 large-file.json
```

3. **API Rate Limits**
```typescript
// Add delays between API calls
await sleep(1000); // 1 second delay
```

## Next Steps

1. Set up automated data fetching
2. Create monitoring dashboards
3. Implement data quality checks
4. Build notification system for important changes