import { z } from 'zod';
import * as fs from 'fs/promises';
import * as path from 'path';
import { createHmac, randomBytes } from 'crypto';
import { EnhancedBookmark } from './enhanced-bookmark-schema';
import { BookmarkDeltaETL } from './delta-load-pipeline';
import { getCredentialsManager, CredentialsManager } from './credentials-manager';

// Schema for Twitter/Grok conversation data
const TwitterThreadSchema = z.object({
  id: z.string(),
  conversation_id: z.string(),
  author: z.object({
    username: z.string(),
    name: z.string(),
    id: z.string()
  }),
  created_at: z.string(),
  text: z.string(),
  in_reply_to_id: z.string().optional(),
  referenced_tweets: z.array(z.object({
    type: z.enum(['replied_to', 'quoted', 'retweeted']),
    id: z.string()
  })).optional(),
  public_metrics: z.object({
    retweet_count: z.number(),
    reply_count: z.number(),
    like_count: z.number(),
    quote_count: z.number()
  }).optional(),
  entities: z.object({
    urls: z.array(z.object({
      url: z.string(),
      expanded_url: z.string(),
      display_url: z.string()
    })).optional(),
    hashtags: z.array(z.object({
      tag: z.string()
    })).optional(),
    mentions: z.array(z.object({
      username: z.string()
    })).optional()
  }).optional()
});

type TwitterThread = z.infer<typeof TwitterThreadSchema>;

export class TwitterGrokFetcher {
  private etl: BookmarkDeltaETL;
  private dataDir: string;
  private credentialsManager: CredentialsManager;
  private lastFetchedId: string | null = null;
  
  constructor(etl: BookmarkDeltaETL, dataDir: string = './bookmark-delta-data') {
    this.etl = etl;
    this.dataDir = dataDir;
    this.credentialsManager = getCredentialsManager();
  }
  
  // Load existing Grok conversations from the unified chat data
  async loadGrokConversations(): Promise<any[]> {
    try {
      // Look for the most recent unified chat data
      const files = await fs.readdir(path.join(this.dataDir, '..'));
      const unifiedFiles = files.filter(f => f.startsWith('unified_chat_full_data'));
      
      if (unifiedFiles.length === 0) {
        console.log('No unified chat data found');
        return [];
      }
      
      // Sort by timestamp and get the most recent
      unifiedFiles.sort().reverse();
      const latestFile = unifiedFiles[0];
      
      const data = JSON.parse(
        await fs.readFile(path.join(this.dataDir, '..', latestFile), 'utf-8')
      );
      
      // Filter for Grok conversations
      const grokConversations = data.conversations.filter(
        (conv: any) => conv.platform === 'Grok'
      );
      
      console.log(`Found ${grokConversations.length} Grok conversations`);
      return grokConversations;
    } catch (error) {
      console.error('Error loading Grok conversations:', error);
      return [];
    }
  }
  
  // Convert Twitter/Grok thread to bookmark format
  private threadToBookmark(thread: TwitterThread, conversationUrl: string): Partial<EnhancedBookmark> {
    const hashtags = thread.entities?.hashtags?.map(h => h.tag) || [];
    const mentions = thread.entities?.mentions?.map(m => `@${m.username}`) || [];
    const urls = thread.entities?.urls?.map(u => u.expanded_url) || [];
    
    return {
      id: `twitter_${thread.id}`,
      url: conversationUrl,
      title: `${thread.author.name} on X: "${thread.text.slice(0, 100)}..."`,
      description: thread.text,
      
      // Temporal data
      created_at: thread.created_at,
      updated_at: thread.created_at,
      access_count: 1,
      
      // Content analysis
      content_hash: this.generateHash(thread.text),
      content_length: thread.text.length,
      reading_time: Math.ceil(thread.text.split(' ').length / 200),
      language: 'en', // TODO: Detect language
      
      // Metadata
      meta_tags: {
        source: 'twitter',
        platform: 'grok',
        author: thread.author,
        conversation_id: thread.conversation_id,
        thread_id: thread.id,
        metrics: thread.public_metrics,
        entities: thread.entities,
        urls: urls,
        is_reply: !!thread.in_reply_to_id,
        is_thread_start: !thread.in_reply_to_id
      },
      
      // Technical details
      response_time: 0,
      ssl_valid: true,
      mobile_friendly: true,
      
      // AI enrichment placeholders
      categories: [...hashtags, ...mentions, 'Twitter', 'Grok', 'Conversation'],
      sentiment: 0,
      readability_score: 0,
      key_topics: hashtags,
      
      // Social signals
      social_shares: {
        twitter: thread.public_metrics?.retweet_count || 0,
        linkedin: 0,
        reddit: 0
      },
      
      // Delta tracking
      change_frequency: 0,
      content_stability: 1,
      last_delta_hash: this.generateHash(thread.text)
    };
  }
  
