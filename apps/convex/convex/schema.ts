import { defineSchema, defineTable } from "convex/server"

export default defineSchema({
  bookmarks_min: defineTable({
    uid: "string",
    source: "string",
    created_at: "string",
    created_at_ms: "number",
    url: "string",
    title: "string",
    text: "string",
    content_hash: "string",
    inserted_at: "number",
  })
    .index("byCreated", ["created_at_ms"])
    .index("bySourceCreated", ["source", "created_at_ms"])
    .uniqueIndex("byUid", ["uid"]),
})
