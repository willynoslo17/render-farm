#!/usr/bin/env bash
# Usage: install-linux.sh <opentoonz|pinta|vidcutter|olive|affine|azpainter>   — sha256-verified / commit-pinned
set -euo pipefail
APP=$1; D=$(cd "$(dirname "$0")" && pwd); DEST=${DEST:-$HOME/Applications}; mkdir -p "$DEST"
case "$APP" in
  opentoonz|pinta)
    ID=$( [ "$APP" = opentoonz ] && echo io.github.OpenToonz || echo com.github.PintaProject.Pinta )
    C=$(awk -v i="$ID" '$1==i{print $2}' "$D/flatpak.lock")
    flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
    flatpak install --user -y --noninteractive flathub "$ID"
    flatpak update --user -y --noninteractive --commit="$C" "$ID"; flatpak mask --user "$ID"   # stay pinned
    echo "installed $ID @ $C";;
  azpainter)  # upstream ships source only (Linux)
    read -r _ _ SHA URL < <(awk '$1=="azpainter" && $2=="linux-src"' "$D/apps.lock")
    T=$(mktemp -d); curl -fsSL --proto '=https' -o "$T/src.tgz" "$URL"; echo "$SHA  $T/src.tgz" | sha256sum -c -
    tar -xzf "$T/src.tgz" -C "$T"; cd "$T"/azpainter-*; ./configure && cd build && make -j"$(nproc)" && sudo make install;;
  *)
    LINE=$(awk -v a="$APP" '$1==a && $2=="linux"' "$D/apps.lock"); [ -n "$LINE" ] || { echo "no linux build for $APP"; exit 1; }
    read -r _ _ SHA URL <<< "$LINE"; OUT="$DEST/$(basename "$URL")"; curl -fsSL --proto '=https' -o "$OUT" "$URL"
    echo "$SHA  $OUT" | sha256sum -c - || { rm -f "$OUT"; exit 1; }; chmod +x "$OUT"; echo "installed $OUT";;
esac
