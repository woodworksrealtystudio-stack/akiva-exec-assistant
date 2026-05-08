---
title: Brokerage Pipeline
type: concept
tags: [brokerage, growth, scale, pipeline]
created: 2026-05-07
updated: 2026-05-07
sources: 1
---

# Brokerage Pipeline

The third-party brokerage side of Akiva's operation. He said on 5/7:

> "I just got my real estate license to also broker deals... the goal is to be able to take on more clients."

Property management runs on his own portfolio. Brokerage = he represents OTHER owners' deals. This is the growth lane.

---

## Two Distinct Lanes

| Property Management | Brokerage |
|---|---|
| His ~50 tenants | Third-party clients |
| Owned portfolio | Other owners' properties |
| Long-term relationships | Transactional (commission-based) |
| Already running | New, scaling |

The Context OS handles both. Skills like `lead-parser`, `tour-scheduler`, `vacancy-marketing`, `comp-analysis` work for either lane -- the workflow is identical, only the property + client identity changes.

---

## What's Different in Brokerage

When a workflow is for a brokerage client (not his own portfolio):

- **Wiki context:** the property is owned by someone else -- track owner contact, their preferences, their flexibility
- **Communication:** Akiva is the rep, not the principal -- emails should reflect that ("On behalf of [owner]" framing)
- **Pricing:** the owner sets the price; Akiva advises and negotiates
- **Conflict of interest watch:** if a prospect is interested in a brokerage listing AND one of his own owned vacancies, disclose
- **Commission tracking:** every brokerage deal has a commission -- track in `wiki/synthesis/deals/<address>.md`

---

## Brokerage Wiki Structure

When a brokerage client is added:
- `wiki/entities/<owner-name>.md` -- the principal owner (separate from prospect tenants)
- `wiki/entities/<address>.md` -- the property he's representing
- `wiki/synthesis/deals/<address>.md` -- the deal record (LOI, lease, commission, timeline)

When a brokerage transaction closes:
- Lease lands in `wiki/synthesis/leases/` (same as owned portfolio)
- Tag it `brokerage: true` in frontmatter so queries can separate
- Commission record stays in `wiki/synthesis/deals/`

---

## Scaling Signal

Akiva's pace target on the brokerage side:
- Today: 0 brokerage clients (just licensed)
- 30-day pilot goal: first brokerage client signed
- 90-day goal: 3 brokerage clients in pipeline
- 1-year stretch: 10+ brokerage clients, separate from owned portfolio management

The point of this assistant is so he can take on these clients **without** the time cost of running them manually -- the workflows are already drawn; he just plugs in new clients.

---

## Related

- [[Akiva Halpern]]
- [[Lead Consolidation]] -- inbound brokerage leads work the same way
- [[Vacancy Marketing]] -- brokerage listings get the same flyer treatment
