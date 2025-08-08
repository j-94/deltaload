import * as fs from 'fs/promises';
import * as path from 'path';

export interface TwitterCredentials {
  ct0?: string;
  auth_token?: string;
  kdt?: string;
  bearer_token?: string;
  api_key?: string;
  api_secret?: string;
  access_token?: string;
  access_token_secret?: string;
}

export interface OpenAICredentials {
  api_key?: string;
  organization?: string;
}

export interface Credentials {
  twitter: TwitterCredentials;
  openai: OpenAICredentials;
  anthropic: {
    api_key?: string;
  };
  last_checked: string;
  has_twitter_cookies: boolean;
  has_twitter_api: boolean;
  has_openai: boolean;
  has_anthropic: boolean;
}

export class CredentialsManager {
  private credentials: Credentials | null = null;
  private configPath: string;
  
  constructor(configPath: string = './bookmark-delta-data/credentials.json') {
    this.configPath = configPath;
  }
  
  // Load credentials from environment and config file
  async loadCredentials(): Promise<Credentials> {
    if (this.credentials) {
      return this.credentials;
    }
    
    // Load from environment variables
    const envCredentials: Credentials = {
      twitter: {
        // X.com cookies (for scraping)
        ct0: process.env.TWITTER_CT0 || process.env.X_CT0,
        auth_token: process.env.TWITTER_AUTH_TOKEN || process.env.X_AUTH_TOKEN,
        kdt: process.env.TWITTER_KDT || process.env.X_KDT,
        
        // Twitter API v2 (for official API)
        bearer_token: process.env.TWITTER_BEARER_TOKEN || process.env.X_BEARER_TOKEN,
        api_key: process.env.TWITTER_API_KEY || process.env.X_API_KEY,
        api_secret: process.env.TWITTER_API_SECRET || process.env.X_API_SECRET,
        access_token: process.env.TWITTER_ACCESS_TOKEN || process.env.X_ACCESS_TOKEN,
        access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET || process.env.X_ACCESS_TOKEN_SECRET,
      },
      openai: {
        api_key: process.env.OPENAI_API_KEY,
        organization: process.env.OPENAI_ORGANIZATION,
      },
      anthropic: {
        api_key: process.env.ANTHROPIC_API_KEY || process.env.CLAUDE_API_KEY,
      },
      last_checked: new Date().toISOString(),
      has_twitter_cookies: false,
      has_twitter_api: false,
      has_openai: false,
      has_anthropic: false,
    };
    
    // Check what credentials are available
    envCredentials.has_twitter_cookies = !!(envCredentials.twitter.ct0 && envCredentials.twitter.auth_token);
    envCredentials.has_twitter_api = !!(envCredentials.twitter.bearer_token || (envCredentials.twitter.api_key && envCredentials.twitter.api_secret));
    envCredentials.has_openai = !!envCredentials.openai.api_key;
    envCredentials.has_anthropic = !!envCredentials.anthropic.api_key;
    
    // Try to load additional credentials from config file
    try {
      const configData = await fs.readFile(this.configPath, 'utf-8');
      const fileCredentials = JSON.parse(configData);
      
      // Merge file credentials with env credentials (env takes priority)
      this.credentials = this.mergeCredentials(envCredentials, fileCredentials);
    } catch (error) {
      // Config file doesn't exist or is invalid, use env credentials
      this.credentials = envCredentials;
    }
    
    // Save current state to config file for reference
    await this.saveCredentials(this.credentials);
    
    return this.credentials;
  }
  
  // Merge two credential objects, prioritizing the first
  private mergeCredentials(priority: Credentials, fallback: Credentials): Credentials {
    return {
      twitter: { ...fallback.twitter, ...priority.twitter },
      openai: { ...fallback.openai, ...priority.openai },
      anthropic: { ...fallback.anthropic, ...priority.anthropic },
      last_checked: priority.last_checked,
      has_twitter_cookies: priority.has_twitter_cookies || fallback.has_twitter_cookies,
      has_twitter_api: priority.has_twitter_api || fallback.has_twitter_api,
      has_openai: priority.has_openai || fallback.has_openai,
      has_anthropic: priority.has_anthropic || fallback.has_anthropic,
    };
  }
  
