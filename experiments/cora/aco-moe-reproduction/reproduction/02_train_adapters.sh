#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"
gpu_guard
disk_guard

ROOTS=""
for task in "${DATA_TASKS[@]}"; do
  root="${DATA_DIR}/${task}_vdcs_seg${IMAGE_SIZE}_split"
  [[ -d "${root}/train" && -d "${root}/val" ]] || {
    echo "Dataset missing: ${root}" >&2; exit 2;
  }
  ROOTS="${ROOTS:+${ROOTS},}${root}"
done

# variant:num_experts:base_channels:lambda_rgb:lambda_mask:lambda_final
VARIANTS=(
  "full:9:9:1:1:1"
  "single:1:21:1:1:1"
  "mask_only:9:9:0:1:1"
  "rgb_only:9:9:1:0:1"
)

train_adapter() {
  local spec="$1" seed="$2" gpu="$3"
  local variant experts channels lrgb lmask lfinal
  IFS=: read -r variant experts channels lrgb lmask lfinal <<<"${spec}"
  local out="${CHECKPOINT_DIR}/${variant}/seed_${seed}"
  local tblog="${LOG_ROOT}/adapter/${variant}/seed_${seed}"
  local stdout="${LOG_ROOT}/stdout/adapter_${variant}_seed${seed}.log"
  mkdir -p "${out}" "${tblog}"
  if [[ "${SKIP_COMPLETED}" == "1" && -f "${out}/moe_unet_best.pth" && -f "${out}/moe_unet_latest.pth" ]]; then
    saved_step="$(python -c "import torch; print(int(torch.load('${out}/moe_unet_latest.pth', map_location='cpu', weights_only=False).get('step', 0)))")"
    if (( saved_step >= ACO_STEPS )); then
      echo "[SKIP] completed adapter=${variant} seed=${seed} step=${saved_step}"
      return
    fi
  fi
  local resume=()
  [[ -f "${out}/moe_unet_latest.pth" ]] && resume=(--resume "${out}/moe_unet_latest.pth")
  echo "[GPU ${gpu}] adapter=${variant} seed=${seed} experts=${experts} C=${channels}"
  CUDA_VISIBLE_DEVICES="${gpu}" MUJOCO_GL="${MUJOCO_GL:-egl}" \
    python -m scripts.train_aco_moe \
      --data_roots "${ROOTS}" \
      --output_dir "${out}" \
      --log_dir "${tblog}" \
      --steps "${ACO_STEPS}" \
      --batch_size "${ACO_MICRO_BATCH}" \
      --grad_accum_steps "${ACO_GRAD_ACCUM}" \
      --val_batch_size "${ACO_VAL_BATCH}" \
      --num_workers "${ACO_WORKERS}" \
      --num_experts "${experts}" \
      --base_channels "${channels}" \
      --router_hidden 256 \
      --lr 1e-4 --weight_decay 1e-4 \
      --lambda_rgb "${lrgb}" --lambda_mask "${lmask}" --lambda_final "${lfinal}" \
      --seed "${seed}" --amp "${resume[@]}" 2>&1 | tee "${stdout}"
}

BATCH_PIDS=()
job=0
for seed in "${ADAPTER_SEEDS[@]}"; do
  for spec in "${VARIANTS[@]}"; do
    gpu="${GPUS[$((job % ${#GPUS[@]}))]}"
    run_batch train_adapter "${spec}" "${seed}" "${gpu}"
    job=$((job + 1))
  done
done
finish_batch
