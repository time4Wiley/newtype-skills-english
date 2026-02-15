---
name: project-sync-pack
description: Visual deliverables generator that reads master panorama markdown and regenerates PPTX presentation (PptxGenJS, crimson+gold design system) and mobile-friendly PNG infographic (Pillow dual-font renderer). Optionally runs dual-model quality review before generation.
---

# Project Sync Pack

Regenerates visual deliverables from the master panorama markdown. Encodes the
proven design system and rendering patterns from the original production run.

## Workflow Overview

```
Master MD (新华人App_项目全景梳理.md)
        |
        v
  [Read & parse content]
        |
        v
  [Optional: dual-model quality review]
        |
        v
  [Generate PPTX]  ────  PptxGenJS + crimson/gold design
        |
        v
  [Generate PNG]   ────  Pillow dual-font renderer
        |
        v
  [Visual QA]      ────  Screenshot verification
        |
        v
  Output: .pptx + .png in workspace
```

## Step 1: Read the Master Document

Find and read `新华人App_项目全景梳理.md` in the workspace. Parse its 9 sections:

1. 项目定位与背景
2. App 信息架构（五大Tab）
3. 义工痛点与需求
4. 项目路线图（三阶段）
5. AI技术方向与数字人战略
6. 论语班改革动态
7. 核心团队与分工
8. 关键决策与待办
9. 金句摘录

## Step 2: Optional Dual-Model Quality Review

Before generating visuals, optionally verify content quality using GPT-5.2 +
Gemini 3 Pro (requires `OPENAI_API_KEY` and `GEMINI_API_KEY`).

Read `references/dual-model-analyze.md` for the script template.

**Review prompt focus:**

```
Review this project panorama document for:
1. Consistency — do sections contradict each other?
2. Completeness — are any recent decisions missing context?
3. Clarity — which sections need tighter language for slides?
4. Visual hierarchy — suggest which items deserve prominence in PPTX/PNG

Document:
---
{md_content}
---
```

## Step 3: Generate PPTX (PptxGenJS)

### Design System

Read `references/design-system.md` for the full color/font/layout specification.

**Quick reference:**

| Token       | Value     | Usage                        |
| ----------- | --------- | ---------------------------- |
| dark        | `#8B1A1A` | Headers, primary backgrounds |
| accent      | `#D4A574` | Gold accents, highlights     |
| cream       | `#FFF8F0` | Slide backgrounds            |
| text        | `#2D2020` | Body text                    |
| textLight   | `#6B5A5A` | Muted text                   |
| Font (head) | Georgia   | Titles, headers              |
| Font (body) | Calibri   | Body text, bullets           |

### Critical PptxGenJS Patterns

Read `references/pptx-patterns.md` for the full list. Key pitfalls:

1. **Factory functions for options** — `makeShadow()` not shared `shadow` object.
   PptxGenJS mutates option objects internally. Reusing causes corruption.

2. **Unicode escapes for Chinese in template literals** — backtick strings
   with Chinese characters can cause encoding issues. Use `\uXXXX` escapes.

3. **`bullet: true`** — use the API's bullet property, not unicode bullet chars.

4. **Chinese filenames** — if using `soffice` for conversion, copy to ASCII
   filename first. Chinese filenames fail silently.

### Script Template

Read `scripts/create_pptx_template.js` for the full PptxGenJS script structure.

**Generation steps:**

```bash
# 1. Install pptxgenjs if not available
npm list pptxgenjs 2>/dev/null || npm install pptxgenjs

# 2. Write the script (adapting template with current MD content)
# 3. Run it
node create_pptx.js

# 4. Verify output exists and has reasonable size (>100KB)
ls -la output.pptx
```

### Slide Structure (10 slides)

| #   | Content           | Layout                       |
| --- | ----------------- | ---------------------------- |
| 1   | Title             | Dark bg, gold accents        |
| 2   | Table of Contents | Left nav + right stats       |
| 3   | 项目定位与背景    | Two-card split               |
| 4   | App信息架构       | 5 vertical tab cards         |
| 5   | 义工痛点          | 2×3 grid cards               |
| 6   | 跨平台数据孤岛    | 3-platform → solution flow   |
| 7   | 三阶段路线图      | Timeline + 3 phase cards     |
| 8   | AI技术+数字人     | 2×2 quadrant                 |
| 9   | 关键决策与待办    | Left decisions + right todos |
| 10  | Closing quotes    | Dark bg, gold quotes         |

