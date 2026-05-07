---
name: comp-analysis
description: Pull rent comps, sale comps, and CRE pricing analysis. Use this skill whenever Akiva asks to pull comps, analyze pricing, prep an offer, evaluate an asking rate, or build a market report on a property or submarket.
---

# Comp Analysis

CRE-specific comp analysis. Pulls rent comps (lease) or sale comps (investment), normalizes to $/SF and cap rate, and outputs a clean one-page report.

---

## Process

1. Read `context/market.md` for submarket benchmarks Akiva has logged.
2. Ask: are we doing a rent comp (leasing) or sale comp (investment)?
3. Pull live data via `python3 tools/research.py "..."` if comps weren't provided.
4. Normalize and output the report below.

---

## Required Inputs

**Subject Property:**
- Address
- Type (retail / office / mixed-use / industrial / multifamily)
- SF (rentable + usable if applicable)
- Year built / last renovation
- Condition

**For Rent Comp:**
- Asking rate (or current rent)
- Lease type (NNN / modified gross / FSG)
- Term Akiva is targeting
- TI Akiva is willing to give

**For Sale Comp:**
- Asking price (or target acquisition price)
- NOI (or pro-forma NOI)
- Tenant mix + lease maturities

**Comparables (3-5 minimum):**
- Address
- $/SF (lease) or sale price + cap rate
- Lease type or sale date
- Key differences vs. subject

---

## Rent Comp Report Format

```
RENT COMP ANALYSIS
---
Subject: [address, suite]
Submarket: [Toco Hills / Sandy Springs / etc.]
Date: [date]

SUBJECT PROPERTY
[type] | [SF] sqft | [year built/renovated] | [condition]
Asking: $[X]/SF [NNN/MG/FSG] | Term: [X yrs] | TI: $[X]/SF

LEASE COMPS
---
[Address] | $[X]/SF [type] | [SF] | [date] | [tenant if known]
  Differences: [why this comp is relevant -- adjustments]

[repeat for each comp]

NORMALIZED RANGE
Low: $[X]/SF [type]
Mid: $[X]/SF [type]
High: $[X]/SF [type]

MARKET SNAPSHOT
[2-3 sentences from context/market.md + research -- vacancy, rent direction, deal velocity]

RECOMMENDATION
Asking rate: $[X]/SF [type]
Rationale: [why this rate, given the comps + subject + market]
Negotiation floor: $[X]/SF
Walk-away: $[X]/SF
```

---

## Sale Comp Report Format

```
SALE COMP ANALYSIS
---
Subject: [address]
Type: [retail / office / etc.] | [SF] sqft
Date: [date]

SUBJECT PROPERTY
NOI: $[X] | $/SF: $[X] | Cap Rate (target): [X]%
Tenant mix: [summary]

SALE COMPS
---
[Address] | $[total price] | $[X]/SF | Cap [X]% | Sold [date]
  NOI: $[X] | Tenant: [primary tenant if relevant]
  Differences: [why this comp is relevant]

[repeat for each comp]

NORMALIZED RANGE
Cap rate range: [X]% -- [Y]%
$/SF range: $[X] -- $[Y]
NOI multiple range: [X]x -- [Y]x

MARKET SNAPSHOT
[2-3 sentences -- transaction velocity, cap rate trend, debt market]

RECOMMENDATION
Target price: $[X] (cap rate [Y]%)
Walk-away price: $[X]
Risks: [vacancy exposure, lease maturities, capex needed]
```

---

## Notes (CRE-specific)

- Always normalize to $/SF and cap rate -- those are the comp languages
- Flag when the comp is a different lease type (NNN vs. FSG) -- you can't compare directly without grossing up
- Tenant credit matters -- a national tenant comp at $30/SF is not the same as a local at $30/SF
- If the comp is from before the most recent rate-cycle shift, flag it
- Cap rate compression / expansion in the last 12 months is the headline market signal -- always include it
