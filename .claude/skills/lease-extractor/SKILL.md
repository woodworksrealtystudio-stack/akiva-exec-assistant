---
name: lease-extractor
description: Extract structured data from a lease document and build the lease database in wiki/synthesis/leases/. Different from contract-summary -- this builds a queryable, growing record of every lease in the portfolio so Akiva can ask "what's the term on Suite 200" or "which leases expire in Q3" without re-reading the doc. Use when Akiva pastes a lease, asks to "log this lease," "add this lease to the wiki," or "extract the terms."
---

# Lease Extractor

Builds the lease database. Every lease processed lands as a structured page in `wiki/synthesis/leases/<address>-<suite>.md` and updates `context/portfolio.md`.

This is how Akiva can later ask: "show me every lease that expires in 2026" or "which tenants have personal guaranties capped" -- the wiki has the answer because every lease was logged.

---

## Process

1. Parse the lease (paste-in text or read from OneDrive via M365 connector).
2. Extract the structured fields below.
3. Write to `wiki/synthesis/leases/<address>-<suite>.md` (overwrite if exists, version history in git).
4. Update `wiki/entities/<tenant>.md` to link to the lease.
5. Update `context/portfolio.md` Active Tenants table.
6. Append `wiki/log.md` with the ingest entry.
7. Output a 1-page summary for Akiva.

---

## Output File Format

`wiki/synthesis/leases/<address>-<suite>.md`:

```yaml
---
title: Lease -- [address, suite]
type: synthesis
tags: [lease, [tenant-slug], [property-slug]]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Lease -- [Property Address, Suite]

## Parties
- Landlord: [entity name]
- Tenant: [entity name + DBA]
- Personal Guaranty: [yes -- capped at $X / yes -- uncapped / no / burn-down schedule]

## Premises
- Address: [full address + suite]
- Rentable SF: [X]
- Usable SF: [X if different]
- Use: [permitted use clause -- verbatim]

## Term
- Commencement: [date]
- Expiration: [date]
- Total months: [N]
- Holdover rent: [X% of base]

## Economics
- Base rent year 1: $[X]/SF [NNN/MG/FSG]
- Annual increases: [X% / CPI / fixed schedule]
- Free rent: [X months, dates]
- Concessions: [list]

## Operating Expenses (NNN)
- CAM: [tenant pro-rata / cap]
- Taxes: [tenant pro-rata / base year]
- Insurance: [carries own / pro-rata]
- Utilities: [direct meter / sub-meter / pro-rata]

## Tenant Improvements
- TI Allowance: $[X]/SF
- Construction by: [LL / Tenant]
- TI completion deadline: [date]

## Options + Rights
- Renewal: [X x Y years at FMV / fixed]
- Right of First Refusal: [yes/no -- terms]
- Termination right: [yes/no -- terms]
- Assignment / Sublease: [permitted with consent / restricted]

## Security
- Security deposit: $[X]
- Letter of credit: [if applicable]

## Key Dates (forward-looking)
- Next rent escalation: [date]
- Renewal notice deadline: [date]
- Expiration: [date]

## Red Flags / Watch Items
- [unusual clauses, aggressive language, missing standard provisions]

## Source
- Original document: [path or "pasted-in YYYY-MM-DD"]
- Ingested: [date]
```

---

## Output to Akiva (in chat)

```
LEASE LOGGED
---
[tenant] @ [address, suite]
Term: [start] -- [end]  ([N] months)
Base rent year 1: $[X]/SF [type]
TI: $[X]/SF
Personal guaranty: [status]

Saved to: wiki/synthesis/leases/<file>.md
Linked from: wiki/entities/<tenant>.md

KEY DATES (added to your watch list)
- [date] -- [milestone]
- [date] -- [milestone]

RED FLAGS
- [or "None unusual"]

NEXT ACTION
[Renewal calendar entry / TI tracking / nothing -- just logged]
```

---

## Database Queries Akiva Can Run

Once leases are in the database, he can ask:
- "Show me every lease expiring in the next 12 months"
- "Which tenants have uncapped personal guaranties"
- "What's our average $/SF NNN across the portfolio"
- "Which leases have free rent burning off this year"

Claude reads the synthesis files + portfolio.md to answer.
