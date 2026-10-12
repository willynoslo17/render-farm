# Media tools licenses (verified 2026-10-12). Not legal advice.
Rule of thumb: GPL/MPL/AGPL **applications** don't restrict what you produce with them (your ads/photos/videos are yours); they only matter if you redistribute or (AGPL) network-serve a *modified* version. ML **weights** are judged by their own license + training-data terms.

| Tool | Code license (quote/URL) | Weights / data | Commercial output | Box install | Headless job |
|---|---|---|---|---|---|
| darktable 5.0.1 (box) / Ubuntu 24.04 pkg (CI) | GPL-3.0 — https://github.com/darktable-org/darktable/blob/master/LICENSE | – | Yes | apt | `raw2jpg` |
| Hugin 2024.0.1 | GPL-2.0+ — https://hugin.sourceforge.io | – | Yes | apt | `panorama` |
| LibreOffice Impress 25.2 | MPL-2.0 — https://www.libreoffice.org/about-us/licenses | – | Yes | apt | `office2pdf` |
| MKVToolNix 92.0 | GPL-2.0 — https://mkvtoolnix.download/doc/COPYING.txt | – | Yes | apt | `mux` |
| AzPainter | GPL-3.0 — https://gitlab.com/azelpg/azpainter | – | Yes | flatpak | – (GUI) |
| Marp CLI 4.5.1 | MIT — https://github.com/marp-team/marp-cli/blob/main/LICENSE | – | Yes | npm -g | `marp` |
| OpenToonz 1.8.0 (headless `toonz_render` via tcomposer) | Modified BSD-3 ("Some of code ... derived from thirdparty libraries") — https://github.com/opentoonz/opentoonz/blob/master/LICENSE.txt | – | Yes | flatpak | – (GUI) |
| Imagine | Not verified: no GPL-2.0 "Imagine" converter found. meowtec/Imagine (now meowtec/imgo) has **no LICENSE** (all rights reserved) | – | Unclear → skipped | – | `resize` uses ImageMagick (ImageMagick License, Apache-2.0-style) instead |
| OvenMediaEngine 0.21.0 | **AGPL-3.0** — https://github.com/OvenMediaLabs/OvenMediaEngine/blob/master/LICENSE ; use unmodified | – | Yes (streams are yours) | docker compose (Azure, not deployed) | – |
| Real-ESRGAN (ncnn-vulkan 20220424) | BSD-3 — https://github.com/xinntao/Real-ESRGAN/blob/master/LICENSE ; ncnn port MIT | RealESRGAN_x4plus released under repo BSD-3; trained on DF2K (DIV2K/Flickr2K "academic research") + OST | Yes, with caveat (training-data terms) | /opt/media-tools/realesrgan | `upscale` |
| BasicSR | Apache-2.0 — https://github.com/XPixelGroup/BasicSR/blob/master/LICENSE.txt | – | Yes | not installed (framework, not needed) | – |
| GFPGAN | Apache-2.0 (README: "GFPGAN is released under Apache License Version 2.0") | trained on FFHQ (CC BY-NC-SA 4.0 dataset) + StyleGAN2 | Unclear → **not exposed**; and per user **never applied to his face** | not installed | – |
| Slidev 53.0.0 | MIT — https://github.com/slidevjs/slidev/blob/main/LICENSE | – | Yes | npm -g | `slidev` |
| RIFE (rife-ncnn-vulkan 20221029, model v4.6) | MIT — https://github.com/nihui/rife-ncnn-vulkan , https://github.com/hzwer/Practical-RIFE | model shipped in MIT release; trained on Vimeo-90K (research dataset) | Yes, with caveat | /opt/media-tools/rife… | `interpolate` |
| ZLMediaKit | MIT — https://github.com/ZLMediaKit/ZLMediaKit/blob/master/LICENSE | – | Yes | docker compose (profile zlm) | – |
| DPlayer 1.27.1 | MIT — https://github.com/DIYgod/DPlayer | – | Yes | snippet (SRI) | – |
| XGPlayer 3.0.26 (ByteDance) | MIT — https://github.com/bytedance/xgplayer | – | Yes | snippet (SRI) | – |
| AFFiNE 0.27.4 | MIT for client; "packages/backend ... licensed under ... packages/backend/server/LICENSE" (EE) — https://github.com/toeverything/AFFiNE/blob/canary/LICENSE | – | Yes (client) | not installed (desktop AppImage; use cloud/desktop on your PC) | – |
| U2-Net (via rembg 2.0.85, MIT) | Apache-2.0 — https://github.com/xuebinqin/U-2-Net | u2net.onnx (repo Apache-2.0; trained on DUTS-TR) | Yes | venv /opt/media-tools/venv | `bg_remove` model=u2net |
| IS-Net (DIS) | Apache-2.0 code — https://github.com/xuebinqin/DIS | trained on DIS5K: "commercial use of this dataset is prohibited even after copying, editing, processing" (DIS5K-Dataset-Terms-of-Use.pdf) | **No** → refused when commercial=true (falls back to u2net) | venv | `bg_remove` model=isnet (commercial=false only) |
| Pinta | MIT — https://github.com/PintaProject/Pinta | – | Yes | flatpak | – (GUI) |
| Olive | GPL-3.0 — https://github.com/olive-editor/olive (no stable release; 0.2 alpha) | – | Yes | flatpak | – (GUI) |
| VidCutter 6.0.5.1 | GPL-3.0 — https://github.com/ozmartian/vidcutter | – | Yes | flatpak | – (GUI) |

Weights in CI are sha256-pinned in `media/weights.lock`; CLI versions pinned (marp 4.5.1, slidev 53.0.0, rembg 2.0.85); apt tools come from the pinned runner image `ubuntu-24.04`.

GUI apps: pinned installers/scripts in `desktop/` (apps.lock sha256, flatpak.lock commits); mirror release via `desktop-mirror.yml`. Olive has no stable 0.2 release (nightly pinned by hash). AzPainter ships source only (Linux). No headless mode: Pinta, Olive, VidCutter, AFFiNE, AzPainter.