  // Compose threads from individual tweets
  async composeThreads(tweets: TwitterThread[]): Promise<Map<string, TwitterThread[]>> {
    const threads = new Map<string, TwitterThread[]>();
    
    // Group by conversation ID
    for (const tweet of tweets) {
      const convId = tweet.conversation_id;
      if (!threads.has(convId)) {
        threads.set(convId, []);
      }
      threads.get(convId)!.push(tweet);
    }
    
    // Sort each thread by creation date
    for (const [convId, threadTweets] of threads) {
      threadTweets.sort((a, b) => 
        new Date(a.created_at).getTime() - new Date(b.created_at).getTime()
      );
    }
    
    return threads;
  }
  
  // Create a composite bookmark for an entire thread
  private createThreadBookmark(
    thread: TwitterThread[], 
    conversationUrl: string
  ): Partial<EnhancedBookmark> {
    const firstTweet = thread[0];
    const lastTweet = thread[thread.length - 1];
    
    // Combine all text
    const fullText = thread.map(t => t.text).join('\n\n---\n\n');
    
    // Aggregate metrics
    const totalMetrics = thread.reduce((acc, tweet) => ({
      retweet_count: acc.retweet_count + (tweet.public_metrics?.retweet_count || 0),
      reply_count: acc.reply_count + (tweet.public_metrics?.reply_count || 0),
      like_count: acc.like_count + (tweet.public_metrics?.like_count || 0),
      quote_count: acc.quote_count + (tweet.public_metrics?.quote_count || 0)
    }), { retweet_count: 0, reply_count: 0, like_count: 0, quote_count: 0 });
    
    // Collect all entities
    const allHashtags = new Set<string>();
    const allMentions = new Set<string>();
    const allUrls = new Set<string>();
    
    for (const tweet of thread) {
      tweet.entities?.hashtags?.forEach(h => allHashtags.add(h.tag));
      tweet.entities?.mentions?.forEach(m => allMentions.add(`@${m.username}`));
      tweet.entities?.urls?.forEach(u => allUrls.add(u.expanded_url));
    }
    
    return {
      id: `twitter_thread_${firstTweet.conversation_id}`,
      url: conversationUrl,
      title: `Thread by ${firstTweet.author.name}: "${firstTweet.text.slice(0, 80)}..."`,
      description: fullText,
      
      // Temporal data
      created_at: firstTweet.created_at,
      updated_at: lastTweet.created_at,
      access_count: thread.length,
      
      // Content analysis
      content_hash: this.generateHash(fullText),
      content_length: fullText.length,
      reading_time: Math.ceil(fullText.split(' ').length / 200),
      language: 'en',
      
      // Metadata
      meta_tags: {
        source: 'twitter',
        platform: 'grok',
        author: firstTweet.author,
        conversation_id: firstTweet.conversation_id,
        thread_length: thread.length,
        metrics: totalMetrics,
        hashtags: Array.from(allHashtags),
        mentions: Array.from(allMentions),
        urls: Array.from(allUrls),
        is_thread: true,
        thread_tweets: thread.map(t => ({
          id: t.id,
          text: t.text,
          created_at: t.created_at
        }))
      },
      
      // Categories
      categories: [
        ...Array.from(allHashtags),
        ...Array.from(allMentions),
        'Twitter',
        'Grok',
        'Thread',
        'Conversation'
      ],
      
      // Social signals
      social_shares: {
        twitter: totalMetrics.retweet_count,
        linkedin: 0,
        reddit: 0
      },
      
      // Other fields
      sentiment: 0,
      readability_score: 0,
      key_topics: Array.from(allHashtags),
      response_time: 0,
      ssl_valid: true,
      mobile_friendly: true,
      change_frequency: 0,
      content_stability: 1,
      last_delta_hash: this.generateHash(fullText)
    };
  }
  
