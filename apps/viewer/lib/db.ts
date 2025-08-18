import Database from "better-sqlite3"
import { join } from "path"
import { mkdirSync } from "fs"

const dbPath = join(process.cwd(), "data", "viewer.db")
mkdirSync(join(process.cwd(), "data"), { recursive: true })

const db = new Database(dbPath)
db.pragma("journal_mode = WAL")

export default db
