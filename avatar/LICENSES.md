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
| **LongCat-Video-Avatar 1.5** (Meituan) — installed `longcat` | MIT (meituan-longcat/LongCat-Video @6b3f4b8) | HF meituan-longcat/LongCat-Video-Avatar-1.5 @92016c7: MIT | **Yes** | https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5 |
| HF Space meituan-longcat/LongCat-Video-Avatar-1.5-Demo @472c881 (official, ZeroGPU) | no license declared (official author Space) | inherits MIT | Yes (inherited) | https://huggingface.co/spaces/meituan-longcat/LongCat-Video-Avatar-1.5-Demo |
| **AniPortrait** (Tencent) — installed `aniportrait` | Apache-2.0 @7f6593f | HF ZJYang/AniPortrait @dae1484: Apache-2.0; base SD1.5 = CreativeML OpenRAIL-M (commercial OK, use restrictions); face landmarks via MediaPipe (Apache-2.0) | **Yes** | https://github.com/Zejun-Yang/AniPortrait |
| HF Space ZJYang/AniPortrait_official @8dc5037 (official, ZeroGPU) | Apache-2.0 | inherits | Yes | https://huggingface.co/spaces/ZJYang/AniPortrait_official |
| LiveAvatar (Alibaba Quark) — not installed | Apache-2.0 @c3c47d0 | HF Quark-Vision/Live-Avatar: Apache-2.0 (14B, Wan2.2 base Apache-2.0) | Yes | https://github.com/Alibaba-Quark/LiveAvatar |
| SoulX-FlashTalk (Soul AI Lab) — not installed | Apache-2.0 @2ba2e1e | HF Soul-AILab/SoulX-FlashTalk-14B: Apache-2.0 | Yes | https://github.com/Soul-AILab/SoulX-FlashTalk |
| EchoMimicV3-Flash (Ant Group) — not installed | Apache-2.0 @7e89489 | HF BadToBest/EchoMimicV3 (echomimicv3-flash-pro): Apache-2.0 | Yes | https://github.com/antgroup/echomimic_v3 |
| Hallo / Hallo2 (Fudan) — not installed | MIT (@8fd7c57 / @58a9aa6) | HF fudan-generative-ai/hallo(2): MIT, **but** requires InsightFace face_analysis models (non-commercial) | **No** (unless InsightFace replaced) | https://github.com/fudan-generative-vision/hallo2 |
| Sonic (Tencent) — not installed | **CC BY-NC-SA 4.0** | LeonJoe13/Sonic: same (README: "our license is non-commercial") | **No** | https://github.com/jixiaozhong/Sonic |
| V-Express (Tencent AI Lab) — not installed | Code: academic + commercial (README; no LICENSE file) | tk93/V-Express checkpoints: "for non-commercial research purposes only" | **No** | https://github.com/tencent-ailab/V-Express |
| daVinci-MagiHuman (Sand.ai + GAIR) — not installed | **No LICENSE file** in GAIR-NLP/ or SandAI-org/daVinci-MagiHuman repos (all rights reserved by default) | HF GAIR/daVinci-MagiHuman: Apache-2.0 | **Unclear → No** | https://huggingface.co/GAIR/daVinci-MagiHuman |
| KeySync (Imperial College + Wrocław) — not installed | Apache-2.0 (antonibigata/keysync @5e2503b) | HF toninio19/keysync: Apache-2.0 | Yes | https://github.com/antonibigata/keysync |
| Sync 1.9 (sync.so) — not installed | proprietary, paid API | n/a | n/a (not free) | https://sync.so/pricing |
| MegaPortraits (Samsung) — not installed | no official code/weights released (only unofficial re-implementations) | n/a | n/a | https://arxiv.org/abs/2207.07621 |
| MEMO (Skywork/NTU/NUS) — not installed | Apache-2.0 @151b024 | HF memoavatar/memo @9df2487 Apache-2.0, but README: "preview model for research purposes" | **No** (research-only) | https://github.com/memoavatar/memo |
| FaceFormer (MPI) — not installed | MIT @dfaea81 | vocaset.pth/biwi.pth trained on VOCASET/BIWI (non-commercial research licenses); demo needs VOCASET templates.pkl (registration-gated) | **No** | https://github.com/EvelynFan/FaceFormer |
| Perceptual 3D Talking Head (KAIST, CVPR'25) — not installed | MIT @2bf9d3b | perceptual-loss + eval checkpoints only (Google Drive), built on FaceFormer/VOCASET | **No** (VOCASET) | https://github.com/kaist-ami/Perceptual-3D-Talking-Head |
| DIRFA (NTU) — not installed | no official public code/weights found | n/a | n/a | — |
| **VOICEVOX engine 0.25.2** (voice, `voice.yml`) | LGPL-3.0 (dual; used unmodified via Docker digest sha256:148b7ad…) ; core MIT | Character voices ずんだもん/四国めたん: commercial OK **with credit** "VOICEVOX:ずんだもん" / "VOICEVOX:四国めたん"; banned: political/religious, fake/misleading, info-products, adult business | **Yes, with credit** | https://github.com/VOICEVOX/voicevox_engine · https://zunko.jp/con_ongen_kiyaku.html |
| COEIROINK — not installed | proprietary freeware (closed source, no pinned Linux build) | per-character terms | n/a | https://coeiroink.com |

`commercial` (default `true`) in avatar.yml: allowed = sadtalker, latentsync, longcat, aniportrait; wav2lip / liveportrait / echomimic are refused and replaced by sadtalker; codeformer is skipped. Set `"commercial":"false"` only for private/non-monetized tests.
