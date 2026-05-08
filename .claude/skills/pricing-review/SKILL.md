---
name: pricing-review
description: Review what Akiva is currently charging on a specific unit vs market comps. Use when Akiva asks "what should I charge for [suite]," "is [suite] underpriced," "should I raise rent on [tenant]," "renewal pricing for [tenant]," or anything questioning current rents on his own portfolio. Different from comp-analysis -- this looks INWARD at his portfolio, not outward at new comps.
---

# Pricing Review

Internal pricing intelligence on Akiva's existing portfolio. Answers "am I underpriced on this unit" or "what should I charge for renewal" by comparing his current rents to current market.

Akiva said it best on 5/7: *"I want to be able to evaluate what's the price per square foot that I'm charging for the unit. You know, to be able to see where I can negotiate."*

---

## Process

1. Read the target unit from `wiki/synthesis/leases/<file>.md` -- pull current $/SF, term remaining, lease type, escalations.
2. Read `context/portfolio.md` for the property + tenant context.
3. Run `comp-analysis` on the submarket to get current market $/SF.
4. Calculate the gap: where his rent sits vs. low / mid / high of current market.
5. Account for tenant-quality factors (long-term relationship, credit risk, build-out invested).
6. Output a recommendation with negotiation framing.

---

## Required Inputs

- Target property + suite (or tenant name -- skill resolves to suite)
- Reason for the review (renewal coming up / wondering if underpriced / negotiating mid-term / etc.)

---

## Output Format

```
PRICING REVIEW
---
Subject: [property + suite]
Tenant: [name @ company]
Current lease: $[X]/SF [type] | Term ends [date] | [N] months remaining
Current annual rent: $[X]

MARKET POSITION
- Submarket comp range: $[low] -- $[high]/SF [type]
- Mid-market: $[mid]/SF
- Akiva's current: $[X]/SF
- Gap to mid-market: [X% below / on-market / X% above]
- Gap to high-market: [X% below]

ADJUSTMENTS TO CONSIDER
- Tenant tenure: [N] years (longer tenure = relationship discount may apply)
- Build-out invested: [if any]
- Tenant credit: [strong / moderate / unknown]
- TI burn-down remaining: [if applicable]
- Escalation already in lease: [X% / fixed schedule]

NEGOTIATION RANGE (Akiva's call)
- Status quo: $[current]/SF -- "honor the current term, address at renewal"
- Soft increase (renewal): $[mid - 10%]/SF -- "below market but reflects 50-tenant relationship-first stance"
- Mid-market (renewal): $[mid]/SF -- "fair market reset"
- Aggressive (renewal): $[mid + 5-10%]/SF -- "if comps are firm and tenant has invested in the space"

RECOMMENDED PLAY
[2-3 sentences -- what would I do here, why. References his relationship-first style if tenant is long-term + reliable.]

CONVERSATION DRAFT (for the renewal conversation)
[Short script Akiva can use opening the renewal conversation. References specifics.
Honors his relationship-first tone -- not aggressive.]
```

---

## Tone Rules

- This is INTERNAL analysis. Show the math, then give a clean recommendation.
- Honor Akiva's relationship-first stance -- if a tenant is long-term and reliable, the recommendation should default toward "soft increase," not "mid-market reset."
- Always show the full range so Akiva can pick. Don't push a number on him.
- The conversation draft should sound like him -- short, direct, no aggressive language.

---

## Cross-Portfolio Pricing Audit

Akiva can also ask "review pricing across the whole portfolio" -- in which case run this for every active tenant in `context/portfolio.md` and output a one-page table:

```
PORTFOLIO PRICING AUDIT
Property | Suite | Tenant | Current $/SF | Mid-market $/SF | Gap | Renewal in
```

Sort by "renewal in" ascending so he sees nearest-renewal first.