  // Save credentials to config file (excluding sensitive data)
  private async saveCredentials(credentials: Credentials): Promise<void> {
    try {
      // Create config directory if it doesn't exist
      const configDir = path.dirname(this.configPath);
      await fs.mkdir(configDir, { recursive: true });
      
      // Save only status and non-sensitive metadata
      const configToSave = {
        last_checked: credentials.last_checked,
        has_twitter_cookies: credentials.has_twitter_cookies,
        has_twitter_api: credentials.has_twitter_api,
        has_openai: credentials.has_openai,
        has_anthropic: credentials.has_anthropic,
        twitter: {
          // Only save masked versions for debugging
          ct0: credentials.twitter.ct0 ? `${credentials.twitter.ct0.slice(0, 4)}...` : undefined,
          auth_token: credentials.twitter.auth_token ? `${credentials.twitter.auth_token.slice(0, 4)}...` : undefined,
          bearer_token: credentials.twitter.bearer_token ? `${credentials.twitter.bearer_token.slice(0, 8)}...` : undefined,
        },
        openai: {
          api_key: credentials.openai.api_key ? `${credentials.openai.api_key.slice(0, 8)}...` : undefined,
        },
        anthropic: {
          api_key: credentials.anthropic.api_key ? `${credentials.anthropic.api_key.slice(0, 8)}...` : undefined,
        }
      };
      
      await fs.writeFile(this.configPath, JSON.stringify(configToSave, null, 2));
    } catch (error) {
      console.warn('Could not save credentials config:', error);
    }
  }
  
  // Get Twitter credentials for scraping
  getTwitterScrapingCredentials(): { hasCredentials: boolean; credentials: TwitterCredentials } {
    const creds = this.credentials;
    if (!creds) {
      return { hasCredentials: false, credentials: {} };
    }
    
    return {
      hasCredentials: creds.has_twitter_cookies,
      credentials: {
        ct0: creds.twitter.ct0,
        auth_token: creds.twitter.auth_token,
        kdt: creds.twitter.kdt,
      }
    };
  }
  
  // Get Twitter API credentials
  getTwitterAPICredentials(): { hasCredentials: boolean; credentials: TwitterCredentials } {
    const creds = this.credentials;
    if (!creds) {
      return { hasCredentials: false, credentials: {} };
    }
    
    return {
      hasCredentials: creds.has_twitter_api,
      credentials: {
        bearer_token: creds.twitter.bearer_token,
        api_key: creds.twitter.api_key,
        api_secret: creds.twitter.api_secret,
        access_token: creds.twitter.access_token,
        access_token_secret: creds.twitter.access_token_secret,
      }
    };
  }
  
  // Get OpenAI credentials
  getOpenAICredentials(): { hasCredentials: boolean; credentials: OpenAICredentials } {
    const creds = this.credentials;
    if (!creds) {
      return { hasCredentials: false, credentials: {} };
    }
    
    return {
      hasCredentials: creds.has_openai,
      credentials: {
        api_key: creds.openai.api_key,
        organization: creds.openai.organization,
      }
    };
  }
  
  // Get Anthropic credentials
  getAnthropicCredentials(): { hasCredentials: boolean; credentials: { api_key?: string } } {
    const creds = this.credentials;
    if (!creds) {
      return { hasCredentials: false, credentials: {} };
    }
    
    return {
      hasCredentials: creds.has_anthropic,
      credentials: {
        api_key: creds.anthropic.api_key,
      }
    };
  }
  
