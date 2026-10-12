"""Optional high-quality route: call a Hugging Face Space via gradio_client.
Usage: python hf_space.py photo.jpg audio.wav out.mp4
Env: HF_TOKEN, AVATAR_SPACE (e.g. owner/space), AVATAR_SPACE_API (default /predict).
Exits non-zero on any failure so the workflow falls back to SadTalker."""
import os, shutil, sys
from gradio_client import Client, handle_file

photo, audio, out = sys.argv[1:4]
space = os.environ["AVATAR_SPACE"]
api = os.environ.get("AVATAR_SPACE_API") or "/predict"
client = Client(space, hf_token=os.environ["HF_TOKEN"])
res = client.predict(handle_file(photo), handle_file(audio), api_name=api)
if isinstance(res, (list, tuple)):
    res = res[0]
if isinstance(res, dict):
    res = res.get("video") or res.get("path") or res.get("value")
if not res or not os.path.isfile(str(res)):
    sys.exit(f"Space returned no video file: {res!r}")
shutil.copy(res, out)
print("HF Space render OK:", out)
