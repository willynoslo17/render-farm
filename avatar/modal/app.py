"""Modal GPU entry for MuseTalk / LatentSync 1.6 / EchoMimicV3-Flash.
Secrets stay in Modal / GitHub Actions, never in this public tree.
Deploy after MODAL_TOKEN_* are set: modal deploy avatar/modal/app.py
"""
from __future__ import annotations

import modal

app = modal.App("ml-avatar-gpu")
image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("ffmpeg", "git", "curl")
    .pip_install("torch", "torchvision", "torchaudio", extra_index_url="https://download.pytorch.org/whl/cu121")
)

@app.function(image=image, gpu="A10G", timeout=1800, secrets=[modal.Secret.from_name("ml-avatar-callback", required=False)])
def render(engine: str, video_url: str, audio_url: str, commercial: bool = True) -> dict:
    """Run pinned self-host engines; commercial=True refuses keysync etc."""
    allowed = {"musetalk", "echomimicv3", "liveavatar", "flashtalk", "latentsync16"}
    if commercial and engine == "keysync":
        return {"ok": False, "error": "keysync blocked in commercial mode"}
    if engine not in allowed and not (engine == "keysync" and not commercial):
        return {"ok": False, "error": f"unsupported engine {engine}"}
    # Full clone+weights path lands when MODAL_TOKEN is available; keep stub deployable.
    return {"ok": False, "error": "deploy weights+run.sh on Modal volume next", "engine": engine}
