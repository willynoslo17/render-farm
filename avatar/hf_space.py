"""HF Space routes via gradio_client (free). Exits non-zero on failure so the workflow can fall back.
Usage:
  python hf_space.py echomimic photo.jpg audio.wav out.mp4   # photo+audio -> half-body (EchoMimic V2)
  python hf_space.py latentsync video.mp4 audio.wav out.mp4  # video+audio -> lip-sync (LatentSync)
  python hf_space.py longcat photo.jpg audio.wav out.mp4     # LongCat-Video-Avatar 1.5 (Meituan, ZeroGPU)
  python hf_space.py aniportrait photo.jpg audio.wav out.mp4 # AniPortrait official (ZeroGPU)
Env: HF_TOKEN (optional; anonymous if empty), ECHOMIMIC_SPACE, LATENTSYNC_SPACE (override defaults).
Spaces are allowlisted below; anything else is refused."""
import os, shutil, sys
from gradio_client import Client, handle_file

ALLOWED = {
    "echomimic": {"fffiloni/echomimic-v2"},
    "latentsync": {"fffiloni/LatentSync"},
    "longcat": {"meituan-longcat/LongCat-Video-Avatar-1.5-Demo"},
    "aniportrait": {"ZJYang/AniPortrait_official"},
}
DEFAULT = {"echomimic": "fffiloni/echomimic-v2", "latentsync": "fffiloni/LatentSync",
           "longcat": "meituan-longcat/LongCat-Video-Avatar-1.5-Demo", "aniportrait": "ZJYang/AniPortrait_official"}
# Space revisions reviewed (Spaces run live code; a change is reported, see avatar/LICENSES.md)
SPACE_REV = {"fffiloni/echomimic-v2": "a48c1cc904d6dc84aaa0a7d3f160528ad04bf0c3",
            "fffiloni/LatentSync": "058d1fbd5e450d527510907a4094b8826cc206a5",
            "meituan-longcat/LongCat-Video-Avatar-1.5-Demo": "472c881f0cb05b4991eee71bb3b86e93600bb7c1",
            "ZJYang/AniPortrait_official": "8dc5037a0c34aea6c5530b912318de96febefab6"}

mode, src, audio, out = sys.argv[1:5]
if mode not in ALLOWED:
    sys.exit(f"unknown mode {mode}")
space = os.environ.get(mode.upper() + "_SPACE") or DEFAULT[mode]
if space not in ALLOWED[mode]:
    sys.exit(f"Space {space} not in allowlist")
tok = os.environ.get("HF_TOKEN") or None
if space in SPACE_REV:
    try:
        from huggingface_hub import HfApi
        live = HfApi().space_info(space, token=tok).sha
        if live != SPACE_REV[space]:
            print(f"::warning title=space revision::{space} is at {live}, verified {SPACE_REV[space]}", file=sys.stderr)
    except Exception:
        pass
try:
    client = Client(space, token=tok, verbose=False)
except TypeError:
    client = Client(space, hf_token=tok, verbose=False)
if mode == "echomimic":
    res = client.predict(handle_file(src), handle_file(audio), "assets/halfbody_demo/pose/01", "Showcase",
                         768, 768, int(os.environ.get("EM_FRAMES", "150")), 20, 16000, 2.5, 24, 12, 3, False, -1,
                         api_name="/generate")
elif mode == "longcat":
    res = client.predict(handle_file(src), handle_file(audio), "A person is talking naturally.",
                         os.environ.get("LC_RES", "480p"), 42, "Clean speech (fast)", "DBCache faster",
                         api_name="/generate_avatar")
elif mode == "aniportrait":
    res = client.predict(handle_file(audio), handle_file(src), None, 512, 20,
                         int(os.environ.get("AP_FRAMES", "150")), 42, api_name="/audio2video")
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
