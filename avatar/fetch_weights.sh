#!/usr/bin/env bash
# Usage: fetch_weights.sh <prefix> <root>  — downloads weights.lock entries whose dest starts with <prefix>, verifies sha256, aborts on mismatch.
set -euo pipefail
prefix=$1; root=$2; lock="$(dirname "$0")/weights.lock"
grep -v '^#' "$lock" | while read -r dest sha url; do
  case "$dest" in "$prefix"/*) ;; *) continue;; esac
  out="$root/${dest#"$prefix"/}"; mkdir -p "$(dirname "$out")"
  curl -fsSL --retry 3 --proto '=https' -o "$out" "$url"
  echo "$sha  $out" | sha256sum -c --quiet - || { echo "CHECKSUM MISMATCH: $dest"; rm -f "$out"; exit 1; }
  echo "verified $dest"
done
