import { mutation } from "./_generated/server"
import { v } from "convex/values"

export const upsertBookmarkMinimal = mutation({
  args: {
    record: v.object({
      uid: v.string(),
      source: v.string(),
      created_at: v.string(),
      created_at_ms: v.number(),
      url: v.string(),
      title: v.string(),
      text: v.string(),
      content_hash: v.string(),
    }),
  },
  handler: async (ctx, { record }) => {
    const existing = await ctx.db
      .query("bookmarks_min")
      .withIndex("byUid", (q) => q.eq("uid", record.uid))
      .unique()
    const now = Date.now()
    if (!existing) {
      await ctx.db.insert("bookmarks_min", { ...record, inserted_at: now })
      return { inserted: 1, updated: 0 }
    } else {
      if (
        existing.content_hash !== record.content_hash ||
        record.created_at_ms < (existing.created_at_ms || Number.MAX_SAFE_INTEGER)
      ) {
        await ctx.db.patch(existing._id, { ...record })
        return { inserted: 0, updated: 1 }
      }
      return { inserted: 0, updated: 0 }
    }
  },
})