  // Check for X.com scraping credentials using global manager
  private async checkCredentials(): Promise<{ hasCredentials: boolean; credentials?: any }> {
    await this.credentialsManager.loadCredentials();
    return this.credentialsManager.getTwitterScrapingCredentials();
  }
  
  // Extract conversation ID from Grok URL
  private extractConversationId(url: string): string | null {
    if (url.includes('conversation=')) {
      return url.split('conversation=')[1].split('&')[0];
    }
    return null;
  }
  
  // Fetch a single Grok conversation using GraphQL
  async fetchGrokConversation(conversationId: string): Promise<any> {
    const { hasCredentials, credentials } = await this.checkCredentials();
    
    if (!hasCredentials) {
      console.warn('⚠️  Skipping Grok fetch - no credentials found');
      return null;
    }
    
    // Grok GraphQL endpoint
    const endpoint = 'https://x.com/i/api/graphql/NS-xp6AJT5wt_LyRS_UjRA/GrokConversationItemsByRestId';
    
    const variables = {
      restId: conversationId
    };
    
    const features = {
      creator_subscriptions_tweet_preview_api_enabled: true,
      premium_content_api_read_enabled: false,
      communities_web_enable_tweet_community_results_fetch: true,
      c9s_tweet_anatomy_moderator_badge_enabled: true,
      responsive_web_grok_analyze_button_fetch_trends_enabled: false,
      responsive_web_grok_analyze_post_followups_enabled: true,
      responsive_web_jetfuel_frame: false,
      responsive_web_grok_share_attachment_enabled: true,
      articles_preview_enabled: true,
      responsive_web_edit_tweet_api_enabled: true,
      graphql_is_translatable_rweb_tweet_is_translatable_enabled: true,
      view_counts_everywhere_api_enabled: true,
      longform_notetweets_consumption_enabled: true,
      responsive_web_twitter_article_tweet_consumption_enabled: true,
      tweet_awards_web_tipping_enabled: false,
      responsive_web_grok_show_grok_translated_post: false,
      responsive_web_grok_analysis_button_from_backend: true,
      creator_subscriptions_quote_tweet_preview_enabled: false,
      freedom_of_speech_not_reach_fetch_enabled: true,
      standardized_nudges_misinfo: true,
      tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled: true,
      longform_notetweets_rich_text_read_enabled: true,
      longform_notetweets_inline_media_enabled: true,
      payments_enabled: false,
      profile_label_improvements_pcf_label_in_post_enabled: true,
      rweb_tipjar_consumption_enabled: true,
      verified_phone_label_enabled: false,
      responsive_web_grok_image_annotation_enabled: true,
      responsive_web_graphql_skip_user_profile_image_extensions_enabled: false,
      responsive_web_graphql_timeline_navigation_enabled: true,
      responsive_web_enhance_cards_enabled: false
    };
    
    const headers = {
      'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.9',
      'Content-Type': 'application/json',
      'Referer': 'https://x.com/',
      'Origin': 'https://x.com',
      'x-twitter-auth-type': 'OAuth2Session',
      'x-twitter-client-language': 'en',
      'x-twitter-active-user': 'yes',
      'x-csrf-token': credentials.ct0,
      'cookie': `ct0=${credentials.ct0}; auth_token=${credentials.auth_token}${credentials.kdt ? `; kdt=${credentials.kdt}` : ''}`
    };
    
    const params = new URLSearchParams({
      variables: JSON.stringify(variables),
      features: JSON.stringify(features)
    });
    
    try {
      console.log(`🔍 Fetching Grok conversation: ${conversationId}`);
      
      const response = await fetch(`${endpoint}?${params}`, {
        method: 'GET',
        headers: headers
      });
      
      if (response.ok) {
        const data = await response.json();
        const grokData = data?.data?.grok_conversation_items_by_rest_id;
        
        // Extract messages
        const messages = [];
        if (grokData?.items) {
          for (const item of grokData.items) {
            messages.push({
              chat_item_id: item.chat_item_id,
              created_at: item.created_at_ms,
              sender_type: item.sender_type || 'unknown',
              content: item.message || '',
              thinking_trace: item.thinking_trace || '',
              grok_mode: item.grok_mode || 'Normal'
            });
          }
        }
        
        return {
          conversation_id: conversationId,
          status: 'success',
          messages: messages,
          created_at: grokData?.createdAt,
          title: grokData?.title || 'Grok Conversation',
          raw_data: grokData
        };
      } else {
        console.error(`❌ Failed to fetch conversation. Status: ${response.status}`);
        if (response.status === 401) {
          console.error('Authentication failed - tokens may be expired');
        }
        return null;
      }
    } catch (error) {
      console.error(`Error fetching conversation ${conversationId}:`, error);
      return null;
    }
  }
  
