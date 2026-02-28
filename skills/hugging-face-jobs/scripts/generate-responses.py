#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "vllm",
#     "datasets",
#     "huggingface-hub",
# ]
# ///
"""Generate responses for a dataset using vLLM.

Usage:
    python generate-responses.py INPUT_DATASET OUTPUT_DATASET \
        --model-id Qwen/Qwen3-30B-A3B-Instruct-2507 \
        --temperature 0.7 --top-p 0.8 --max-tokens 2048
"""
import argparse
import os

from datasets import load_dataset
from huggingface_hub import HfApi
from vllm import LLM, SamplingParams


def parse_args():
    parser = argparse.ArgumentParser(description="Generate responses with vLLM")
    parser.add_argument("input_dataset", help="Input dataset on Hub")
    parser.add_argument("output_dataset", help="Output dataset on Hub")
    parser.add_argument("--messages-column", default="messages")
    parser.add_argument("--model-id", default="Qwen/Qwen3-30B-A3B-Instruct-2507")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-p", type=float, default=0.8)
    parser.add_argument("--max-tokens", type=int, default=2048)
    return parser.parse_args()


def main():
    args = parse_args()
    token = os.environ.get("HF_TOKEN")
    assert token, "HF_TOKEN not set. Add secrets={'HF_TOKEN': '$HF_TOKEN'} to job config."

    print(f"Loading dataset: {args.input_dataset}")
    ds = load_dataset(args.input_dataset, split="train")

    print(f"Loading model: {args.model_id}")
    llm = LLM(model=args.model_id, trust_remote_code=True)
    sampling_params = SamplingParams(
        temperature=args.temperature,
        top_p=args.top_p,
        max_tokens=args.max_tokens,
    )

    # Generate responses
    prompts = []
    for row in ds:
        if args.messages_column in row:
            messages = row[args.messages_column]
            prompt = llm.get_tokenizer().apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        else:
            prompt = row.get("prompt", "")
        prompts.append(prompt)

    print(f"Generating {len(prompts)} responses...")
    outputs = llm.generate(prompts, sampling_params)
    responses = [o.outputs[0].text for o in outputs]

    ds = ds.add_column("response", responses)

    print(f"Pushing to {args.output_dataset}")
    ds.push_to_hub(args.output_dataset, token=token)
    print("Done!")


if __name__ == "__main__":
    main()
