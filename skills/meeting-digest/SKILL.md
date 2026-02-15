---
name: meeting-digest
description: >
  **Meeting Digest Processor for the XinHuaRen App project**: Reads a new meeting
  transcript (.docx, .txt, or pasted text), extracts decisions/todos/insights/team
  changes, diffs against the existing master panorama markdown, and produces an
  updated MD with clear annotations. Optionally runs dual-model analysis (GPT-5.2
  + Gemini 3 Pro) for deeper insight extraction and cross-validation.
  MANDATORY TRIGGERS: meeting notes, meeting transcript, discussion notes, sync notes,
  update the panorama, update the master doc, new discussion, latest meeting,
  any Chinese like: 会议纪要, 会议记录, 最新讨论, 更新全景梳理, 消化会议
---

# Meeting Digest Processor

Processes meeting transcripts from the XinHuaRen App project team and updates the
master panorama markdown. Born from the real workflow of processing 6 source
documents across multiple sessions — encodes the patterns that actually worked.

## Workflow Overview

```
New transcript (.docx/.txt/pasted)
        |
        v
  [Extract raw text]
        |
        v
  [Dual-model analysis]  <-- GPT-5.2 + Gemini 3 Pro (optional)
        |
        v
  [Categorize extractions]
  Decisions | Todos | Insights | Team | Completed | Quotes
        |
        v
  [Diff against existing master MD]
        |
        v
  [Update master MD section by section]
        |
        v
  [Generate change summary]
        |
        v
  [Suggest: run project-sync-pack for PPTX+PNG refresh]
```

## Step 1: Locate the Master Document

Find the existing panorama markdown in the workspace. Default name:
`新华人App_项目全景梳理.md`

Read it fully. You need to understand the current state to identify what's new.

## Step 2: Extract Content from the New Transcript

**For .docx files** — use python-docx:

```python
pip install python-docx --break-system-packages -q
from docx import Document
doc = Document("path/to/transcript.docx")
full_text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
```

**For .txt or pasted content** — read directly.

**For .m4a audio** — check for companion `.txt.bak` or `.docx` transcription files
(the team often has pre-transcribed versions alongside audio files).

## Step 3: Dual-Model Deep Analysis (Recommended)

When `OPENAI_API_KEY` and `GEMINI_API_KEY` environment variables are available,
run dual-model analysis for cross-validated insight extraction. This catches
nuances and strategic implications a single pass might miss.

Read `references/dual-model-analyze.md` for the complete script template.

**Integration approach:**

1. Construct a focused analysis prompt:

```
You are analyzing a meeting transcript from the XinHuaRen (新华人) App project.
This project builds an overseas Chinese cultural education platform with AI
integration, digital human (数字人) capabilities, and volunteer (义工) workflow
optimization.

Key team members to watch for:
- 张静 (strategic leader, project direction)
- 孙伟 (total architect, tech decisions)
- 白文娟 (execution, operations)
- 陈建妹 (overseas liaison)
- 张兆强 (community support)

Extract and categorize with HIGH precision:

1. DECISIONS — anything confirmed, agreed on, or explicitly ruled out
2. ACTION ITEMS — who owns what, by when
3. STRATEGIC SHIFTS — changes from previous direction or new paradigms
4. TECHNICAL APPROACHES — new tools, models, architecture choices
5. TEAM/ROLE CHANGES — reassignments, new members, responsibility shifts
6. NOTABLE QUOTES — statements capturing vision, values, or key insights

For each item, explain its significance to the project trajectory.

Here is the transcript:
---
{transcript_content}
---
```

2. Write the script using the template from `references/dual-model-analyze.md`,
   substituting `{user_prompt}` with the above prompt
3. Run: `uv run _meeting_analyze.py`
4. **Synthesize** both outputs:
   - **Both models agree** → high confidence, include directly
   - **Only one model found it** → review carefully, usually still valid
   - **Models contradict** → flag for human review with both perspectives

If API keys are unavailable, proceed with Claude-only analysis (still effective,
just without the cross-validation safety net).

## Step 4: Categorize Extractions

Organize everything found into these buckets:

