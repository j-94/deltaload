#!/usr/bin/env bun

import { BookmarkDeltaETL } from './delta-load-pipeline';
import { AIBookmarkEnricher } from './ai-sdk-bookmark-enricher';
import { execSync } from 'child_process';
import * as fs from 'fs/promises';
import * as path from 'path';

interface ETLConfig {
  sources: string[];
  enableAI: boolean;
  enableDocETL: boolean;
  outputDir: string;
  enrichmentOptions?: {
    includeContent?: boolean;
    includeSocial?: boolean;
    includeTemporal?: boolean;
    batchSize?: number;
  };
}

class BookmarkETLRunner {
  private config: ETLConfig;
  private etl: BookmarkDeltaETL;
  private enricher: AIBookmarkEnricher;
  
  constructor(config: ETLConfig) {
    this.config = {
      outputDir: './bookmark-delta-data',
      enableAI: true,
      enableDocETL: true,
      ...config
    };
    this.etl = new BookmarkDeltaETL(this.config.outputDir);
    this.enricher = new AIBookmarkEnricher(this.etl);
  }
  
  async run() {
    console.log('🚀 Starting Comprehensive Bookmark ETL Pipeline');
    console.log('=' .repeat(50));
    
    // Phase 1: Delta Load ETL
    console.log('\n📦 Phase 1: Delta Load ETL');
    const etlResult = await this.etl.runETL(this.config.sources);
    console.log(`✅ Processed ${etlResult.processed} bookmarks with ${etlResult.changes.length} changes`);
    
    // Phase 2: AI Enrichment
    if (this.config.enableAI) {
      console.log('\n🤖 Phase 2: AI Enrichment');
      await this.runAIEnrichment();
    }
    
    // Phase 3: DocETL Processing
    if (this.config.enableDocETL) {
      console.log('\n📊 Phase 3: DocETL Intelligence Generation');
      await this.runDocETL();
    }
    
    // Phase 4: Generate Reports
    console.log('\n📈 Phase 4: Generating Reports');
    await this.generateReports();
    
    // Phase 5: Create Snapshot
    console.log('\n💾 Phase 5: Creating Snapshot');
    const snapshot = await this.etl.createSnapshot();
    console.log(`✅ Snapshot saved: ${snapshot}`);
    
    console.log('\n🎉 ETL Pipeline Complete!');
  }
  
  private async runAIEnrichment() {
    try {
      // Load current bookmarks
      const bookmarksPath = path.join(this.config.outputDir, 'bookmarks.json');
      const bookmarks = JSON.parse(await fs.readFile(bookmarksPath, 'utf-8'));
      
      // Determine which bookmarks need enrichment
      const needsEnrichment = bookmarks.filter((b: any) => 
        !b.enriched_at || 
        new Date(b.enriched_at) < new Date(Date.now() - 7 * 24 * 60 * 60 * 1000) // 7 days old
      );
      
      console.log(`📝 ${needsEnrichment.length} bookmarks need enrichment`);
      
      if (needsEnrichment.length > 0) {
        // Enrich in batches
        const batchSize = this.config.enrichmentOptions?.batchSize || 10;
        const enriched = [];
        
        for (let i = 0; i < needsEnrichment.length; i += batchSize) {
          const batch = needsEnrichment.slice(i, i + batchSize);
          console.log(`   Processing batch ${Math.floor(i/batchSize) + 1}/${Math.ceil(needsEnrichment.length/batchSize)}`);
          
          const enrichedBatch = await this.enricher.enrichBookmarkBatch(
            batch, 
            this.config.enrichmentOptions
          );
          enriched.push(...enrichedBatch);
          
          // Save progress
          await this.saveEnrichedBookmarks(enriched);
        }
        
        console.log(`✅ Enriched ${enriched.length} bookmarks`);
        
        // Generate clusters
        console.log('🗂️  Generating bookmark clusters...');
        const { clusters } = await this.enricher.clusterBookmarks(enriched);
        await fs.writeFile(
          path.join(this.config.outputDir, 'bookmark-clusters.json'),
          JSON.stringify(clusters, null, 2)
        );
        console.log(`✅ Generated ${clusters.length} clusters`);
        
        // Generate insights
        console.log('💡 Generating insights...');
        const insights = await this.enricher.generateInsights(enriched);
        await fs.writeFile(
          path.join(this.config.outputDir, 'bookmark-insights.json'),
          JSON.stringify(insights, null, 2)
        );
      }
    } catch (error) {
      console.error('❌ AI Enrichment failed:', error);
    }
  }
  
