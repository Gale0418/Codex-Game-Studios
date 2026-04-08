#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAGE_FILE="$ROOT/production/stage.txt"
ACTIVE_FILE="$ROOT/production/active.md"

stage="unknown"
lane="unknown"

if [ -f "$STAGE_FILE" ]; then
  stage="$(tr -d '\r' < "$STAGE_FILE" | head -n 1)"
fi

if [ -f "$ACTIVE_FILE" ]; then
  lane_line="$(grep -m1 '^-\s*`lane`:' "$ACTIVE_FILE" || true)"
  if [ -n "$lane_line" ]; then
    lane="${lane_line#*: }"
  fi
fi

printf 'stage=%s lane=%s\n' "$stage" "$lane"
