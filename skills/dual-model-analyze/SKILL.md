---
name: dual-model-analyze
description: Run data analysis using both GPT-5.2 (high reasoning) and Gemini 3 Pro (high thinking) in parallel, then synthesize outputs. Requires OPENAI_API_KEY and GEMINI_API_KEY environment variables and uv tool.
allowed-tools: Bash, Write, Read
---

# Dual-Model Data Analyze

Run data analysis using both GPT-5.2 (high reasoning) and Gemini 3 Pro (high thinking) in parallel, then synthesize their outputs into a unified analysis.

## Instructions

### 1. Parse the Analysis Prompt

Extract the analysis request from: **$ARGUMENTS**

If `$ARGUMENTS` is empty, ask the user what data or topic they want analyzed.

### 2. Validate API Keys

Check that both environment variables are set:
- `OPENAI_API_KEY` - Required for GPT-5.2
- `GEMINI_API_KEY` - Required for Gemini 3 Pro

```bash
# Quick validation
python3 -c "import os; [print(f'{"OK" if os.environ.get(k) else "MISSING"}: {k}') for k in ('OPENAI_API_KEY', 'GEMINI_API_KEY')]"
```

If either key is missing, warn the user and stop.

### 3. Generate the Analysis Script

Create a Python script using **uv inline script metadata** so it runs with zero setup via `uv run`. The script should:

1. Send the user's prompt to **both models in parallel** using `asyncio` + `concurrent.futures`
2. Use **GPT-5.2** with `reasoning.effort = "high"` via the Responses API
3. Use **Gemini 3 Pro Preview** with `thinking_level = HIGH` via the GenAI SDK
4. Collect both responses and print them side-by-side
5. Optionally synthesize a combined summary

#### Script Template

Use this as the base template, adapting the prompt from `$ARGUMENTS`:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "openai>=1.82.0",
#     "google-genai>=1.51.0",
# ]
# ///
"""Dual-model data analysis: GPT-5.2 (high) + Gemini 3 Pro (high)."""

import os
import sys
import asyncio
from concurrent.futures import ThreadPoolExecutor

from openai import OpenAI
from google import genai
from google.genai import types


ANALYSIS_PROMPT = """
{user_prompt}
""".strip()

SYSTEM_PROMPT = (
    "You are a senior data analyst. Provide structured, evidence-based analysis. "
    "Use sections, bullet points, and quantitative reasoning where possible."
)


def call_gpt52(prompt: str) -> str:
    """Call GPT-5.2 with high reasoning effort."""
    client = OpenAI()  # uses OPENAI_API_KEY
    response = client.responses.create(
        model="gpt-5.2",
        input=[
            {"role": "developer", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        reasoning={"effort": "high"},
    )
    parts = []
    for item in response.output:
        if hasattr(item, "content"):
            for content in item.content:
                if hasattr(content, "text"):
                    parts.append(content.text)
    return "\n".join(parts)


def call_gemini3(prompt: str) -> str:
    """Call Gemini 3 Pro Preview with high thinking."""
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=f"{SYSTEM_PROMPT}\n\n{prompt}",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level=types.ThinkingLevel.HIGH,
            ),
        ),
    )
    parts = []
    for part in response.candidates[0].content.parts:
        if not part.thought:
            parts.append(part.text)
    return "\n".join(parts)


async def analyze(prompt: str) -> None:
    """Run both models in parallel and print results."""
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=2) as pool:
        gpt_future = loop.run_in_executor(pool, call_gpt52, prompt)
        gem_future = loop.run_in_executor(pool, call_gemini3, prompt)
        gpt_result, gem_result = await asyncio.gather(
            gpt_future, gem_future, return_exceptions=True
        )

    print("=" * 72)
    print("GPT-5.2 (high reasoning)")
    print("=" * 72)
    if isinstance(gpt_result, Exception):
        print(f"ERROR: {gpt_result}")
    else:
        print(gpt_result)

    print()
    print("=" * 72)
    print("Gemini 3 Pro (high thinking)")
    print("=" * 72)
    if isinstance(gem_result, Exception):
        print(f"ERROR: {gem_result}")
    else:
        print(gem_result)


if __name__ == "__main__":
    # Allow overriding prompt via CLI argument
    prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ANALYSIS_PROMPT
    if not prompt.strip():
        print("Usage: uv run dual_analyze.py <analysis prompt>")
        sys.exit(1)

    missing = [k for k in ("OPENAI_API_KEY", "GEMINI_API_KEY") if not os.environ.get(k)]
    if missing:
        print(f"Missing environment variables: {', '.join(missing)}")
        sys.exit(1)

    asyncio.run(analyze(prompt))
```

### 4. Write and Run the Script

1. Write the generated script to a temporary file (e.g., `_dual_analyze.py`)
2. Replace `{user_prompt}` in `ANALYSIS_PROMPT` with the actual content from `$ARGUMENTS`
3. Run it with: `uv run _dual_analyze.py`
4. Display both model outputs to the user
5. Provide a brief synthesis highlighting where the models agree and diverge
6. Clean up the temporary script file

### 5. Post-Analysis Synthesis

After both models respond, summarize:

- **Agreement** - Key findings both models converge on
- **Divergence** - Where they differ in interpretation or emphasis
- **Recommendation** - Which model's output is stronger for this specific analysis and why
- **Combined insight** - Any conclusions that emerge from comparing both outputs

## Usage Examples

```bash
# Analyze a dataset pattern
/dual-model-analyze Analyze the correlation between API response times and error rates in this CSV data: [paste data]

# Market analysis
/dual-model-analyze Compare the competitive landscape of LLM API providers in 2026, focusing on pricing, capabilities, and developer experience

# Code performance analysis
/dual-model-analyze Analyze the time complexity and potential bottlenecks in this algorithm: [paste code]

# Business metrics
/dual-model-analyze Given these quarterly metrics, identify trends and forecast Q3: Revenue $2.1M, $2.4M, Churn 3.2%, 2.8%, NPS 42, 47
```

## Requirements

- **Environment variables**: `OPENAI_API_KEY`, `GEMINI_API_KEY`
- **Runtime**: `uv` (no pre-installed packages needed; uv handles dependencies inline)
- **Python**: 3.11+
- **Packages** (auto-installed by uv): `openai>=1.82.0`, `google-genai>=1.51.0`
