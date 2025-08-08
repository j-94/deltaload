#!/usr/bin/env bun

import { BookmarkDeltaETL } from './delta-load-pipeline';
import { AIBookmarkEnricher } from './ai-sdk-bookmark-enricher';
import { TwitterGrokFetcher } from './twitter-grok-fetcher';
import { getCredentialsManager, printCredentialsStatus } from './credentials-manager';
import { execSync } from 'child_process';
import * as fs from 'fs/promises';
import * as path from 'path';

interface ETLConfig {
  sources: string[];
  enableAI: boolean;
  enableDocETL: boolean;
  enableTwitter: boolean;
  twitterUsername?: string;
  outputDir: string;
  enrichmentOptions?: {
    includeContent?: boolean;
    includeSocial?: boolean;
    includeTemporal?: boolean;
    batchSize?: number;
  };
}

class EnhancedBookmarkETLRunner {
  private config: ETLConfig;
  private etl: BookmarkDeltaETL;
  private enricher: AIBookmarkEnricher;
  private twitterFetcher: TwitterGrokFetcher;
  private credentialsManager = getCredentialsManager();
  
  constructor(config: ETLConfig) {
    this.config = {
      outputDir: './bookmark-delta-data',
      enableAI: true,
      enableDocETL: true,
      enableTwitter: true,
      ...config
    };
    this.etl = new BookmarkDeltaETL(this.config.outputDir);
    this.enricher = new AIBookmarkEnricher(this.etl);
    this.twitterFetcher = new TwitterGrokFetcher(this.etl, this.config.outputDir);
  }
  
  async run() {
    console.log('🚀 Starting Enhanced Bookmark ETL Pipeline with Twitter Integration');
    console.log('=' .repeat(60));
    
    // Check credentials and show status
    await this.credentialsManager.loadCredentials();
    this.credentialsManager.printStatus();
    
    // Phase 0: Twitter/Grok Integration
    if (this.config.enableTwitter) {
      console.log('\n🐦 Phase 0: Twitter/Grok Data Integration');
      await this.runTwitterIntegration();
    }
    
    // Phase 1: Delta Load ETL
    console.log('\n📦 Phase 1: Delta Load ETL');
    const etlResult = await this.etl.runETL(this.config.sources);
    console.log(`✅ Processed ${etlResult.processed} bookmarks with ${etlResult.changes.length} changes`);
    
    // Phase 2: AI Enrichment
    if (this.config.enableAI) {
      console.log('\n🤖 Phase 2: AI Enrichment');
      await this.runAIEnrichment();
    }
    
    // Phase 3: Thread Composition
    console.log('\n🧵 Phase 3: Thread Composition');
    await this.composeBookmarkThreads();
    
    // Phase 4: DocETL Processing
    if (this.config.enableDocETL) {
      console.log('\n📊 Phase 4: DocETL Intelligence Generation');
      await this.runDocETL();
    }
    
    // Phase 5: Generate Reports
    console.log('\n📈 Phase 5: Generating Reports');
    await this.generateReports();
    
    // Phase 6: Create Snapshot
    console.log('\n💾 Phase 6: Creating Snapshot');
    const snapshot = await this.etl.createSnapshot();
    console.log(`✅ Snapshot saved: ${snapshot}`);
    
    console.log('\n🎉 Enhanced ETL Pipeline Complete!');
  }
  
  private async runTwitterIntegration() {
    try {
      // Process existing Grok conversations
      console.log('📱 Processing existing Grok conversations...');
      await this.twitterFetcher.processTwitterGrokData();
      
      // Optionally fetch new timeline data
      if (this.config.twitterUsername) {
        console.log(`📱 Fetching timeline for @${this.config.twitterUsername}...`);
        await this.twitterFetcher.updateFromTimeline(this.config.twitterUsername);
      }
    } catch (error) {
      console.error('❌ Twitter integration failed:', error);
    }
  }
  
