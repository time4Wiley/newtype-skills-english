#!/usr/bin/env python3
"""
Mobile-friendly PNG infographic template for 新华人 App 项目全景梳理
Dual-font approach: Lato for Latin/numbers, DroidSans for CJK

Usage:
  pip install Pillow --break-system-packages -q  # if not installed
  python create_infographic.py

IMPORTANT:
- Two-pass rendering: measure height first, then render
- Character-level font switching via is_cjk()
- Curly quotes, em dashes, arrows → Lato (NOT DroidSans)
- Use \\uXXXX escapes for Chinese in Python source to avoid SyntaxError
"""
from PIL import Image, ImageDraw, ImageFont

# ====== DESIGN SYSTEM ======
W = 1080
PAD = 50
CONTENT_W = W - PAD * 2

COLORS = {
    "bg": "#FFF8F0",
    "header_bg": "#8B1A1A",
    "gold": "#D4A574",
    "text": "#2D2D2D",
    "text_muted": "#6B6B6B",
    "text_light": "#FFFFFF",
    "accent": "#8B1A1A",
    "card_bg": "#FFFFFF",
    "card_border": "#E8DCD0",
    "green": "#2D8B4E",
    "tag_new": "#C75B39",
}

# ====== FONTS ======
FONT_CJK = "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"
FONT_LATIN = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
FONT_LATIN_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

