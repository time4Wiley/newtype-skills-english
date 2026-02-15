---
name: super-fact-checker
description: Systematic fact-checking skill with claim extraction, priority matrix, source credibility hierarchy, and verification methodology. Use when user needs to verify claims, check data accuracy, validate sources, review content for factual correctness, or annotate articles with verification status.
---

# Super Fact-Checker

> Identify claims → Assess priority → Verify → Annotate results

---

## Workflow

```
Content → Extract claims → Classify (verifiable/non-verifiable)
                        → Prioritize
                        → Verify (find sources)
                        → Annotate (results)
```

**Core Principles**:
- Only check verifiable claims
- High impact + high suspicion checked first
- Trace back to primary sources
- Annotations must be clear, not ambiguous

---

## Step 1: Extract and Classify Claims

### Verifiable Claims
- ✅ Factual statements: "Tesla delivered 1.8 million vehicles in 2024"
- ✅ Data citations: "According to Gartner report..."
- ✅ Historical events: "Apple released the iPhone in 2007"
- ✅ Quoted statements: "Musk said..."

### Non-Verifiable Claims
- ❌ Opinions/judgments: "This is the best solution"
- ❌ Predictions: "The market will grow 50% next year"
- ❌ Subjective feelings: "User experience is good"
- ❌ Vague statements: "Many people think..."

**Processing**: Extract all claims, mark which are verifiable and which are not.

---

## Step 2: Determine Verification Priority

### Priority Matrix

|  | High Suspicion | Low Suspicion |
|--|----------------|---------------|
| **High Impact** | 🔴 Must verify | 🟡 Should verify |
| **Low Impact** | 🟡 Should verify | 🟢 Optional verify |

### Suspicion Signals
- 🚩 Numbers too precise or too round ("exactly 1 million")
- 🚩 Vague sources ("studies show", "experts believe")
- 🚩 Conflicts with common sense or known facts
- 🚩 Overly absolute language ("only", "first", "never")
- 🚩 Repeatedly retold information

### Impact Assessment
- High impact: Core arguments, key data, decision basis
- Low impact: Background information, examples, minor details

---

## Step 3: Verification

### Source Credibility Hierarchy

| Level | Source Type | Reliability | Examples |
|-------|-------------|-------------|----------|
| 1 | Official primary sources | ⭐⭐⭐ | Financial reports, official announcements, court documents |
| 2 | Authoritative academic sources | ⭐⭐⭐ | Peer-reviewed papers, official statistics |
| 3 | Authoritative media | ⭐⭐ | NYT, WSJ, FT, Caixin, etc. |
| 4 | Industry reports | ⭐⭐ | McKinsey, Gartner (note methodology) |
| 5 | General media | ⭐ | General news websites |
| 6 | Self-media/social | ⚠️ | For leads only, cannot serve as verification source |

### Verification Methods

**Data Claims**:
1. Find original data source (financial reports, official statistics)
2. Verify specific numbers and units
3. Confirm time range

**Citation Claims**:
1. Find original source (original text, original video)
2. Check for context manipulation
3. Confirm speaker identity and context

**Event Claims**:
1. Find multiple independent reports
2. Cross-verify key details
3. Note timeline and causal relationships

### Triangulation
Key claims require cross-verification from 2-3 independent sources:
- Independent = not citing each other, different organizations, different times
- If only single source, annotate "single source, pending verification"

---

## Step 4: Annotate Results

### Annotation System

| Annotation | Meaning | Usage Scenario |
|------------|---------|----------------|
| ✅ Verified | Found reliable source, information accurate | Consistent with primary/authoritative sources |
| ⚠️ Partially verified | Core correct, details differ | Numbers slightly off, expression imprecise |
| ❓ Cannot verify | Cannot find reliable source | Source unclear, information too old |
| ❌ Incorrect | Conflicts with reliable sources | Data error, factual error |
| 🔍 Requires further investigation | Important but currently unconfirmable | Needs expert knowledge or more time |

### Output Format

```markdown
## Verification Report

### Summary
- Total claims: X
- Verifiable: X
- Verified: X
- Problematic claims: X

### Verification Results

| # | Claim | Result | Notes |
|---|-------|--------|-------|
| 1 | "Tesla delivered 1.8M vehicles in 2024" | ✅ | Consistent with financial report (Source: Tesla Q4 2024 Report) |
| 2 | "Market share exceeds 50%" | ⚠️ | Actually 47% (Source: XX Report) |
| 3 | "Experts believe..." | ❓ | Specific source not found |

### Recommended Changes
1. [Claim 2]: Suggest changing to "Market share approximately 47%"
2. [Claim 3]: Suggest deleting or adding specific source

### Source List
- [Source 1]: URL/citation
- [Source 2]: URL/citation
```

---

## Key Principles

### Don't Do
- ❌ Treat "cannot verify" as "incorrect"
- ❌ Only find sources that support conclusion (confirmation bias)
- ❌ Use secondary source to verify secondary source
- ❌ Ignore conflicts of interest in sources

### Do
- ✅ Trace back to primary sources
- ✅ Annotate source credibility
- ✅ Explain verification process
- ✅ Distinguish "factual error" from "imprecise expression"
