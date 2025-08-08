import { generateObject, streamObject } from 'ai';
import { openai } from '@ai-sdk/openai';
import { z } from 'zod';
import * as cheerio from 'cheerio';
import { BookmarkDeltaETL } from './delta-load-pipeline';

// Enrichment schemas
const contentAnalysisSchema = z.object({
  main_topics: z.array(z.string()).min(3).max(10),
  entities: z.array(z.object({
    name: z.string(),
    type: z.enum(['person', 'organization', 'technology', 'concept', 'place']),
    relevance: z.number().min(0).max(1)
  })),
  technical_level: z.enum(['beginner', 'intermediate', 'advanced', 'expert']),
  content_purpose: z.enum(['educational', 'reference', 'news', 'entertainment', 'tool', 'commercial']),
  actionability: z.number().min(0).max(10),
  uniqueness: z.number().min(0).max(10),
  citations_quality: z.number().min(0).max(10),
  bias_indicators: z.array(z.string()),
  recommended_audience: z.array(z.string())
});

const socialSignalsSchema = z.object({
  estimated_shares: z.number(),
  virality_potential: z.number().min(0).max(1),
  controversy_score: z.number().min(0).max(1),
  engagement_prediction: z.enum(['low', 'medium', 'high', 'viral']),
  shareability_factors: z.array(z.string())
});

const temporalAnalysisSchema = z.object({
  content_lifespan: z.enum(['ephemeral', 'short', 'medium', 'long', 'evergreen']),
  peak_relevance_period: z.string(),
  obsolescence_risk: z.number().min(0).max(1),
  update_indicators: z.array(z.string()),
  historical_value: z.boolean()
});

export class AIBookmarkEnricher {
  private etl: BookmarkDeltaETL;
  private model: string;
  
  constructor(etl: BookmarkDeltaETL, model: string = 'gpt-4o-mini') {
    this.etl = etl;
    this.model = model;
  }
  
  // Fetch and analyze webpage content
  async fetchWebpageContent(url: string): Promise<{
    content: string;
    metadata: Record<string, any>;
    metrics: Record<string, any>;
  }> {
    try {
      const startTime = Date.now();
      const response = await fetch(url, {
        headers: {
          'User-Agent': 'Mozilla/5.0 (compatible; BookmarkBot/1.0)'
        },
        signal: AbortSignal.timeout(10000)
      });
      
      const responseTime = Date.now() - startTime;
      const html = await response.text();
      const $ = cheerio.load(html);
      
      // Extract content
      $('script, style').remove();
      const content = $('body').text().replace(/\s+/g, ' ').trim();
      
      // Extract metadata
      const metadata: Record<string, any> = {
        title: $('title').text(),
        description: $('meta[name="description"]').attr('content') || '',
        keywords: $('meta[name="keywords"]').attr('content') || '',
        author: $('meta[name="author"]').attr('content') || '',
        og: {
          title: $('meta[property="og:title"]').attr('content'),
          description: $('meta[property="og:description"]').attr('content'),
          image: $('meta[property="og:image"]').attr('content'),
          type: $('meta[property="og:type"]').attr('content'),
        },
        twitter: {
          card: $('meta[name="twitter:card"]').attr('content'),
          title: $('meta[name="twitter:title"]').attr('content'),
          description: $('meta[name="twitter:description"]').attr('content'),
        }
      };
      
      // Extract metrics
      const metrics = {
        response_time: responseTime,
        content_length: content.length,
        images_count: $('img').length,
        links_count: $('a').length,
        headings_count: $('h1, h2, h3, h4, h5, h6').length,
        ssl_valid: url.startsWith('https://'),
      };
      
      return { content, metadata, metrics };
    } catch (error) {
      console.error(`Error fetching ${url}:`, error);
      return {
        content: '',
        metadata: {},
        metrics: { error: error.message }
      };
    }
  }
  
  // Deep content analysis with AI leveraging all metadata
  async analyzeContent(bookmark: any, content: string): Promise<any> {
    // Parse metadata if needed
    let metadata = bookmark.metadata || bookmark.meta_tags;
    if (typeof metadata === 'string') {
      try {
        metadata = JSON.parse(metadata);
      } catch (e) {
        metadata = {};
      }
    }
    
    // Build rich context from all available fields
    const enrichedContext = {
      url: bookmark.url,
      title: metadata?.title || bookmark.title,
      description: metadata?.description || bookmark.description,
      author: metadata?.author?.name || metadata?.original_author || metadata?.author,
      published: metadata?.published_date || metadata?.created_at,
      language: metadata?.lang || metadata?.language,
      source: bookmark.source,
      
      // GitHub-specific context
      ...(bookmark.source === 'github' && {
        stars: metadata?.stars,
        forks: metadata?.forks,
        readme_preview: metadata?.github_readme?.substring(0, 500),
        programming_language: metadata?.language,
        license: metadata?.license
      }),
      
      // Twitter-specific context
      ...(bookmark.source === 'twitter' && {
        engagement: metadata?.tweet_metrics,
        user_influence: {
          followers: metadata?.user_followers,
          verified: metadata?.user_verified
        },
        thread_context: metadata?.thread_id
      }),
      
      // Content metrics
      word_count: metadata?.word_count,
      read_time: metadata?.read_time,
      has_video: !!metadata?.opengraph?.video || !!metadata?.twitter_card?.player,
      has_structured_data: !!metadata?.json_ld
    };
    
    const { object } = await generateObject({
      model: openai(this.model),
      schema: contentAnalysisSchema,
      prompt: `Analyze this content with full context:

${JSON.stringify(enrichedContext, null, 2)}

Content Sample (first 2000 chars): ${content.substring(0, 2000)}

Provide comprehensive analysis considering:
- Source-specific signals (GitHub stars, Twitter engagement, etc.)
- Content quality indicators from metadata
- Technical depth based on available data
- Audience fit based on platform and metrics`
    });
    
    return object;
  }
  