  private async composeBookmarkThreads() {
    try {
      // Load all bookmarks
      const bookmarksPath = path.join(this.config.outputDir, 'bookmarks.json');
      const bookmarks = JSON.parse(await fs.readFile(bookmarksPath, 'utf-8'));
      
      console.log(`🧵 Composing threads from ${bookmarks.length} bookmarks...`);
      
      // Group bookmarks by various criteria
      const threads = {
        bySource: new Map<string, any[]>(),
        byTopic: new Map<string, any[]>(),
        byAuthor: new Map<string, any[]>(),
        byConversation: new Map<string, any[]>(),
        temporal: [] as any[]
      };
      
      // Organize bookmarks into threads
      for (const bookmark of bookmarks) {
        // By source
        const source = bookmark.meta_tags?.source || 'unknown';
        if (!threads.bySource.has(source)) {
          threads.bySource.set(source, []);
        }
        threads.bySource.get(source)!.push(bookmark);
        
        // By conversation (for Twitter/Grok)
        const convId = bookmark.meta_tags?.conversation_id;
        if (convId) {
          if (!threads.byConversation.has(convId)) {
            threads.byConversation.set(convId, []);
          }
          threads.byConversation.get(convId)!.push(bookmark);
        }
        
        // By author
        const author = bookmark.author || bookmark.meta_tags?.author?.name || 'unknown';
        if (!threads.byAuthor.has(author)) {
          threads.byAuthor.set(author, []);
        }
        threads.byAuthor.get(author)!.push(bookmark);
        
        // By topic (use categories)
        for (const category of bookmark.categories || []) {
          if (!threads.byTopic.has(category)) {
            threads.byTopic.set(category, []);
          }
          threads.byTopic.get(category)!.push(bookmark);
        }
      }
      
      // Sort temporal thread by date
      threads.temporal = [...bookmarks].sort((a, b) => 
        new Date(a.created_at).getTime() - new Date(b.created_at).getTime()
      );
      
      // Create conversation-style exports
      const conversations = [];
      
      // Convert Twitter/Grok threads to conversations
      for (const [convId, convBookmarks] of threads.byConversation) {
        const conversation = {
          id: convId,
          platform: 'twitter/grok',
          title: convBookmarks[0].title,
          created_at: convBookmarks[0].created_at,
          updated_at: convBookmarks[convBookmarks.length - 1].updated_at,
          messages: convBookmarks.map(b => ({
            role: 'user',
            content: b.description,
            timestamp: new Date(b.created_at).getTime() / 1000,
            metadata: b.meta_tags
          })),
          bookmark_ids: convBookmarks.map(b => b.id)
        };
        conversations.push(conversation);
      }
      
      // Save thread compositions
      const threadsOutput = {
        timestamp: new Date().toISOString(),
        total_bookmarks: bookmarks.length,
        thread_counts: {
          by_source: threads.bySource.size,
          by_topic: threads.byTopic.size,
          by_author: threads.byAuthor.size,
          conversations: threads.byConversation.size
        },
        threads: {
          by_source: Object.fromEntries(threads.bySource),
          by_topic: Object.fromEntries(
            Array.from(threads.byTopic.entries())
              .filter(([topic, items]) => items.length > 3) // Only topics with 3+ bookmarks
              .sort((a, b) => b[1].length - a[1].length) // Sort by count
              .slice(0, 20) // Top 20 topics
          ),
          by_author: Object.fromEntries(
            Array.from(threads.byAuthor.entries())
              .filter(([author, items]) => items.length > 2) // Authors with 2+ bookmarks
              .sort((a, b) => b[1].length - a[1].length)
          ),
          conversations: conversations
        },
        temporal_sequence: threads.temporal.map(b => ({
          id: b.id,
          date: b.created_at,
          title: b.title,
          source: b.meta_tags?.source
        }))
      };
      
      await fs.writeFile(
        path.join(this.config.outputDir, 'bookmark-threads.json'),
        JSON.stringify(threadsOutput, null, 2)
      );
      
      console.log(`✅ Composed ${conversations.length} conversations and multiple thread types`);
      
      // Generate markdown summary
      const summary = `# Bookmark Threads Summary

Generated: ${new Date().toISOString()}

## Statistics
- Total Bookmarks: ${bookmarks.length}
- Sources: ${threads.bySource.size}
- Topics: ${threads.byTopic.size}
- Authors: ${threads.byAuthor.size}
- Conversations: ${threads.byConversation.size}

## Top Topics
${Array.from(threads.byTopic.entries())
  .sort((a, b) => b[1].length - a[1].length)
  .slice(0, 10)
  .map(([topic, items]) => `- **${topic}**: ${items.length} bookmarks`)
  .join('\n')}

## Twitter/Grok Conversations
${conversations.slice(0, 5).map(conv => 
  `### ${conv.title}
- ID: ${conv.id}
- Messages: ${conv.messages.length}
- Created: ${conv.created_at}
`).join('\n')}

## Recent Activity
${threads.temporal.slice(-10).reverse().map(b => 
  `- ${b.created_at}: ${b.title} (${b.meta_tags?.source || 'unknown'})`
).join('\n')}
`;
      
      await fs.writeFile(
        path.join(this.config.outputDir, 'bookmark-threads-summary.md'),
        summary
      );
      
    } catch (error) {
      console.error('❌ Thread composition failed:', error);
    }
  }
  