_font_cache = {}
def get_font(size, bold=False, cjk=False):
    if cjk:
        key = (FONT_CJK, size)
    elif bold:
        key = (FONT_LATIN_BOLD, size)
    else:
        key = (FONT_LATIN, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(key[0], key[1])
    return _font_cache[key]


def is_cjk(ch):
    """Check if character needs CJK font.

    CRITICAL: Do NOT map these to CJK (DroidSans lacks them):
    - Curly quotes: \\u201c \\u201d \\u2018 \\u2019
    - Em dash: \\u2014
    - Ellipsis: \\u2026
    - Middot: \\u00b7
    - Arrow: \\u2192
    - Check: \\u2713
    """
    cp = ord(ch)
    if 0x4E00 <= cp <= 0x9FFF: return True   # CJK Unified Ideographs
    if 0x3400 <= cp <= 0x4DBF: return True   # CJK Ext A
    if 0x20000 <= cp <= 0x2A6DF: return True # CJK Ext B
    if 0x3000 <= cp <= 0x303F: return True   # CJK punctuation
    if 0xFF00 <= cp <= 0xFFEF: return True   # Fullwidth
    if 0x3040 <= cp <= 0x30FF: return True   # Hiragana/Katakana
    if 0xF900 <= cp <= 0xFAFF: return True   # CJK Compatibility
    return False


def measure_mixed_text(draw, text, size, bold=False):
    """Measure width of mixed CJK/Latin text."""
    total_w = 0
    for ch in text:
        f = get_font(size, bold, is_cjk(ch))
        bbox = draw.textbbox((0, 0), ch, font=f)
        total_w += bbox[2] - bbox[0]
    return total_w


def draw_mixed_text(draw, xy, text, size, color, bold=False):
    """Draw text with automatic CJK/Latin font switching."""
    if draw is None:
        return
    x, y = xy
    for ch in text:
        f = get_font(size, bold, is_cjk(ch))
        draw.text((x, y), ch, font=f, fill=color)
        bbox = draw.textbbox((0, 0), ch, font=f)
        x += bbox[2] - bbox[0]
    return x


def wrap_mixed_text(draw, text, max_width, size, bold=False):
    """Word-wrap mixed CJK/Latin text."""
    lines = []
    for paragraph in text.split("\n"):
        current = ""
        current_w = 0
        for ch in paragraph:
            f = get_font(size, bold, is_cjk(ch))
            bbox = draw.textbbox((0, 0), ch, font=f)
            ch_w = bbox[2] - bbox[0]
            if current_w + ch_w > max_width and current:
                lines.append(current)
                current = ch
                current_w = ch_w
            else:
                current += ch
                current_w += ch_w
        if current:
            lines.append(current)
    return lines


def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw rounded rectangle (Pillow compat)."""
    if draw is None:
        return
    x0, y0, x1, y1 = xy
    r = min(radius, (x1-x0)//2, (y1-y0)//2)
    if r < 1:
        if fill:
            draw.rectangle([x0, y0, x1, y1], fill=fill)
        if outline:
            draw.rectangle([x0, y0, x1, y1], outline=outline, width=width)
        return
    if fill:
        draw.rectangle([x0 + r, y0, x1 - r, y1], fill=fill)
        draw.rectangle([x0, y0 + r, x1, y1 - r], fill=fill)
        draw.pieslice([x0, y0, x0 + 2*r, y0 + 2*r], 180, 270, fill=fill)
        draw.pieslice([x1 - 2*r, y0, x1, y0 + 2*r], 270, 360, fill=fill)
        draw.pieslice([x0, y1 - 2*r, x0 + 2*r, y1], 90, 180, fill=fill)
        draw.pieslice([x1 - 2*r, y1 - 2*r, x1, y1], 0, 90, fill=fill)
    if outline:
        draw.arc([x0, y0, x0 + 2*r, y0 + 2*r], 180, 270, fill=outline, width=width)
        draw.arc([x1 - 2*r, y0, x1, y0 + 2*r], 270, 360, fill=outline, width=width)
        draw.arc([x0, y1 - 2*r, x0 + 2*r, y1], 90, 180, fill=outline, width=width)
        draw.arc([x1 - 2*r, y1 - 2*r, x1, y1], 0, 90, fill=outline, width=width)
        draw.line([x0 + r, y0, x1 - r, y0], fill=outline, width=width)
        draw.line([x0 + r, y1, x1 - r, y1], fill=outline, width=width)
        draw.line([x0, y0 + r, x0, y1 - r], fill=outline, width=width)
        draw.line([x1, y0 + r, x1, y1 - r], fill=outline, width=width)


class Renderer:
    """Two-pass renderer: measure → allocate canvas → render.

    Usage:
        r = Renderer()
        r.generate()
    """
    def __init__(self):
        self.y = 0
        self.draw = None
        self.measuring = False
        self._mimg = Image.new("RGB", (W, 100), "white")
        self._mdraw = ImageDraw.Draw(self._mimg)

    @property
    def d(self):
        return self._mdraw if self.measuring else self.draw

    def text(self, x, y, text, size, color, bold=False):
        if not self.measuring and self.draw:
            draw_mixed_text(self.draw, (x, y), text, size, color, bold)

    def wrapped(self, x, y, text, size, color, max_w, line_h, bold=False):
        lines = wrap_mixed_text(self.d, text, max_w, size, bold)
        cy = y
        for line in lines:
            self.text(x, cy, line, size, color, bold)
            cy += line_h
        return cy

    def card(self, x, y, w, h, radius=12):
        if not self.measuring and self.draw:
            draw_rounded_rect(self.draw, (x+3, y+3, x+w+3, y+h+3), radius, fill="#E8E0D8")
            draw_rounded_rect(self.draw, (x, y, x+w, y+h), radius,
                            fill=COLORS["card_bg"], outline=COLORS["card_border"])

    def badge(self, x, y, text, size, bg_color, text_color, pad_x=14, pad_y=4):
        tw = measure_mixed_text(self.d, text, size, bold=True)
        bw = tw + pad_x * 2
        bh = size + pad_y * 2 + 4
        if not self.measuring and self.draw:
            draw_rounded_rect(self.draw, (x, y, x + bw, y + bh), 6, fill=bg_color)
            draw_mixed_text(self.draw, (x + pad_x, y + pad_y), text, size, text_color, bold=True)
        return bw

    def tag(self, x, y, text, bg_color, text_color):
        f = get_font(14, bold=True)
        bbox = self.d.textbbox((0, 0), text, font=f)
        tw = bbox[2] - bbox[0] + 14
        if not self.measuring and self.draw:
            draw_rounded_rect(self.draw, (x, y, x + tw, y + 24), 4, fill=bg_color)
            self.draw.text((x + 7, y + 3), text, font=f, fill=text_color)
        return tw

    def section_header(self, num, title, subtitle=""):
        y = self.y
        cx = PAD + 22
        if not self.measuring and self.draw:
            self.draw.ellipse([cx-22, y, cx+22, y+44], fill=COLORS["header_bg"])
            f = get_font(24, bold=True)
            bbox = self.draw.textbbox((0, 0), num, font=f)
            tw = bbox[2] - bbox[0]
            self.draw.text((cx - tw//2, y+8), num, font=f, fill=COLORS["text_light"])
        self.text(PAD + 56, y + 4, title, 32, COLORS["text"], bold=True)
        y += 50
        if subtitle:
            self.text(PAD + 56, y - 4, subtitle, 20, COLORS["text_muted"])
            y += 30
        if not self.measuring and self.draw:
            self.draw.rectangle([PAD, y, PAD+CONTENT_W, y+3], fill=COLORS["gold"])
        y += 20
        self.y = y

    def bullet(self, x, y, text, size, color, max_w, line_h):
        if not self.measuring and self.draw:
            self.draw.ellipse([x, y+8, x+10, y+18], fill=COLORS["gold"])
        return self.wrapped(x + 18, y, text, size, color, max_w - 18, line_h)

    def render(self):
        """Main render function. TODO: Adapt content from master MD.

        Structure:
        1. Header (crimson bar with title)
        2. Section 1: Project positioning
        3. Section 2: App architecture (5 tabs)
        4. Section 3: Pain points
        5. Section 4: Roadmap (3 phases)
        6. Section 5: AI & Digital Human strategy
        7. Section 6: Team
        8. Section 7: Decisions & Todos
        9. Section 8: Quotes
        10. Footer
        """
        self.y = 0
        CX = PAD + 28
        CW = CONTENT_W - 56

        # ====== HEADER ======
        if not self.measuring and self.draw:
            self.draw.rectangle([0, 0, W, 280], fill=COLORS["header_bg"])
            self.draw.rectangle([PAD, 55, PAD+80, 59], fill=COLORS["gold"])
        # TODO: Update header text from master MD
        self.text(PAD, 70, "\u65b0\u534e\u4eba App", 52, COLORS["text_light"], bold=True)
        self.text(PAD, 140, "\u9879\u76ee\u5168\u666f\u68b3\u7406", 40, COLORS["gold"], bold=True)
        self.text(PAD, 196, "\u6d77\u5916\u534e\u5b66...", 22, "#FFFFFFB0")
        self.text(PAD, 238, "2026\u5e74X\u6708 \u00b7 ...", 18, "#FFFFFF80")
        self.y = 310

        # TODO: Implement all sections following patterns from the production script.
        # Each section follows the pattern:
        #
        #   self.section_header("N", "Title", "Subtitle")
        #   # Calculate card height based on content
        #   lines = wrap_mixed_text(self.d, content, CW, font_size)
        #   ch = len(lines) * line_height + padding
        #   self.card(PAD, self.y, CONTENT_W, ch)
        #   # Render content inside card
        #   self.y += ch + spacing

        # ====== FOOTER ======
        if not self.measuring and self.draw:
            self.draw.rectangle([0, self.y, W, self.y + 120], fill=COLORS["header_bg"])
            self.draw.rectangle([PAD, self.y + 20, PAD + 60, self.y + 23], fill=COLORS["gold"])
        self.text(PAD, self.y + 36, "\u771f\u5b9e\u7684\u4eba + AI\u7684\u667a\u80fd = \u6709\u6e29\u5ea6\u7684\u667a\u80fd\u5316\u670d\u52a1",
                  24, COLORS["text_light"], bold=True)
        self.text(PAD, self.y + 76, "\u65b0\u534e\u4eba App \u9879\u76ee\u7ec4 \u00b7 2026\u5e74X\u6708",
                  18, "#FFFFFF99")
        self.y += 120

        return self.y

    def generate(self):
        # Pass 1: measure total height
        self.measuring = True
        total_h = self.render() + 40
        print(f"Measured height: {total_h}")

        # Pass 2: render onto canvas
        self.measuring = False
        self.img = Image.new("RGB", (W, total_h), COLORS["bg"])
        self.draw = ImageDraw.Draw(self.img)
        self.render()

        # TODO: Update output path
        output = "/sessions/exciting-jolly-goldberg/mnt/requirements/output.png"
        self.img.save(output, "PNG", optimize=True)
        import os
        size_mb = os.path.getsize(output) / 1024 / 1024
        print(f"Saved: {output} ({size_mb:.1f} MB, {W}x{total_h})")


if __name__ == "__main__":
    r = Renderer()
    r.generate()
