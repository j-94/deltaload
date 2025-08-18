#!/usr/bin/env node
const Database = require("better-sqlite3");
const { resolve } = require("path");

const envPath = process.env.VIEWER_DB_PATH;
const defaultPath = resolve(process.cwd(), "data", "viewer.db");
const dbPath = envPath && envPath.length > 0 ? envPath : defaultPath;

const db = new Database(dbPath);
const sources = db.prepare("SELECT source, COUNT(*) as c FROM bookmarks_min GROUP BY source ORDER BY c DESC").all();
const total = db.prepare("SELECT COUNT(*) as c FROM bookmarks_min").get().c;
const minmax = db.prepare("SELECT MIN(created_at_ms) as min, MAX(created_at_ms) as max FROM bookmarks_min").get();
console.log(JSON.stringify({ total, sources, min: minmax.min, max: minmax.max }, null, 2));
