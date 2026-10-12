#!/usr/bin/env bash
# Self-hosted GPU route (NOT run on free GitHub runners). Untested by policy (no test renders).
# Usage: run.sh <engine> <photo.jpg|video.mp4> <audio.wav> <out.mp4>
# Engines: musetalk | echomimicv3 | keysync | liveavatar | flashtalk | latentsync16
# Code pinned to commits; weights fetched only via fetch_weights.sh (sha256-verified, avatar/weights.lock).
# VRAM (upstream): musetalk ~8GB, echomimicv3 flash ~16-24GB, latentsync16 ~18GB, keysync ~24GB, liveavatar >=48GB (fp8) / 80GB, flashtalk 14B ~64-80GB.
set -euo pipefail
ENGINE=$1; SRC=$(realpath "$2"); AUDIO=$(realpath "$3"); OUT=$(realpath -m "$4")
HERE=$(cd "$(dirname "$0")/.." && pwd); W=${WORK:-/tmp/selfhost}; mkdir -p "$W"
declare -A REPO=( [musetalk]=TMElyralab/MuseTalk [echomimicv3]=antgroup/echomimic_v3 [keysync]=antonibigata/keysync
  [liveavatar]=Alibaba-Quark/LiveAvatar [flashtalk]=Soul-AILab/SoulX-FlashTalk [latentsync16]=bytedance/LatentSync )
declare -A COMMIT=( [musetalk]=0a89dec45a0192b824e3cf4daf96c239440c5ed8 [echomimicv3]=7e89489ca51c0d008fc1963ec6c03fc5bd0b9397
  [keysync]=5e2503b171c6ddb4d88cd4cb9702347dcc4aa370 [liveavatar]=c3c47d031d8bf3247428333c1fe610579c71a551
  [flashtalk]=2ba2e1e801d59a9f526212a5aae5d374db8f2978 [latentsync16]=a229c3948406bc2cf6eaf4873e662e70c6a04746 )
[ -n "${REPO[$ENGINE]:-}" ] || { echo "unknown engine $ENGINE"; exit 2; }
C=${COMMIT[$ENGINE]}
D="$W/$ENGINE"; [ -d "$D/.git" ] || git clone -q "https://github.com/${REPO[$ENGINE]}.git" "$D"
git -C "$D" fetch -q origin "$C" 2>/dev/null || true; git -C "$D" checkout -q "$C"
bash "$HERE/fetch_weights.sh" "$ENGINE" "$D"
python -m venv "$W/venv-$ENGINE" && . "$W/venv-$ENGINE/bin/activate" && pip install -q -r "$D/requirements.txt"
cd "$D"; rm -rf out_sh; mkdir -p out_sh
case "$ENGINE" in
  musetalk)
    printf 'task_0:\n video_path: "%s"\n audio_path: "%s"\n' "$SRC" "$AUDIO" > out_sh/task.yaml
    python -m scripts.inference --inference_config out_sh/task.yaml --result_dir out_sh \
      --unet_model_path models/musetalkV15/unet.pth --unet_config models/musetalkV15/musetalk.json --version v15 ;;
  echomimicv3)
    python infer_flash.py --image_path "$SRC" --audio_path "$AUDIO" --prompt "A person is speaking." --num_inference_steps 8 \
      --config_path config/config.yaml --model_name models/Wan2.1-Fun-V1.1-1.3B-InP --ckpt_idx 50000 \
      --transformer_path models/flash/echomimicv3-flash-pro/diffusion_pytorch_model.safetensors --save_path out_sh \
      --wav2vec_model_dir models/chinese-wav2vec2-base --sampler_name Flow_Unipc --video_length 81 --guidance_scale 6.0 \
      --audio_guidance_scale 3.0 --audio_scale 1.0 --neg_scale 1.0 --neg_steps 0 --seed 43 --enable_teacache \
      --teacache_threshold 0.1 --num_skip_start_steps 5 --riflex_k 6 --ulysses_degree 1 --ring_degree 1 \
      --weight_dtype bfloat16 --sample_size 768 768 --fps 25 --add_prompt "" --negative_prompt "" --shift 5.0 ;;
  keysync)   # video dubbing: SRC must be a video
    echo "$SRC" > out_sh/videos.txt; echo "$AUDIO" > out_sh/audios.txt
    bash scripts/inference.sh --output_folder out_sh --file_list out_sh/videos.txt --file_list_audio out_sh/audios.txt \
      --keyframes_ckpt pretrained_models/checkpoints/keyframe_dub.pt --interpolation_ckpt pretrained_models/checkpoints/interpolation_dub.pt ;;
  liveavatar)
    torchrun --nproc_per_node=1 --master_port=29101 minimal_inference/s2v_streaming_interact.py --ulysses_size 1 --task s2v-14B \
      --size "704*384" --base_seed 420 --training_config liveavatar/configs/s2v_causal_sft.yaml --offload_model True \
      --convert_model_dtype --prompt "A person is talking naturally." --image "$SRC" --audio "$AUDIO" --infer_frames 48 \
      --load_lora --lora_path_dmd ckpt/LiveAvatar --sample_steps 4 --sample_guide_scale 0 --num_gpus_dit 1 \
      --sample_solver euler --single_gpu --ckpt_dir ckpt/Wan2.2-S2V-14B/ --fp8 --save_dir out_sh ;;
  flashtalk)
    python generate_video.py --ckpt_dir models/SoulX-FlashTalk-14B --wav2vec_dir models/chinese-wav2vec2-base \
      --input_prompt "A person is talking. Only the foreground characters are moving, the background remains static." \
      --cond_image "$SRC" --audio_path "$AUDIO" --audio_encode_mode stream --save_file out_sh/out.mp4 ;;
  latentsync16)  # video lip-sync, LatentSync 1.6 (512px)
    python -m scripts.inference --unet_config_path configs/unet/stage2_512.yaml --inference_ckpt_path checkpoints/latentsync_unet.pt \
      --inference_steps 20 --guidance_scale 1.5 --video_path "$SRC" --audio_path "$AUDIO" --video_out_path out_sh/out.mp4 ;;
esac
V=$(find out_sh -name '*.mp4' -printf '%T@ %p\n' | sort -nr | head -1 | cut -d' ' -f2-); test -s "$V"
ffmpeg -v error -y -i "$V" -i "$AUDIO" -map 0:v -map 1:a -shortest -c:v libx264 -pix_fmt yuv420p "$OUT"
echo "selfhost OK: $ENGINE -> $OUT"
