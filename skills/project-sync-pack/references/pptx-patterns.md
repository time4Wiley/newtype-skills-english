# PptxGenJS Patterns & Pitfalls

Hard-won lessons from building the XinHuaRen project PPTX.

## Pattern 1: Factory Functions for Options

**CRITICAL**: PptxGenJS mutates option objects internally. If you reuse a
shadow or options object across multiple elements, later elements get corrupted.

```javascript
// BAD — will cause subtle corruption
const shadow = { type: "outer", color: "000000", blur: 4, offset: 2, angle: 135, opacity: 0.10 };
slide1.addShape(pres.shapes.RECTANGLE, { ..., shadow });
slide2.addShape(pres.shapes.RECTANGLE, { ..., shadow }); // corrupted!

// GOOD — factory function creates fresh object each time
const makeShadow = () => ({ type: "outer", color: "000000", blur: 4, offset: 2, angle: 135, opacity: 0.10 });
slide1.addShape(pres.shapes.RECTANGLE, { ..., shadow: makeShadow() });
slide2.addShape(pres.shapes.RECTANGLE, { ..., shadow: makeShadow() });
```

## Pattern 2: Unicode Escapes in Template Literals

When Chinese characters appear inside backtick template literals, Node.js
can sometimes produce encoding issues. Use `\uXXXX` escapes for safety:

```javascript
// OK for simple strings
slide.addText("项目全景梳理", { ... });

// SAFER for template literals and complex strings
slide.addText("\u9879\u76EE\u5168\u666F\u68B3\u7406", { ... });
```

## Pattern 3: Rich Text Arrays for Mixed Styling

PptxGenJS supports rich text via arrays of text objects:

```javascript
slide.addText(
  [
    { text: '标题：', options: { bold: true, color: '8B1A1A' } },
    { text: '正文内容', options: { color: '6B5A5A' } },
    { text: '', options: { breakLine: true, fontSize: 8 } }, // spacer
    { text: '下一段', options: { breakLine: true, color: '2D2020' } },
  ],
  { x: 0.8, y: 2.0, w: 3.7, h: 2.0, fontSize: 13, fontFace: 'Calibri' }
)
```

**Key**: Use `{ text: "", options: { breakLine: true, fontSize: 8 } }` for
vertical spacing between rich text segments.

## Pattern 4: Block Scoping for Slides

Wrap each slide in a block `{ }` to avoid variable name collisions:

```javascript
// SLIDE 1
{
  const slide = pres.addSlide()
  // ... slide 1 content
}

// SLIDE 2
{
  const slide = pres.addSlide()
  // ... slide 2 content (no conflict with slide 1's 'slide' variable)
}
```

## Pattern 5: Section Headers

Consistent header pattern across content slides:

```javascript
// Full-width header bar
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0,
  y: 0,
  w: 10,
  h: 1.0,
  fill: { color: C.dark },
})
slide.addText('NN  Section Title', {
  x: 0.6,
  y: 0.15,
  w: 8,
  h: 0.7,
  fontSize: 28,
  fontFace: FONT.head,
  color: C.white,
  bold: true,
  align: 'left',
  margin: 0,
})
```

## Pattern 6: Card Layout

Standard card with top accent bar and shadow:

```javascript
// Card background
slide.addShape(pres.shapes.RECTANGLE, {
  x,
  y,
  w,
  h,
  fill: { color: C.white },
  shadow: makeCardShadow(),
})
// Top color accent
slide.addShape(pres.shapes.RECTANGLE, {
  x,
  y,
  w,
  h: 0.06,
  fill: { color: C.accent },
})
```

## Pitfall: Bullets

Use `bullet: true` property, NOT unicode bullet characters:

```javascript
// BAD
slide.addText("• Item 1\n• Item 2", { ... });

// GOOD
slide.addText("Item 1\nItem 2", { ..., bullet: true });
```

## Pitfall: Chinese Filename + soffice

`soffice` (LibreOffice) silently fails with Chinese filenames:

```bash
# BAD — fails silently
soffice --headless --convert-to pdf "新华人App.pptx"

# GOOD — copy to ASCII name first
cp "新华人App.pptx" temp_export.pptx
soffice --headless --convert-to pdf temp_export.pptx
```

## Pitfall: margin: 0

Always set `margin: 0` on text elements. The default margin adds
unexpected padding that throws off precise positioning.

## File Output

```javascript
pres
  .writeFile({ fileName: '/path/to/output.pptx' })
  .then(() => console.log('PPTX created successfully!'))
  .catch((err) => console.error('Error:', err))
```
