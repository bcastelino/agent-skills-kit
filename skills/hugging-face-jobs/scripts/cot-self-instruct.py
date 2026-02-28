#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "vllm",
#     "datasets",
#     "huggingface-hub",
# ]
# ///
"""Generate synthetic prompts/answers via CoT Self-Instruct.

Usage:
    python cot-self-instruct.py \
        --seed-dataset davanstrien/s1k-reasoning \
        --output-dataset username/synthetic-math \
        --task-type reasoning --num-samples 5000
"""
import argparse
import os

from datasets import Dataset, load_dataset
from huggingface_hub import HfApi
from vllm import LLM, SamplingParams


def parse_args():
    parser = argparse.ArgumentParser(description="CoT Self-Instruct generation")
    parser.add_argument("--seed-dataset", required=True, help="Seed dataset on Hub")
    parser.add_argument("--output-dataset", required=True, help="Output dataset on Hub")
    parser.add_argument("--task-type", default="reasoning", help="Task type")
    parser.add_argument("--num-samples", type=int, default=5000)
    parser.add_argument("--filter-method", default="answer-consistency",
                        choices=["answer-consistency", "rip", "none"])
    parser.add_argument("--model-id", default="Qwen/Qwen3-30B-A3B-Instruct-2507")
    return parser.parse_args()


def main():
    args = parse_args()
    token = os.environ.get("HF_TOKEN")
    assert token, "HF_TOKEN not set."

    print(f"Loading seed dataset: {args.seed_dataset}")
    seeds = load_dataset(args.seed_dataset, split="train")

    print(f"Loading model: {args.model_id}")
    llm = LLM(model=args.model_id, trust_remote_code=True)
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=4096)

    results = []
    for i in range(args.num_samples):
        seed = seeds[i % len(seeds)]
        prompt = f"Create a new {args.task_type} problem similar to: {seed.get('question', seed.get('prompt', ''))}"
        output = llm.generate([prompt], sampling_params)[0].outputs[0].text
        results.append({"prompt": prompt, "response": output, "task_type": args.task_type})

        if (i + 1) % 100 == 0:
            print(f"Generated {i + 1}/{args.num_samples}")

    ds = Dataset.from_list(results)
    print(f"Pushing {len(ds)} samples to {args.output_dataset}")
    ds.push_to_hub(args.output_dataset, token=token)
    print("Done!")


if __name__ == "__main__":
    main()
