#!/usr/bin/env bun
import * as fs from 'fs/promises';
import * as path from 'path';
import { normalizeBookmark, normalizeUnifiedChat } from '../unified/normalize';
import { UnifiedDelta } from '../unified/delta';

function usage() {
  console.log(`
Unified Delta Loader

Usage: bun src/cli/unified.ts [--out DIR] [--mode snapshot|append] <type>:<path>

Types:
  bookmark:<file.json|file.jsonl>     Process bookmarks JSON/JSONL (raindrop/github/twitter shapes)
  chat_unified:<file.json>            Process unified chat JSON (with conversations[])

Examples:
  bun src/cli/unified.ts bookmark:/path/to/processed_bookmarks_for_docetl.jsonl
  bun src/cli/unified.ts chat_unified:/path/to/unified_chat.json
  bun src/cli/unified.ts --out ./unified --mode snapshot bookmark:more-bookmarks.jsonl chat_unified:../Donkeyv1/.../unified_chat.json
`);
}

async function readJsonl(file: string): Promise<any[]> {
  const raw = await fs.readFile(file, 'utf-8');
  const out: any[] = [];
  for (const line of raw.split('\n')) {
    if (!line.trim()) continue;
    try { out.push(JSON.parse(line)); } catch { /* ignore */ }
  }
  return out;
}

async function main() {
  const args = process.argv.slice(2);
  if (args.length === 0 || args.includes('--help') || args.includes('-h')) return usage();

  let outDir = path.join(process.cwd(), 'unified');
  let mode: 'snapshot' | 'append' = 'snapshot';
  const inputs: { kind: 'bookmark' | 'chat_unified'; file: string }[] = [];

  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a === '--out') { outDir = args[++i]; continue; }
    if (a === '--mode') { const v = args[++i]; mode = v === 'append' ? 'append' : 'snapshot'; continue; }
    const [kind, file] = a.split(':');
    if (!file) continue;
    if (kind === 'bookmark' || kind === 'chat_unified') inputs.push({ kind, file });
  }

  if (inputs.length === 0) { usage(); process.exit(1); }

  const normalized = [] as any[];
  for (const inp of inputs) {
    if (inp.kind === 'bookmark') {
      const rows = inp.file.endsWith('.jsonl') ? await readJsonl(inp.file) : JSON.parse(await fs.readFile(inp.file, 'utf-8'));
      const arr = Array.isArray(rows) ? rows : [rows];
      for (const r of arr) normalized.push(normalizeBookmark(r, { sourcePath: inp.file }));
    } else if (inp.kind === 'chat_unified') {
      const json = JSON.parse(await fs.readFile(inp.file, 'utf-8'));
      normalized.push(...normalizeUnifiedChat(json, { sourcePath: inp.file }));
    }
  }

  const delta = new UnifiedDelta(outDir, mode);
  const { changes, outFile } = await delta.diffAndWrite(normalized);
  const summary = {
    outFile,
    counts: changes.reduce((acc, c) => { acc[c.type] = (acc[c.type] || 0) + 1; return acc; }, {} as Record<string, number>),
    total: changes.length,
  };
  console.log(JSON.stringify(summary, null, 2));
}

if (import.meta.main) {
  main().catch(err => { console.error(err); process.exit(1); });
}
