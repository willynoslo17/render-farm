#!/usr/bin/env bash
# Usage: install-mac.sh <opentoonz|pinta|vidcutter|olive|affine>  — pinned official asset, sha256-verified, then opens installer.
# Homebrew alternative (not version-pinned): brew install --cask pinta affine opentoonz
set -euo pipefail
APP=$1; D=$(cd "$(dirname "$0")" && pwd); ARCH=$( [ "$(uname -m)" = arm64 ] && echo arm64 || echo x86_64 )
LINE=$(awk -v a="$APP" -v o="macos-$ARCH" '$1==a && $2==o' "$D/apps.lock"); [ -n "$LINE" ] || LINE=$(awk -v a="$APP" '$1==a && $2=="macos"' "$D/apps.lock")
[ -n "$LINE" ] || { echo "no macOS build for $APP"; exit 1; }
read -r _ _ SHA URL <<< "$LINE"; OUT="$HOME/Downloads/$(basename "$URL")"
curl -fsSL --proto '=https' -o "$OUT" "$URL"; echo "$SHA  $OUT" | shasum -a 256 -c - || { rm -f "$OUT"; exit 1; }
case "$OUT" in *.pkg) sudo installer -pkg "$OUT" -target / ;; *.dmg) open "$OUT" ;; esac
