#!/usr/bin/env bun
import { RaindropFetcher } from '../fetchers/raindrop-fetcher';
import * as fs from 'fs/promises';
import * as path from 'path';

async function main() {
  const apiKey = process.env.RAINDROP_API_KEY;
  if (!apiKey) {
    console.error('❌ RAINDROP_API_KEY missing. Copy .env.example to .env and fill it.');
    process.exit(1);
  }
  const outDir = path.join(process.cwd(), 'raw');
  await fs.mkdir(outDir, { recursive: true });
  const date = new Date().toISOString().slice(0, 19).replace(/[:]/g, '-');
  const file = path.join(outDir, `raindrop-${date}.json`);
  const fetcher = new RaindropFetcher({ apiKey });
  await fetcher.exportToFile(file);
}

if (import.meta.main) main().catch(err => { console.error(err); process.exit(1); });

