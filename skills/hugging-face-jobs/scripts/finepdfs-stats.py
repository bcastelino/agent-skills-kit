#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "polars",
#     "huggingface-hub",
# ]
# ///
"""Compute temporal statistics over FinePDFs parquet data.

Usage:
    python finepdfs-stats.py --limit 10000 [--output-repo username/finepdfs-stats]
"""
import argparse
import os

import polars as pl
from huggingface_hub import HfApi


def parse_args():
    parser = argparse.ArgumentParser(description="FinePDFs temporal statistics")
    parser.add_argument("--limit", type=int, default=10000, help="Row limit")
    parser.add_argument("--show-plan", action="store_true", help="Show query plan")
    parser.add_argument("--output-repo", default=None, help="Hub repo for results")
    return parser.parse_args()


def main():
    args = parse_args()

    print(f"Scanning FinePDFs parquet (limit: {args.limit})...")
    # Scan parquet directly from Hub (lazy, no full download)
    lf = pl.scan_parquet("hf://datasets/HuggingFaceFW/FinePDFs/**/*.parquet")

    if args.show_plan:
        print(lf.explain())
        return

    df = lf.head(args.limit).collect()
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns")

    # Compute basic statistics
    stats = {
        "total_rows": len(df),
        "columns": df.columns,
        "null_counts": {col: df[col].null_count() for col in df.columns},
    }

    # Numeric column statistics
    for col in df.select(pl.col(pl.NUMERIC_DTYPES)).columns:
        stats[f"{col}_mean"] = df[col].mean()
        stats[f"{col}_std"] = df[col].std()

    print("\nStatistics:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    # Optionally push results to Hub
    if args.output_repo:
        token = os.environ.get("HF_TOKEN")
        if not token:
            print("Warning: HF_TOKEN not set, skipping upload")
            return
        api = HfApi(token=token)
        results_path = "stats_results.json"
        import json
        with open(results_path, "w") as f:
            json.dump({k: str(v) for k, v in stats.items()}, f, indent=2)
        api.upload_file(
            path_or_fileobj=results_path,
            path_in_repo="stats_results.json",
            repo_id=args.output_repo,
            repo_type="dataset",
        )
        print(f"Results uploaded to {args.output_repo}")


if __name__ == "__main__":
    main()
