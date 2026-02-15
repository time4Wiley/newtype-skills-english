/**
 * PptxGenJS Template — XinHuaRen App Project Panorama
 *
 * Crimson + Gold design system, 10 slides.
 * Adapt content from the master MD before running.
 *
 * Usage:
 *   npm install pptxgenjs   # if not installed
 *   node create_pptx.js
 *
 * IMPORTANT PATTERNS:
 * - Use makeShadow()/makeCardShadow() factory functions (never share objects)
 * - Use \uXXXX escapes for Chinese in template literals
 * - Set margin: 0 on all text elements
 * - Block-scope each slide with { }
 */

const pptxgen = require('pptxgenjs')

const pres = new pptxgen()
pres.layout = 'LAYOUT_16x9'
pres.author = '\u65B0\u534E\u4EBA App \u9879\u76EE\u7EC4'
pres.title = '\u65B0\u534E\u4EBA App \u9879\u76EE\u5168\u666F\u68B3\u7406'

// =============  DESIGN SYSTEM  =============
const C = {
  dark: '8B1A1A',
  darkAlt: '6B1414',
  mid: 'B94040',
  accent: 'D4A574',
  cream: 'FFF8F0',
  white: 'FFFFFF',
  offWhite: 'F5EDE3',
  text: '2D2020',
  textLight: '6B5A5A',
  textWhite: 'FFF8F0',
  cardBg: 'FFFFFF',
  sectionBg: 'FDF6EF',
}

const FONT = { head: 'Georgia', body: 'Calibri' }

// Factory functions — NEVER reuse option objects directly
const makeShadow = () => ({
  type: 'outer',
  color: '000000',
  blur: 4,
  offset: 2,
  angle: 135,
  opacity: 0.1,
})
const makeCardShadow = () => ({
  type: 'outer',
  color: '000000',
  blur: 6,
  offset: 3,
  angle: 135,
  opacity: 0.12,
})

// =============  HELPER: Section Header  =============
function addSectionHeader(slide, num, title) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0,
    y: 0,
    w: 10,
    h: 1.0,
    fill: { color: C.dark },
  })
  slide.addText(`${num}  ${title}`, {
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
}

// =============  HELPER: Card  =============
function addCard(slide, x, y, w, h, accentColor) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x,
    y,
    w,
    h,
    fill: { color: C.white },
    shadow: makeCardShadow(),
  })
  if (accentColor) {
    slide.addShape(pres.shapes.RECTANGLE, {
      x,
      y,
      w,
      h: 0.06,
      fill: { color: accentColor },
    })
  }
}

// =============================================
// SLIDE 1 — TITLE
// =============================================
{
  const slide = pres.addSlide()
  slide.background = { color: C.dark }

  // Decorative accents
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 7.5,
    y: 0,
    w: 2.5,
    h: 0.15,
    fill: { color: C.accent },
  })
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0,
    y: 5.475,
    w: 3,
    h: 0.15,
    fill: { color: C.accent },
  })

  // TODO: Update title text from master MD
  slide.addText('\u65B0\u534E\u4EBA App', {
    x: 0.8,
    y: 1.2,
    w: 8.4,
    h: 1.2,
    fontSize: 48,
    fontFace: FONT.head,
    color: C.white,
    bold: true,
    align: 'left',
    margin: 0,
  })
  slide.addText('\u9879\u76EE\u5168\u666F\u68B3\u7406', {
    x: 0.8,
    y: 2.3,
    w: 8.4,
    h: 0.8,
    fontSize: 32,
    fontFace: FONT.head,
    color: C.accent,
    align: 'left',
    margin: 0,
  })
  slide.addText(
    '\u6D77\u5916\u534E\u5B66\u5B66\u957F\u7EBF\u4E0A\u5B66\u4E60\u4E0E\u6587\u5316\u4F20\u64AD\u5E73\u53F0',
    {
      x: 0.8,
      y: 3.5,
      w: 8.4,
      h: 0.5,
      fontSize: 16,
      fontFace: FONT.body,
      color: C.textWhite,
      align: 'left',
      margin: 0,
    }
  )

  // TODO: Update date and source line
  slide.addText('2026\u5E74X\u6708 \u00B7 \u7EFC\u5408\u6574\u7406\u81EA...', {
    x: 0.8,
    y: 4.6,
    w: 8.4,
    h: 0.4,
    fontSize: 11,
    fontFace: FONT.body,
    color: C.textLight,
    align: 'left',
    margin: 0,
  })
}

