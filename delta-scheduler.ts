#!/usr/bin/env bun

import { BookmarkDeltaETL } from './delta-load-pipeline';
import { AIBookmarkEnricher } from './ai-sdk-bookmark-enricher';
import { RaindropFetcher } from './fetchers/raindrop-fetcher';
import { GitHubFetcher } from './fetchers/github-fetcher';
import * as fs from 'fs/promises';
import * as path from 'path';

interface SchedulerConfig {
  sources: {
    raindrop?: { enabled: boolean; apiKey?: string };
    github?: { enabled: boolean; token?: string };
    twitter?: { enabled: boolean; bearerToken?: string };
    local?: { enabled: boolean; paths: string[] };
  };
  schedule: {
    fetchInterval: number; // minutes
    enrichInterval: number; // minutes
    cleanupDays: number; // days to keep old data
  };
  etl: {
    dataDir: string;
    enableAI: boolean;
    aiOptions?: {
      batchSize: number;
      includeContent: boolean;
      includeSocial: boolean;
      includeTemporal: boolean;
    };
  };
}

class DeltaScheduler {
  private config: SchedulerConfig;
  private etl: BookmarkDeltaETL;
  private enricher: AIBookmarkEnricher;
  private isRunning = false;
  
  constructor(config: SchedulerConfig) {
    this.config = config;
    this.etl = new BookmarkDeltaETL(config.etl.dataDir);
    this.enricher = new AIBookmarkEnricher(this.etl);
  }
  
  async start() {
    console.log('🚀 Starting Delta Load Scheduler');
    console.log(`📅 Fetch interval: ${this.config.schedule.fetchInterval} minutes`);
    console.log(`🤖 AI enrichment: ${this.config.etl.enableAI ? 'Enabled' : 'Disabled'}\n`);
    
    // Initial run
    await this.runDeltaLoad();
    
    // Schedule regular runs
    setInterval(() => this.runDeltaLoad(), this.config.schedule.fetchInterval * 60 * 1000);
    
    // Schedule cleanup
    setInterval(() => this.cleanup(), 24 * 60 * 60 * 1000); // Daily
  }
  
  async runDeltaLoad() {
    if (this.isRunning) {
      console.log('⏳ Previous delta load still running, skipping...');
      return;
    }
    
    this.isRunning = true;
    const startTime = Date.now();
    console.log(`\n🔄 Starting delta load at ${new Date().toISOString()}`);
    
    try {
      // Step 1: Fetch new data from all sources
      const sources = await this.fetchAllSources();
      
      if (sources.length === 0) {
        console.log('⚠️  No sources to process');
        return;
      }
      
      // Step 2: Run delta ETL
      console.log('\n📊 Running delta ETL...');
      const result = await this.etl.runETL(sources);
      
      console.log(`✅ Delta ETL complete:`);
      console.log(`   - Processed: ${result.processed} bookmarks`);
      console.log(`   - Changes: ${result.changes.length}`);
      console.log(`   - Duration: ${result.duration}ms`);
      
      // Step 3: AI Enrichment (if enabled and there are changes)
      if (this.config.etl.enableAI && result.changes.length > 0) {
        console.log('\n🤖 Running AI enrichment for changed bookmarks...');
        await this.enrichChangedBookmarks(result.changes);
      }
      
      // Step 4: Generate report
      await this.generateDeltaReport(result);
      
      const totalTime = Date.now() - startTime;
      console.log(`\n✨ Delta load completed in ${Math.round(totalTime / 1000)}s`);
      
    } catch (error) {
      console.error('❌ Delta load failed:', error);
    } finally {
      this.isRunning = false;
    }
  }
  
  async fetchAllSources(): Promise<string[]> {
    const sources: string[] = [];
    const dataDir = path.join(this.config.etl.dataDir, 'sources');
    await fs.mkdir(dataDir, { recursive: true });
    
    // Fetch from Raindrop
    if (this.config.sources.raindrop?.enabled) {
      try {
        console.log('🌧️  Fetching from Raindrop.io...');
        const apiKey = this.config.sources.raindrop.apiKey || process.env.RAINDROP_API_KEY;
        if (apiKey) {
          const fetcher = new RaindropFetcher({ apiKey });
          const filename = path.join(dataDir, `raindrop-${Date.now()}.json`);
          await fetcher.exportToFile(filename);
          sources.push(filename);
        }
      } catch (error) {
        console.error('❌ Raindrop fetch failed:', error);
      }
    }
    
    // Fetch from GitHub
    if (this.config.sources.github?.enabled) {
      try {
        console.log('⭐ Fetching from GitHub...');
        const token = this.config.sources.github.token || process.env.GITHUB_TOKEN;
        if (token) {
          const fetcher = new GitHubFetcher({ token });
          const filename = path.join(dataDir, `github-${Date.now()}.json`);
          await fetcher.exportToFile(filename);
          sources.push(filename);
        }
      } catch (error) {
        console.error('❌ GitHub fetch failed:', error);
      }
    }
    
    // Add local sources
    if (this.config.sources.local?.enabled) {
      for (const localPath of this.config.sources.local.paths) {
        try {
          await fs.access(localPath);
          sources.push(localPath);
          console.log(`📁 Added local source: ${localPath}`);
        } catch {
          console.warn(`⚠️  Local source not found: ${localPath}`);
        }
      }
    }
    
    return sources;
  }
  
