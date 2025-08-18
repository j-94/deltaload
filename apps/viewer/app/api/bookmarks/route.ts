export const runtime = "nodejs"

import { NextRequest } from "next/server"
import db from "../../../lib/db"
import { ensureSchema } from "../../../lib/schema"

ensureSchema()

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url)
  const source = searchParams.get("source")
  const limit = Math.min(Number(searchParams.get("limit") ?? "100"), 500)
  const offset = Number(searchParams.get("offset") ?? "0")

  if (source) {
    const rows = db
      .prepare(
        "SELECT uid, source, created_at, created_at_ms, url, title, text FROM bookmarks_min WHERE source=? ORDER BY created_at_ms DESC LIMIT ? OFFSET ?"
      )
      .all(source, limit, offset)
    return new Response(JSON.stringify({ rows }), { headers: { "Content-Type": "application/json" } })
  } else {
    const rows = db
      .prepare(
        "SELECT uid, source, created_at, created_at_ms, url, title, text FROM bookmarks_min ORDER BY created_at_ms DESC LIMIT ? OFFSET ?"
      )
      .all(limit, offset)
    return new Response(JSON.stringify({ rows }), { headers: { "Content-Type": "application/json" } })
  }
}
