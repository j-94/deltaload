import { query } from "./_generated/server"

export const listAll = query({
  args: { limit: "number?", cursor: "string?" },
  handler: async (ctx, { limit = 100 }) => {
    const results = await ctx.db.query("bookmarks_min").withIndex("byCreated").order("desc").take(limit)
    return results
  },
})

export const listBySource = query({
  args: { source: "string", limit: "number?" },
  handler: async (ctx, { source, limit = 100 }) => {
    const results = await ctx.db
      .query("bookmarks_min")
      .withIndex("bySourceCreated", (q) => q.eq("source", source))
      .order("desc")
      .take(limit)
    return results
  },
})

export const getByUid = query({
  args: { uid: "string" },
  handler: async (ctx, { uid }) => {
    const r = await ctx.db.query("bookmarks_min").withIndex("byUid", (q) => q.eq("uid", uid)).unique()
    return r
  },
})
