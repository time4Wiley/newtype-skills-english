# Dual-Model Analysis Script Template

Use this template to run parallel analysis with GPT-5.2 and Gemini 3 Pro.
Requires `OPENAI_API_KEY` and `GEMINI_API_KEY` environment variables.

## Usage

1. Copy the script below into `_meeting_analyze.py`
2. Replace `{user_prompt}` with your analysis prompt (see SKILL.md Step 3)
3. Run: `uv run _meeting_analyze.py`

## Script Template

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "openai>=1.82.0",
#     "google-genai>=1.51.0",
# ]
# ///
"""
Dual-model meeting analysis: GPT-5.2 + Gemini 3 Pro
Zero-setup via uv inline metadata — just run: uv run _meeting_analyze.py
"""

import asyncio
import os
import sys
from concurrent.futures import ThreadPoolExecutor

from openai import OpenAI
from google import genai
from google.genai import types

SYSTEM_PROMPT = """You are a senior analyst specializing in organizational strategy
and project management for cultural education technology platforms. You extract
structured insights from meeting transcripts with high precision."""

USER_PROMPT = """{user_prompt}"""


def call_gpt52(prompt: str) -> str:
    """Call GPT-5.2 with high reasoning effort."""
    client = OpenAI()  # uses OPENAI_API_KEY env var
    response = client.responses.create(
        model="gpt-5.2",
        input=[
            {"role": "developer", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        reasoning={"effort": "high"},
    )
    texts = []
    for item in response.output:
        if hasattr(item, "text"):
            texts.append(item.text)
        elif hasattr(item, "content"):
            for block in item.content:
                if hasattr(block, "text"):
                    texts.append(block.text)
    return "\n".join(texts)


def call_gemini3(prompt: str) -> str:
    """Call Gemini 3 Pro with high thinking."""
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
    texts = []
    for part in response.candidates[0].content.parts:
        if not hasattr(part, "thought") or not part.thought:
            texts.append(part.text)
    return "\n".join(texts)


async def run_parallel(prompt: str):
    """Run both models in parallel and print results."""
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=2) as pool:
        gpt_future = loop.run_in_executor(pool, call_gpt52, prompt)
        gem_future = loop.run_in_executor(pool, call_gemini3, prompt)
        gpt_result, gem_result = await asyncio.gather(
            gpt_future, gem_future, return_exceptions=True
        )

    print("=" * 60)
    print("GPT-5.2 ANALYSIS")
    print("=" * 60)
    if isinstance(gpt_result, Exception):
        print(f"ERROR: {gpt_result}")
    else:
        print(gpt_result)

    print("\n" + "=" * 60)
    print("GEMINI 3 PRO ANALYSIS")
    print("=" * 60)
    if isinstance(gem_result, Exception):
        print(f"ERROR: {gem_result}")
    else:
        print(gem_result)

    # Synthesis guidance
    print("\n" + "=" * 60)
    print("SYNTHESIS GUIDANCE")
    print("=" * 60)
    print("""
Review both outputs and categorize each finding:

HIGH CONFIDENCE (both models agree):
  → Include directly in master document update

SINGLE-MODEL FINDING (only one model found it):
  → Review carefully — usually still valid, include with note

CONTRADICTION (models disagree):
  → Flag for human review, present both perspectives
""")


if __name__ == "__main__":
    asyncio.run(run_parallel(USER_PROMPT))
```

## Synthesis Protocol

After running, Claude should:

1. **Compare outputs** side by side
2. **Mark confidence levels**:
   - Both agree → ✅ High confidence
   - One found it → ⚠️ Review needed
   - Contradiction → ❌ Flag for human
3. **Merge into unified extraction** following the categorization in SKILL.md Step 4
