#!/usr/bin/env bun

import * as fs from 'fs/promises';

interface GitHubConfig {
  token: string;
  includeReadme?: boolean;
  includeForks?: boolean;
}

class GitHubFetcher {
  private config: GitHubConfig;
  private headers: HeadersInit;
  
  constructor(config: GitHubConfig) {
    this.config = {
      includeReadme: true,
      includeForks: false,
      ...config
    };
    
    this.headers = {
      'Authorization': `Bearer ${this.config.token}`,
      'Accept': 'application/vnd.github.v3+json'
    };
  }
  
  async fetchStarredRepos(): Promise<any[]> {
    const bookmarks: any[] = [];
    let page = 1;
    let hasMore = true;
    
    console.log('⭐ Fetching GitHub starred repositories...');
    
    while (hasMore) {
      const response = await fetch(
        `https://api.github.com/user/starred?per_page=100&page=${page}`,
        { headers: this.headers }
      );
      
      if (!response.ok) {
        throw new Error(`GitHub API error: ${response.status} ${response.statusText}`);
      }
      
      const repos = await response.json();
      
      if (repos.length === 0) {
        hasMore = false;
        break;
      }
      
      // Transform repos to bookmark format
      for (const repo of repos) {
        // Skip forks if configured
        if (!this.config.includeForks && repo.fork) {
          continue;
        }
        
        // Fetch README if configured
        let readmeContent = '';
        if (this.config.includeReadme) {
          readmeContent = await this.fetchReadme(repo.full_name);
        }
        
        const bookmark = {
          id: `github-${repo.id}`,
          url: repo.html_url,
          title: repo.full_name,
          description: repo.description || '',
          created_at: repo.created_at,
          source: 'github',
          metadata: {
            // Core GitHub fields
            title: repo.name,
            description: repo.description,
            domain: 'github.com',
            created_at: repo.created_at,
            updated_at: repo.updated_at,
            
            // Repository metrics
            stars: repo.stargazers_count,
            forks: repo.forks_count,
            watchers: repo.watchers_count,
            open_issues: repo.open_issues_count,
            
            // Repository details
            language: repo.language,
            license: repo.license?.name || repo.license?.spdx_id,
            topics: repo.topics || [],
            
            // Owner information
            owner: {
              login: repo.owner.login,
              avatar_url: repo.owner.avatar_url,
              type: repo.owner.type
            },
            
            // Additional metadata
            repo: repo.name,
            repo_created_at: repo.created_at,
            repo_pushed_at: repo.pushed_at,
            repo_updated_at: repo.updated_at,
            
            // Content
            has_readme: !!readmeContent,
            github_readme: readmeContent,
            readme_path: readmeContent ? 'README.md' : null,
            
            // GitHub specific
            github_id: repo.id,
            default_branch: repo.default_branch,
            homepage: repo.homepage,
            size: repo.size,
            archived: repo.archived,
            disabled: repo.disabled,
            visibility: repo.visibility,
            
            // Processing metadata
            processed_with: 'GitHubFetcher',
            github_processed_at: new Date().toISOString(),
            
            // Preserve full repo data
            ...repo
          }
        };
        
        bookmarks.push(bookmark);
      }
      
      console.log(`  Fetched page ${page}: ${repos.length} repos (total: ${bookmarks.length})`);
      
      // Check if there are more pages
      hasMore = repos.length === 100;
      page++;
      
      // Rate limiting
      if (hasMore) {
        await new Promise(resolve => setTimeout(resolve, 1000));
      }
    }
    
    return bookmarks;
  }
  
  async fetchReadme(repoFullName: string): Promise<string> {
    try {
      const response = await fetch(
        `https://api.github.com/repos/${repoFullName}/readme`,
        { 
          headers: {
            ...this.headers,
            'Accept': 'application/vnd.github.v3.raw'
          }
        }
      );
      
      if (response.ok) {
        return await response.text();
      }
    } catch (error) {
      // Silently fail for README fetch
    }
    
    return '';
  }
  
  async exportToFile(filename: string): Promise<void> {
    try {
      const bookmarks = await this.fetchStarredRepos();
      await fs.writeFile(filename, JSON.stringify(bookmarks, null, 2));
      
      console.log(`\n✅ Exported ${bookmarks.length} GitHub stars to ${filename}`);
      
      // Summary statistics
      const stats = {
        total: bookmarks.length,
        languages: [...new Set(bookmarks.map(b => b.metadata.language).filter(Boolean))],
        totalStars: bookmarks.reduce((sum, b) => sum + b.metadata.stars, 0),
        withReadme: bookmarks.filter(b => b.metadata.has_readme).length,
        archived: bookmarks.filter(b => b.metadata.archived).length
      };
      
      console.log('\n📊 Summary:');
      console.log(`  Total repositories: ${stats.total}`);
      console.log(`  Languages: ${stats.languages.length} (${stats.languages.slice(0, 5).join(', ')}${stats.languages.length > 5 ? '...' : ''})`);
      console.log(`  Total stars: ${stats.totalStars.toLocaleString()}`);
      console.log(`  With README: ${stats.withReadme}`);
      console.log(`  Archived: ${stats.archived}`);
      
    } catch (error) {
      console.error('❌ Export failed:', error);
      throw error;
    }
  }
}

// CLI usage
async function main() {
  const token = process.env.GITHUB_TOKEN;
  
  if (!token) {
    console.error('❌ Please set GITHUB_TOKEN environment variable');
    console.log('\nUsage:');
    console.log('  export GITHUB_TOKEN=your_github_token');
    console.log('  bun run github-fetcher.ts [output.json]');
    console.log('\nGet a token at: https://github.com/settings/tokens');
    process.exit(1);
  }
  
  const outputFile = process.argv[2] || `github-stars-${new Date().toISOString().split('T')[0]}.json`;
  
  const fetcher = new GitHubFetcher({ 
    token,
    includeReadme: true,
    includeForks: false
  });
  
  await fetcher.exportToFile(outputFile);
}

if (import.meta.main) {
  main().catch(console.error);
}

export { GitHubFetcher };