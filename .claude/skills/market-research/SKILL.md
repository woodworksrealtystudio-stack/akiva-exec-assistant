---
name: market-research
description: Research any commercial real estate market, submarket, building, lead, or competitor using live web data. Use when Akiva asks to research anything that needs current information.
---

# Market Research

Pulls current data on any CRE topic using Claude Code's built-in WebSearch and WebFetch tools.

---

## How to Use

Use the WebSearch tool for any query needing fresh data:
- Submarket conditions, rents, vacancy rates
- Sale comps, cap rates, NOI
- Prospect / broker / firm research
- News, market shifts, regulatory changes

For specific URLs (a LoopNet listing, a county tax record, a broker bio), use WebFetch.

Synthesize results into a clear, actionable brief for Akiva.

---

## Common Queries

**Submarket conditions:**
> "Toco Hills Atlanta retail commercial real estate market 2026 -- average rents per SF NNN, vacancy rates, recent leases"

**Rent comps:**
> "comparable retail leases Toco Hills Atlanta 2025-2026 -- $/SF NNN, suite size, tenant mix"

**Sale comps / cap rates:**
> "retail commercial real estate sales Atlanta 2025-2026 -- cap rates, $/SF, NOI"

**Prospect / broker research:**
> "[person or firm name] Atlanta commercial real estate -- background, recent deals, reviews"

**Acquisition target intel:**
> "[address or property] ownership history, last sale, tax record, tenant list if public"

**News / market shifts:**
> "Atlanta commercial real estate market trends [month] 2026 -- retail, office, mixed-use"

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