  // Print credentials status
  printStatus(): void {
    if (!this.credentials) {
      console.log('❌ Credentials not loaded');
      return;
    }
    
    console.log('\n🔑 Credentials Status:');
    console.log('─'.repeat(40));
    
    // Twitter/X
    console.log('🐦 Twitter/X:');
    if (this.credentials.has_twitter_cookies) {
      console.log('  ✅ Scraping cookies (ct0, auth_token)');
    } else {
      console.log('  ❌ Scraping cookies missing');
    }
    
    if (this.credentials.has_twitter_api) {
      console.log('  ✅ API credentials (bearer token or OAuth)');
    } else {
      console.log('  ❌ API credentials missing');
    }
    
    // OpenAI
    console.log('🤖 OpenAI:');
    if (this.credentials.has_openai) {
      console.log('  ✅ API key configured');
    } else {
      console.log('  ❌ API key missing');
    }
    
    // Anthropic
    console.log('🧠 Anthropic/Claude:');
    if (this.credentials.has_anthropic) {
      console.log('  ✅ API key configured');
    } else {
      console.log('  ❌ API key missing');
    }
    
    console.log('─'.repeat(40));
    console.log(`Last checked: ${this.credentials.last_checked}\n`);
  }
  
  // Print setup instructions for missing credentials
  printSetupInstructions(): void {
    if (!this.credentials) {
      console.log('❌ Credentials not loaded');
      return;
    }
    
    let needsSetup = false;
    
    if (!this.credentials.has_twitter_cookies) {
      needsSetup = true;
      console.log(`
🐦 Twitter/X Scraping Setup (for Grok conversations):
1. Log in to X.com in your browser
2. Open Developer Tools (F12) → Application → Cookies
3. Copy these cookie values:
   export X_CT0="your_ct0_value"
   export X_AUTH_TOKEN="your_auth_token_value"
   export X_KDT="your_kdt_value"  # optional
`);
    }
    
    if (!this.credentials.has_twitter_api) {
      needsSetup = true;
      console.log(`
🔗 Twitter API Setup (for timeline fetching):
Get credentials from: https://developer.twitter.com/en/portal/dashboard
   export TWITTER_BEARER_TOKEN="your_bearer_token"
   # OR OAuth 1.0a:
   export TWITTER_API_KEY="your_api_key"
   export TWITTER_API_SECRET="your_api_secret"
   export TWITTER_ACCESS_TOKEN="your_access_token"
   export TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
`);
    }
    
    if (!this.credentials.has_openai) {
      needsSetup = true;
      console.log(`
🤖 OpenAI Setup (for AI enrichment):
Get API key from: https://platform.openai.com/api-keys
   export OPENAI_API_KEY="your_openai_key"
`);
    }
    
    if (!this.credentials.has_anthropic) {
      needsSetup = true;
      console.log(`
🧠 Anthropic Setup (for Claude AI):
Get API key from: https://console.anthropic.com/
   export ANTHROPIC_API_KEY="your_anthropic_key"
`);
    }
    
    if (!needsSetup) {
      console.log('✅ All credentials are configured!');
    }
  }
  
  // Check if specific features are available
  canScrapeGrok(): boolean {
    return this.credentials?.has_twitter_cookies || false;
  }
  
  canUseTwitterAPI(): boolean {
    return this.credentials?.has_twitter_api || false;
  }
  
  canUseAI(): boolean {
    return this.credentials?.has_openai || this.credentials?.has_anthropic || false;
  }
}

// Global instance
let globalCredentialsManager: CredentialsManager | null = null;

export function getCredentialsManager(configPath?: string): CredentialsManager {
  if (!globalCredentialsManager) {
    globalCredentialsManager = new CredentialsManager(configPath);
  }
  return globalCredentialsManager;
}

// Convenience functions
export async function checkCredentials(): Promise<Credentials> {
  const manager = getCredentialsManager();
  return await manager.loadCredentials();
}

export async function printCredentialsStatus(): Promise<void> {
  const manager = getCredentialsManager();
  await manager.loadCredentials();
  manager.printStatus();
  manager.printSetupInstructions();
}