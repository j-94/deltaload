import { z } from 'zod';
import * as fs from 'fs/promises';
import * as path from 'path';
import { createHash } from 'crypto';
import { CompleteBookmark, flattenBookmarkMetadata, extractSourceMetadata } from './enhanced-bookmark-schema';

// Delta Load interfaces based on j-94/deltaload patterns
interface DeltaLoadState {
  lastProcessedAt: string;
  lastProcessedId: string;
  processedHashes: Set<string>;
  totalProcessed: number;
  lastSnapshot: string;
}

interface DeltaChange {
  type: 'added' | 'modified' | 'deleted';
  id: string;
  hash: string;
  timestamp: string;
  data?: any;
}

// Enhanced bookmark schema with flexible typing
const enhancedBookmarkSchema = z.object({
  // Core fields
  id: z.string(),
  url: z.string(),
  title: z.string(),
  description: z.string(),
  
  // Temporal data
  created_at: z.string(),
  updated_at: z.string(),
  last_accessed: z.string().optional(),
  access_count: z.number().default(0),
  
  // Content analysis
  content_hash: z.string(),
  content_length: z.number(),
  reading_time: z.number(), // in minutes
  language: z.string(),
  
  // Metadata extraction - flexible to handle all data types
  meta_tags: z.record(z.any()),
  open_graph: z.object({
    title: z.string().optional(),
    description: z.string().optional(),
    image: z.string().optional(),
    type: z.string().optional(),
  }).optional(),
  
  // Technical details
  response_time: z.number(), // ms
  ssl_valid: z.boolean(),
  mobile_friendly: z.boolean(),
  
  // AI enrichment
  categories: z.array(z.string()),
  sentiment: z.number(), // -1 to 1
  readability_score: z.number(), // 0 to 100
  key_topics: z.array(z.string()),
  
  // Social signals
  social_shares: z.object({
    twitter: z.number().optional(),
    linkedin: z.number().optional(),
    reddit: z.number().optional(),
  }).optional(),
  
  // Delta tracking
  change_frequency: z.number(), // changes per month
  content_stability: z.number(), // 0 to 1
  last_delta_hash: z.string(),
});

type EnhancedBookmark = z.infer<typeof enhancedBookmarkSchema>;

export class BookmarkDeltaETL {
  private stateFile: string;
  private state: DeltaLoadState;
  private dataDir: string;
  
  constructor(dataDir: string = './bookmark-data') {
    this.dataDir = dataDir;
    this.stateFile = path.join(dataDir, 'delta-state.json');
    this.state = {
      lastProcessedAt: new Date().toISOString(),
      lastProcessedId: '',
      processedHashes: new Set(),
      totalProcessed: 0,
      lastSnapshot: '',
    };
  }
  
  // Initialize delta load state
  async initialize() {
    await fs.mkdir(this.dataDir, { recursive: true });
    
    try {
      const stateData = await fs.readFile(this.stateFile, 'utf-8');
      const parsed = JSON.parse(stateData);
      this.state = {
        ...parsed,
        processedHashes: new Set(parsed.processedHashes || []),
      };
    } catch (error) {
      console.log('Initializing new delta state');
      await this.saveState();
    }
  }
  
  // Save current state
  private async saveState() {
    const stateToSave = {
      ...this.state,
      processedHashes: Array.from(this.state.processedHashes),
    };
    await fs.writeFile(this.stateFile, JSON.stringify(stateToSave, null, 2));
  }
  
  // Generate hash for change detection
  private generateHash(bookmark: any): string {
    // Include all relevant fields for comprehensive change detection
    const relevantData = {
      url: bookmark.url,
      title: bookmark.title || bookmark.metadata?.title,
      description: bookmark.description || bookmark.metadata?.description,
      content_length: bookmark.content?.length || bookmark.metadata?.word_count,
      source_specific: bookmark.source === 'github' 
        ? bookmark.metadata?.stars + bookmark.metadata?.forks
        : bookmark.source === 'twitter'
        ? bookmark.metadata?.tweet_metrics
        : bookmark.metadata?.tags
    };
    return createHash('sha256').update(JSON.stringify(relevantData)).digest('hex');
  }
  