  // Fetch user timeline using X.com's GraphQL API
  async fetchUserTimeline(username: string, sinceId?: string): Promise<TwitterThread[]> {
    console.log(`📱 Fetching timeline for @${username}${sinceId ? ` since ${sinceId}` : ''}`);

    // Prefer official Twitter API v2 if available; fall back to cookies-based scraping later
    const { hasCredentials: hasApiCreds, credentials: apiCreds } = this.credentialsManager.getTwitterAPICredentials();

    if (!hasApiCreds) {
      console.warn('⚠️  Twitter API credentials not configured. Will try cookies-based GraphQL fetch.');
    }

    try {
      // 1) Resolve user by username to get user id and name
      const userLookupUrl = `https://api.twitter.com/2/users/by/username/${encodeURIComponent(username)}`;
      const userLookupParams: Record<string, string> = { 'user.fields': 'name,username' };
      const userHeaders: HeadersInit = apiCreds.bearer_token
        ? { Authorization: `Bearer ${apiCreds.bearer_token}` }
        : this.buildOAuth1Header('GET', userLookupUrl, userLookupParams);
      const userRes = await fetch(`${userLookupUrl}?${new URLSearchParams(userLookupParams)}`, { headers: userHeaders });
      if (!userRes.ok) {
        console.error(`❌ Failed to resolve user @${username}: ${userRes.status}`);
        // Fall back to cookies-based flow below
        throw new Error(`user-lookup-${userRes.status}`);
      }
      const userJson = await userRes.json();
      const user = userJson?.data;
      if (!user?.id) {
        console.warn(`⚠️  No user id for @${username}`);
        return [];
      }

      // 2) Fetch tweets in pages, honoring since_id when provided
      const collected: TwitterThread[] = [];
      let nextToken: string | undefined = undefined;
      let page = 0;

      do {
        const params = new URLSearchParams({
          max_results: '100',
          'tweet.fields': [
            'created_at',
            'public_metrics',
            'entities',
            'conversation_id',
            'referenced_tweets',
            'in_reply_to_user_id'
          ].join(','),
          ...(sinceId ? { since_id: sinceId } : {}),
          ...(nextToken ? { pagination_token: nextToken } : {})
        } as Record<string, string>);

        const baseUrl = `https://api.twitter.com/2/users/${user.id}/tweets`;
        const headers: HeadersInit = apiCreds.bearer_token
          ? { Authorization: `Bearer ${apiCreds.bearer_token}` }
          : this.buildOAuth1Header('GET', baseUrl, Object.fromEntries(params));
        const res = await fetch(`${baseUrl}?${params.toString()}`, { headers });
        if (!res.ok) {
          console.error(`❌ Timeline fetch error: ${res.status}`);
          break;
        }
        const json = await res.json();
        const tweets = Array.isArray(json?.data) ? json.data : [];
        const meta = json?.meta || {};

        for (const t of tweets) {
          const thread: TwitterThread = {
            id: t.id,
            conversation_id: t.conversation_id || t.id,
            author: { username: user.username, name: user.name, id: user.id },
            created_at: t.created_at,
            text: t.text,
            in_reply_to_id: t?.referenced_tweets?.find((r: any) => r.type === 'replied_to')?.id,
            referenced_tweets: (t.referenced_tweets || []).map((r: any) => ({ type: r.type, id: r.id })),
            public_metrics: t.public_metrics ? {
              retweet_count: t.public_metrics.retweet_count || 0,
              reply_count: t.public_metrics.reply_count || 0,
              like_count: t.public_metrics.like_count || 0,
              quote_count: t.public_metrics.quote_count || 0,
            } : undefined,
            entities: t.entities ? {
              urls: (t.entities.urls || []).map((u: any) => ({
                url: u.url,
                expanded_url: u.expanded_url || u.url,
                display_url: u.display_url || u.expanded_url || u.url,
              })),
              hashtags: (t.entities.hashtags || []).map((h: any) => ({ tag: h.tag })),
              mentions: (t.entities.mentions || []).map((m: any) => ({ username: m.username }))
            } : undefined,
          };
          collected.push(thread);
        }

        nextToken = meta?.next_token;
        page += 1;
        // Avoid hammering the API
        if (nextToken) {
          await new Promise(r => setTimeout(r, 350));
        }
      } while (nextToken);

      // Sort ascending by created_at to maintain state correctness
      collected.sort((a, b) => new Date(a.created_at).getTime() - new Date(b.created_at).getTime());
      console.log(`✅ Retrieved ${collected.length} tweets for @${username}`);
      return collected;
    } catch (err) {
      console.warn('⚠️  API-based fetch failed or unavailable, attempting cookies-based GraphQL fetch...');
      try {
        const threads = await this.fetchTimelineViaCookies(username, sinceId);
        return threads;
      } catch (e) {
        console.error('❌ Cookies-based GraphQL fetch failed:', e);
        return [];
      }
    }
  }

