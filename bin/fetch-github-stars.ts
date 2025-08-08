#!/usr/bin/env bun
import * as fs from 'fs/promises';
import * as path from 'path';

async function fetchAll(token: string) {
  const headers = {
    Authorization: `Bearer ${token}`,
    Accept: 'application/vnd.github.v3+json',
  } as HeadersInit;
  const out: any[] = [];
  let page = 1;
  while (true) {
    const res = await fetch(`https://api.github.com/user/starred?per_page=100&page=${page}`, { headers });
    if (!res.ok) throw new Error(`GitHub API error ${res.status}`);
    const arr = await res.json();
    if (!Array.isArray(arr) || arr.length === 0) break;
    for (const repo of arr) {
      out.push({
        id: `github-${repo.id}`,
        url: repo.html_url,
        title: repo.full_name,
        description: repo.description || '',
        created_at: repo.created_at,
        source: 'github',
        metadata: {
          title: repo.name,
          description: repo.description,
          domain: 'github.com',
          created_at: repo.created_at,
          updated_at: repo.updated_at,
          stars: repo.stargazers_count,
          forks: repo.forks_count,
          watchers: repo.watchers_count,
          open_issues: repo.open_issues_count,
          language: repo.language,
          license: repo.license?.spdx_id,
          owner: { login: repo.owner?.login, type: repo.owner?.type, avatar_url: repo.owner?.avatar_url },
          repo: repo.full_name,
          topics: repo.topics || [],
        }
      });
    }
    page++;
    await new Promise(r => setTimeout(r, 200));
  }
  return out;
}

async function main() {
  const token = process.env.GITHUB_TOKEN;
  if (!token) {
    console.error('❌ GITHUB_TOKEN missing. Copy .env.example to .env and fill it.');
    process.exit(1);
  }
  const outDir = path.join(process.cwd(), 'raw');
  await fs.mkdir(outDir, { recursive: true });
  const date = new Date().toISOString().slice(0, 19).replace(/[:]/g, '-');
  const file = path.join(outDir, `github-stars-${date}.json`);
  console.log('⭐ Fetching GitHub starred repos...');
  const data = await fetchAll(token);
  await fs.writeFile(file, JSON.stringify(data, null, 2));
  console.log(`✅ Saved ${data.length} repos to ${file}`);
}

if (import.meta.main) main().catch(err => { console.error(err); process.exit(1); });

