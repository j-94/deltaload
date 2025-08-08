import * as fs from 'fs/promises';
import * as path from 'path';
import { UnifiedRecordSchema } from '../unified/schema';

export interface VerifyReport {
  files_checked: string[];
  total_records: number;
  by_type: Record<string, number>;
  unique_uids: number;
  duplicate_uids: string[];
  schema_errors: { file: string; line: number; error: string }[];
}

export async function verifyUnifiedDir(dir: string): Promise<VerifyReport> {
  const files = (await fs.readdir(dir))
    .filter(f => f.startsWith('run-') && f.endsWith('.jsonl'))
    .map(f => path.join(dir, f))
    .sort();

  const seen = new Set<string>();
  const dupes = new Set<string>();
  const byType: Record<string, number> = {};
  const schemaErrors: VerifyReport['schema_errors'] = [];
  let total = 0;

  for (const file of files) {
    const raw = await fs.readFile(file, 'utf-8');
    const lines = raw.split('\n').filter(Boolean);
    let lineNo = 0;
    for (const line of lines) {
      lineNo++;
      try {
        const obj = JSON.parse(line);
        const rec = UnifiedRecordSchema.parse(obj);
        total++;
        byType[rec.record_type] = (byType[rec.record_type] || 0) + 1;
        if (seen.has(rec.uid)) dupes.add(rec.uid);
        seen.add(rec.uid);
      } catch (e: any) {
        schemaErrors.push({ file, line: lineNo, error: String(e?.message || e) });
      }
    }
  }

  return {
    files_checked: files,
    total_records: total,
    by_type: byType,
    unique_uids: seen.size,
    duplicate_uids: Array.from(dupes),
    schema_errors: schemaErrors,
  };
}

// CLI
if (import.meta.main) {
  const dir = process.argv[2] || './unified';
  verifyUnifiedDir(dir)
    .then(r => {
      console.log(JSON.stringify(r, null, 2));
      if (r.schema_errors.length > 0) process.exitCode = 2;
      if (r.duplicate_uids.length > 0) process.exitCode = 3;
    })
    .catch(err => {
      console.error('Verify failed:', err);
      process.exit(1);
    });
}
