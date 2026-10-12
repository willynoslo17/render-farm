# render-farm (Remotion + Blender, free on GitHub Actions)

Trigger from Make (HTTP module) or n8n (HTTP Request):

POST https://api.github.com/repos/willynoslo17/render-farm/dispatches
Headers: Authorization: Bearer <fine-grained PAT, this repo only, Contents: read/write>
         Accept: application/vnd.github+json
Body (Remotion):
{"event_type":"remotion","client_payload":{"composition":"Main","props":{"title":"Hola"},"job_id":"123","callback_url":"https://<n8n>/webhook/render-done"}}
Body (Blender):
{"event_type":"blender","client_payload":{"scene":"blender/scene.blend","start":1,"end":120,"job_id":"124","callback_url":"..."}}

Output: uploaded to Cloudinary (cloud yiq9yzmu, unsigned preset ml_unsigned); URL POSTed to callback_url.

Setup still needed: `remotion/` project (npx create-video@latest), a `blender/scene.blend`.
Limits: public repo = unlimited free minutes, 4 vCPU/16 GB runner; private = 2,000 min/mo, 2 vCPU/7 GB. Max 6 h per job. No GPU.
Note: public repo means code + logs are public; never put secrets in payloads/logs.

## Avatar (talking photo) — `event_type: "avatar"`
Body (Make PRINCIPAL HTTP module, same headers as above):
{"event_type":"avatar","client_payload":{"engine":"wav2lip","photo_id":"willy_camisa","audio_url":"https://res.cloudinary.com/yiq9yzmu/....wav","job_id":"125","callback_url":"https://hook.eu1.make.com/..."}}

| engine | runs on | input | notes |
|---|---|---|---|
| sadtalker (default) | GitHub CPU | photo + audio | also the fallback for every other engine |
| wav2lip | GitHub CPU | photo + audio | lip-sync only, fastest |
| liveportrait | GitHub CPU | photo + audio | `base_engine` (wav2lip\|sadtalker) makes the audio-driven video, then LivePortrait re-animates the original photo with it; on failure the base video is delivered |
| echomimic | HF Space fffiloni/echomimic-v2 | photo + audio | Space is on CPU, often times out -> SadTalker |
| latentsync | HF Space fffiloni/LatentSync (ZeroGPU) | `video_url` (our Cloudinary .mp4) + audio | |
| longcat | HF Space meituan-longcat/LongCat-Video-Avatar-1.5-Demo (official, ZeroGPU) | photo + audio | LongCat-Video-Avatar 1.5, 480p, 5 s per call (Space limit); MIT |
| aniportrait | HF Space ZJYang/AniPortrait_official (official, ZeroGPU) | photo + audio | 512px, `AP_FRAMES` default 150; Apache-2.0 |

`"commercial"` (default `"true"`): only commercially-licensed engines run (sadtalker, latentsync, longcat, aniportrait); wav2lip/liveportrait/echomimic fall back to sadtalker and codeformer is skipped. See avatar/LICENSES.md.
Optional `"codeformer":"true"`: CodeFormer face restoration (CPU, slow). It modifies the face, so it is OFF by default.
Callback JSON: `{job,url,engine,commercial,fallback_reason,codeformer_failed}`. `fallback_reason` is non-empty when the requested engine failed/timed out (also shown as a warning + run summary).
All code is pinned to commits; all model weights are pinned to immutable revisions and verified with sha256 (`avatar/weights.lock`, `avatar/fetch_weights.sh`).
MuseTalk: not installed — official Space is in RUNTIME_ERROR and self-hosting needs mmcv/mmpose + GPU (not feasible on free CPU).
Not installed (see avatar/LICENSES.md): LiveAvatar, SoulX-FlashTalk, EchoMimicV3-Flash, KeySync — commercial-OK but need a GPU (14B / 24GB+) and no working official Space (KeySync Space RUNTIME_ERROR); Hallo/Hallo2 (InsightFace non-commercial, Space paused), Sonic (CC BY-NC-SA), V-Express (non-commercial weights) — no free route and not sellable; daVinci-MagiHuman — code repo has no license and its Space is text-prompt only (no audio input); Sync 1.9 — paid sync.so API; MegaPortraits — no official code.

## Voice (Japanese TTS) — `event_type: "voice"`
{"event_type":"voice","client_payload":{"text":"こんにちは","voice":"zundamon","job_id":"126","callback_url":"https://hook.eu1.make.com/..."}}
VOICEVOX engine 0.25.2 (Docker, pinned digest, CPU). Voices: zundamon, metan only (no cloning). Commercial OK **only with credit** in the video description (`credit_required` in callback). Output .wav on Cloudinary ml/voice.
Not installed: MEMO (research-only, needs GPU, Space RUNTIME_ERROR), FaceFormer + Perceptual 3D Talking Head (VOCASET non-commercial + gated templates), DIRFA (no public code), COEIROINK (closed freeware), "Talking Face Generation with Multilingual TTS" (no weights), SEA-LION (LLM, not an avatar/voice engine).
