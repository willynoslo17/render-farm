"""HF Space routes via gradio_client (free). Exits non-zero on failure so the workflow can fall back.
Usage:
  python hf_space.py echomimic photo.jpg audio.wav out.mp4   # photo+audio -> half-body (EchoMimic V2)
  python hf_space.py latentsync video.mp4 audio.wav out.mp4  # video+audio -> lip-sync (LatentSync)
Env: HF_TOKEN (optional; anonymous if empty), ECHOMIMIC_SPACE, LATENTSYNC_SPACE (override defaults).
Spaces are allowlisted below; anything else is refused."""
import os, shutil, sys
from gradio_client import Client, handle_file

ALLOWED = {
    "echomimic": {"fffiloni/echomimic-v2"},
    "latentsync": {"fffiloni/LatentSync"},
}
DEFAULT = {"echomimic": "fffiloni/echomimic-v2", "latentsync": "fffiloni/LatentSync"}

mode, src, audio, out = sys.argv[1:5]
if mode not in ALLOWED:
    sys.exit(f"unknown mode {mode}")
space = os.environ.get(mode.upper() + "_SPACE") or DEFAULT[mode]
if space not in ALLOWED[mode]:
    sys.exit(f"Space {space} not in allowlist")
client = Client(space, hf_token=os.environ.get("HF_TOKEN") or None, verbose=False)
if mode == "echomimic":
    res = client.predict(handle_file(src), handle_file(audio), "assets/halfbody_demo/pose/01", "Showcase",
                         768, 768, int(os.environ.get("EM_FRAMES", "150")), 20, 16000, 2.5, 24, 12, 3, False, -1,
                         api_name="/generate")
else:
    res = client.predict(handle_file(src), handle_file(audio), api_name="/generate_lip_sync_video")
if isinstance(res, (list, tuple)):
    res = res[0]
if isinstance(res, dict):
    res = res.get("video") or res.get("path") or res.get("value")
if not res or not os.path.isfile(str(res)):
    sys.exit(f"Space returned no video file: {res!r}")
shutil.copy(res, out)
print("HF Space render OK:", mode, out)
