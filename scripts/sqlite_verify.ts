#!/usr/bin/env bun
import Database from "better-sqlite3"
import { join } from "path"

const db = new Database(join(process.cwd(), "data", "viewer.db"))
const total = db.prepare("SELECT COUNT(*) as c FROM bookmarks_min").get().c as number
const sources = db.prepare("SELECT source, COUNT(*) as c FROM bookmarks_min GROUP BY source ORDER BY c DESC").all() as {
  source: string
  c: number
}[]
const range = db.prepare("SELECT MIN(created_at_ms) as min, MAX(created_at_ms) as max FROM bookmarks_min").get() as {
  min: number
  max: number
}
console.log(JSON.stringify({ total, sources, min: range.min, max: range.max }, null, 2))
