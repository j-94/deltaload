#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR/apps/convex"
npx convex dev & 
CONVEX_PID=$!

sleep 2
CONVEX_URL="http://127.0.0.1:3210"

trap 'kill $CONVEX_PID >/dev/null 2>&1 || true' INT TERM EXIT
cd "$ROOT_DIR/apps/viewer"
NEXT_PUBLIC_CONVEX_URL="$CONVEX_URL" npm run dev
