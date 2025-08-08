#!/usr/bin/env bun
import * as fs from 'fs/promises';
import * as path from 'path';

async function latestRunFiles(dir: string) {
  const files = await fs.readdir(dir);
  const runs = files.filter(f => f.startsWith('run-') && f.endsWith('.jsonl')).sort();
  const changes = files.filter(f => f.startsWith('changes-') && f.endsWith('.json')).sort();
  const manifest = path.join(dir, 'unified-manifest.json');
  return {
    run: runs.length ? path.join(dir, runs[runs.length - 1]) : null,
    changes: changes.length ? path.join(dir, changes[changes.length - 1]) : null,
    manifest: await exists(manifest) ? manifest : null,
    allRuns: runs.map(f => path.join(dir, f))
  };
}

async function exists(p: string) {
  try { await fs.access(p); return true; } catch { return false; }
}

async function readJsonl(file: string) {
  const raw = await fs.readFile(file, 'utf-8');
  return raw.split('\n').filter(Boolean).map(l => JSON.parse(l));
}

async function main() {
  const dir = process.argv[2] || './unified';
  const { run, changes, manifest, allRuns } = await latestRunFiles(dir);
  if (!run) {
    console.error(`No run-*.jsonl found in ${dir}`);
    process.exit(1);
  }

  const records = await readJsonl(run);
  const byType: Record<string, number> = {};
  const bySource: Record<string, number> = {};
  let withCreated = 0;
  const byDay: Record<string, number> = {};
  for (const r of records) {
    byType[r.record_type] = (byType[r.record_type] || 0) + 1;
    bySource[r.source] = (bySource[r.source] || 0) + 1;
    if (r.created_at) {
      withCreated++;
      const day = String(r.created_at).slice(0, 10);
      byDay[day] = (byDay[day] || 0) + 1;
    }
  }

  let changeCounts: Record<string, number> = {};
  if (changes) {
    const ch = JSON.parse(await fs.readFile(changes, 'utf-8')) as any[];
    for (const c of ch) changeCounts[c.type] = (changeCounts[c.type] || 0) + 1;
  }

  const manifestData = manifest ? JSON.parse(await fs.readFile(manifest, 'utf-8')) : null;
  const report = {
    params: {
      dir,
      mode: manifestData?.mode ?? 'unknown',
      runs_total: allRuns.length,
    },
    files: { run, changes: changes ?? null, manifest: manifest ?? null },
    stats: {
      total_records: records.length,
      by_type: byType,
      by_source: bySource,
      created_at_coverage: `${withCreated}/${records.length}`,
      by_day: Object.fromEntries(Object.entries(byDay).sort(([a],[b]) => a.localeCompare(b))),
      changes: changeCounts,
    }
  };

  console.log(JSON.stringify(report, null, 2));

  // Write a friendly markdown snapshot
  const md = `# Unified Data Report\n\n` +
    `Dir: ${dir}\n\n` +
    `## Params\n- Mode: ${report.params.mode}\n- Runs: ${report.params.runs_total}\n\n` +
    `## Files\n- run: ${report.files.run}\n- changes: ${report.files.changes}\n- manifest: ${report.files.manifest}\n\n` +
    `## Totals\n- Records: ${report.stats.total_records}\n- Created_at coverage: ${report.stats.created_at_coverage}\n\n` +
    `## By Type\n` + Object.entries(report.stats.by_type).map(([k,v]) => `- ${k}: ${v}`).join('\n') + '\n\n' +
    `## By Source\n` + Object.entries(report.stats.by_source).map(([k,v]) => `- ${k}: ${v}`).join('\n') + '\n\n' +
    `## Changes\n` + Object.entries(report.stats.changes).map(([k,v]) => `- ${k}: ${v}`).join('\n') + '\n\n';

  await fs.writeFile(path.join(dir, 'REPORT.md'), md);
}

if (import.meta.main) {
  main().catch(err => { console.error(err); process.exit(1); });
}
