import { mutation } from "convex/server"

export const upsertBookmarkMinimal = mutation({
  args: { record: "any" },
  handler: async (ctx, { record }) => {
    const existing = await ctx.db
      .query("bookmarks_min")
      .withIndex("byUid", (q) => q.eq("uid", record.uid))
      .unique()
    const now = Date.now()
    if (!existing) {
      await ctx.db.insert("bookmarks_min", { ...record, text: record.text, inserted_at: now })
      return { inserted: 1, updated: 0 }
    } else {
      if (existing.content_hash !== record.content_hash || record.created_at_ms < (existing.created_at_ms || Number.MAX_SAFE_INTEGER)) {
        await ctx.db.patch(existing._id, { ...record, text: record.text })
        return { inserted: 0, updated: 1 }
      }
      return { inserted: 0, updated: 0 }
    }
  },
})
