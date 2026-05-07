---
name: lead-research
description: Research a CRE lead -- LoopNet inquiry, broker rep, prospect tenant, or potential acquisition target. Use this skill whenever Akiva asks to look up someone, research a contact, build a profile, or prep for a tour or negotiation.
---

# Lead Research

Compiles a CRE-specific profile so Akiva walks into every conversation prepared. Works for prospect tenants, brokers, sellers, or buyers.

---

## Process

1. Read `context/portfolio.md` for any existing notes on this contact.
2. Ask Akiva for any information he already has (the LoopNet email, the broker's call, the referral source).
3. Use Claude Code's WebSearch / WebFetch tools to pull anything missing -- LinkedIn, county records, business reviews, broker bio.
4. Build the profile using the format below.
5. Flag what's still unknown and suggest where to find it (LinkedIn, county records, broker public profile, business website).

---

## Required Inputs

- Name (person + company / brokerage / business if applicable)
- Any known contact info (email, phone)
- How they came in (LoopNet, Google Voice, referral, broker intro, etc.)
- What Akiva knows so far
- Property in question (if applicable)

---

## Profile Format

```
LEAD PROFILE
---
Name: [full name]
Company: [brokerage / business / entity]
Contact: [email] | [phone]
Source: [LoopNet / Google Voice / referral / broker]
Date added: [date]

BACKGROUND
[2-3 sentences: who they are, profession, business if known, any personal context]

CRE SITUATION
- Side: [tenant rep / LL rep / buyer / seller / direct prospect / investor]
- Looking for: [type, SF range, area, use, budget]
- Timeline: [immediate / 30-60 days / exploring]
- Decision maker: [self / partner / committee]
- Motivation: [why they're moving / buying / selling]

PROPERTY HISTORY (if applicable)
[Properties they currently own, lease, or have transacted -- from county records or what they shared]

NOTES FOR FIRST MEETING / TOUR
- [Something specific to reference]
- [A question to ask]
- [A comp or Matterport link to bring]

RED FLAGS / WATCH-OUTS
[Anything from research that warrants caution -- credit, prior litigation, broker reputation]

NEXT ACTION
[Specific next step with suggested timing]
```

---

## What to Look For

- LinkedIn for professional background, employer, tenure
- Company website + reviews (for prospect tenants)
- County tax records for current property ownership
- Loopnet / Costar transaction history if available publicly
- Broker's public deal sheet (for broker reps)
- Mutual connections (referral source context)
