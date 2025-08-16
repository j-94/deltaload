"use client"

import { useEffect, useMemo, useState } from "react"
import { ConvexReactClient } from "convex/react"

type Row = {
  _id?: string
  uid: string
  source: string
  created_at: string
  created_at_ms: number
  url: string
  title: string
  text: string
  content_hash: string
}

function useConvexSafe(url?: string | null) {
  const [client, setClient] = useState<ConvexReactClient | null>(null)
  useEffect(() => {
    if (!url) return
    try {
      const c = new ConvexReactClient(url)
      setClient(c)
    } catch {
      setClient(null)
    }
  }, [url])
  return client
}

export default function Page() {
  const convexUrl = typeof window !== "undefined" ? process.env.NEXT_PUBLIC_CONVEX_URL || "" : ""
  const client = useConvexSafe(convexUrl)
  const [rows, setRows] = useState<Row[]>([])
  const [loading, setLoading] = useState(false)
  const [source, setSource] = useState<string | null>(null)

  const title = useMemo(() => (source ? `Feed — ${source}` : "Feed — All"), [source])

  useEffect(() => {
    let cancelled = false
    async function fetchRows() {
      if (!client) return
      setLoading(true)
      try {
        const fnName = source ? "queries:listBySource" : "queries:listAll"
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        const result = await (client as any).query(fnName, source ? { source, limit: 200 } : { limit: 200 })
        if (!cancelled) setRows(result as Row[])
      } catch (e) {
        if (!cancelled) console.error(e)
      } finally {
        if (!cancelled) setLoading(false)
      }
    }
    fetchRows()
    const interval = setInterval(fetchRows, 4000)
    return () => {
      cancelled = true
      clearInterval(interval)
    }
  }, [client, source])

  return (
    <div style={{ display: "grid", gridTemplateRows: "auto 1fr", minHeight: "100vh" }}>
      <header style={{ padding: "12px 16px", borderBottom: "1px solid #1f1f22", display: "flex", gap: 12, alignItems: "center" }}>
        <div style={{ fontWeight: 600 }}>{title}</div>
        <div style={{ marginLeft: "auto", display: "flex", gap: 8 }}>
          <button onClick={() => setSource(null)} style={{ background: source === null ? "#2a2a2f" : "transparent", color: "#e6e7ea", border: "1px solid #2a2a2f", borderRadius: 6, padding: "6px 10px" }}>All</button>
          <button onClick={() => setSource("raindrop")} style={{ background: source === "raindrop" ? "#2a2a2f" : "transparent", color: "#e6e7ea", border: "1px solid #2a2a2f", borderRadius: 6, padding: "6px 10px" }}>Raindrop</button>
          <button onClick={() => setSource("github")} style={{ background: source === "github" ? "#2a2a2f" : "transparent", color: "#e6e7ea", border: "1px solid #2a2a2f", borderRadius: 6, padding: "6px 10px" }}>GitHub</button>
          <button onClick={() => setSource("chat")} style={{ background: source === "chat" ? "#2a2a2f" : "transparent", color: "#e6e7ea", border: "1px solid #2a2a2f", borderRadius: 6, padding: "6px 10px" }}>Chat</button>
          <button onClick={() => setSource("twitter")} style={{ background: source === "twitter" ? "#2a2a2f" : "transparent", color: "#e6e7ea", border: "1px solid #2a2a2f", borderRadius: 6, padding: "6px 10px" }}>Twitter</button>
        </div>
      </header>
      <main style={{ padding: 16 }}>
        {!convexUrl ? (
          <div style={{ color: "#f0c" }}>Set NEXT_PUBLIC_CONVEX_URL in apps/viewer/.env.local</div>
        ) : loading && rows.length === 0 ? (
          <div>Loading…</div>
        ) : rows.length === 0 ? (
          <div>No rows yet.</div>
        ) : (
          <div style={{ display: "grid", gap: 12 }}>
            {rows.map((r) => (
              <article key={r.uid} style={{ border: "1px solid #1f1f22", borderRadius: 10, padding: 12, background: "#0f0f12" }}>
                <div style={{ fontSize: 12, opacity: 0.8, marginBottom: 6 }}>
                  <span style={{ textTransform: "uppercase", letterSpacing: 0.6 }}>{r.source}</span>
                  <span style={{ marginLeft: 8 }}>{new Date(r.created_at).toLocaleString()}</span>
                </div>
                <div style={{ fontWeight: 600, marginBottom: 6 }}>
                  {r.url ? <a href={r.url} target="_blank" rel="noreferrer" style={{ color: "#8ab4ff", textDecoration: "none" }}>{r.title || r.url}</a> : (r.title || "(no title)")}
                </div>
                {r.text ? <div style={{ whiteSpace: "pre-wrap", color: "#c9cbd1" }}>{r.text.slice(0, 500)}</div> : null}
              </article>
            ))}
          </div>
        )}
      </main>
    </div>
  )
}
