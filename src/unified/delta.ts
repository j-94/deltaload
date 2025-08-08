import * as fs from 'fs/promises';
import * as path from 'path';
import { UnifiedRecord } from './schema';

export type DeltaType = 'added' | 'modified' | 'deleted' | 'unchanged';

export interface ManifestEntry {
  uid: string;
  hash: string;
  record_type: string;
  source: string;
  original_id?: string | null;
  last_seen_run: string; // timestamp
}

export interface Manifest {
  version: 1;
  created_at: string;
  updated_at: string;
  mode: 'snapshot' | 'append';
  entries: Record<string, ManifestEntry>; // uid -> entry
}

export interface DeltaChange {
  type: DeltaType;
  uid: string;
  hash: string;
  record: UnifiedRecord | null;
}

export class UnifiedDelta {
  constructor(private outDir: string, private mode: 'snapshot' | 'append' = 'snapshot') {}

  private manifestPath() {
    return path.join(this.outDir, 'unified-manifest.json');
  }

  async ensureOutDir() {
    await fs.mkdir(this.outDir, { recursive: true });
  }

  async loadManifest(): Promise<Manifest> {
    await this.ensureOutDir();
    try {
      const raw = await fs.readFile(this.manifestPath(), 'utf-8');
      const m: Manifest = JSON.parse(raw);
      return m;
    } catch {
      const now = new Date().toISOString();
      return { version: 1, created_at: now, updated_at: now, mode: this.mode, entries: {} };
    }
  }

  async saveManifest(m: Manifest) {
    m.updated_at = new Date().toISOString();
    await fs.writeFile(this.manifestPath(), JSON.stringify(m, null, 2));
  }

  async diffAndWrite(records: UnifiedRecord[]): Promise<{ changes: DeltaChange[]; outFile: string }> {
    const runId = new Date().toISOString().replace(/[:]/g, '-');
    const m = await this.loadManifest();

    const changes: DeltaChange[] = [];
    const seen = new Set<string>();

    for (const r of records) {
      const prev = m.entries[r.uid];
      if (!prev) {
        changes.push({ type: 'added', uid: r.uid, hash: r.hash, record: r });
      } else if (prev.hash !== r.hash) {
        changes.push({ type: 'modified', uid: r.uid, hash: r.hash, record: r });
      } else {
        changes.push({ type: 'unchanged', uid: r.uid, hash: r.hash, record: null });
      }
      m.entries[r.uid] = {
        uid: r.uid,
        hash: r.hash,
        record_type: r.record_type,
        source: r.source,
        original_id: r.original_id ?? null,
        last_seen_run: runId,
      };
      seen.add(r.uid);
    }

    if (this.mode === 'snapshot') {
      for (const uid of Object.keys(m.entries)) {
        if (!seen.has(uid) && m.entries[uid].last_seen_run !== runId) {
          // Previously seen, now missing in snapshot -> deleted
          changes.push({ type: 'deleted', uid, hash: m.entries[uid].hash, record: null });
          // Keep entry but update last_seen_run for history
          m.entries[uid].last_seen_run = runId;
        }
      }
    }

    await this.saveManifest(m);

    const outFile = path.join(this.outDir, `run-${runId}.jsonl`);
    const changeFile = path.join(this.outDir, `changes-${runId}.json`);
    const lines = records.map(r => JSON.stringify(r)).join('\n') + (records.length ? '\n' : '');
    await fs.writeFile(outFile, lines);
    await fs.writeFile(changeFile, JSON.stringify(changes, null, 2));
    return { changes, outFile };
  }
}
