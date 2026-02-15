# Design System — XinHuaRen App Project

Crimson + Gold palette inspired by Chinese cultural aesthetics.
Used consistently across PPTX and PNG deliverables.

## Color Palette

### PPTX Colors (hex without #)

```javascript
const C = {
  dark: '8B1A1A', // deep crimson — headers, primary bg
  darkAlt: '6B1414', // darker crimson — overlays
  mid: 'B94040', // medium red — secondary accent
  accent: 'D4A574', // warm gold/tan — highlights, decorative
  cream: 'FFF8F0', // warm cream — slide background
  white: 'FFFFFF',
  offWhite: 'F5EDE3', // sand — subtle backgrounds
  text: '2D2020', // dark brown — primary text
  textLight: '6B5A5A', // muted text
  textWhite: 'FFF8F0', // text on dark bg
  cardBg: 'FFFFFF', // card backgrounds
  sectionBg: 'FDF6EF', // section backgrounds
}
```

### PNG Colors (hex with #)

```python
COLORS = {
    "bg": "#FFF8F0",          # cream background
    "header_bg": "#8B1A1A",   # crimson header
    "gold": "#D4A574",        # warm gold
    "text": "#2D2D2D",        # dark text
    "text_muted": "#6B6B6B",  # muted text
    "text_light": "#FFFFFF",  # white text
    "accent": "#8B1A1A",      # crimson accent
    "card_bg": "#FFFFFF",     # white cards
    "card_border": "#E8DCD0", # subtle card border
    "green": "#2D8B4E",       # completed/positive
    "tag_new": "#C75B39",     # NEW tag background
}
```

## Typography

### PPTX Fonts

- **Headings**: Georgia (serif, classical feel)
- **Body**: Calibri (clean sans-serif for readability)

### PNG Fonts

- **CJK**: `/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf`
- **Latin**: `/usr/share/fonts/truetype/lato/Lato-Regular.ttf`
- **Latin Bold**: `/usr/share/fonts/truetype/lato/Lato-Bold.ttf`

**Font selection rule**: Character-level switching via `is_cjk()`.
CJK unified ideographs, CJK punctuation, fullwidth characters → DroidSans.
Everything else (Latin, numbers, curly quotes, em dashes, arrows) → Lato.

## Layout Constants

### PPTX

- Slide layout: 16:9 (`LAYOUT_16x9`)
- Typical content margins: x=0.5-0.8, width=8.4-9.0
- Section header bar: full-width, 1.0" tall, dark crimson
- Card shadows: `{ type: "outer", color: "000000", blur: 6, offset: 3, angle: 135, opacity: 0.12 }`

### PNG

- Width: 1080px (fixed, mobile-optimized)
- Padding: 50px each side
- Content width: 980px
- Section headers: number in circle (44px) + title text
- Cards: white background, subtle border, rounded corners (12px radius)
- Card shadow: 3px offset, #E8E0D8

## Component Patterns

### Stats Row (PNG)

Four colored boxes in a row, alternating crimson/gold.
Each box: centered number (32pt bold) + label (16pt).

### Pain Point Card (PNG)

Role name (bold, crimson) → pain tag + text → direction tag + text.
Tags: small rounded rectangles with label ("痛点" / "方向").

### Decision List (both)

Numbered items with colored dot/circle prefix.
Completed items: green with checkmark.
New items: `（MM.DD新增）` suffix + NEW tag.

### Quote Blocks (both)

Vertical gold bar on left. Italic text + speaker attribution.
