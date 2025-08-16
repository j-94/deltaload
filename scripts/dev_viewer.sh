#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR/apps/convex"
echo "Starting Convex dev (if not initialized yet, this may print a warning)..."
npx convex dev & 
CONVEX_PID=$!

sleep 2
CONVEX_URL="http://127.0.0.1:3210"
echo "Using Convex URL: $CONVEX_URL"

trap 'kill $CONVEX_PID >/dev/null 2>&1 || true' INT TERM EXIT
cd "$ROOT_DIR/apps/viewer"
echo "Starting viewer at http://localhost:3050 ..."
NEXT_PUBLIC_CONVEX_URL="$CONVEX_URL" npm run dev
