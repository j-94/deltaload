import { z } from 'zod';

// Complete bookmark schema based on the 185 fields discovered
export const CompleteBookmarkSchema = z.object({
  // Core fields
  id: z.string(),
  url: z.string().url(),
  content: z.string().optional(),
  created_at: z.string(),
  full_text: z.string().optional(),
  markdown: z.string().optional(),
  processed_at: z.string().optional(),
  processing_error: z.string().optional(),
  source: z.enum(['raindrop', 'twitter', 'github']),
  status: z.string().optional(),
  
  // Metadata fields (parsed from JSON string)
  metadata: z.object({
    // Basic metadata
    author: z.union([
      z.string(),
      z.object({
        name: z.string().optional(),
        profile_image_url: z.string().optional(),
        screen_name: z.string().optional()
      })
    ]).optional(),
    canonical_url: z.string().optional(),
    cover: z.string().optional(),
    created_at: z.string().optional(),
    description: z.string().optional(),
    domain: z.string().optional(),
    extracted_at: z.string().optional(),
    favicon: z.string().optional(),
    favorite: z.boolean().optional(),
    favorite_count: z.number().optional(),
    folder: z.string().optional(),
    
    // GitHub specific
    forks: z.number().optional(),
    github_processed_at: z.string().optional(),
    github_readme: z.string().optional(),
    has_readme: z.boolean().optional(),
    language: z.string().optional(),
    license: z.string().optional(),
    open_issues: z.number().optional(),
    owner: z.object({
      avatar_url: z.string().optional(),
      login: z.string().optional(),
      type: z.string().optional()
    }).optional(),
    processed_with: z.string().optional(),
    pushed_at: z.string().optional(),
    readme_path: z.string().optional(),
    repo: z.string().optional(),
    repo_created_at: z.string().optional(),
    repo_pushed_at: z.string().optional(),
    repo_updated_at: z.string().optional(),
    stars: z.number().optional(),
    watchers: z.number().optional(),
    
    // Content metadata
    highlights: z.array(z.string()).optional(),
    json_ld: z.any().optional(),
    lang: z.string().optional(),
    modified_date: z.string().optional(),
    original_author: z.string().optional(),
    published_date: z.string().optional(),
    read_time: z.number().optional(),
    site_name: z.string().optional(),
    tags: z.array(z.string()).optional(),
    title: z.string().optional(),
    type: z.string().optional(),
    updated_at: z.string().optional(),
    web_processed_at: z.string().optional(),
    word_count: z.number().optional(),
    
    // OpenGraph metadata
    opengraph: z.object({
      'article:modified_time': z.string().optional(),
      'article:published_time': z.string().optional(),
      'article:section': z.string().optional(),
      'article:section:color': z.string().optional(),
      audio: z.string().optional(),
      author: z.string().optional(),
      availability: z.string().optional(),
      card: z.string().optional(),
      description: z.string().optional(),
      email: z.string().optional(),
      height: z.string().optional(),
      ignore_canonical: z.string().optional(),
      image: z.string().optional(),
      'image:alt': z.string().optional(),
      'image:height': z.string().optional(),
      'image:secure': z.string().optional(),
      'image:secure_url': z.string().optional(),
      'image:type': z.string().optional(),
      'image:url': z.string().optional(),
      'image:user_generated': z.string().optional(),
      'image:width': z.string().optional(),
      latitude: z.string().optional(),
      locale: z.string().optional(),
      'locale:alternate': z.string().optional(),
      locality: z.string().optional(),
      logo: z.string().optional(),
      longitude: z.string().optional(),
      'price:amount': z.string().optional(),
      'price:currency': z.string().optional(),
      'publish-date': z.string().optional(),
      publish_date: z.string().optional(),
      root_path: z.string().optional(),
      secure_url: z.string().optional(),
      see_also: z.string().optional(),
      site_name: z.string().optional(),
      title: z.string().optional(),
      ttl: z.string().optional(),
      type: z.string().optional(),
      updated_time: z.string().optional(),
      url: z.string().optional(),
      video: z.string().optional(),
      'video:height': z.string().optional(),
      'video:secure': z.string().optional(),
      'video:secure_url': z.string().optional(),
      'video:tag': z.string().optional(),
      'video:type': z.string().optional(),
      'video:url': z.string().optional(),
      'video:width': z.string().optional(),
      width: z.string().optional()
    }).optional(),
    
    // Twitter specific
    quote_count: z.number().optional(),
    reply_count: z.number().optional(),
    retweet_count: z.number().optional(),
    retweet_fixed: z.boolean().optional(),
    retweet_fixed_method: z.string().optional(),
    thread_id: z.string().optional(),
    tweet_count: z.number().optional(),
    tweet_metrics: z.object({
      likes: z.number().optional(),
      replies: z.number().optional(),
      retweets: z.number().optional()
    }).optional(),
    tweet_processed_at: z.string().optional(),
    tweets: z.array(z.any()).optional(),
    
    // Twitter card metadata
    twitter_card: z.object({
      account_id: z.string().optional(),
      'app:android': z.string().optional(),
      'app:id:googleplay': z.string().optional(),
      'app:id:ipad': z.string().optional(),
      'app:id:iphone': z.string().optional(),
      'app:name:googleplay': z.string().optional(),
      'app:name:ipad': z.string().optional(),
      'app:name:iphone': z.string().optional(),
      'app:url:googleplay': z.string().optional(),
      'app:url:ipad': z.string().optional(),
      'app:url:iphone': z.string().optional(),
      card: z.string().optional(),
      creator: z.string().optional(),
      'creator:id': z.string().optional(),
      data1: z.string().optional(),
      data2: z.string().optional(),
      data3: z.string().optional(),
      data4: z.string().optional(),
      description: z.string().optional(),
      dnt: z.string().optional(),
      domain: z.string().optional(),
      image: z.string().optional(),
      'image-height': z.string().optional(),
      'image-width': z.string().optional(),
      'image:alt': z.string().optional(),
      'image:height': z.string().optional(),
      'image:src': z.string().optional(),
      'image:type': z.string().optional(),
      'image:width': z.string().optional(),
      label1: z.string().optional(),
      label2: z.string().optional(),
      label3: z.string().optional(),
      label4: z.string().optional(),
      player: z.string().optional(),
      'player:height': z.string().optional(),
      'player:width': z.string().optional(),
      site: z.string().optional(),
      'site:id': z.string().optional(),
      site_name: z.string().optional(),
      'text:description': z.string().optional(),
      'text:title': z.string().optional(),
      title: z.string().optional(),
      url: z.string().optional(),
      'widgets:csp': z.string().optional(),
      'widgets:new-embed-design': z.string().optional()
    }).optional(),
    
    // User metadata
    user: z.object({
      followers_count: z.number().optional(),
      following_count: z.number().optional(),
      id: z.string().optional(),
      name: z.string().optional(),
      screen_name: z.string().optional(),
      statuses_count: z.number().optional(),
      verified: z.boolean().optional()
    }).optional(),
    user_followers: z.number().optional(),
    user_following: z.number().optional(),
    user_id: z.string().optional(),
    user_name: z.string().optional(),
    user_tweets: z.number().optional(),
    user_verified: z.boolean().optional(),
    username: z.string().optional()
  }).optional()
});