  // Extract phase: Get bookmarks from various sources
  async extract(sources: string[]): Promise<any[]> {
    const bookmarks: any[] = [];
    
    for (const source of sources) {
      if (source.endsWith('.json') || source.endsWith('.jsonl')) {
        const data = await fs.readFile(source, 'utf-8');
        
        if (source.endsWith('.jsonl')) {
          // Handle JSONL format
          const lines = data.trim().split('\n');
          for (const line of lines) {
            if (line) {
              try {
                bookmarks.push(JSON.parse(line));
              } catch (e) {
                console.error('Error parsing JSONL line:', e);
              }
            }
          }
        } else {
          // Handle regular JSON
          const parsed = JSON.parse(data);
          bookmarks.push(...(Array.isArray(parsed) ? parsed : [parsed]));
        }
      } else if (source.endsWith('.csv')) {
        // Handle CSV extraction
        console.log('CSV format not yet implemented');
      }
    }
    
    return bookmarks;
  }
  
  // Transform phase: Enrich and transform bookmarks
  async transform(bookmarks: any[]): Promise<EnhancedBookmark[]> {
    const transformed: EnhancedBookmark[] = [];
    
    for (const bookmark of bookmarks) {
      try {
        // Extract all metadata fields
        const flattened = flattenBookmarkMetadata(bookmark);
        const { source, sourceMetadata } = extractSourceMetadata(bookmark);
        
        // Parse metadata if it's a string
        let metadata = bookmark.metadata;
        if (typeof metadata === 'string') {
          try {
            metadata = JSON.parse(metadata);
          } catch (e) {
            metadata = {};
          }
        }
        
        // Basic transformation with all fields
        const enhanced: Partial<EnhancedBookmark> = {
          id: String(bookmark.id || this.generateId(bookmark.url)),
          url: bookmark.url,
          title: metadata?.title || bookmark.title || bookmark.name || '',
          description: metadata?.description || bookmark.description || '',
          
          // Temporal data
          created_at: bookmark.created_at || metadata?.created_at || new Date().toISOString(),
          updated_at: metadata?.updated_at || new Date().toISOString(),
          access_count: bookmark.access_count || 0,
          
          // Content analysis
          content_hash: this.generateHash(bookmark),
          content_length: bookmark.content?.length || metadata?.word_count || 0,
          reading_time: metadata?.read_time || this.calculateReadingTime(bookmark.content || ''),
          language: metadata?.lang || metadata?.language || 'en',
          
          // Metadata - including all discovered fields
          meta_tags: {
            ...metadata,
            source: bookmark.source,
            sourceMetadata: sourceMetadata,
            opengraph: metadata?.opengraph,
            twitter_card: metadata?.twitter_card,
            processed_with: metadata?.processed_with,
            processing_error: bookmark.processing_error
          },
          
          // Technical details
          response_time: 0,
          ssl_valid: bookmark.url?.startsWith('https://') || false,
          mobile_friendly: true, // Would need actual check
          
          // AI enrichment (would be done by AI service)
          categories: metadata?.tags || bookmark.categories || [],
          sentiment: 0,
          readability_score: this.calculateReadability(bookmark.content || ''),
          key_topics: [],
          
          // Social signals from metadata
          social_shares: {
            twitter: metadata?.tweet_metrics?.retweets || metadata?.retweet_count || 0,
            linkedin: 0,
            reddit: 0,
          },
          
          // Delta tracking
          change_frequency: 0,
          content_stability: 1,
          last_delta_hash: this.generateHash(bookmark),
        };
        
        // Add source-specific fields
        if (source === 'github' && metadata) {
          enhanced.meta_tags.github_data = {
            stars: metadata.stars,
            forks: metadata.forks,
            watchers: metadata.watchers,
            open_issues: metadata.open_issues,
            has_readme: metadata.has_readme,
            readme_content: metadata.github_readme
          };
        } else if (source === 'twitter' && metadata) {
          enhanced.meta_tags.twitter_data = {
            tweet_count: metadata.tweet_count,
            tweet_metrics: metadata.tweet_metrics,
            user_followers: metadata.user_followers,
            user_verified: metadata.user_verified
          };
        }
        
        // Validate and add
        const validated = enhancedBookmarkSchema.parse(enhanced);
        transformed.push(validated);
      } catch (error) {
        console.error(`Error transforming bookmark ${bookmark.url}:`, error);
      }
    }
    
    return transformed;
  }
  