## Step 4: Generate Mobile PNG (Pillow)

### Dual-Font Rendering Architecture

The PNG uses a two-pass approach with character-level font switching:

- **Pass 1 (measure)**: Calculate total height without drawing
- **Pass 2 (render)**: Allocate canvas at exact height, draw everything

**Font pairing:**

- CJK characters → `DroidSansFallbackFull.ttf`
- Latin/numbers/punctuation → `Lato-Regular.ttf` / `Lato-Bold.ttf`
- Special chars (`""—…·→✓`) → Lato (NOT CJK font — DroidSans lacks these)

Read `scripts/create_infographic_template.py` for the full renderer.

### Key Implementation Notes

1. **`is_cjk()` function** — maps characters to correct font. Critical: curly
   quotes `\u201c\u201d`, em dash `\u2014`, check mark `\u2713`, middot `\u00b7`,
   and arrow `\u2192` must NOT be mapped to CJK font.

2. **NEW tags** — position inline after text, not above. Measure text width
   first, then place tag at `x + text_width + 8`.

3. **Canvas dimensions** — width fixed at 1080px, height determined by measure
   pass. Typical range: 5000-6500px depending on content.

4. **Rounded rectangles** — custom implementation using pieslice + rectangles
   (Pillow lacks native rounded rect in older versions).

### Generation steps:

```bash
# Pillow should be pre-installed. If not:
pip install Pillow --break-system-packages -q

# Write the script (adapting template with current MD content)
python create_infographic.py

# Verify output
ls -la output.png
# Should be 0.5-1.0 MB, 1080×5000-6500px
```

## Step 5: Visual QA

After generating both files:

1. **PPTX**: Open with `soffice` and take screenshots of key slides
   - Remember: copy to ASCII filename first if name contains Chinese
   - `cp "中文名.pptx" temp_verify.pptx && soffice --headless --convert-to pdf temp_verify.pptx`
   - Then verify PDF pages

2. **PNG**: View directly with the Read tool (it renders images natively)
   - Check: all text readable, no □ boxes, NEW tags positioned correctly
   - Check: color scheme matches (crimson headers, cream background, gold accents)
   - Check: stats row numbers render correctly (Latin font, not CJK)

## Step 6: Deliver & Suggest

After successful generation:

1. Save both files to workspace:
   - `新华人App_项目全景梳理.pptx`
   - `新华人App_项目全景梳理_手机版.png`

2. Provide computer:// links for both files

3. Remind the user:
   > "Visual deliverables regenerated. If new meeting content needs to be
   > integrated first, use the `meeting-digest` skill."

## Critical Knowledge (from production experience)

1. **PptxGenJS shadow object mutation** — ALWAYS use factory functions like
   `makeShadow()`. Never share a shadow/options object between slides.

2. **DroidSansFallbackFull coverage gaps** — this font handles CJK well but
   CANNOT render: curly quotes, em dashes, check marks, arrows, middots.
   These fall through to Lato.

3. **Chinese filenames + soffice** — soffice silently fails with non-ASCII
   filenames. Always copy to ASCII name before conversion.

4. **node-canvas won't work** — the container can't install native dependencies
   (no sudo). Use Pillow (Python) for image generation, PptxGenJS (Node) for PPTX.

5. **Two-pass rendering is essential** — Pillow's Image requires fixed dimensions
   at creation. The measure pass calculates exact height, avoiding truncation or
   excessive whitespace.

6. **Unicode escapes in Python strings** — when embedding Chinese text with
   special punctuation (curly quotes, em dashes) in Python source code, use
   `\uXXXX` escapes to avoid `SyntaxError: invalid character` issues.

## Resources

### references/

- `design-system.md` — Complete color palette, font pairing, and layout constants
- `pptx-patterns.md` — PptxGenJS patterns, pitfalls, and best practices
- `dual-model-analyze.md` — Dual-model quality review script template

### scripts/

- `create_pptx_template.js` — PptxGenJS script template (10-slide structure)
- `create_infographic_template.py` — Pillow dual-font PNG renderer template