  private async runAIEnrichment() {
    // ... (keep existing AI enrichment logic from run-bookmark-etl.ts)
    try {
      const bookmarksPath = path.join(this.config.outputDir, 'bookmarks.json');
      const bookmarks = JSON.parse(await fs.readFile(bookmarksPath, 'utf-8'));
      
      const needsEnrichment = bookmarks.filter((b: any) => 
        !b.enriched_at || 
        new Date(b.enriched_at) < new Date(Date.now() - 7 * 24 * 60 * 60 * 1000)
      );
      
      console.log(`📝 ${needsEnrichment.length} bookmarks need enrichment`);
      
      if (needsEnrichment.length > 0) {
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
          
          await this.saveEnrichedBookmarks(enriched);
        }
        
        console.log(`✅ Enriched ${enriched.length} bookmarks`);
        
        // Generate clusters including Twitter threads
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
    // ... (keep existing DocETL logic)
    try {
      const pipelinePath = path.join(__dirname, 'bookmark-delta-docetl.yaml');
      
      try {
        execSync('docetl --version', { stdio: 'ignore' });
      } catch {
        console.log('⚠️  DocETL not found, skipping...');
        return;
      }
      
      console.log('🔄 Running DocETL pipeline...');
      execSync(`docetl run ${pipelinePath}`, { stdio: 'inherit' });
      console.log('✅ DocETL processing complete');
    } catch (error) {
      console.error('❌ DocETL processing failed:', error);
    }
  }
  
  private async generateReports() {
    const stats = await this.etl.getStatistics();
    
    // Load thread data
    let threadData: any = { thread_counts: {} };
    try {
      threadData = JSON.parse(
        await fs.readFile(path.join(this.config.outputDir, 'bookmark-threads.json'), 'utf-8')
      );
    } catch {}
    
    const report = `# Enhanced Bookmark ETL Report
Generated: ${new Date().toISOString()}

## Summary Statistics
- Total Bookmarks: ${stats.totalBookmarks}
- Changes in Last 24h: ${stats.changesLast24h}
- Average Change Frequency: ${stats.averageChangeFrequency.toFixed(2)} changes/month

## Thread Composition
- Conversations: ${threadData.thread_counts.conversations || 0}
- Topics: ${threadData.thread_counts.by_topic || 0}
- Authors: ${threadData.thread_counts.by_author || 0}
- Sources: ${threadData.thread_counts.by_source || 0}

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
- Twitter/Grok conversations: ${threadData.thread_counts.conversations || 0}

## Next Steps
1. Review bookmarks requiring attention
2. Update stale content
3. Fill identified content gaps
4. Process new Twitter/Grok conversations
5. Schedule next ETL run based on change patterns
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
Enhanced Bookmark Delta ETL Runner with Twitter Integration

Usage: bun run-bookmark-etl-with-twitter.ts [options] <source-files...>

Options:
  --no-ai          Disable AI enrichment
  --no-docetl      Disable DocETL processing
  --no-twitter     Disable Twitter/Grok integration
  --twitter <user> Fetch timeline for specific Twitter user
  --output <dir>   Output directory (default: ./bookmark-delta-data)
  --content        Include webpage content fetching
  --social         Include social signal analysis
  --temporal       Include temporal analysis
  --batch <size>   AI enrichment batch size (default: 10)
  
Examples:
  bun run-bookmark-etl-with-twitter.ts bookmarks.json
  bun run-bookmark-etl-with-twitter.ts --twitter elonmusk *.json
  bun run-bookmark-etl-with-twitter.ts --output ./data --content bookmarks.csv
`);
    process.exit(0);
  }
  
  // Parse arguments
  const sources: string[] = [];
  const config: Partial<ETLConfig> = {
    enrichmentOptions: {},
    enableTwitter: true
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
      case '--no-twitter':
        config.enableTwitter = false;
        break;
      case '--twitter':
        config.twitterUsername = args[++i];
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
  
  if (sources.length === 0 && !config.twitterUsername) {
    console.error('❌ No source files specified and no Twitter username provided');
    console.log('Run with --help for usage information');
    process.exit(1);
  }
  
  config.sources = sources;
  
  // Run ETL
  const runner = new EnhancedBookmarkETLRunner(config as ETLConfig);
  await runner.run();
}

// Run if main
if (import.meta.main) {
  main().catch(console.error);
}