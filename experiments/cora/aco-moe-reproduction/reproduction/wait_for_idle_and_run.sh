#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"

POLL_SECONDS="${POLL_SECONDS:-120}"
REQUIRED_IDLE_CHECKS="${REQUIRED_IDLE_CHECKS:-3}"
COMMAND=("$@")
if (( ${#COMMAND[@]} == 0 )); then
  echo "Usage: wait_for_idle_and_run.sh command [args ...]" >&2
  exit 2
fi

lock_dir="${LARGE_ROOT}/locks"
mkdir -p "${lock_dir}"
lock_file="${lock_dir}/gpu_waiter.lock"
exec 9>"${lock_file}"
if ! flock -n 9; then
  echo "Another ACO reproduction waiter is already active: ${lock_file}" >&2
  exit 3
fi

echo "Waiting for GPUs ${GPUS[*]} to remain idle for ${REQUIRED_IDLE_CHECKS} checks."
echo "Thresholds: util<=${MAX_GPU_UTIL}% and memory<=${MAX_GPU_MEMORY_MIB}MiB"
idle_checks=0
while (( idle_checks < REQUIRED_IDLE_CHECKS )); do
  busy=0
  status=()
  for gpu in "${GPUS[@]}"; do
    IFS=',' read -r util mem < <(
      nvidia-smi --id="${gpu}" --query-gpu=utilization.gpu,memory.used \
        --format=csv,noheader,nounits | tr -d ' '
    )
    process_count="$(nvidia-smi --id="${gpu}" --query-compute-apps=pid --format=csv,noheader,nounits | sed '/^[[:space:]]*$/d' | wc -l)"
    status+=("gpu${gpu}:util=${util}% mem=${mem}MiB procs=${process_count}")
    if (( util > MAX_GPU_UTIL || mem > MAX_GPU_MEMORY_MIB || process_count > 0 )); then busy=1; fi
  done
  printf '[%s] %s\n' "$(date -u +%FT%TZ)" "${status[*]}"
  if (( busy == 0 )); then idle_checks=$((idle_checks + 1)); else idle_checks=0; fi
  if (( idle_checks < REQUIRED_IDLE_CHECKS )); then sleep "${POLL_SECONDS}"; fi
done

echo "GPUs are stably idle; running: ${COMMAND[*]}"
exec "${COMMAND[@]}"

