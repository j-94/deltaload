import Database from "better-sqlite3"
import { join, resolve } from "path"
import { mkdirSync } from "fs"

const envPath = process.env.VIEWER_DB_PATH
const defaultPath = resolve(process.cwd(), "../../data", "viewer.db")
const dbPath = envPath && envPath.length > 0 ? envPath : defaultPath
mkdirSync(join(dbPath, ".."), { recursive: true })

const db = new Database(dbPath)
db.pragma("journal_mode = WAL")

export default db
