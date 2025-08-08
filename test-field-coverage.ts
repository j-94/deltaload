#!/usr/bin/env bun

import { BookmarkDeltaETL } from './delta-load-pipeline';
import { AIBookmarkEnricher } from './ai-sdk-bookmark-enricher';
import { flattenBookmarkMetadata, extractSourceMetadata } from './enhanced-bookmark-schema';
import * as fs from 'fs/promises';

async function testFieldCoverage() {
  console.log('🧪 Testing Enhanced ETL Field Coverage\n');
  
  // Load a sample of the actual bookmark data
  const dataPath = '../context/bookmark/docetl_bookmarkv0/processed_bookmarks_for_docetl.jsonl';
  const data = await fs.readFile(dataPath, 'utf-8');
  const lines = data.trim().split('\n').slice(0, 10); // Test with first 10 bookmarks
  
  const bookmarks = lines.map(line => JSON.parse(line));
  
  console.log(`📚 Testing with ${bookmarks.length} bookmarks\n`);
  
  // Group by source
  const bySource = bookmarks.reduce((acc, b) => {
    acc[b.source] = (acc[b.source] || 0) + 1;
    return acc;
  }, {} as Record<string, number>);
  
  console.log('Sources:', bySource, '\n');
  
  // Test field extraction for each source type
  for (const source of Object.keys(bySource)) {
    console.log(`\n=== Testing ${source.toUpperCase()} bookmarks ===`);
    
    const sourceBookmarks = bookmarks.filter(b => b.source === source);
    const sample = sourceBookmarks[0];
    
    if (sample) {
      // Flatten and extract metadata
      const flattened = flattenBookmarkMetadata(sample);
      const { sourceMetadata } = extractSourceMetadata(sample);
      
      console.log(`\n📄 Sample bookmark: ${sample.url}`);
      console.log(`Total flattened fields: ${Object.keys(flattened).length}`);
      console.log(`Source-specific fields: ${Object.keys(sourceMetadata).length}`);
      
      // Show key fields
      console.log('\nKey fields extracted:');
      const keyFields = source === 'github' 
        ? ['metadata.stars', 'metadata.forks', 'metadata.language', 'metadata.has_readme']
        : source === 'twitter'
        ? ['metadata.tweet_metrics', 'metadata.user_followers', 'metadata.retweet_count']
        : ['metadata.tags', 'metadata.folder', 'metadata.favorite'];
        
      keyFields.forEach(field => {
        console.log(`  ${field}: ${flattened[field] !== undefined ? '✅' : '❌'} ${
          flattened[field] !== undefined ? `(${JSON.stringify(flattened[field]).substring(0, 50)}...)` : ''
        }`);
      });
    }
  }
  
  // Test ETL pipeline
  console.log('\n\n=== Testing ETL Pipeline ===');
  const etl = new BookmarkDeltaETL('./test-delta-data');
  
  try {
    // Save test data
    await fs.writeFile('./test-bookmarks.json', JSON.stringify(bookmarks, null, 2));
    
    // Run ETL
    const result = await etl.runETL(['./test-bookmarks.json']);
    console.log(`\n✅ ETL completed successfully`);
    console.log(`   Processed: ${result.processed} bookmarks`);
    console.log(`   Changes detected: ${result.changes.length}`);
    console.log(`   Duration: ${result.duration}ms`);
    
    // Check transformed data
    const transformedData = await fs.readFile('./test-delta-data/bookmarks.json', 'utf-8');
    const transformed = JSON.parse(transformedData);
    
    console.log('\n📊 Field preservation check:');
    const sampleTransformed = transformed[0];
    if (sampleTransformed) {
      console.log(`  Core fields: ${Object.keys(sampleTransformed).length}`);
      console.log(`  Metadata fields: ${Object.keys(sampleTransformed.meta_tags || {}).length}`);
      
      // Check for specific metadata preservation
      const checks = [
        { field: 'opengraph', exists: !!sampleTransformed.meta_tags?.opengraph },
        { field: 'twitter_card', exists: !!sampleTransformed.meta_tags?.twitter_card },
        { field: 'github_data', exists: !!sampleTransformed.meta_tags?.github_data },
        { field: 'twitter_data', exists: !!sampleTransformed.meta_tags?.twitter_data },
        { field: 'sourceMetadata', exists: !!sampleTransformed.meta_tags?.sourceMetadata }
      ];
      
      checks.forEach(({ field, exists }) => {
        console.log(`  ${field}: ${exists ? '✅ Preserved' : '⚠️  Not found'}`);
      });
    }
    
    // Test AI enrichment with metadata
    console.log('\n\n=== Testing AI Enrichment ===');
    const enricher = new AIBookmarkEnricher(etl);
    
    // Test with one bookmark of each type
    const testSamples = ['github', 'twitter', 'raindrop']
      .map(source => bookmarks.find(b => b.source === source))
      .filter(Boolean)
      .slice(0, 2); // Limit to 2 for API cost
    
    if (testSamples.length > 0) {
      console.log(`Testing enrichment on ${testSamples.length} samples...`);
      
      const enriched = await enricher.enrichBookmarkBatch(testSamples, {
        includeContent: false, // Skip content fetching for test
        includeSocial: true,
        includeTemporal: false,
        parallel: 1
      });
      
      console.log('\n✅ Enrichment results:');
      enriched.forEach((e, i) => {
        console.log(`\n  ${i + 1}. ${e.source} bookmark:`);
        console.log(`     Social signals: ${e.social_signals ? '✅' : '❌'}`);
        if (e.social_signals) {
          console.log(`     - Virality: ${e.social_signals.virality_potential}`);
          console.log(`     - Engagement: ${e.social_signals.engagement_prediction}`);
        }
      });
    }
    
    // Cleanup
    await fs.rm('./test-bookmarks.json');
    await fs.rm('./test-delta-data', { recursive: true });
    
  } catch (error) {
    console.error('❌ Test failed:', error);
  }
  
  console.log('\n\n🎉 Field coverage test complete!');
}

// Run test
testFieldCoverage().catch(console.error);