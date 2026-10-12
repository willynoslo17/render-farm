# Avatar engine licenses (verified 2026-10-12 from upstream, at pinned commits where pinned)
Not legal advice. "Commercial" = may the generated videos be monetized.

| Engine | Code license | Weights license | Commercial | Source |
|---|---|---|---|---|
| SadTalker @cd4c046 | Apache-2.0 (README: "removed the non-commercial restriction") | Released by authors with repo, no separate restriction. **Caveat:** download bundle also includes BFM_Fitting (Basel Face Model, registration/research terms), a Wav2Lip checkpoint (LRS2, non-commercial) and GFPGAN/facexlib helpers | **Yes, with caveat** (allowed when commercial=true) | https://github.com/OpenTalker/SadTalker/blob/cd4c0465ae0b54a6f85af57f5c65fec9fe23e7f8/LICENSE |
| LatentSync (ByteDance) | Apache-2.0 | ByteDance/LatentSync(-1.5) on HF: CreativeML OpenRAIL++-M (commercial OK, use-based restrictions) | **Yes** | https://github.com/bytedance/LatentSync · https://huggingface.co/ByteDance/LatentSync-1.5 |
| MuseTalk (Tencent Music) — not installed | MIT | README: "available for any purpose, even commercially" (deps whisper/sd-vae/dwpose/S3FD keep own licenses) | **Yes** | https://github.com/TMElyralab/MuseTalk |
| EchoMimic V2 (Ant Group) | Apache-2.0 | HF BadToBest/EchoMimicV2: no license declared; README: "intended for academic research" | **No (unclear → refused)** | https://github.com/antgroup/echomimic_v2 · https://huggingface.co/BadToBest/EchoMimicV2 |
| LivePortrait @9b294b3 (Kuaishou) | MIT | LivePortrait weights MIT, **but** required InsightFace buffalo_l (det_10g, 2d106det) = non-commercial research only | **No** (unless InsightFace replaced, e.g. MediaPipe) | https://github.com/KwaiVGI/LivePortrait · https://github.com/deepinsight/insightface#license |
| Wav2Lip @bac9a81 | Non-commercial (README: "any form of commercial use is strictly prohibited", LRS2) | same | **No** | https://github.com/Rudrabha/Wav2Lip/tree/bac9a81e63ecc153202353372e5724b83d9e6322 |
| CodeFormer @b33cc7d | S-Lab License 1.0 (non-commercial) | same | **No** | https://github.com/sczhou/CodeFormer/blob/b33cc7d639d6545bfcccc7e0bc6ae51f24e79c2b/LICENSE |
| HF Space fffiloni/echomimic-v2 @a48c1cc | no license declared | inherits EchoMimicV2 | No | https://huggingface.co/spaces/fffiloni/echomimic-v2 |
| HF Space fffiloni/LatentSync @058d1fb | no license declared | inherits LatentSync (OpenRAIL++) | Yes (inherited) | https://huggingface.co/spaces/fffiloni/LatentSync |

`commercial` (default `true`) in avatar.yml: wav2lip / liveportrait / echomimic are refused and replaced by sadtalker; codeformer is skipped. Set `"commercial":"false"` only for private/non-monetized tests.