  private async saveEnrichedBookmarks(enrichedBookmarks: any[]) {
    const bookmarksPath = path.join(this.config.outputDir, 'bookmarks.json');
    const allBookmarks = JSON.parse(await fs.readFile(bookmarksPath, 'utf-8'));
    
    // Update bookmarks with enriched data
    const bookmarkMap = new Map(allBookmarks.map((b: any) => [b.id, b]));
    enrichedBookmarks.forEach(enriched => {
      bookmarkMap.set(enriched.id, enriched);
    });
    
    await fs.writeFile(
      bookmarksPath,
      JSON.stringify(Array.from(bookmarkMap.values()), null, 2)
    );
  }
  
  private async runDocETL() {
    try {
      const pipelinePath = path.join(__dirname, 'bookmark-delta-docetl.yaml');
      
      // Check if DocETL is installed
      try {
        execSync('docetl --version', { stdio: 'ignore' });
      } catch {
        console.log('⚠️  DocETL not found, skipping...');
        return;
      }
      
      console.log('🔄 Running DocETL pipeline...');
      execSync(`docetl run ${pipelinePath}`, { stdio: 'inherit' });
      console.log('✅ DocETL processing complete');
      
      // Load and display summary of results
      try {
        const report = JSON.parse(
          await fs.readFile('bookmark-intelligence-report.json', 'utf-8')
        );
        console.log('\n📋 Intelligence Report Summary:');
        console.log(`   - ${report.executive_summary?.substring(0, 100)}...`);
        console.log(`   - Top valuable bookmarks: ${report.top_valuable_bookmarks?.length || 0}`);
        console.log(`   - Attention required: ${report.attention_required?.length || 0}`);
        console.log(`   - Content gaps identified: ${report.content_gaps?.length || 0}`);
      } catch (error) {
        console.log('⚠️  Could not load intelligence report');
      }
    } catch (error) {
      console.error('❌ DocETL processing failed:', error);
    }
  }
  
  private async generateReports() {
    // Get statistics
    const stats = await this.etl.getStatistics();
    
    // Generate markdown report
    const report = `# Bookmark ETL Report
Generated: ${new Date().toISOString()}

## Summary Statistics
- Total Bookmarks: ${stats.totalBookmarks}
- Changes in Last 24h: ${stats.changesLast24h}
- Average Change Frequency: ${stats.averageChangeFrequency.toFixed(2)} changes/month

## Most Changed Bookmarks
${stats.mostChanged.map((b, i) => 
  `${i + 1}. **${b.title}** (${b.change_frequency} changes)\n   - URL: ${b.url}\n   - Stability: ${b.content_stability}`
).join('\n')}

## Most Stable References
${stats.mostStable.map((b, i) => 
  `${i + 1}. **${b.title}** (Stability: ${b.content_stability})\n   - URL: ${b.url}`
).join('\n')}

## Data Quality Metrics
- Bookmarks with AI enrichment: ${await this.getEnrichmentStats()}
- Bookmarks with content analysis: ${await this.getContentAnalysisStats()}
- Average value score: ${await this.getAverageValueScore()}

## Next Steps
1. Review bookmarks requiring attention
2. Update stale content
3. Fill identified content gaps
4. Schedule next ETL run based on change patterns
`;
    
    await fs.writeFile(
      path.join(this.config.outputDir, 'etl-report.md'),
      report
    );
    
    console.log(`✅ Report saved to ${this.config.outputDir}/etl-report.md`);
  }
  