  // Analyze social signals and virality using actual metrics
  async analyzeSocialSignals(bookmark: any): Promise<any> {
    // Parse metadata
    let metadata = bookmark.metadata || bookmark.meta_tags;
    if (typeof metadata === 'string') {
      try {
        metadata = JSON.parse(metadata);
      } catch (e) {
        metadata = {};
      }
    }
    
    // Extract actual social metrics
    const actualMetrics = {
      twitter: {
        retweets: metadata?.retweet_count || metadata?.tweet_metrics?.retweets || 0,
        likes: metadata?.favorite_count || metadata?.tweet_metrics?.likes || 0,
        replies: metadata?.reply_count || metadata?.tweet_metrics?.replies || 0,
        quotes: metadata?.quote_count || 0,
        user_followers: metadata?.user_followers || metadata?.user?.followers_count || 0,
        user_verified: metadata?.user_verified || metadata?.user?.verified || false
      },
      github: {
        stars: metadata?.stars || 0,
        forks: metadata?.forks || 0,
        watchers: metadata?.watchers || 0,
        issues: metadata?.open_issues || 0
      }
    };
    
    const { object } = await generateObject({
      model: openai(this.model),
      schema: socialSignalsSchema,
      prompt: `Analyze social signals with actual metrics:

URL: ${bookmark.url}
Title: ${metadata?.title || bookmark.title}
Source: ${bookmark.source}
Published: ${metadata?.published_date || bookmark.created_at}

Actual Metrics:
${JSON.stringify(actualMetrics, null, 2)}

Additional Context:
- Has OpenGraph image: ${!!metadata?.opengraph?.image}
- Has Twitter Card: ${!!metadata?.twitter_card}
- Content length: ${metadata?.word_count || 'unknown'} words
- Domain: ${metadata?.domain}

Analyze virality potential based on:
1. Actual engagement metrics (not estimates)
2. Author influence and verification status
3. Content shareability factors
4. Platform-specific viral patterns`
    });
    
    return object;
  }
  
  // Temporal analysis for content lifecycle
  async analyzeTemporalAspects(bookmark: any, changeHistory: any[]): Promise<any> {
    const { object } = await generateObject({
      model: openai(this.model),
      schema: temporalAnalysisSchema,
      prompt: `Analyze temporal aspects of this content:

URL: ${bookmark.url}
Title: ${bookmark.title}
Created: ${bookmark.created_at}
Last Updated: ${bookmark.updated_at}
Change Frequency: ${bookmark.change_frequency}
Content Stability: ${bookmark.content_stability}

Recent Changes: ${changeHistory.slice(0, 5).map(c => `${c.type} at ${c.timestamp}`).join(', ')}

Determine content lifespan, peak relevance, obsolescence risk, and historical value.`
    });
    
    return object;
  }
  
  // Stream enrichment for real-time updates
  async *streamEnrichBookmark(bookmark: any): AsyncGenerator<any> {
    const enrichmentPrompt = `Progressively enrich this bookmark with detailed analysis:

${JSON.stringify(bookmark, null, 2)}

Provide enrichments for: topics, quality, recommendations, and insights.`;

    const { partialObjectStream } = await streamObject({
      model: openai(this.model),
      schema: z.object({
        enrichment_stage: z.string(),
        topics_extracted: z.array(z.string()).optional(),
        quality_assessment: z.object({
          score: z.number(),
          factors: z.array(z.string())
        }).optional(),
        recommendations: z.array(z.string()).optional(),
        key_insights: z.array(z.string()).optional()
      }),
      prompt: enrichmentPrompt
    });
    
    for await (const partial of partialObjectStream) {
      yield partial;
    }
  }
  
