---
name: market-research
description: Research any commercial real estate market, submarket, building, lead, or competitor using live web data. Use when Akiva asks to research anything that needs current information.
---

# Market Research

Uses live Perplexity search to pull current data on any CRE topic.

---

## How to Use

Run the research tool:
```bash
python3 tools/research.py "your query here"
```

Then synthesize results into a clear, actionable brief for Akiva.

---

## Common Use Cases

**Submarket conditions:**
```bash
python3 tools/research.py "Toco Hills Atlanta retail commercial real estate market 2026 -- average rents per SF NNN, vacancy rates, recent leases"
```

**Rent comps:**
```bash
python3 tools/research.py "comparable retail leases Toco Hills Atlanta 2025-2026 -- $/SF NNN, suite size, tenant mix"
```

**Sale comps / cap rates:**
```bash
python3 tools/research.py "retail commercial real estate sales Atlanta 2025-2026 -- cap rates, $/SF, NOI"
```

**Prospect / broker research:**
```bash
python3 tools/research.py "[person or firm name] Atlanta commercial real estate -- background, recent deals, reviews"
```

**Acquisition target intel:**
```bash
python3 tools/research.py "[address or property] ownership history, last sale, tax record, tenant list if public"
```

**News / market shifts:**
```bash
python3 tools/research.py "Atlanta commercial real estate market trends April 2026 -- retail, office, mixed-use"
```

---

## Output Format

Present results as:
- 3-5 bullet takeaways (the most actionable facts)
- What this means for Akiva specifically (his portfolio, his market, his pipeline)
- Numbers always cited with source + date
- Any follow-up questions to investigate

---

## CRE-specific notes

- Default to Atlanta + Toco Hills + Sandy Springs unless told otherwise
- CRE economics use $/SF NNN, $/SF FSG (full service gross), $/SF modified gross -- never default to "monthly rent" the way residential research does
- Cap rate and NOI are the headline numbers for sale comps
- Vacancy rate + average rent + rent growth are the headlines for lease comps
