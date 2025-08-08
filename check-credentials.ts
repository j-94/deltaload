#!/usr/bin/env bun

import { printCredentialsStatus, getCredentialsManager } from './credentials-manager';

async function main() {
  const args = process.argv.slice(2);
  
  if (args.includes('--help') || args.includes('-h')) {
    console.log(`
Credentials Checker for Bookmark ETL System

Usage: bun check-credentials.ts [options]

Options:
  --setup    Show setup instructions for missing credentials
  --test     Test credential functionality
  --config   Show config file location
  
This tool checks for:
  🐦 Twitter/X scraping cookies (ct0, auth_token)
  🔗 Twitter API credentials (bearer token, OAuth)
  🤖 OpenAI API key
  🧠 Anthropic/Claude API key
`);
    process.exit(0);
  }
  
  console.log('🔍 Checking Credentials for Bookmark ETL System');
  console.log('='.repeat(50));
  
  const manager = getCredentialsManager();
  await manager.loadCredentials();
  
  // Always show status
  manager.printStatus();
  
  if (args.includes('--setup')) {
    manager.printSetupInstructions();
  }
  
  if (args.includes('--test')) {
    console.log('\n🧪 Testing Credential Functionality:');
    console.log('─'.repeat(40));
    
    // Test Grok scraping capability
    if (manager.canScrapeGrok()) {
      console.log('✅ Can scrape Grok conversations');
    } else {
      console.log('❌ Cannot scrape Grok conversations (need X.com cookies)');
    }
    
    // Test Twitter API capability
    if (manager.canUseTwitterAPI()) {
      console.log('✅ Can use Twitter API');
    } else {
      console.log('❌ Cannot use Twitter API (need API credentials)');
    }
    
    // Test AI capability
    if (manager.canUseAI()) {
      console.log('✅ Can use AI enrichment');
    } else {
      console.log('❌ Cannot use AI enrichment (need OpenAI or Anthropic key)');
    }
    
    console.log('─'.repeat(40));
  }
  
  if (args.includes('--config')) {
    console.log('\n📁 Configuration:');
    console.log('─'.repeat(40));
    console.log(`Config file: ./bookmark-delta-data/credentials.json`);
    console.log(`Environment: Loaded from process.env`);
    console.log(`Priority: Environment variables override config file`);
    console.log('─'.repeat(40));
  }
  
  // Summary
  const credentials = await manager.loadCredentials();
  const capabilities = [];
  
  if (credentials.has_twitter_cookies) capabilities.push('Grok Scraping');
  if (credentials.has_twitter_api) capabilities.push('Twitter API');
  if (credentials.has_openai) capabilities.push('OpenAI');
  if (credentials.has_anthropic) capabilities.push('Anthropic');
  
  console.log('\n📊 Summary:');
  console.log(`Available capabilities: ${capabilities.length > 0 ? capabilities.join(', ') : 'None'}`);
  
  if (capabilities.length === 0) {
    console.log('\n⚠️  No credentials configured. Run with --setup for instructions.');
  } else if (capabilities.length < 4) {
    console.log('\n💡 Tip: Run with --setup to configure additional services.');
  } else {
    console.log('\n🎉 All services configured! Ready to run full ETL pipeline.');
  }
}

if (import.meta.main) {
  main().catch(console.error);
}