  // Load phase: Store bookmarks with delta tracking
  async load(bookmarks: EnhancedBookmark[]): Promise<DeltaChange[]> {
    const changes: DeltaChange[] = [];
    const timestamp = new Date().toISOString();
    
    // Load existing data
    const existingFile = path.join(this.dataDir, 'bookmarks.json');
    let existingBookmarks: Map<string, EnhancedBookmark> = new Map();
    
    try {
      const existingData = await fs.readFile(existingFile, 'utf-8');
      const parsed = JSON.parse(existingData);
      parsed.forEach((b: EnhancedBookmark) => existingBookmarks.set(b.id, b));
    } catch (error) {
      console.log('No existing bookmarks found');
    }
    
    // Process each bookmark
    for (const bookmark of bookmarks) {
      const hash = this.generateHash(bookmark);
      const existing = existingBookmarks.get(bookmark.id);
      
      if (!existing) {
        // New bookmark
        changes.push({
          type: 'added',
          id: bookmark.id,
          hash: hash,
          timestamp: timestamp,
          data: bookmark,
        });
        existingBookmarks.set(bookmark.id, bookmark);
        this.state.processedHashes.add(hash);
      } else if (existing.last_delta_hash !== hash) {
        // Modified bookmark
        changes.push({
          type: 'modified',
          id: bookmark.id,
          hash: hash,
          timestamp: timestamp,
          data: bookmark,
        });
        existingBookmarks.set(bookmark.id, {
          ...bookmark,
          change_frequency: (existing.change_frequency || 0) + 1,
          content_stability: this.calculateStability(existing, bookmark),
        });
        this.state.processedHashes.add(hash);
      }
    }
    
    // Check for deletions
    for (const [id, existing] of existingBookmarks) {
      if (!bookmarks.find(b => b.id === id)) {
        changes.push({
          type: 'deleted',
          id: id,
          hash: existing.last_delta_hash,
          timestamp: timestamp,
        });
        existingBookmarks.delete(id);
      }
    }
    
    // Save updated bookmarks
    await fs.writeFile(
      existingFile,
      JSON.stringify(Array.from(existingBookmarks.values()), null, 2)
    );
    
    // Save changes log
    if (changes.length > 0) {
      const changesFile = path.join(
        this.dataDir,
        `changes-${timestamp.replace(/:/g, '-')}.json`
      );
      await fs.writeFile(changesFile, JSON.stringify(changes, null, 2));
    }
    
    // Update state
    this.state.lastProcessedAt = timestamp;
    this.state.totalProcessed += bookmarks.length;
    await this.saveState();
    
    return changes;
  }
  
  // Run full ETL pipeline
  async runETL(sources: string[]): Promise<{
    processed: number;
    changes: DeltaChange[];
    duration: number;
  }> {
    const startTime = Date.now();
    
    await this.initialize();
    
    console.log('🔄 Starting Delta ETL Pipeline');
    console.log(`📅 Last run: ${this.state.lastProcessedAt}`);
    
    // Extract
    console.log('📥 Extracting bookmarks...');
    const rawBookmarks = await this.extract(sources);
    console.log(`   Found ${rawBookmarks.length} bookmarks`);
    
    // Transform
    console.log('🔄 Transforming bookmarks...');
    const transformed = await this.transform(rawBookmarks);
    console.log(`   Transformed ${transformed.length} bookmarks`);
    
    // Load
    console.log('📤 Loading bookmarks...');
    const changes = await this.load(transformed);
    console.log(`   Detected ${changes.length} changes`);
    
    const duration = Date.now() - startTime;
    console.log(`✅ ETL completed in ${duration}ms`);
    
    return {
      processed: transformed.length,
      changes: changes,
      duration: duration,
    };
  }
  