// Helper to extract all metadata fields into a flat structure for analysis
export function flattenBookmarkMetadata(bookmark: any): Record<string, any> {
  const flat: Record<string, any> = {
    id: bookmark.id,
    url: bookmark.url,
    content: bookmark.content,
    created_at: bookmark.created_at,
    full_text: bookmark.full_text,
    markdown: bookmark.markdown,
    processed_at: bookmark.processed_at,
    processing_error: bookmark.processing_error,
    source: bookmark.source,
    status: bookmark.status
  };
  
  // Parse metadata if it's a string
  let metadata = bookmark.metadata;
  if (typeof metadata === 'string') {
    try {
      metadata = JSON.parse(metadata);
    } catch (e) {
      return flat;
    }
  }
  
  if (!metadata) return flat;
  
  // Flatten metadata fields
  const flattenObject = (obj: any, prefix = '') => {
    for (const key in obj) {
      const value = obj[key];
      const newKey = prefix ? `${prefix}.${key}` : key;
      
      if (value && typeof value === 'object' && !Array.isArray(value)) {
        flattenObject(value, newKey);
      } else {
        flat[`metadata.${newKey}`] = value;
      }
    }
  };
  
  flattenObject(metadata);
  return flat;
}

// Extract source-specific metadata
export function extractSourceMetadata(bookmark: any): {
  source: string;
  sourceMetadata: Record<string, any>;
} {
  const flat = flattenBookmarkMetadata(bookmark);
  const source = bookmark.source;
  const sourceMetadata: Record<string, any> = {};
  
  switch (source) {
    case 'github':
      // Extract GitHub-specific fields
      const githubFields = [
        'forks', 'stars', 'watchers', 'open_issues', 'language', 'license',
        'has_readme', 'github_readme', 'readme_path', 'repo', 'owner',
        'repo_created_at', 'repo_pushed_at', 'repo_updated_at',
        'github_processed_at', 'processed_with'
      ];
      githubFields.forEach(field => {
        const key = `metadata.${field}`;
        if (flat[key] !== undefined) {
          sourceMetadata[field] = flat[key];
        }
      });
      break;
      
    case 'twitter':
      // Extract Twitter-specific fields
      const twitterFields = [
        'tweet_count', 'reply_count', 'retweet_count', 'quote_count',
        'tweet_metrics', 'tweets', 'thread_id', 'tweet_processed_at',
        'retweet_fixed', 'retweet_fixed_method', 'user', 'user_followers',
        'user_following', 'user_tweets', 'user_verified', 'twitter_card'
      ];
      twitterFields.forEach(field => {
        const key = `metadata.${field}`;
        if (flat[key] !== undefined) {
          sourceMetadata[field] = flat[key];
        }
      });
      break;
      
    case 'raindrop':
      // Extract Raindrop-specific fields
      const raindropFields = [
        'folder', 'tags', 'highlights', 'favorite', 'cover'
      ];
      raindropFields.forEach(field => {
        const key = `metadata.${field}`;
        if (flat[key] !== undefined) {
          sourceMetadata[field] = flat[key];
        }
      });
      break;
  }
  
  return { source, sourceMetadata };
}

// Type exports
export type CompleteBookmark = z.infer<typeof CompleteBookmarkSchema>;
