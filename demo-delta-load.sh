#!/bin/bash

echo "🚀 Bookmark Delta Load Demo"
echo "=========================="
echo ""

# Step 1: Initial load
echo "📥 Step 1: Initial data load (100 bookmarks)"
head -100 ../context/bookmark/docetl_bookmarkv0/processed_bookmarks_for_docetl.jsonl > demo-batch-1.jsonl
bun run run-bookmark-etl.ts --no-ai --no-docetl demo-batch-1.jsonl
echo ""

# Show status
echo "📊 Current status:"
bun run delta-monitor.ts status | jq '.overview'
echo ""

# Step 2: Add more data
echo "📥 Step 2: Adding 50 more bookmarks"
tail -200 ../context/bookmark/docetl_bookmarkv0/processed_bookmarks_for_docetl.jsonl | head -50 > demo-batch-2.jsonl
bun run run-bookmark-etl.ts --no-ai --no-docetl demo-batch-1.jsonl demo-batch-2.jsonl
echo ""

# Show changes
echo "📊 Changes detected:"
ls -la bookmark-delta-data/changes-*.json | tail -1
echo ""

# Step 3: Run again with no changes
echo "📥 Step 3: Running again with same data (no changes expected)"
bun run run-bookmark-etl.ts --no-ai --no-docetl demo-batch-1.jsonl demo-batch-2.jsonl
echo ""

# Final dashboard
echo "📊 Final Dashboard:"
bun run delta-monitor.ts dashboard

# Cleanup
rm demo-batch-*.jsonl