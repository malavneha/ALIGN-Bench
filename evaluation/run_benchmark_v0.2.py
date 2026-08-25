"""
ALIGN-Bench v0.2 model runner (OpenAI Responses API).

Reads the benchmark CSV and records the exact model outputs.
Never put an API key in this file or commit one to GitHub.

Install:
    pip install openai pandas

Set your API key locally:
    export OPENAI_API_KEY="YOUR_KEY"

Run:
    python run_benchmark_v0.2.py \
        --input data/benchmark_v0.2.3.csv \
        --output results/openai_run1.csv \
        --model gpt-5.6-luna \
        --run-number 1
"""

import argparse
import os
import time
from datetime import datetime, timezone

import pandas as pd
from openai import OpenAI


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--run-number", type=int, default=1)
    parser.add_argument("--delay", type=float, default=0.5)
    args = parser.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set.")

    df = pd.read_csv(args.input)

    if "item_id" not in df.columns or "prompt" not in df.columns:
        raise ValueError("Benchmark must contain item_id and prompt columns.")

    client = OpenAI()
    rows = []

    for _, item in df.iterrows():
        prompt = str(item["prompt"])
        started = datetime.now(timezone.utc).isoformat()

        try:
            response = client.responses.create(
                model=args.model,
                input=prompt,
            )
            text = response.output_text
            status = "success"
            error = ""
        except Exception as exc:
            text = ""
            status = "error"
            error = repr(exc)

        rows.append({
            "item_id": item["item_id"],
            "prompt": prompt,
            "expected_label": item.get("expected_label", ""),
            "model": args.model,
            "model_version": args.model,
            "run_number": args.run_number,
            "response": text,
            "timestamp_utc": started,
            "status": status,
            "error": error,
        })

        pd.DataFrame(rows).to_csv(args.output, index=False)
        time.sleep(args.delay)

    print(f"Completed {len(rows)} benchmark items.")
    print(f"Saved responses to: {args.output}")


if __name__ == "__main__":
    main()
