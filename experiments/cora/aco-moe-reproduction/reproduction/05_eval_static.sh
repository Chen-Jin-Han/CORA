#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"
gpu_guard

DEGRADATIONS=(
  "rain:0.6" "fog:0.6" "snow:0.6" "motion_blur:0.35"
  "gaussian_noise:0.5" "low_light:0.7" "jpeg:0.7"
)

eval_static() {
  local method="$1" deg="$2" intensity="$3" task="$4" seed="$5" gpu="$6"
  local policy adapter logdir stdout
  policy="$(policy_checkpoint "${task}" "${seed}")"
  require_file "${policy}"
  logdir="${LOG_ROOT}/eval/static/${method}/${deg}/${task}/seed_${seed}"
  stdout="${LOG_ROOT}/stdout/eval_static_${method}_${deg}_${task}_seed${seed}.log"
  mkdir -p "${logdir}"
  if eval_completed "${logdir}"; then
    echo "[SKIP] completed static=${deg} method=${method} task=${task} seed=${seed}"
    return
  fi
  local configs=(paper_dmc_vision paper_vdcs_static)
  local extra=()
  if [[ "${method}" == "aco" ]]; then
    configs+=(paper_aco)
    adapter="$(adapter_checkpoint full 0)"
    require_file "${adapter}"
    extra+=(--dual_stream_unet_checkpoint "${adapter}")
  fi
  echo "[GPU ${gpu}] static=${deg} method=${method} task=${task} seed=${seed}"
  CUDA_VISIBLE_DEVICES="${gpu}" MUJOCO_GL="${MUJOCO_GL:-egl}" \
    python dreamer.py --configs "${configs[@]}" \
      --task "dmc_${task}" --seed "${seed}" --device cuda:0 \
      --vdcs_degradation_type "${deg}" --vdcs_intensity "${intensity}" \
      --logdir "${logdir}" --policy_checkpoint "${policy}" \
      --eval_only True --eval_episode_num "${EVAL_EPISODES}" --compile False \
      "${extra[@]}" 2>&1 | tee "${stdout}"
  if [[ "${PRUNE_EVAL_EPISODES}" == "1" ]]; then
    safe_prune_log_dir "${logdir}/eval_eps"
    safe_prune_log_dir "${logdir}/train_eps"
  fi
}

BATCH_PIDS=()
job=0
for seed in "${SEEDS[@]}"; do
  for task in "${DATA_TASKS[@]}"; do
    for ds in "${DEGRADATIONS[@]}"; do
      IFS=: read -r deg intensity <<<"${ds}"
      for method in raw aco; do
        gpu="${GPUS[$((job % ${#GPUS[@]}))]}"
        run_batch eval_static "${method}" "${deg}" "${intensity}" "${task}" "${seed}" "${gpu}"
        job=$((job + 1))
      done
    done
  done
done
finish_batch
