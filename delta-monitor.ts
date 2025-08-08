#!/usr/bin/env bun

import { BookmarkDeltaETL } from './delta-load-pipeline';
import * as fs from 'fs/promises';
import * as path from 'path';

class DeltaMonitor {
  private dataDir: string;
  
  constructor(dataDir: string = './bookmark-delta-data') {
    this.dataDir = dataDir;
  }
  
  async getStatus(): Promise<any> {
    const etl = new BookmarkDeltaETL(this.dataDir);
    const stats = await etl.getStatistics();
    
    // Load delta state
    const stateFile = path.join(this.dataDir, 'delta-state.json');
    const state = JSON.parse(await fs.readFile(stateFile, 'utf-8'));
    
    // Get recent changes
    const changesDir = this.dataDir;
    const files = await fs.readdir(changesDir);
    const changeFiles = files.filter(f => f.startsWith('changes-')).sort().reverse();
    
    const recentChanges = [];
    for (const file of changeFiles.slice(0, 5)) {
      const changes = JSON.parse(await fs.readFile(path.join(changesDir, file), 'utf-8'));
      recentChanges.push({
        file,
        timestamp: changes[0]?.timestamp,
        count: changes.length,
        types: changes.reduce((acc: any, c: any) => {
          acc[c.type] = (acc[c.type] || 0) + 1;
          return acc;
        }, {})
      });
    }
    
    // Source breakdown
    const bookmarksFile = path.join(this.dataDir, 'bookmarks.json');
    const bookmarks = JSON.parse(await fs.readFile(bookmarksFile, 'utf-8'));
    const sourceBreakdown = bookmarks.reduce((acc: any, b: any) => {
      const source = b.source || b.meta_tags?.source || 'unknown';
      acc[source] = (acc[source] || 0) + 1;
      return acc;
    }, {});
    
    // Enrichment status
    const enrichedCount = bookmarks.filter((b: any) => b.enriched_at).length;
    const needsEnrichment = bookmarks.filter((b: any) => 
      !b.enriched_at || 
      new Date(b.enriched_at) < new Date(Date.now() - 7 * 24 * 60 * 60 * 1000)
    ).length;
    
    return {
      overview: {
        totalBookmarks: stats.totalBookmarks,
        lastProcessed: state.lastProcessedAt,
        totalProcessed: state.totalProcessed,
        lastSnapshot: state.lastSnapshot
      },
      activity: {
        changesLast24h: stats.changesLast24h,
        averageChangeFrequency: stats.averageChangeFrequency,
        recentChanges
      },
      sources: sourceBreakdown,
      enrichment: {
        enriched: enrichedCount,
        needsEnrichment,
        percentage: Math.round((enrichedCount / stats.totalBookmarks) * 100)
      },
      trending: {
        mostChanged: stats.mostChanged.slice(0, 5),
        mostStable: stats.mostStable.slice(0, 5)
      }
    };
  }
  
  async displayDashboard() {
    const status = await this.getStatus();
    
    console.clear();
    console.log('📊 Bookmark Delta Load Monitor');
    console.log('==============================\n');
    
    // Overview
    console.log('📈 Overview');
    console.log(`  Total Bookmarks: ${status.overview.totalBookmarks.toLocaleString()}`);
    console.log(`  Last Processed: ${new Date(status.overview.lastProcessed).toLocaleString()}`);
    console.log(`  Total Processed: ${status.overview.totalProcessed.toLocaleString()}`);
    
    // Activity
    console.log('\n🔄 Activity');
    console.log(`  Changes (24h): ${status.activity.changesLast24h}`);
    console.log(`  Avg Change Rate: ${status.activity.averageChangeFrequency.toFixed(2)}/month`);
    
    // Recent changes
    if (status.activity.recentChanges.length > 0) {
      console.log('\n  Recent Changes:');
      status.activity.recentChanges.forEach((change: any) => {
        const time = new Date(change.timestamp).toLocaleString();
        const types = Object.entries(change.types)
          .map(([type, count]) => `${type}: ${count}`)
          .join(', ');
        console.log(`    ${time} - ${types}`);
      });
    }
    
    // Sources
    console.log('\n📚 Sources');
    Object.entries(status.sources).forEach(([source, count]) => {
      console.log(`  ${source}: ${count} bookmarks`);
    });
    
    // Enrichment
    console.log('\n🤖 AI Enrichment');
    console.log(`  Enriched: ${status.enrichment.enriched}/${status.overview.totalBookmarks} (${status.enrichment.percentage}%)`);
    console.log(`  Needs Update: ${status.enrichment.needsEnrichment}`);
    
    // Trending
    console.log('\n🔥 Most Active Bookmarks');
    status.trending.mostChanged.forEach((b: any, i: number) => {
      console.log(`  ${i + 1}. ${b.title || b.url}`);
      console.log(`     Changes: ${b.change_frequency}, Stability: ${b.content_stability.toFixed(2)}`);
    });
    
    console.log('\n🏔️  Most Stable References');
    status.trending.mostStable.forEach((b: any, i: number) => {
      console.log(`  ${i + 1}. ${b.title || b.url}`);
      console.log(`     Stability: ${b.content_stability.toFixed(2)}`);
    });
    
    // Footer
    console.log('\n' + '─'.repeat(50));
    console.log('Updated:', new Date().toLocaleString());
  }
  
  async watch(intervalSeconds: number = 30) {
    // Initial display
    await this.displayDashboard();
    
    // Update regularly
    setInterval(async () => {
      try {
        await this.displayDashboard();
      } catch (error) {
        console.error('Error updating dashboard:', error);
      }
    }, intervalSeconds * 1000);
  }
  
  async exportReport(filename: string) {
    const status = await this.getStatus();
    const report = {
      generated: new Date().toISOString(),
      ...status
    };
    
    await fs.writeFile(filename, JSON.stringify(report, null, 2));
    console.log(`✅ Report exported to ${filename}`);
  }
}

// CLI usage
async function main() {
  const args = process.argv.slice(2);
  const command = args[0] || 'dashboard';
  const dataDir = args[1] || './bookmark-delta-data';
  
  const monitor = new DeltaMonitor(dataDir);
  
  switch (command) {
    case 'dashboard':
      await monitor.displayDashboard();
      break;
      
    case 'watch':
      const interval = parseInt(args[1]) || 30;
      console.log(`Watching with ${interval}s refresh...`);
      await monitor.watch(interval);
      break;
      
    case 'export':
      const filename = args[1] || `delta-report-${Date.now()}.json`;
      await monitor.exportReport(filename);
      break;
      
    case 'status':
      const status = await monitor.getStatus();
      console.log(JSON.stringify(status, null, 2));
      break;
      
    default:
      console.log(`
Bookmark Delta Monitor

Usage:
  bun run delta-monitor.ts [command] [options]

Commands:
  dashboard    Show current status (default)
  watch [sec]  Auto-refresh dashboard
  export [file] Export status report
  status       Output raw JSON status

Examples:
  bun run delta-monitor.ts
  bun run delta-monitor.ts watch 60
  bun run delta-monitor.ts export report.json
      `);
  }
}

if (import.meta.main) {
  main().catch(console.error);
}

export { DeltaMonitor };