| Category            | What to look for                                 | Section in master MD |
| ------------------- | ------------------------------------------------ | -------------------- |
| Decisions           | "we decided", "confirmed", "ruled out", "agreed" | Section 8            |
| Todos               | Action items, "need to", assignments, deadlines  | Section 8            |
| Strategic insights  | Vision shifts, new concepts, paradigm changes    | Section 1, 5         |
| Team changes        | Role changes, new members, responsibility shifts | Section 7            |
| Completed items     | Previously-open todos now done                   | Section 8            |
| Technical decisions | Tool choices, architecture, AI model selections  | Section 4, 5         |
| Pain point updates  | New or resolved volunteer pain points            | Section 3            |
| Reform updates      | Changes to 论语班 operations                     | Section 6            |
| Quotes              | Memorable statements with speaker + date         | Section 9            |

## Step 5: Update the Master Document

The master document structure (preserve this exactly):

```
# 新华人 App 项目全景梳理
> 综合整理自：[source list]
> 整理时间：[date]
---
## 一、项目定位与背景
## 二、App 信息架构（五大Tab）
## 三、义工痛点与需求（按角色分类）
## 四、项目路线图（三阶段）
## 五、AI技术方向与数字人战略
## 六、论语班改革动态（61期）
## 七、核心团队与分工
## 八、关键决策与待办
## 九、金句摘录
```

**Update rules:**

- **Header**: Append new source document name to the `综合整理自` list. Update date.
- **Sections 1-6**: Modify only when the new meeting introduces relevant changes.
  Integrate naturally — don't append a "NEW SECTION" block, weave it into the
  existing narrative while preserving flow.
- **Section 5 (AI/Digital Human)**: Changes most frequently. New technical
  decisions, prototype results, and strategy pivots go here. Subsections:
  5.1 技术路线决策, 5.2 数字人战略, 5.3 AI运营智能体, 5.4 多语言国际化
- **Section 7 (Team table)**: Update if roles changed. Use the table format:
  `| 角色 | 负责人 | 主要职责 |`
- **Section 8 (Decisions & Todos)**:
  - New decisions: add with `（MM.DD新增）` suffix
  - Completed todos: mark with `~~strikethrough~~`
  - New todos: add with `（MM.DD新增）` suffix
  - Keep sequential numbering
- **Section 9 (Quotes)**: Append new quotes as blockquotes with speaker and
  date: `> "quote" ——Speaker（MM.DD）`

## Step 6: Generate Change Summary

After updating, output a concise summary:

```markdown
## 本次更新摘要 (MM.DD)

**来源**: [document name]

### 新增决策 (N)

1. [decision]
2. [decision]

### 新增待办 (N)

1. [todo with owner]

### 主要变更

- 第X节: [what changed]
- 第Y节: [what changed]

### 已完成

- ~~[completed item]~~

### 双模型分析置信度 (if used)

- 高置信 (双模型一致): N items
- 单模型发现: N items
- 待人工确认: N items
```

## Step 7: Suggest Next Steps

After updating the MD, always remind the user:

> "Master document updated. To regenerate the PPTX and mobile PNG, use the
> `project-sync-pack` skill."

## Critical Domain Knowledge

These patterns come from real issues encountered across 6 documents:

1. **紫杉 is ruled out** — this was a key decision. If new meetings reference 紫杉,
   it's historical context only, not a reconsideration

2. **Digital human (数字人) is extremely sensitive** — 肖老师's representation carries
   enormous responsibility ("一语讲错堕多少世为狐"). Flag any changes to this strategy
   prominently

3. **Two-step digital human approach** — near-term: intelligent clip retrieval (real
   肖老师 audio/video); parallel: digital human training. Don't confuse these

4. **张静 = strategic direction, 孙伟 = technical architecture** — when they align
   on something, it's a confirmed decision. 白文娟's operational concerns reflect
   ground truth from the volunteer front lines

5. **Meeting transcripts are messy** — people interrupt, revisit topics, sometimes
   contradict earlier statements. Always capture the _final consensus_, not every
   intermediate position

6. **AI全流程赋能** — AI isn't limited to product; it covers operations, marketing,
   learning, translation — every aspect of the project

## Resources

### references/

- `dual-model-analyze.md` — Complete dual-model (GPT-5.2 + Gemini 3 Pro) analysis
  script template with uv inline metadata. Read this before running dual-model analysis.

### scripts/

- `extract_docx.py` — Helper to extract text from .docx files with paragraph preservation
