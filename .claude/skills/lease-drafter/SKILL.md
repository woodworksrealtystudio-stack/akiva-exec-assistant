---
name: lease-drafter
description: Draft commercial lease language and clauses during negotiations. Use when Akiva says "draft a clause for X," "write the [TI / option / personal guaranty / use clause] language," "redline this," or "give me alternative wording for X." Different from contract-summary (reads) and lease-extractor (logs to database) -- this WRITES new lease language.
---

# Lease Drafter

Drafts specific clauses, redlines, and alternative language during lease negotiations. Akiva said: *"I want to help draft the lease. You know, like, in negotiations."*

This is NOT lease-from-scratch (attorney work). It's clause-by-clause drafting that Akiva uses to push back on broker-supplied LOIs and tenant redlines.

---

## Process

1. Identify the clause type Akiva needs (use, term, option, TI, personal guaranty, assignment, holdover, default, casualty, etc.).
2. Read `wiki/synthesis/leases/` for examples of how Akiva has handled similar clauses in his existing portfolio (consistency matters).
3. Read `context/me.md` for his stance (relationship-first, owner-friendly, soft-touch operator).
4. Generate the clause.
5. Offer 2-3 alternative wordings if relevant.
6. Flag anything that should go to attorney review.

---

## Common Clause Types

### Permitted Use
- Specific use (one tenant, one purpose)
- Permitted use + retained right of LL approval for change of use
- Broad permitted use with carve-outs (no automotive, no cannabis, no restaurants without venting, etc.)

### Term + Options
- Initial term + N x Y-year renewal options at FMV
- Initial term + N x Y-year renewal options at fixed escalation
- Initial term + early termination right (with kick-out fee)

### Rent + Escalations
- Base rent / SF / year, NNN
- Annual escalations: fixed % / CPI / fixed schedule
- Free rent: front-loaded vs. spread
- Caps + floors on CPI escalations

### Tenant Improvements
- TI allowance with construction by LL (turnkey)
- TI allowance with construction by tenant (LL approval of plans)
- LL takes back unused TI vs. tenant credits unused TI to rent

### Personal Guaranty
- Full personal guaranty
- Capped guaranty (X months rent)
- Burn-down guaranty (reduces over time)
- No guaranty (corporate only)

### Assignment + Sublease
- Permitted with LL consent (consent not unreasonably withheld)
- Permitted to affiliates without consent, others with consent
- Restricted (no assignment without explicit written consent + 50/50 of profit)

### Operating Expenses (NNN)
- Tenant pro-rata share of CAM, taxes, insurance
- Caps on controllable CAM
- Base year + annual increases over base year (modified gross)

### Holdover
- Standard 150% of base rent
- 200% holdover (more aggressive)
- Holdover + LL right to terminate at any time

### Default + Cure
- Standard cure: 10 days monetary, 30 days non-monetary
- Aggressive: 5 days monetary, 15 days non-monetary
- Soft: 30 days monetary, 60 days non-monetary

### Casualty + Condemnation
- LL right to terminate if X% of building damaged
- Tenant right to terminate if premises unusable for X days
- Rent abatement during repair

### Akiva's Standard Stance (apply unless told otherwise)
- Permitted use: specific to current use + LL consent for change
- Personal guaranty: capped or burn-down -- relationship-first
- Late fees: minimal language (Akiva rarely charges them anyway)
- Default cure: standard 10/30
- Holdover: 150% (standard, not aggressive)

---

## Output Format

```
CLAUSE: [type]
Context: [tenant + property + situation]

DRAFT LANGUAGE -- Recommended
[Full clause text, properly formatted, ready to drop into the lease.]

ALTERNATIVE 1 -- [softer / harder / different framing]
[Full clause text]

ALTERNATIVE 2 -- [if relevant]
[Full clause text]

NEGOTIATION NOTES
- [Why this language vs. the alternatives]
- [What the broker / tenant pushback might be]
- [Akiva's typical stance for this clause type]

FLAG FOR ATTORNEY
[Only if relevant -- anything novel, unusually aggressive, jurisdiction-specific, or carrying real liability tail]
```

---

## When to Flag for Attorney

Always flag (don't auto-draft a final version) for:
- Indemnification language (significant liability allocation)
- Environmental clauses
- Insurance provisions with specific waivers / subrogation language
- Anything involving real-money damages caps
- Anything that deviates from market norms

For these, draft an OPTION but explicitly say: "This is a starting point -- run it past your attorney before signing."

---

## Tone

- Plain language wherever possible
- Use defined terms consistently (Tenant, Landlord, Premises, Building, Lease)
- Keep clauses short -- one idea per paragraph
- No legalese for legalese's sake
