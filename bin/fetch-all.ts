#!/usr/bin/env bun
import * as fs from 'fs/promises';
import * as path from 'path';
import { $ } from 'bun';

async function pickLatest(dir: string, prefix: string): Promise<string | null> {
  try {
    const files = (await fs.readdir(dir)).filter(f => f.startsWith(prefix)).sort();
    if (!files.length) return null;
    return path.join(dir, files[files.length - 1]);
  } catch {
    return null;
  }
}

async function main() {
  const rawDir = path.join(process.cwd(), 'raw');
  await fs.mkdir(rawDir, { recursive: true });

  // 1) Fetch sources if credentials exist
  if (process.env.RAINDROP_API_KEY) {
    try {
      await $`bun bin/fetch-raindrop.ts`;
    } catch (e) {
      console.warn('⚠️  Raindrop fetch failed, continuing:', e instanceof Error ? e.message : e);
    }
  } else {
    console.log('ℹ️  Skip Raindrop (RAINDROP_API_KEY not set)');
  }
  if (process.env.GITHUB_TOKEN) {
    try {
      await $`bun bin/fetch-github-stars.ts`;
    } catch (e) {
      console.warn('⚠️  GitHub fetch failed, continuing:', e instanceof Error ? e.message : e);
    }
  } else {
    console.log('ℹ️  Skip GitHub (GITHUB_TOKEN not set)');
  }

  // 2) Prepare inputs for unified CLI
  const inputs: string[] = [];
  const latestRaindrop = await pickLatest(rawDir, 'raindrop-');
  const latestGitHub = await pickLatest(rawDir, 'github-stars-');
  if (latestRaindrop) inputs.push(`bookmark:${latestRaindrop}`);
  if (latestGitHub) inputs.push(`bookmark:${latestGitHub}`);

  const unifiedChatPath = process.env.UNIFIED_CHAT_PATH;
  if (unifiedChatPath) inputs.push(`chat_unified:${unifiedChatPath}`);

  if (!inputs.length) {
    console.log('❌ No inputs found; set credentials and/or UNIFIED_CHAT_PATH');
    process.exit(1);
  }

  // 3) Run unified delta snapshot
  await $`bun src/cli/unified.ts --out ./unified --mode snapshot ${inputs}`;

  // 4) Verify + Report
  try {
    await $`bun src/cli/verify.ts ./unified`;
  } catch (e) {
    console.warn('⚠️  Verify reported issues (continuing):', e instanceof Error ? e.message : e);
  }
  try {
    await $`bun src/cli/report.ts ./unified`;
  } catch (e) {
    console.warn('⚠️  Report failed (continuing):', e instanceof Error ? e.message : e);
  }
}

if (import.meta.main) main().catch(err => { console.error(err); process.exit(1); });
