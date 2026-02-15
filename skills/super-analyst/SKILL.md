---
name: super-analyst
description: Systematic analysis skill with 12 frameworks (SWOT, Porter's Five Forces, First Principles, 5 Whys, Design Thinking, etc.) and research methodology. Use when user needs strategic analysis, competitive research, investment decisions, root cause diagnosis, or any complex analytical task. Automatically detects complexity level and selects appropriate frameworks.
license: MIT
metadata:
  author: huangyihe
  version: "1.0"
  language: en
---

# Super Analyst

> Assess complexity → Systematic research → Select framework → Output conclusion

---

## Workflow

```
Question → Complexity assessment → [Simple] Direct answer
                                 → [Medium] 1 framework + basic research
                                 → [Complex] Combined frameworks + deep research
```

**Core Principles**:
- Simple questions get direct answers, no framework needed
- Frameworks are tools, not rituals
- Research emphasizes methodology, not quantity

---

## Complexity Assessment

### Simple (Direct Answer)
- Concept explanation: "What is SWOT?"
- Single-dimension question
- User has provided complete information
- **Approach**: Direct answer, no framework

### Medium (1 Framework)
- Requires some external information
- 2-3 analysis dimensions
- Clear scope
- Example: "Analyze Tesla's competitive advantages"
- **Approach**: Basic research + 1 framework

### Complex (Combined Frameworks)
- Requires deep research
- Multi-dimensional strategic decision
- Example: "Should we enter the India market?"
- **Approach**: Deep research + 2-3 combined frameworks

---

## Research Methodology

### Information Hierarchy (Priority from High to Low)

| Level | Type | Reliability | Examples |
|-------|------|-------------|----------|
| Primary Sources | Raw data, official statements, firsthand accounts | ⭐⭐⭐ | Financial reports, official announcements, court documents, patents |
| Secondary Sources | Analysis and interpretation of primary sources | ⭐⭐ | Academic papers, authoritative media deep dives, industry reports |
| Tertiary Sources | Citations and retellings of secondary sources | ⭐ | Self-media articles, news aggregators, encyclopedia entries |

**Principle**: Trace back to primary sources whenever possible; be cautious with tertiary sources.

### Source Credibility Assessment

| Source Type | Reliability | Usage Recommendation |
|-------------|-------------|----------------------|
| Official statements/financial reports | High | Can cite directly, note conflicts of interest |
| Academic papers (peer-reviewed) | High | Can cite directly, note timeliness |
| Authoritative media (NYT, WSJ, FT, Caixin, etc.) | Medium-High | Can cite, cross-verification preferred |
| Industry reports (McKinsey, Gartner, etc.) | Medium-High | Note methodology and sample size |
| General news media | Medium | Requires cross-verification |
| Self-media/blogs | Low | Reference only, must verify |
| Social media | Low | For leads only, cannot cite directly |

### Information Triangulation

**Core Principle**: Key facts require cross-verification from 2-3 independent sources.

```
    Source A
       /\
      /  \
     /    \
Source B ---- Source C
```

**Definition of "Independent"**:
- ❌ Sources citing each other are not independent
- ❌ Different channels of the same media conglomerate are not independent
- ✅ Reports from different organizations, different times, different angles count as independent

### Search Strategy

**When Research is Needed**:
- Involves specific companies/products/markets
- Requires current data (prices, rankings, trends)
- Needs case studies, best practices
- User explicitly requests research

**When Research is Not Needed**:
- Pure conceptual/theoretical questions
- User has provided sufficient context
- General knowledge suffices

**Search Execution**:
- **Keyword Matrix**: Core terms + qualifiers (time, location, type)
- **Cross-Language Coordination**: For international topics, search in both Chinese and English, compare information gaps
- **Time Constraints**: For data-related information, limit to recent 1-2 years
- **Dynamic Adjustment**: Decide whether to continue searching based on information quality

**Tool Selection**:
- Web search tool: Quick overview, multi-source comparison
- Web scraping tool: Deep reports, long-form content retrieval

### Research Output Structure

```markdown
## Research Summary
[2-3 sentences summarizing findings]

## Key Findings
- [Finding 1] (Source: XX, Reliability: High/Medium/Low)
- [Finding 2] (Source: XX, Reliability: High/Medium/Low)

## Source List
| Source | Type | Reliability | Key Information |
|--------|------|-------------|-----------------|
| [Source Name] | Primary/Secondary/Tertiary | High/Medium/Low | [Summary] |

## Information Gaps
- [Information not found]
- [Information requiring further verification]
```

---

## Framework Selection Reference

| Question Type | Primary Framework | Alternatives |
|---------------|-------------------|--------------|
| Strategic assessment, market positioning | SWOT | Porter's Five Forces |
| Industry analysis, competitive strategy | Porter's Five Forces | SWOT |
| Investment decisions, project evaluation | Cost-Benefit | Pareto |
| Root cause diagnosis, troubleshooting | 5 Whys | First Principles |
| Innovation breakthrough, redesign | First Principles | Design Thinking |
| User problems, product innovation | Design Thinking | Systems Thinking |
| Complex systems, long-term strategy | Systems Thinking | Scenario Planning |
| Future planning, uncertainty | Scenario Planning | Hypothesis-Driven |
| Problem breakdown, structured thinking | MECE | Pareto |
| Priority ranking, efficiency improvement | Pareto | MECE |
| Hypothesis validation, research testing | Hypothesis-Driven | Socratic Method |
| Deep understanding, challenging assumptions | Socratic Method | First Principles |

### Common Combinations (Use 2-3 for Complex Problems)

- **Strategy + Competition**: SWOT + Porter's Five Forces
- **Diagnosis + Innovation**: 5 Whys + First Principles
- **Decision + Priority**: MECE + Pareto + Cost-Benefit
- **System + Future**: Systems Thinking + Scenario Planning

---

## 12 Frameworks Quick Reference

### 1. First Principles
**Use for**: Innovation breakthrough, fundamental redesign
**Steps**:
1. Identify core problem and existing assumptions
2. Break down to most basic facts/principles
3. Verify each basic fact
4. Rebuild solution from fundamentals
5. Summarize insights and recommendations

### 2. 5 Whys
**Use for**: Root cause diagnosis, troubleshooting
**Steps**:
1. Clearly describe the problem
2. Ask "why" 5 times consecutively, each time targeting the previous answer
3. Identify the root cause
4. Propose solutions targeting the root cause

### 3. SWOT
**Use for**: Strategic assessment, business planning
**Steps**:
1. Describe the analysis subject and context
2. List internal Strengths (5-7 items)
3. List internal Weaknesses (5-7 items)
4. List external Opportunities (5-7 items)
5. List external Threats (5-7 items)
6. Generate SO/ST/WO/WT strategies

### 4. Porter's Five Forces
**Use for**: Industry analysis, competitive strategy
**Steps**:
1. Define industry and context
2. Assess supplier bargaining power
3. Assess buyer bargaining power
4. Assess threat of substitutes
5. Assess threat of new entrants
6. Assess intensity of existing competition
7. Comprehensively judge industry attractiveness

### 5. Cost-Benefit Analysis
**Use for**: Investment decisions, project evaluation
**Steps**:
1. Describe the decision and context
2. Identify and categorize all costs
3. Identify and categorize all benefits
4. Quantitative analysis (NPV, IRR, BCR)
5. Compare options, discuss qualitative factors
6. Summarize recommendations

### 6. Design Thinking
**Use for**: User problems, product innovation
**Steps**:
1. Empathize: Understand user pain points and needs
2. Define: Define core problem ("How Might We...")
3. Ideate: Brainstorm 10-15 ideas
4. Prototype: Select 3-5 for low-fidelity prototypes
5. Test: Plan testing methods and iteration

### 7. Systems Thinking
**Use for**: Complex systems, long-term strategy
**Steps**:
1. Define system boundaries and core elements
2. Map relationships and feedback loops
3. Analyze dynamic behavior and patterns
4. Identify leverage points and intervention strategies
5. Simulate scenarios to assess impact

### 8. Socratic Method
**Use for**: Deep understanding, challenging assumptions
**Steps**:
1. Clarify the question and key concepts
2. Identify and question implicit assumptions
3. Explore consequences and analogies
4. Seek consensus or refutation
5. Summarize new understanding

### 9. Pareto Analysis
**Use for**: Priority ranking, efficiency improvement
**Steps**:
1. Collect and categorize data
2. Sort by impact, calculate cumulative percentage
3. Identify "vital few" (20% causing 80% impact)
4. Analyze insights and root causes
5. Propose priority actions

### 10. MECE (Mutually Exclusive, Collectively Exhaustive)
**Use for**: Problem breakdown, structured thinking
**Steps**:
1. Define problem scope
2. Break down into mutually exclusive, collectively exhaustive subcategories
3. Analyze each category individually
4. Integrate and prioritize
5. Summarize recommendations

### 11. Hypothesis-Driven Analysis
**Use for**: Hypothesis validation, research testing
**Steps**:
1. Propose 3-5 initial hypotheses
2. Design validation methods and metrics
3. Collect evidence to verify hypotheses
4. Iteratively adjust hypotheses
5. Summarize insights and recommendations

### 12. Scenario Planning
**Use for**: Future planning, dealing with uncertainty
**Steps**:
1. Identify key driving factors and uncertainties
2. Construct 4-6 scenarios (2x2 matrix)
3. Analyze impact of each scenario
4. Develop robust cross-scenario strategies
5. Establish monitoring metrics

---

## Output Format

### Simple Questions
Direct answer, no format needed.

### Medium/Complex Questions

```markdown
# Analysis Report: [Topic]

## TL;DR
[1-2 paragraphs: Direct conclusion]

## Analysis Process
### [Framework Name]
[Expand analysis according to framework steps]

**Key Findings**:
- [Insight 1]
- [Insight 2]

## Action Recommendations
- [ ] Short-term: ...
- [ ] Medium-term: ...

## Information Sources
- [Search sources]
- [Frameworks used]
```