  // Utility functions
  private generateId(url: string): string {
    return createHash('md5').update(url).digest('hex').substring(0, 12);
  }
  
  private calculateReadingTime(content: string): number {
    const wordsPerMinute = 200;
    const wordCount = content.split(/\s+/).length;
    return Math.ceil(wordCount / wordsPerMinute);
  }
  
  private calculateReadability(content: string): number {
    // Simple readability score (0-100)
    const avgWordLength = content.length / content.split(/\s+/).length;
    const avgSentenceLength = content.split(/[.!?]+/).length;
    return Math.max(0, Math.min(100, 100 - (avgWordLength * 2 + avgSentenceLength)));
  }
  
  private calculateStability(old: EnhancedBookmark, new_: EnhancedBookmark): number {
    // Calculate content stability (0-1)
    const titleChanged = old.title !== new_.title ? 0.2 : 0;
    const descChanged = old.description !== new_.description ? 0.3 : 0;
    const contentChanged = old.content_hash !== new_.content_hash ? 0.5 : 0;
    
    return Math.max(0, 1 - (titleChanged + descChanged + contentChanged));
  }
  
  // Generate snapshot for recovery
  async createSnapshot(): Promise<string> {
    const timestamp = new Date().toISOString();
    const snapshotFile = path.join(
      this.dataDir,
      `snapshot-${timestamp.replace(/:/g, '-')}.json`
    );
    
    const bookmarksFile = path.join(this.dataDir, 'bookmarks.json');
    const bookmarks = await fs.readFile(bookmarksFile, 'utf-8');
    
    const snapshot = {
      timestamp: timestamp,
      state: this.state,
      bookmarks: JSON.parse(bookmarks),
    };
    
    await fs.writeFile(snapshotFile, JSON.stringify(snapshot, null, 2));
    
    this.state.lastSnapshot = snapshotFile;
    await this.saveState();
    
    return snapshotFile;
  }
  
  // Get delta statistics
  async getStatistics(): Promise<{
    totalBookmarks: number;
    changesLast24h: number;
    averageChangeFrequency: number;
    mostChanged: EnhancedBookmark[];
    mostStable: EnhancedBookmark[];
  }> {
    const bookmarksFile = path.join(this.dataDir, 'bookmarks.json');
    const bookmarks: EnhancedBookmark[] = JSON.parse(
      await fs.readFile(bookmarksFile, 'utf-8')
    );
    
    const last24h = new Date();
    last24h.setDate(last24h.getDate() - 1);
    
    const recentChanges = bookmarks.filter(
      b => new Date(b.updated_at) > last24h
    ).length;
    
    const avgChangeFreq = bookmarks.reduce(
      (sum, b) => sum + (b.change_frequency || 0), 0
    ) / bookmarks.length;
    
    const sorted = [...bookmarks].sort(
      (a, b) => (b.change_frequency || 0) - (a.change_frequency || 0)
    );
    
    return {
      totalBookmarks: bookmarks.length,
      changesLast24h: recentChanges,
      averageChangeFrequency: avgChangeFreq,
      mostChanged: sorted.slice(0, 5),
      mostStable: sorted.slice(-5).reverse(),
    };
  }
}

// Example usage
if (import.meta.main) {
  const etl = new BookmarkDeltaETL('./bookmark-delta-data');
  
  // Run ETL with your bookmark sources
  const sources = [
    'bookmarks.json',
    'test_output.json',
    // Add more sources
  ];
  
  const result = await etl.runETL(sources);
  console.log('\n📊 ETL Results:', result);
  
  // Get statistics
  const stats = await etl.getStatistics();
  console.log('\n📈 Statistics:', stats);
  
  // Create snapshot
  const snapshot = await etl.createSnapshot();
  console.log('\n💾 Snapshot created:', snapshot);
}