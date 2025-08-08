#!/usr/bin/env bun

import * as fs from 'fs/promises';

interface RaindropConfig {
  apiKey: string;
  collectionId?: string; // 0 for all, or specific collection ID
  perpage?: number;
}

class RaindropFetcher {
  private config: RaindropConfig;
  private baseUrl = 'https://api.raindrop.io/rest/v1';
  
  constructor(config: RaindropConfig) {
    this.config = {
      collectionId: '0', // All bookmarks
      perpage: 50,
      ...config
    };
  }
  
  async fetchAllBookmarks(): Promise<any[]> {
    const bookmarks: any[] = [];
    let page = 0;
    let hasMore = true;
    
    console.log('🌧️  Fetching Raindrop.io bookmarks...');
    
    while (hasMore) {
      const response = await fetch(
        `${this.baseUrl}/raindrops/${this.config.collectionId}?perpage=${this.config.perpage}&page=${page}`,
        {
          headers: {
            'Authorization': `Bearer ${this.config.apiKey}`
          }
        }
      );
      
      if (!response.ok) {
        throw new Error(`Raindrop API error: ${response.status} ${response.statusText}`);
      }
      
      const data = await response.json();
      const items = data.items || [];
      
      // Transform to our format
      const transformed = items.map((item: any) => ({
        id: `raindrop-${item._id}`,
        url: item.link,
        title: item.title,
        content: item.excerpt,
        description: item.excerpt,
        created_at: item.created,
        source: 'raindrop',
        metadata: {
          // Core Raindrop fields
          title: item.title,
          description: item.excerpt,
          domain: item.domain,
          created_at: item.created,
          updated_at: item.lastUpdate,
          
          // Organization
          folder: item.collection?.$id,
          tags: item.tags || [],
          favorite: item.important || false,
          
          // Media
          cover: item.cover,
          media: item.media || [],
          type: item.type,
          
          // Additional metadata
          highlights: item.highlights || [],
          annotations: item.note || '',
          
          // Raindrop specific
          raindrop_id: item._id,
          user_id: item.user?.$id,
          broken: item.broken || false,
          cache: item.cache,
          
          // Preserve all original data
          ...item
        }
      }));
      
      bookmarks.push(...transformed);
      console.log(`  Fetched page ${page + 1}: ${items.length} bookmarks (total: ${bookmarks.length})`);
      
      // Check if there are more pages
      hasMore = items.length === this.config.perpage;
      page++;
      
      // Rate limiting
      if (hasMore) {
        await new Promise(resolve => setTimeout(resolve, 500));
      }
    }
    
    return bookmarks;
  }
  
  async fetchCollections(): Promise<any[]> {
    const response = await fetch(`${this.baseUrl}/collections`, {
      headers: {
        'Authorization': `Bearer ${this.config.apiKey}`
      }
    });
    
    if (!response.ok) {
      throw new Error(`Failed to fetch collections: ${response.status}`);
    }
    
    const data = await response.json();
    return data.items || [];
  }
  
  async exportToFile(filename: string): Promise<void> {
    try {
      const bookmarks = await this.fetchAllBookmarks();
      await fs.writeFile(filename, JSON.stringify(bookmarks, null, 2));
      
      console.log(`\n✅ Exported ${bookmarks.length} bookmarks to ${filename}`);
      
      // Summary statistics
      const stats = {
        total: bookmarks.length,
        favorites: bookmarks.filter(b => b.metadata.favorite).length,
        withTags: bookmarks.filter(b => b.metadata.tags.length > 0).length,
        withCover: bookmarks.filter(b => b.metadata.cover).length,
        broken: bookmarks.filter(b => b.metadata.broken).length
      };
      
      console.log('\n📊 Summary:');
      console.log(`  Total bookmarks: ${stats.total}`);
      console.log(`  Favorites: ${stats.favorites}`);
      console.log(`  With tags: ${stats.withTags}`);
      console.log(`  With cover: ${stats.withCover}`);
      console.log(`  Broken links: ${stats.broken}`);
      
    } catch (error) {
      console.error('❌ Export failed:', error);
      throw error;
    }
  }
}

// CLI usage
async function main() {
  const apiKey = process.env.RAINDROP_API_KEY;
  
  if (!apiKey) {
    console.error('❌ Please set RAINDROP_API_KEY environment variable');
    console.log('\nUsage:');
    console.log('  export RAINDROP_API_KEY=your_api_key');
    console.log('  bun run raindrop-fetcher.ts [output.json]');
    process.exit(1);
  }
  
  const outputFile = process.argv[2] || `raindrop-export-${new Date().toISOString().split('T')[0]}.json`;
  
  const fetcher = new RaindropFetcher({ apiKey });
  await fetcher.exportToFile(outputFile);
}

if (import.meta.main) {
  main().catch(console.error);
}

export { RaindropFetcher };