  // Batch enrichment with parallel processing
  async enrichBookmarkBatch(bookmarks: any[], options?: {
    parallel?: number;
    includeContent?: boolean;
    includeSocial?: boolean;
    includeTemporal?: boolean;
  }): Promise<any[]> {
    const opts = {
      parallel: 5,
      includeContent: true,
      includeSocial: true,
      includeTemporal: true,
      ...options
    };
    
    const enriched = [];
    
    // Process in batches
    for (let i = 0; i < bookmarks.length; i += opts.parallel) {
      const batch = bookmarks.slice(i, i + opts.parallel);
      
      const batchPromises = batch.map(async (bookmark) => {
        const enrichment: any = { ...bookmark };
        
        try {
          // Fetch content if needed
          if (opts.includeContent && bookmark.url) {
            const { content, metadata, metrics } = await this.fetchWebpageContent(bookmark.url);
            enrichment.fetched_content = content.substring(0, 5000);
            enrichment.webpage_metadata = metadata;
            enrichment.webpage_metrics = metrics;
            
            // Analyze content
            const contentAnalysis = await this.analyzeContent(bookmark, content);
            enrichment.content_analysis = contentAnalysis;
          }
          
          // Social signals
          if (opts.includeSocial) {
            const socialAnalysis = await this.analyzeSocialSignals(bookmark);
            enrichment.social_signals = socialAnalysis;
          }
          
          // Temporal analysis
          if (opts.includeTemporal) {
            // Get change history (would come from delta ETL)
            const changeHistory = []; // TODO: Get from ETL
            const temporalAnalysis = await this.analyzeTemporalAspects(bookmark, changeHistory);
            enrichment.temporal_analysis = temporalAnalysis;
          }
          
          enrichment.enriched_at = new Date().toISOString();
          enrichment.enrichment_version = '1.0';
          
        } catch (error) {
          console.error(`Error enriching ${bookmark.url}:`, error);
          enrichment.enrichment_error = error.message;
        }
        
        return enrichment;
      });
      
      const batchResults = await Promise.all(batchPromises);
      enriched.push(...batchResults);
      
      console.log(`Enriched ${enriched.length}/${bookmarks.length} bookmarks`);
    }
    
    return enriched;
  }
  
  // Generate bookmark clusters using embeddings
  async clusterBookmarks(bookmarks: any[]): Promise<{
    clusters: Array<{
      id: string;
      name: string;
      description: string;
      bookmarks: any[];
      centroid_topics: string[];
    }>;
  }> {
    const { object } = await generateObject({
      model: openai(this.model),
      schema: z.object({
        clusters: z.array(z.object({
          id: z.string(),
          name: z.string(),
          description: z.string(),
          bookmark_indices: z.array(z.number()),
          centroid_topics: z.array(z.string())
        }))
      }),
      prompt: `Cluster these bookmarks into meaningful groups based on their content and topics:

${bookmarks.map((b, i) => `${i}. ${b.title} - ${b.categories?.join(', ')} - ${b.description?.substring(0, 100)}`).join('\n')}

Create 3-7 clusters that represent natural groupings. Include indices of bookmarks in each cluster.`
    });
    
    // Map indices back to bookmarks
    const clustersWithBookmarks = object.clusters.map(cluster => ({
      ...cluster,
      bookmarks: cluster.bookmark_indices.map(i => bookmarks[i]).filter(Boolean)
    }));
    
    return { clusters: clustersWithBookmarks };
  }
  
  // Generate personalized insights
  async generateInsights(bookmarks: any[]): Promise<{
    insights: string[];
    patterns: string[];
    recommendations: string[];
    warnings: string[];
  }> {
    const { object } = await generateObject({
      model: openai(this.model),
      schema: z.object({
        insights: z.array(z.string()).min(5).max(10),
        patterns: z.array(z.string()).min(3).max(7),
        recommendations: z.array(z.string()).min(5).max(10),
        warnings: z.array(z.string()).min(0).max(5)
      }),
      prompt: `Analyze this bookmark collection and generate personalized insights:

Total bookmarks: ${bookmarks.length}
Categories: ${[...new Set(bookmarks.flatMap(b => b.categories || []))].join(', ')}
Date range: ${new Date(Math.min(...bookmarks.map(b => new Date(b.created_at).getTime()))).toISOString()} to now

Top bookmarks by value score:
${bookmarks.sort((a, b) => (b.value_score || 0) - (a.value_score || 0)).slice(0, 10).map(b => `- ${b.title}: ${b.value_score}`).join('\n')}

Generate insights about:
1. Reading/learning patterns
2. Topic evolution over time
3. Content quality trends
4. Gaps in knowledge coverage
5. Actionable next steps`
    });
    
    return object;
  }
}

// Example usage
if (import.meta.main) {
  const etl = new BookmarkDeltaETL('./bookmark-delta-data');
  const enricher = new AIBookmarkEnricher(etl);
  
  // Load bookmarks
  const bookmarks = await etl.extract(['bookmarks.json']);
  
  // Enrich a batch
  console.log('🤖 Starting AI enrichment...');
  const enriched = await enricher.enrichBookmarkBatch(bookmarks.slice(0, 5), {
    includeContent: true,
    includeSocial: true,
    includeTemporal: true
  });
  
  console.log('✨ Enrichment complete:', enriched.length);
  
  // Generate clusters
  const { clusters } = await enricher.clusterBookmarks(enriched);
  console.log('📊 Generated clusters:', clusters.map(c => `${c.name} (${c.bookmarks.length} items)`));
  
  // Generate insights
  const insights = await enricher.generateInsights(enriched);
  console.log('💡 Insights:', insights);
}