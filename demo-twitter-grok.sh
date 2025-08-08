#!/bin/bash

echo "🐦 Twitter/Grok Bookmark ETL Demo"
echo "================================="
echo ""
echo "This demo shows how to integrate Twitter/Grok conversations into the bookmark system."
echo ""

# Check credentials using the global manager
echo "🔑 Checking Credentials..."
bun check-credentials.ts

# Show what data we have
echo "📊 Available Data Sources:"
echo ""

# Check for unified chat data
UNIFIED_FILES=$(ls ../unified_chat_full_data*.json 2>/dev/null | wc -l)
if [ $UNIFIED_FILES -gt 0 ]; then
    echo "✅ Unified chat data found: $UNIFIED_FILES files"
    LATEST_UNIFIED=$(ls -t ../unified_chat_full_data*.json 2>/dev/null | head -1)
    if [ -f "$LATEST_UNIFIED" ]; then
        GROK_COUNT=$(grep -o '"platform": "Grok"' "$LATEST_UNIFIED" 2>/dev/null | wc -l)
        echo "   - Grok conversations: $GROK_COUNT"
    fi
else
    echo "❌ No unified chat data found"
fi

# Check for existing bookmarks
if [ -f "bookmark-delta-data/bookmarks.json" ]; then
    BOOKMARK_COUNT=$(jq 'length' bookmark-delta-data/bookmarks.json 2>/dev/null || echo "0")
    echo "✅ Existing bookmarks: $BOOKMARK_COUNT"
else
    echo "❌ No existing bookmarks"
fi

echo ""
echo "🚀 Running Enhanced ETL with Twitter/Grok Integration..."
echo ""

# Run the ETL
if [ -f "../context/bookmark/docetl_bookmarkv0/ai_tools_directory_last_1000.json" ]; then
    # Use existing enriched bookmarks
    echo "Using enriched bookmarks as source..."
    bun run-bookmark-etl-with-twitter.ts ../context/bookmark/docetl_bookmarkv0/ai_tools_directory_last_1000.json
else
    # Use sample bookmarks
    echo "Using sample bookmarks..."
    bun run-bookmark-etl-with-twitter.ts ../donkey/data/inputs/bookmarks.json
fi

echo ""
echo "✅ Demo Complete!"
echo ""
echo "📁 Output Files:"
echo "   - bookmark-delta-data/twitter-grok-bookmarks.json - Grok conversations as bookmarks"
echo "   - bookmark-delta-data/bookmark-threads.json - Thread compositions"
echo "   - bookmark-delta-data/bookmark-clusters.json - AI-generated clusters (if AI enabled)"
echo "   - bookmark-delta-data/etl-report.md - Full report"
echo ""
echo "🔍 Next Steps:"
echo "1. View the thread compositions: jq '.threads.conversations' bookmark-delta-data/bookmark-threads.json"
echo "2. Check the report: cat bookmark-delta-data/etl-report.md"
echo "3. Set X.com credentials to fetch full conversation content"
echo "4. Run with --twitter <username> to fetch user timelines (requires API implementation)"