  private async getEnrichmentStats(): Promise<string> {
    try {
      const bookmarks = JSON.parse(
        await fs.readFile(path.join(this.config.outputDir, 'bookmarks.json'), 'utf-8')
      );
      const enriched = bookmarks.filter((b: any) => b.enriched_at).length;
      return `${enriched}/${bookmarks.length} (${Math.round(enriched/bookmarks.length * 100)}%)`;
    } catch {
      return 'N/A';
    }
  }
  
  private async getContentAnalysisStats(): Promise<string> {
    try {
      const bookmarks = JSON.parse(
        await fs.readFile(path.join(this.config.outputDir, 'bookmarks.json'), 'utf-8')
      );
      const analyzed = bookmarks.filter((b: any) => b.content_analysis).length;
      return `${analyzed}/${bookmarks.length} (${Math.round(analyzed/bookmarks.length * 100)}%)`;
    } catch {
      return 'N/A';
    }
  }
  
  private async getAverageValueScore(): Promise<string> {
    try {
      const bookmarks = JSON.parse(
        await fs.readFile(path.join(this.config.outputDir, 'bookmarks.json'), 'utf-8')
      );
      const scores = bookmarks
        .filter((b: any) => b.value_score !== undefined)
        .map((b: any) => b.value_score);
      
      if (scores.length === 0) return 'N/A';
      
      const avg = scores.reduce((a: number, b: number) => a + b, 0) / scores.length;
      return avg.toFixed(2);
    } catch {
      return 'N/A';
    }
  }
}

// CLI Interface
async function main() {
  const args = process.argv.slice(2);
  
  if (args.includes('--help') || args.includes('-h')) {
    console.log(`
Bookmark Delta ETL Runner

Usage: bun run-bookmark-etl.ts [options] <source-files...>

Options:
  --no-ai          Disable AI enrichment
  --no-docetl      Disable DocETL processing
  --output <dir>   Output directory (default: ./bookmark-delta-data)
  --content        Include webpage content fetching
  --social         Include social signal analysis
  --temporal       Include temporal analysis
  --batch <size>   AI enrichment batch size (default: 10)
  
Examples:
  bun run-bookmark-etl.ts bookmarks.json
  bun run-bookmark-etl.ts --no-docetl --batch 5 *.json
  bun run-bookmark-etl.ts --output ./data --content bookmarks.csv
`);
    process.exit(0);
  }
  
  // Parse arguments
  const sources: string[] = [];
  const config: Partial<ETLConfig> = {
    enrichmentOptions: {}
  };
  
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    
    switch (arg) {
      case '--no-ai':
        config.enableAI = false;
        break;
      case '--no-docetl':
        config.enableDocETL = false;
        break;
      case '--output':
        config.outputDir = args[++i];
        break;
      case '--content':
        config.enrichmentOptions!.includeContent = true;
        break;
      case '--social':
        config.enrichmentOptions!.includeSocial = true;
        break;
      case '--temporal':
        config.enrichmentOptions!.includeTemporal = true;
        break;
      case '--batch':
        config.enrichmentOptions!.batchSize = parseInt(args[++i]);
        break;
      default:
        if (!arg.startsWith('--')) {
          sources.push(arg);
        }
    }
  }
  
  if (sources.length === 0) {
    console.error('❌ No source files specified');
    console.log('Run with --help for usage information');
    process.exit(1);
  }
  
  config.sources = sources;
  
  // Run ETL
  const runner = new BookmarkETLRunner(config as ETLConfig);
  await runner.run();
}

// Run if main
if (import.meta.main) {
  main().catch(console.error);
}