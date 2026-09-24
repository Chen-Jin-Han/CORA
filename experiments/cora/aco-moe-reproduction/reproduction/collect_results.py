#!/usr/bin/env python3
"""Collect Dreamer evaluation JSONL files into CSV and Markdown summaries."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


FIELDS = (
    "family",
    "condition",
    "method",
    "degradation",
    "task",
    "seed",
    "eval_return",
    "eval_length",
    "eval_episodes",
    "metrics_path",
)


def last_eval(path: Path):
    found = None
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "eval_return" in item:
            found = item
    return found


def identify(relative: Path):
    parts = relative.parts
    if len(parts) < 5 or parts[0] != "eval":
        return None
    family = parts[1]
    row = {key: "" for key in FIELDS}
    row["family"] = family
    if family == "core" and len(parts) >= 6:
        row.update(condition=parts[2], method=parts[2], task=parts[3], seed=parts[4].removeprefix("seed_"))
    elif family == "static" and len(parts) >= 7:
        row.update(method=parts[2], condition="static", degradation=parts[3], task=parts[4], seed=parts[5].removeprefix("seed_"))
    elif family == "dmcgb" and len(parts) >= 7:
        row.update(condition=parts[2], method=parts[3], task=parts[4], seed=parts[5].removeprefix("seed_"))
    else:
        return None
    return row


def fmt(value: float) -> str:
    return "nan" if not math.isfinite(value) else f"{value:.2f}"


def safe_ratio(numerator: float, denominator: float) -> float:
    return float("nan") if denominator == 0 else 100.0 * numerator / denominator


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-root", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for path in sorted((args.log_root / "eval").glob("**/metrics.jsonl")):
        meta = identify(path.relative_to(args.log_root))
        metrics = last_eval(path)
        if meta is None or metrics is None:
            continue
        meta["eval_return"] = float(metrics["eval_return"])
        meta["eval_length"] = metrics.get("eval_length", "")
        meta["eval_episodes"] = metrics.get("eval_episodes", "")
        meta["metrics_path"] = str(path)
        rows.append(meta)

    csv_path = args.output_dir / "all_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    groups = defaultdict(list)
    for row in rows:
        key = (row["family"], row["condition"], row["method"], row["degradation"], row["task"])
        groups[key].append(float(row["eval_return"]))

    core_by_run = defaultdict(dict)
    for row in rows:
        if row["family"] == "core":
            core_by_run[(row["task"], row["seed"])][row["condition"]] = float(row["eval_return"])

    comparison_rows = []
    for (task, seed), scores in sorted(core_by_run.items()):
        clean = scores.get("clean", float("nan"))
        raw = scores.get("markov_raw", float("nan"))
        oracle = scores.get("markov_oracle", float("nan"))
        for condition, score in sorted(scores.items()):
            gap_denominator = clean - raw
            comparison_rows.append(
                {
                    "task": task,
                    "seed": seed,
                    "condition": condition,
                    "return": score,
                    "relative_clean_pct": safe_ratio(score, clean),
                    "relative_oracle_pct": safe_ratio(score, oracle),
                    "clean_gap_recovered_pct": (
                        float("nan")
                        if not math.isfinite(gap_denominator) or gap_denominator == 0
                        else 100.0 * (score - raw) / gap_denominator
                    ),
                }
            )

    comparison_path = args.output_dir / "core_comparisons.csv"
    comparison_fields = (
        "task", "seed", "condition", "return", "relative_clean_pct",
        "relative_oracle_pct", "clean_gap_recovered_pct",
    )
    with comparison_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=comparison_fields)
        writer.writeheader()
        writer.writerows(comparison_rows)

    md_path = args.output_dir / "summary.md"
    with md_path.open("w", encoding="utf-8") as handle:
        handle.write("# Reproduction evaluation summary\n\n")
        handle.write("| Family | Condition | Method | Degradation | Task | Seeds | Mean return | Std |\n")
        handle.write("|---|---|---|---|---|---:|---:|---:|\n")
        for key, values in sorted(groups.items()):
            std = statistics.stdev(values) if len(values) > 1 else 0.0
            handle.write(
                f"| {' | '.join(key)} | {len(values)} | {fmt(statistics.mean(values))} | {fmt(std)} |\n"
            )

        handle.write("\n## Core conclusion metrics\n\n")
        handle.write("| Condition | Runs | Return | % clean | % oracle | % clean gap recovered |\n")
        handle.write("|---|---:|---:|---:|---:|---:|\n")
        by_condition = defaultdict(list)
        for row in comparison_rows:
            by_condition[row["condition"]].append(row)
        for condition, values in sorted(by_condition.items()):
            def mean_field(field):
                finite = [float(x[field]) for x in values if math.isfinite(float(x[field]))]
                return statistics.mean(finite) if finite else float("nan")
            handle.write(
                f"| {condition} | {len(values)} | {fmt(mean_field('return'))} | "
                f"{fmt(mean_field('relative_clean_pct'))} | {fmt(mean_field('relative_oracle_pct'))} | "
                f"{fmt(mean_field('clean_gap_recovered_pct'))} |\n"
            )

    print(f"Collected {len(rows)} completed evaluations")
    print(f"CSV:      {csv_path}")
    print(f"Core:     {comparison_path}")
    print(f"Markdown: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
