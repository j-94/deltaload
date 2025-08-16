#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR/apps/convex"
echo "[dev:viewer] Starting Convex dev (if not initialized yet, it may prompt for login in an interactive terminal)..."
(npx convex dev || echo "[dev:viewer] Convex dev could not start non-interactively (login required). Run: cd apps/convex && npx convex dev") & 
CONVEX_PID=$!

sleep 2
CONVEX_URL="${CONVEX_URL:-http://127.0.0.1:3210}"
echo "[dev:viewer] Using Convex URL: $CONVEX_URL"

pick_port() {
  for p in 3050 3051 3052; do
    if ! lsof -iTCP -sTCP:LISTEN -P | grep -q ":$p"; then
      echo "$p"
      return 0
    fi
  done
  echo "3050"
}
VIEW_PORT="$(pick_port)"

trap 'kill $CONVEX_PID >/dev/null 2>&1 || true' INT TERM EXIT
cd "$ROOT_DIR/apps/viewer"
echo "[dev:viewer] Starting viewer at http://localhost:$VIEW_PORT ..."
NEXT_PUBLIC_CONVEX_URL="$CONVEX_URL" npm run dev -- -p "$VIEW_PORT"
