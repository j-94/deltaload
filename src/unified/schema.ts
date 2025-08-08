import { z } from 'zod';
import { createHash } from 'crypto';

// Unified record schema that can represent bookmarks, chat messages, files, etc.
export const UnifiedRecordSchema = z.object({
  record_type: z.enum(['bookmark', 'chat_message', 'conversation', 'file', 'note']).describe('Entity type'),
  uid: z.string().min(1).describe('Stable unique id per record'),
  source: z.string().min(1).describe('Origin system e.g. raindrop|chatgpt|claude|github'),
  original_id: z.string().nullable().optional(),
  uri: z.string().nullable().optional(),
  title: z.string().nullable().optional(),
  content: z.string().nullable().optional(),
  created_at: z.string().nullable().optional(),
  updated_at: z.string().nullable().optional(),
  tags: z.array(z.string()).default([]),
  metadata: z.record(z.any()).default({}),
  // Delta tracking
  hash: z.string().min(32).describe('sha256 of core content fields'),
  version: z.number().int().default(1),
  provenance: z
    .object({
      path: z.string(),
      offset: z.number().int().optional(),
      extra: z.record(z.any()).optional(),
    })
    .strict(),
});

export type UnifiedRecord = z.infer<typeof UnifiedRecordSchema>;

export function sha256(input: string): string {
  return createHash('sha256').update(input).digest('hex');
}

export function md5_12(input: string): string {
  return createHash('md5').update(input).digest('hex').slice(0, 12);
}

// Compute a canonical content hash to detect deltas
export function computeContentHash(r: Omit<UnifiedRecord, 'hash'>): string {
  const core = {
    record_type: r.record_type,
    uid: r.uid,
    title: r.title ?? '',
    content: r.content ?? '',
    uri: r.uri ?? '',
    created_at: r.created_at ?? '',
    updated_at: r.updated_at ?? '',
    source: r.source,
  };
  return sha256(JSON.stringify(core));
}