// =============================================
// SLIDE 2 — TABLE OF CONTENTS
// =============================================
{
  const slide = pres.addSlide()
  slide.background = { color: C.cream }

  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0,
    y: 0,
    w: 0.08,
    h: 5.625,
    fill: { color: C.dark },
  })
  slide.addText('\u76EE\u5F55', {
    x: 0.6,
    y: 0.3,
    w: 3,
    h: 0.7,
    fontSize: 32,
    fontFace: FONT.head,
    color: C.dark,
    bold: true,
    align: 'left',
    margin: 0,
  })

  // TODO: Update section titles from master MD
  const items = [
    { num: '01', title: '\u9879\u76EE\u5B9A\u4F4D\u4E0E\u80CC\u666F' },
    { num: '02', title: 'App \u4FE1\u606F\u67B6\u6784' },
    { num: '03', title: '\u4E49\u5DE5\u75DB\u70B9\u4E0E\u9700\u6C42' },
    { num: '04', title: '\u4E09\u9636\u6BB5\u8DEF\u7EBF\u56FE' },
    { num: '05', title: 'AI\u6280\u672F\u65B9\u5411' },
    { num: '06', title: '\u5173\u952E\u51B3\u7B56\u4E0E\u5F85\u529E' },
  ]

  items.forEach((item, i) => {
    const yBase = 1.3 + i * 0.65
    slide.addShape(pres.shapes.OVAL, {
      x: 0.6,
      y: yBase,
      w: 0.45,
      h: 0.45,
      fill: { color: i === 0 ? C.dark : C.offWhite },
    })
    slide.addText(item.num, {
      x: 0.6,
      y: yBase,
      w: 0.45,
      h: 0.45,
      fontSize: 13,
      fontFace: FONT.body,
      color: i === 0 ? C.white : C.dark,
      bold: true,
      align: 'center',
      valign: 'middle',
      margin: 0,
    })
    slide.addText(item.title, {
      x: 1.2,
      y: yBase,
      w: 4,
      h: 0.45,
      fontSize: 18,
      fontFace: FONT.body,
      color: C.text,
      align: 'left',
      valign: 'middle',
      margin: 0,
    })
  })

  // Right side stats
  addCard(slide, 5.8, 1.0, 3.8, 3.8, null)
  slide.addText('\u9879\u76EE\u901F\u89C8', {
    x: 6.1,
    y: 1.2,
    w: 3.2,
    h: 0.45,
    fontSize: 16,
    fontFace: FONT.head,
    color: C.dark,
    bold: true,
    align: 'left',
    margin: 0,
  })

  // TODO: Update stats from master MD
  const stats = [
    { val: '5', label: '\u6838\u5FC3Tab\u6A21\u5757' },
    { val: '7', label: '\u4E49\u5DE5\u89D2\u8272\u75DB\u70B9\u7C7B\u522B' },
    { val: '3', label: '\u9636\u6BB5\u8DEF\u7EBF\u56FE' },
    { val: '1200+', label: '\u4E09\u8FDE\u62A5\u5B66\u5458' },
    { val: '$55', label: 'Zoom\u6708\u8D39/3\u8D26\u53F7' },
  ]

  stats.forEach((s, i) => {
    const yy = 1.85 + i * 0.55
    slide.addText(s.val, {
      x: 6.1,
      y: yy,
      w: 1.2,
      h: 0.45,
      fontSize: 22,
      fontFace: FONT.head,
      color: C.dark,
      bold: true,
      align: 'left',
      valign: 'middle',
      margin: 0,
    })
    slide.addText(s.label, {
      x: 7.3,
      y: yy,
      w: 2.2,
      h: 0.45,
      fontSize: 13,
      fontFace: FONT.body,
      color: C.textLight,
      align: 'left',
      valign: 'middle',
      margin: 0,
    })
  })
}

// =============================================
// SLIDES 3-10: Follow the same patterns
// =============================================
// TODO: Implement slides 3-10 following the patterns above.
// See the slide structure table in SKILL.md for content mapping.
//
// Key patterns for each slide type:
//
// CONTENT SLIDE:
//   addSectionHeader(slide, "0N", "Title");
//   addCard(slide, x, y, w, h, C.accent);
//   slide.addText(content, { ... });
//
// TWO-CARD SPLIT:
//   addCard(slide, 0.5, 1.3, 4.3, 3.8, C.accent);  // left
//   addCard(slide, 5.2, 1.3, 4.3, 3.8, C.dark);     // right
//
// GRID LAYOUT (e.g., pain points):
//   items.forEach((item, i) => {
//     const col = i % 3;
//     const row = Math.floor(i / 3);
//     const x = 0.4 + col * 3.1;
//     const y = 1.25 + row * 2.15;
//     addCard(slide, x, y, 2.9, 1.95, C.dark);
//   });
//
// CLOSING SLIDE:
//   slide.background = { color: C.dark };
//   // Gold accent bars top and bottom
//   // Quote text centered

// =============================================
// WRITE FILE
// =============================================
// TODO: Update output path
const OUTPUT =
  '/sessions/exciting-jolly-goldberg/mnt/requirements/\u65B0\u534E\u4EBAApp_\u9879\u76EE\u5168\u666F\u68B3\u7406.pptx'

pres
  .writeFile({ fileName: OUTPUT })
  .then(() => console.log('PPTX created successfully!'))
  .catch((err) => console.error('Error:', err))
