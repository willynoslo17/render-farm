# Desktop apps (GUI) — pinned + sha256-verified
| App | Version | License | Windows | macOS | Linux | Headless job |
|---|---|---|---|---|---|---|
| OpenToonz | 1.8.0 | BSD-3 (modified) | .exe | .pkg | Flatpak @commit | `toonz_render` (tcomposer) |
| Pinta | 3.1.2 | MIT | .exe | .dmg (arm64/x86_64) | Flatpak @commit | none (no CLI) |
| VidCutter | 6.0.5.1 | GPL-3.0 | .exe | .dmg | AppImage | none (no CLI; use `mux`/ffmpeg) |
| Olive | 0.2.0-nightly (8ac191ce/ea47e4d8; no stable 0.2) | GPL-3.0 | .exe | .dmg | AppImage | none (no CLI export) |
| AFFiNE | 0.27.4 | MIT (client) | .exe | .dmg | AppImage | none |
| AzPainter | 3.0.12 | GPL-3.0 | – | – | source build | none |

Install: `desktop/install-windows.ps1 -App pinta` · `desktop/install-mac.sh pinta` · `desktop/install-linux.sh pinta`.
Download mirror: Actions → "desktop-mirror" → Run (creates release `desktop-apps-2026-10-12` with the same files + SHA256SUMS).
Upstream is the source of truth: every file is re-verified against `apps.lock` before mirroring; GPL apps' source is linked in the release notes.
