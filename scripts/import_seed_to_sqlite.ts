#!/usr/bin/env bun
import { createInterface } from "readline"
import { createReadStream, mkdirSync } from "fs"
import { join, dirname } from "path"
import Database from "better-sqlite3"

const preview = process.argv[2] || "reports/seed_preview.jsonl"
const dbPath = join(process.cwd(), "data", "viewer.db")
mkdirSync(dirname(dbPath), { recursive: true })
const db = new Database(dbPath)
db.pragma("journal_mode = WAL")
db.exec(`
  CREATE TABLE IF NOT EXISTS bookmarks_min (
    uid TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    created_at TEXT NOT NULL,
    created_at_ms INTEGER NOT NULL,
    url TEXT NOT NULL,
    title TEXT NOT NULL,
    text TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    inserted_at_ms INTEGER NOT NULL
  );
  CREATE INDEX IF NOT EXISTS idx_bookmarks_created ON bookmarks_min(created_at_ms DESC);
  CREATE INDEX IF NOT EXISTS idx_bookmarks_source_created ON bookmarks_min(source, created_at_ms DESC);
`)
const upsert = db.prepare(`
  INSERT INTO bookmarks_min(uid, source, created_at, created_at_ms, url, title, text, content_hash, inserted_at_ms)
  VALUES (@uid, @source, @created_at, @created_at_ms, @url, @title, @text, @content_hash, @now)
  ON CONFLICT(uid) DO UPDATE SET
    source=excluded.source,
    created_at=excluded.created_at,
    created_at_ms=excluded.created_at_ms,
    url=excluded.url,
    title=excluded.title,
    text=excluded.text,
    content_hash=excluded.content_hash
`)
async function run() {
  const rl = createInterface({ input: createReadStream(preview), crlfDelay: Infinity })
  let inserted = 0
  let total = 0
  const now = Date.now()
  for await (const line of rl) {
    const s = line.trim()
    if (!s) continue
    let obj: any
    try {
      obj = JSON.parse(s)
    } catch {
      continue
    }
    const rec = {
      uid: obj.uid,
      source: obj.source,
      created_at: obj.created_at,
      created_at_ms: obj.created_at_ms,
      url: obj.url,
      title: obj.title || "",
      text: obj.main_text || obj.text || "",
      content_hash: obj.content_hash,
      now,
    }
    const info = upsert.run(rec)
    if (info.changes === 1) inserted += 1
    total += 1
    if (total % 500 === 0) {
      console.log(JSON.stringify({ progressed: total }))
    }
  }
  console.log(JSON.stringify({ inserted, total }))
}
run()
