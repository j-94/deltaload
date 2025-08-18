import db from "./db"

export function ensureSchema() {
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
}
