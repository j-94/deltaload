#!/usr/bin/env bun
declare const process: any
import { readFileSync } from "fs"
import { createInterface } from "readline"
import { createReadStream } from "fs"
import { join } from "path"

type Minimal = { uid: string; source: string; created_at: string; created_at_ms: number; url: string; title: string; main_text: string; content_hash: string; file?: string }
type UpsertFn = (rec: { uid: string; source: string; created_at: string; created_at_ms: number; url: string; title: string; text: string; content_hash: string }) => Promise<{ inserted: number; updated: number }>

async function loadSeedPreview(path: string): Promise<Minimal[]> {
  const rows: Minimal[] = []
  const rl = createInterface({ input: createReadStream(path), crlfDelay: Infinity })
  for await (const line of rl) {
    const s = line.trim()
    if (!s) continue
    try {
      const obj = JSON.parse(s)
      rows.push(obj)
    } catch {}
  }
  return rows
}

async function run() {
  const args = process.argv.slice(2)
  const dryRun = args.includes("--dry-run")
  const previewPathIdx = args.findIndex((a: string) => a === "--preview")
  const previewPath = previewPathIdx >= 0 ? args[previewPathIdx + 1] : join("reports", "seed_preview.jsonl")
  const limitIdx = args.findIndex((a: string) => a === "--limit")
  const limit = limitIdx >= 0 ? Number(args[limitIdx + 1]) : undefined
  const seed = await loadSeedPreview(previewPath)
  const toSend = typeof limit === "number" ? seed.slice(0, limit) : seed
  let inserted = 0
  let updated = 0
  if (dryRun) {
    console.log(JSON.stringify({ dryRun: true, count: toSend.length }))
    return
  }
  const convexUrl = process.env.CONVEX_URL || ""
  if (!convexUrl) {
    console.error("Missing CONVEX_URL")
    process.exit(1)
  }
  const { ConvexHttpClient } = await import("convex/browser")
  const client = new ConvexHttpClient(convexUrl)
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const setAuth = (client as any).setAuth?.bind(client)
  const token = process.env.CONVEX_AUTH_TOKEN
  if (setAuth && token) {
    setAuth(async () => token)
  }
  const upsert: UpsertFn = async (rec) => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const res = await (client as any).mutation("mutations:upsertBookmarkMinimal", { record: rec })
    return res as { inserted: number; updated: number }
  }
  const batchSize = 200
  for (let i = 0; i < toSend.length; i += batchSize) {
    const batch = toSend.slice(i, i + batchSize)
    const results = await Promise.all(
      batch.map((m) =>
        upsert({
          uid: m.uid,
          source: m.source,
          created_at: m.created_at,
          created_at_ms: m.created_at_ms,
          url: m.url,
          title: m.title,
          text: m.main_text,
          content_hash: m.content_hash,
        })
      )
    )
    for (const r of results) {
      inserted += r.inserted
      updated += r.updated
    }
    console.log(JSON.stringify({ progressed: Math.min(i + batch.length, toSend.length) }))
  }
  console.log(JSON.stringify({ inserted, updated }))
}
run()
