import { UnifiedRecord, UnifiedRecordSchema, computeContentHash, md5_12 } from './schema';

// Normalizers convert source-specific rows into UnifiedRecord

export type BookmarkInput = any; // loose, validated downstream
export type ChatUnifiedInput = any; // unified chat JSON structure

export interface NormalizeOptions {
  sourcePath: string;
}

function toIsoOrNull(v: any): string | null {
  if (v == null) return null;
  if (typeof v === 'string') return v;
  if (typeof v === 'number') {
    const ms = v > 1e12 ? v : v * 1000; // heuristic: seconds vs ms
    try { return new Date(ms).toISOString(); } catch { return String(v); }
  }
  return String(v);
}

export function normalizeBookmark(row: any, opts: NormalizeOptions): UnifiedRecord {
  const source = String(row.source || 'unknown');
  const uri = row.url || row.metadata?.canonical_url || null;
  const original_id = String(row.id ?? md5_12(uri ?? JSON.stringify(row)));
  const title = row.metadata?.title ?? row.title ?? row.name ?? null;
  const content = row.full_text ?? row.markdown ?? row.content ?? null;
  const created_at = toIsoOrNull(row.created_at ?? row.metadata?.created_at ?? null);
  const updated_at = toIsoOrNull(row.metadata?.updated_at ?? null);

  const base = {
    record_type: 'bookmark' as const,
    uid: `bm_${md5_12(`${source}:${original_id}`)}`,
    source,
    original_id,
    uri,
    title,
    content,
    created_at,
    updated_at,
    tags: Array.isArray(row.metadata?.tags) ? row.metadata.tags : [],
    metadata: row.metadata && typeof row.metadata === 'object' ? row.metadata : {},
    version: 1,
    provenance: { path: opts.sourcePath },
  };

  const hash = computeContentHash(base as any);
  const rec: UnifiedRecord = { ...(base as any), hash };
  return UnifiedRecordSchema.parse(rec);
}

// Unified chat structure -> Flatten to chat_message records
export function normalizeUnifiedChat(unified: any, opts: NormalizeOptions): UnifiedRecord[] {
  const out: UnifiedRecord[] = [];
  const conversations = Array.isArray(unified?.conversations) ? unified.conversations : [];
  for (const conv of conversations) {
    const convId: string = String(conv.id ?? conv.uuid ?? conv.original_id ?? md5_12(JSON.stringify(conv).slice(0, 256)));
    const platform: string = String(conv.platform ?? conv.provider ?? 'chat');
    const messages = Array.isArray(conv.messages) ? conv.messages : [];
    let idx = 0;
    for (const m of messages) {
      const role = m.role ?? m.author ?? 'unknown';
      const ts = toIsoOrNull(m.timestamp ?? m.created_at ?? m.time ?? null);
      const content = typeof m.content === 'string' ? m.content : m.text ?? m.body ?? null;
      const title = m.title ?? null;
      const original_id = String(m.id ?? m.uuid ?? `${convId}#${idx}`);
      const base = {
        record_type: 'chat_message' as const,
        uid: `cm_${md5_12(`${platform}:${convId}:${original_id}`)}`,
        source: platform,
        original_id,
        uri: null,
        title,
        content,
        created_at: ts,
        updated_at: ts,
        tags: role ? [String(role)] : [],
        metadata: { conversation_id: convId, role },
        version: 1,
        provenance: { path: opts.sourcePath },
      };
      const hash = computeContentHash(base as any);
      const rec = UnifiedRecordSchema.parse({ ...(base as any), hash });
      out.push(rec);
      idx++;
    }
  }
  return out;
}
