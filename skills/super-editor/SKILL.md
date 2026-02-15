---
name: super-editor
description: 4-layer editing methodology (structure, paragraph, sentence, word) for polishing drafts and improving readability. Use when user needs to edit, revise, or polish written content. Provides systematic editing from macro structure down to word-level precision, with annotated change reports and justifications.
license: MIT
metadata:
  author: huangyihe
  version: "1.0"
  language: en
---

# Super Editor

> Assess level → Edit from large to small → Annotate changes → Explain rationale

---

## Workflow

```
Draft → Assess level → [Structure issues] Structural editing
                     → [Paragraph issues] Paragraph editing
                     → [Sentence issues] Sentence editing
                     → [Word issues] Word editing
```

**Core Principles**:
- Big to small: Structure → Paragraph → Sentence → Word
- Don't edit while writing; work layer by layer
- Every change must have a reason
- Respect author's style, don't over-rewrite

---

## Four Editing Levels

### Level 1: Structural Editing

**Focus**: Overall architecture, chapter arrangement, logical order

**Checklist**:
- [ ] Does the opening hook the reader?
- [ ] Is the main narrative clear?
- [ ] Does the chapter sequence follow logic?
- [ ] Are there redundant chapters?
- [ ] Is the ending strong?

**Common Issues**:
| Issue | Manifestation | Fix Recommendation |
|-------|---------------|-------------------|
| Slow opening | Excessive background setup | Jump straight in, background later |
| Logic gap | Jumps from A to C, missing B | Add transition paragraphs |
| Redundancy | Multiple instances saying the same thing | Merge or delete |
| Weak ending | Conclusion is rushed | Strengthen summary or call-to-action |

### Level 2: Paragraph Editing

**Focus**: Paragraph cohesion, inter-paragraph transitions, information density

**Checklist**:
- [ ] Does each paragraph have only one core point?
- [ ] Are there logical connections between paragraphs?
- [ ] Is paragraph length appropriate (3-7 sentences)?
- [ ] Is information density balanced?

**Common Issues**:
| Issue | Manifestation | Fix Recommendation |
|-------|---------------|-------------------|
| Overly long paragraphs | One paragraph exceeds 10 sentences | Split by sub-points |
| Scattered paragraphs | One paragraph, multiple themes | Extract into separate paragraphs |
| Lack of transitions | Paragraphs jump without connection | Add transition sentences |
| Information imbalance | Key points rushed, details lengthy | Redistribute space |

### Level 3: Sentence Editing

**Focus**: Clarity, flow, rhythm

**Checklist**:
- [ ] Is the meaning of each sentence clear?
- [ ] Does sentence length vary?
- [ ] Are there ambiguities or multiple negatives?
- [ ] Is the subject consistent?

**Common Issues**:
| Issue | Manifestation | Fix Recommendation |
|-------|---------------|-------------------|
| Overly long sentences | One sentence exceeds 40 words | Split into 2-3 sentences |
| Ambiguity | "He told his friend he was wrong" | Clarify reference |
| Multiple negatives | "Not without possibility not..." | Convert to affirmative |
| Excessive passive | "Was...by...the..." | Change to active voice |

### Level 4: Word Editing

**Focus**: Precise word choice, consistency, tone

**Checklist**:
- [ ] Are words precise?
- [ ] Are terms consistent?
- [ ] Are there redundant words?
- [ ] Is tone unified?

**Common Issues**:
| Issue | Manifestation | Fix Recommendation |
|-------|---------------|-------------------|
| Vague words | "some", "many", "approximately" | Be specific or delete |
| Inconsistent terminology | Same concept, multiple names | Unify terminology |
| Redundant words | "very very", "currently now" | Remove duplicates |
| Inconsistent tone | Sometimes formal, sometimes colloquial | Unify style |

---

## Change Annotation Format

```markdown
## Editing Report

### Editing Summary
- Editing level: [Structure/Paragraph/Sentence/Word]
- Number of changes: X locations
- Main issues: [Brief description]

### Change List

#### Structural Level
1. **[Chapter name]**
   - Original: [Keep/Delete/Move]
   - Change: [Specific action]
   - Rationale: [Why this change]

#### Paragraph Level
1. **[Location]**
   - Issue: [Paragraph too long/lacks transition/...]
   - Change: [Specific action]
   - Rationale: [Why]

#### Sentence Level
1. **Original**: "[Original text]"
   **Changed to**: "[Revised text]"
   **Rationale**: [Clarity/flow/...]

#### Word Level
1. "[Original word]" → "[New word]": [Rationale]
```

---

## Editing Style Guide

### Conciseness Principle
- Remove words that don't affect meaning
- Use one word when one word is enough
- Use simple words when possible

### Clarity Principle
- Avoid ambiguity
- Clarify references
- Use fewer abbreviations (explain on first use)

### Consistency Principle
- Unified terminology
- Unified person
- Unified tense
- Unified format

---

## Key Principles

### Don't Do
- ❌ Change the author's core style
- ❌ Edit multiple levels simultaneously
- ❌ Make changes without reason
- ❌ Impose your own preferences

### Do
- ✅ Respect author's intent
- ✅ Edit layer by layer, large to small
- ✅ Provide rationale for every change
- ✅ Preserve original text for comparison
