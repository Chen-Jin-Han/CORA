#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/settings.sh"
cd "${REPRO_ROOT}"
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) ;;
  *) export MUJOCO_GL="${MUJOCO_GL:-egl}" ;;
esac

mkdir -p "${DATA_DIR}" "${CHECKPOINT_DIR}" "${LOG_ROOT}" "${LOG_ROOT}/stdout" \
  "${TORCH_HOME}" "${XDG_CACHE_HOME}" "${PIP_CACHE_DIR}"

require_file() {
  [[ -f "$1" ]] || { echo "Missing required file: $1" >&2; exit 2; }
}

eval_completed() {
  local logdir="$1"
  [[ "${SKIP_COMPLETED}" == "1" ]] || return 1
  [[ -f "${logdir}/metrics.jsonl" ]] || return 1
  grep -q '"eval_return"' "${logdir}/metrics.jsonl"
}

disk_guard() {
  local available_kb available_gb
  available_kb="$(df -Pk "${LARGE_ROOT}" | awk 'NR==2 {print $4}')"
  available_gb=$((available_kb / 1024 / 1024))
  if (( available_gb < MIN_FREE_GB )); then
    echo "Insufficient free disk: ${available_gb} GiB available; ${MIN_FREE_GB} GiB required." >&2
    exit 5
  fi
  echo "Free disk: ${available_gb} GiB"
}

safe_prune_log_dir() {
  local target="$1" resolved root_resolved
  [[ -e "${target}" ]] || return
  resolved="$(realpath -m "${target}")"
  root_resolved="$(realpath -m "${LOG_ROOT}")"
  case "${resolved}" in
    "${root_resolved}"/*) rm -rf -- "${resolved}" ;;
    *) echo "Refusing to prune outside LOG_ROOT: ${resolved}" >&2; exit 6 ;;
  esac
}

adapter_checkpoint() {
  local variant="$1"
  local seed="${2:-0}"
  printf '%s/%s/seed_%s/moe_unet_best.pth' "${CHECKPOINT_DIR}" "${variant}" "${seed}"
}

policy_checkpoint() {
  local task="$1"
  local seed="$2"
  printf '%s/policy/dmc_%s/seed_%s/latest.pt' "${LOG_ROOT}" "${task}" "${seed}"
}

gpu_guard() {
  if [[ "${ALLOW_BUSY_GPUS}" == "1" ]]; then
    echo "[WARN] GPU busy-state guard overridden by ALLOW_BUSY_GPUS=1"
    return
  fi
  command -v nvidia-smi >/dev/null 2>&1 || { echo "nvidia-smi not found" >&2; exit 2; }
  local gpu util mem
  for gpu in "${GPUS[@]}"; do
    IFS=',' read -r util mem < <(
      nvidia-smi --id="${gpu}" --query-gpu=utilization.gpu,memory.used \
        --format=csv,noheader,nounits | tr -d ' '
    )
    if (( util > MAX_GPU_UTIL || mem > MAX_GPU_MEMORY_MIB )); then
      echo "GPU ${gpu} is busy: util=${util}% memory=${mem}MiB" >&2
      echo "Wait for it to become idle, or explicitly set ALLOW_BUSY_GPUS=1." >&2
      exit 3
    fi
  done
}

run_batch() {
  # Usage: run_batch function_name arg1 arg2 ...; caller builds groups no larger
  # than the GPU count and waits between groups.
  "$@" &
  BATCH_PIDS+=("$!")
  if (( ${#BATCH_PIDS[@]} >= ${#GPUS[@]} )); then
    local failed=0 pid
    for pid in "${BATCH_PIDS[@]}"; do wait "${pid}" || failed=1; done
    BATCH_PIDS=()
    (( failed == 0 )) || { echo "At least one parallel job failed." >&2; exit 4; }
  fi
}

finish_batch() {
  if (( ${#BATCH_PIDS[@]} == 0 )); then
    return
  fi
  local failed=0 pid
  for pid in "${BATCH_PIDS[@]}"; do wait "${pid}" || failed=1; done
  BATCH_PIDS=()
  (( failed == 0 )) || { echo "At least one parallel job failed." >&2; exit 4; }
}