  async enrichChangedBookmarks(changes: any[]) {
    // Load current bookmarks
    const bookmarksFile = path.join(this.config.etl.dataDir, 'bookmarks.json');
    const allBookmarks = JSON.parse(await fs.readFile(bookmarksFile, 'utf-8'));
    
    // Get bookmarks that changed
    const changedIds = new Set(changes.map(c => c.id));
    const toEnrich = allBookmarks.filter((b: any) => changedIds.has(b.id));
    
    if (toEnrich.length === 0) return;
    
    console.log(`🧪 Enriching ${toEnrich.length} changed bookmarks...`);
    
    const enriched = await this.enricher.enrichBookmarkBatch(
      toEnrich,
      this.config.etl.aiOptions
    );
    
    // Update bookmarks with enriched data
    const bookmarkMap = new Map(allBookmarks.map((b: any) => [b.id, b]));
    enriched.forEach(e => bookmarkMap.set(e.id, e));
    
    await fs.writeFile(
      bookmarksFile,
      JSON.stringify(Array.from(bookmarkMap.values()), null, 2)
    );
    
    console.log(`✅ Enriched ${enriched.length} bookmarks`);
  }
  
  async generateDeltaReport(result: any) {
    const reportDir = path.join(this.config.etl.dataDir, 'reports');
    await fs.mkdir(reportDir, { recursive: true });
    
    const report = {
      timestamp: new Date().toISOString(),
      processed: result.processed,
      changes: result.changes.length,
      duration: result.duration,
      changeDetails: result.changes.map((c: any) => ({
        type: c.type,
        id: c.id,
        timestamp: c.timestamp
      }))
    };
    
    const reportFile = path.join(
      reportDir,
      `delta-report-${new Date().toISOString().split('T')[0]}.json`
    );
    
    await fs.writeFile(reportFile, JSON.stringify(report, null, 2));
  }
  
  async cleanup() {
    console.log('🧹 Running cleanup...');
    
    const cutoffDate = new Date();
    cutoffDate.setDate(cutoffDate.getDate() - this.config.schedule.cleanupDays);
    
    // Clean old source files
    const sourceDir = path.join(this.config.etl.dataDir, 'sources');
    try {
      const files = await fs.readdir(sourceDir);
      for (const file of files) {
        const filePath = path.join(sourceDir, file);
        const stats = await fs.stat(filePath);
        if (stats.mtime < cutoffDate) {
          await fs.unlink(filePath);
          console.log(`  Deleted old source: ${file}`);
        }
      }
    } catch (error) {
      // Source dir might not exist
    }
    
    // Clean old change logs
    const changeFiles = await fs.readdir(this.config.etl.dataDir);
    const changePattern = /^changes-.*\.json$/;
    for (const file of changeFiles) {
      if (changePattern.test(file)) {
        const filePath = path.join(this.config.etl.dataDir, file);
        const stats = await fs.stat(filePath);
        if (stats.mtime < cutoffDate) {
          await fs.unlink(filePath);
          console.log(`  Deleted old changes: ${file}`);
        }
      }
    }
  }
}

// Configuration
const defaultConfig: SchedulerConfig = {
  sources: {
    raindrop: { enabled: true },
    github: { enabled: true },
    local: { 
      enabled: true,
      paths: ['./manual-bookmarks.json']
    }
  },
  schedule: {
    fetchInterval: 60, // Every hour
    enrichInterval: 120, // Every 2 hours
    cleanupDays: 30 // Keep 30 days of history
  },
  etl: {
    dataDir: './bookmark-delta-data',
    enableAI: true,
    aiOptions: {
      batchSize: 10,
      includeContent: false,
      includeSocial: true,
      includeTemporal: true
    }
  }
};

// CLI usage
async function main() {
  console.log('📚 Bookmark Delta Load Scheduler');
  console.log('================================\n');
  
  // Load config from file if exists
  let config = defaultConfig;
  try {
    const configFile = await fs.readFile('./delta-scheduler-config.json', 'utf-8');
    config = { ...defaultConfig, ...JSON.parse(configFile) };
    console.log('✅ Loaded config from delta-scheduler-config.json');
  } catch {
    console.log('ℹ️  Using default configuration');
  }
  
  const scheduler = new DeltaScheduler(config);
  await scheduler.start();
  
  // Keep process running
  console.log('\n👀 Scheduler is running. Press Ctrl+C to stop.\n');
}

if (import.meta.main) {
  main().catch(console.error);
}

export { DeltaScheduler };