  // Build OAuth 1.0a Authorization header for Twitter API requests
  private buildOAuth1Header(
    method: 'GET' | 'POST',
    url: string,
    queryParams: Record<string, string>
  ): HeadersInit {
    const { credentials } = this.credentialsManager.getTwitterAPICredentials();
    const consumerKey = credentials.api_key || '';
    const consumerSecret = credentials.api_secret || '';
    const token = credentials.access_token || '';
    const tokenSecret = credentials.access_token_secret || '';

    const oauthParams: Record<string, string> = {
      oauth_consumer_key: consumerKey,
      oauth_nonce: randomBytes(16).toString('hex'),
      oauth_signature_method: 'HMAC-SHA1',
      oauth_timestamp: Math.floor(Date.now() / 1000).toString(),
      oauth_token: token,
      oauth_version: '1.0',
    };

    const allParams: Record<string, string> = { ...queryParams, ...oauthParams };

    const percentEncode = (str: string) => encodeURIComponent(str)
      .replace(/[!'()*]/g, c => '%' + c.charCodeAt(0).toString(16).toUpperCase());

    const paramString = Object.keys(allParams)
      .sort()
      .map(k => `${percentEncode(k)}=${percentEncode(allParams[k])}`)
      .join('&');

    const signatureBaseString = [
      method.toUpperCase(),
      percentEncode(url),
      percentEncode(paramString),
    ].join('&');

    const signingKey = `${percentEncode(consumerSecret)}&${percentEncode(tokenSecret)}`;
    const signature = createHmac('sha1', signingKey)
      .update(signatureBaseString)
      .digest('base64');

    const authHeader = 'OAuth ' + [
      `oauth_consumer_key="${percentEncode(consumerKey)}"`,
      `oauth_nonce="${percentEncode(oauthParams.oauth_nonce)}"`,
      `oauth_signature="${percentEncode(signature)}"`,
      `oauth_signature_method="HMAC-SHA1"`,
      `oauth_timestamp="${oauthParams.oauth_timestamp}"`,
      `oauth_token="${percentEncode(token)}"`,
      `oauth_version="1.0"`,
    ].join(', ');

    return { Authorization: authHeader };
  }

  // Cookies-based timeline fetch using X.com GraphQL UserTweets endpoint
  private async fetchTimelineViaCookies(username: string, sinceId?: string): Promise<TwitterThread[]> {
    const { hasCredentials, credentials } = await this.checkCredentials();
    if (!hasCredentials) {
      console.warn('⚠️  No X.com cookies found (X_CT0, X_AUTH_TOKEN).');
      return [];
    }

    // Use env-provided user id if available, since GraphQL hashes for user lookup change frequently
    const userId = process.env.TWITTER_USER_ID;
    if (!userId) {
      throw new Error('TWITTER_USER_ID not set; set it to use cookies-based timeline fetch.');
    }

    // Known (subject to change) GraphQL endpoint for UserTweets
    const endpoint = 'https://x.com/i/api/graphql/V7H0Ap3_Hh2FyS75OCDO3Q/UserTweets';

    const features = {
      rweb_tipjar_consumption_enabled: true,
      responsive_web_graphql_exclude_directive_enabled: true,
      verified_phone_label_enabled: false,
      responsive_web_graphql_timeline_navigation_enabled: true,
      responsive_web_graphql_skip_user_profile_image_extensions_enabled: false,
      tweet_awards_web_tipping_enabled: false,
      freedom_of_speech_not_reach_fetch_enabled: true,
      standardized_nudges_misinfo: true,
      tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled: true,
      longform_notetweets_inline_media_enabled: true,
      longform_notetweets_rich_text_read_enabled: true,
      responsive_web_edit_tweet_api_enabled: true,
      graphql_is_translatable_rweb_tweet_is_translatable_enabled: true,
      view_counts_everywhere_api_enabled: true,
      longform_notetweets_consumption_enabled: true,
      responsive_web_twitter_article_tweet_consumption_enabled: true,
      creator_subscriptions_tweet_preview_api_enabled: true
    };

    const variablesBase: any = {
      userId: userId,
      count: 100,
      includePromotedContent: false,
      withQuickPromoteEligibilityTweetFields: true,
      withVoice: true,
      withV2Timeline: true
    };

    // Prepare headers with cookies
    const headers = {
      'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
      'User-Agent': 'Mozilla/5.0',
      'Accept': '*/*',
      'Content-Type': 'application/json',
      'x-twitter-auth-type': 'OAuth2Session',
      'x-twitter-client-language': 'en',
      'x-twitter-active-user': 'yes',
      'x-csrf-token': credentials.ct0!,
      'cookie': `ct0=${credentials.ct0}; auth_token=${credentials.auth_token}${credentials.kdt ? `; kdt=${credentials.kdt}` : ''}`
    } as HeadersInit;

    const collected: TwitterThread[] = [];
    let cursor: string | undefined = undefined;
    let page = 0;

    while (true) {
      const variables = {
        ...variablesBase,
        ...(cursor ? { cursor } : {}),
      };

      const params = new URLSearchParams({
        variables: JSON.stringify(variables),
        features: JSON.stringify(features)
      });

      const res = await fetch(`${endpoint}?${params}`, { headers });
      if (!res.ok) {
        throw new Error(`UserTweets GraphQL error ${res.status}`);
      }
      const json = await res.json();

      // Walk entries to extract tweets
      const entries = json?.data?.user?.result?.timeline_v2?.timeline?.instructions?.flatMap((ins: any) => ins.entries || []) || [];
      for (const entry of entries) {
        const content = entry?.content;
        if (content?.itemContent?.tweet_results?.result) {
          const t = content.itemContent.tweet_results.result.legacy;
          const core = content.itemContent.tweet_results.result.core?.user_results?.result?.legacy;
          if (!t) continue;
          const thread: TwitterThread = {
            id: t.id_str,
            conversation_id: t.conversation_id_str || t.id_str,
            author: {
              username: core?.screen_name || username,
              name: core?.name || username,
              id: content.itemContent.tweet_results.result.core?.user_results?.result?.rest_id || userId
            },
            created_at: new Date(t.created_at).toISOString(),
            text: t.full_text || t.text || '',
            in_reply_to_id: t?.in_reply_to_status_id_str,
            referenced_tweets: [],
            public_metrics: {
              retweet_count: t.retweet_count || 0,
              reply_count: t.reply_count || 0,
              like_count: t.favorite_count || 0,
              quote_count: t.quote_count || 0
            },
            entities: t.entities ? {
              urls: (t.entities.urls || []).map((u: any) => ({ url: u.url, expanded_url: u.expanded_url || u.url, display_url: u.display_url || u.expanded_url || u.url })),
              hashtags: (t.entities.hashtags || []).map((h: any) => ({ tag: h.text || h.tag })),
              mentions: (t.entities.user_mentions || []).map((m: any) => ({ username: m.screen_name || m.username }))
            } : undefined
          };
          // sinceId filter (client-side) if provided
          if (!sinceId || thread.id > sinceId) {
            collected.push(thread);
          }
        }
        // Pagination cursor
        if (content?.operation?.cursor?.value) {
          cursor = content.operation.cursor.value;
        }
      }

      page += 1;
      if (!cursor || page >= 5) break; // limit pages to avoid long runs
      await new Promise(r => setTimeout(r, 800));
    }

    collected.sort((a, b) => new Date(a.created_at).getTime() - new Date(b.created_at).getTime());
    console.log(`✅ Retrieved ${collected.length} tweets for userId ${userId} via cookies`);
    return collected;
  }
  
  // Process and integrate Twitter/Grok data into bookmarks
  async processTwitterGrokData(): Promise<void> {
    console.log('🐦 Processing Twitter/Grok data for bookmark ETL');
    
    // Step 1: Load existing Grok conversation metadata
    const grokConversations = await this.loadGrokConversations();
    
    if (grokConversations.length === 0) {
      console.log('⚠️  No Grok conversations found in unified data');
      return;
    }
    
    // Step 2: Check if we can fetch full content
    const { hasCredentials } = await this.checkCredentials();
    
    // Step 3: Process conversations
    const bookmarks: Partial<EnhancedBookmark>[] = [];
    let fetchedCount = 0;
    
    for (const conv of grokConversations) {
      let fullConversation = null;
      
      // Try to fetch full conversation content if we have credentials
      if (hasCredentials && conv.conversation_id) {
        try {
          fullConversation = await this.fetchGrokConversation(conv.conversation_id);
          if (fullConversation && fullConversation.status === 'success') {
            fetchedCount++;
            await new Promise(resolve => setTimeout(resolve, 2000)); // Rate limiting
          }
        } catch (error) {
          console.error(`Failed to fetch conversation ${conv.conversation_id}:`, error);
        }
      }
      
      // Create bookmark with full content if available, otherwise use metadata
      if (fullConversation && fullConversation.messages.length > 0) {
        // Create rich bookmark from fetched data
        const messages = fullConversation.messages;
        const fullText = messages.map((m: any) => 
          `${m.sender_type}: ${m.content}${m.thinking_trace ? `\n[Thinking: ${m.thinking_trace}]` : ''}`
        ).join('\n\n');
        
        const bookmark: Partial<EnhancedBookmark> = {
          id: `grok_${conv.conversation_id}`,
          url: conv.url || `https://x.com/i/grok/conversation=${conv.conversation_id}`,
          title: fullConversation.title || conv.title || 'Grok Conversation',
          description: fullText,
          
          created_at: fullConversation.created_at || conv.timestamp ? new Date(conv.timestamp * 1000).toISOString() : new Date().toISOString(),
          updated_at: new Date().toISOString(),
          access_count: messages.length,
          
          content_hash: this.generateHash(fullText),
          content_length: fullText.length,
          reading_time: Math.ceil(fullText.split(' ').length / 200),
          language: 'en',
          
          meta_tags: {
            source: 'grok',
            platform: 'twitter',
            conversation_id: conv.conversation_id,
            message_count: messages.length,
            has_full_content: true,
            grok_modes: [...new Set(messages.map((m: any) => m.grok_mode))],
            messages: messages,
            scraped_at: new Date().toISOString()
          },
          
          response_time: 0,
          ssl_valid: true,
          mobile_friendly: true,
          
          categories: ['Grok', 'AI', 'Conversation', 'Twitter', 'Scraped'],
          sentiment: 0,
          readability_score: 0,
          key_topics: this.extractTopicsFromMessages(messages),
          
          social_shares: {
            twitter: 0,
            linkedin: 0,
            reddit: 0
          },
          
          change_frequency: 0,
          content_stability: 1,
          last_delta_hash: this.generateHash(fullText)
        };
        
        bookmarks.push(bookmark);
      } else {
        // Create basic bookmark from metadata only
        const bookmark: Partial<EnhancedBookmark> = {
          id: `grok_${conv.conversation_id}`,
          url: conv.url || `https://x.com/i/grok/conversation=${conv.conversation_id}`,
          title: conv.title || 'Grok Conversation',
          description: conv.note || 'Grok conversation (metadata only - enable scraping for full content)',
          
          created_at: conv.timestamp ? new Date(conv.timestamp * 1000).toISOString() : new Date().toISOString(),
          updated_at: new Date().toISOString(),
          access_count: 0,
          
          content_hash: this.generateHash(conv.conversation_id),
          content_length: 0,
          reading_time: 0,
          language: 'en',
          
          meta_tags: {
            source: 'grok',
            platform: 'twitter',
            conversation_id: conv.conversation_id,
            export_note: conv.note,
            source_file: conv.source_file,
            has_full_content: false
          },
          
          response_time: 0,
          ssl_valid: true,
          mobile_friendly: true,
          
          categories: ['Grok', 'AI', 'Conversation', 'Twitter', 'Metadata Only'],
          sentiment: 0,
          readability_score: 0,
          key_topics: [],
          
          social_shares: {
            twitter: 0,
            linkedin: 0,
            reddit: 0
          },
          
          change_frequency: 0,
          content_stability: 1,
          last_delta_hash: this.generateHash(conv.conversation_id)
        };
        
        bookmarks.push(bookmark);
      }
    }
    
    // Step 4: Save to bookmark ETL format
    if (bookmarks.length > 0) {
      const outputFile = path.join(this.dataDir, 'twitter-grok-bookmarks.json');
      await fs.writeFile(outputFile, JSON.stringify(bookmarks, null, 2));
      console.log(`✅ Processed ${bookmarks.length} Grok conversations`);
      console.log(`   - ${fetchedCount} with full content (scraped)`);
      console.log(`   - ${bookmarks.length - fetchedCount} with metadata only`);
      console.log(`   - Saved to ${outputFile}`);
      
      // Step 5: Run ETL to integrate with existing bookmarks
      console.log('🔄 Running ETL to integrate Twitter/Grok data...');
      await this.etl.runETL([outputFile]);
    } else {
      console.log('⚠️  No Twitter/Grok conversations could be processed');
    }
  }
  
  // Extract topics from Grok messages
  private extractTopicsFromMessages(messages: any[]): string[] {
    const topics = new Set<string>();
    
    for (const msg of messages) {
      // Simple topic extraction - could be enhanced with NLP
      const text = msg.content.toLowerCase();
      
      // Extract hashtag-like patterns
      const hashtagMatches = text.match(/#\w+/g);
      if (hashtagMatches) {
        hashtagMatches.forEach(tag => topics.add(tag.slice(1)));
      }
      
      // Extract common AI/tech terms
      const techTerms = ['ai', 'ml', 'gpt', 'llm', 'api', 'code', 'python', 'javascript', 'data'];
      techTerms.forEach(term => {
        if (text.includes(term)) {
          topics.add(term.toUpperCase());
        }
      });
    }
    
    return Array.from(topics);
  }
  
  // Generate hash for content
  private generateHash(content: string): string {
    // Simple hash implementation (would use crypto in production)
    let hash = 0;
    for (let i = 0; i < content.length; i++) {
      const char = content.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash = hash & hash;
    }
    return Math.abs(hash).toString(16);
  }
  
  // Fetch new tweets and update bookmarks
  async updateFromTimeline(username: string): Promise<void> {
    console.log(`🔄 Updating bookmarks from @${username} timeline`);
    
    // Get the most recent tweet ID we've processed
    const stateFile = path.join(this.dataDir, 'twitter-fetch-state.json');
    let state: any = {};
    
    try {
      const stateData = await fs.readFile(stateFile, 'utf-8');
      state = JSON.parse(stateData);
    } catch (error) {
      console.log('No previous fetch state found');
    }
    
    const sinceId = state[username]?.lastTweetId;
    
    // Fetch new tweets
    const tweets = await this.fetchUserTimeline(username, sinceId);
    
    if (tweets.length === 0) {
      console.log('No new tweets found');
      return;
    }
    
    // Compose threads
    const threads = await this.composeThreads(tweets);
    console.log(`Found ${threads.size} conversation threads`);
    
    // Convert to bookmarks
    const bookmarks: Partial<EnhancedBookmark>[] = [];
    
    for (const [convId, thread] of threads) {
      const threadBookmark = this.createThreadBookmark(
        thread,
        // Use a standard X.com status URL pointing to the first tweet
        `https://x.com/${thread[0].author.username}/status/${thread[0].id}`
      );
      bookmarks.push(threadBookmark);
    }
    
    // Save bookmarks
    const outputFile = path.join(this.dataDir, `twitter-timeline-${username}-${Date.now()}.json`);
    await fs.writeFile(outputFile, JSON.stringify(bookmarks, null, 2));
    
    // Update state
    if (tweets.length > 0) {
      state[username] = {
        lastTweetId: tweets[tweets.length - 1].id,
        lastFetch: new Date().toISOString()
      };
      await fs.writeFile(stateFile, JSON.stringify(state, null, 2));
    }
    
    // Run ETL
    console.log('Running ETL to integrate new timeline data...');
    await this.etl.runETL([outputFile]);
  }
}

// Example usage
if (import.meta.main) {
  const etl = new BookmarkDeltaETL('./bookmark-delta-data');
  const fetcher = new TwitterGrokFetcher(etl);
  
  // Process existing Grok conversations
  await fetcher.processTwitterGrokData();
  
  // Update from a user's timeline (requires API implementation)
  // await fetcher.updateFromTimeline('elonmusk');
}