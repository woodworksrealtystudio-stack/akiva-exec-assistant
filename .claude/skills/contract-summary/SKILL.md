---
name: contract-summary
description: Summarize a commercial lease, LOI, or purchase agreement. Use this skill whenever Akiva asks to summarize a contract, pull key dates, flag redlines, or create a clean deal summary.
---

# Contract Summary

Parses a commercial real estate document (lease, LOI, purchase agreement, amendment) and outputs a clean 1-page summary with key economic terms, dates, and a red-flag list.

---

## Process

1. Ask Akiva to paste the document text or key sections (or read from an uploaded file if available).
2. Extract all required fields.
3. Output the summary in the format below.
4. Flag unusual clauses, missing standard provisions, tight deadlines, or aggressive landlord/tenant favorability.

---

## Summary Formats

### For a LEASE (or LOI)

```
LEASE SUMMARY
---
Property: [address, suite]
Landlord: [entity]
Tenant: [name + entity]
Use: [permitted use]

ECONOMIC TERMS
- Premises: [SF]
- Term: [X years, commencing [date]]
- Base Rent: $[X]/SF NNN (or modified gross / FSG)
- Annual Increases: [X% or CPI]
- Free Rent: [X months]
- TI Allowance: $[X]/SF
- Security Deposit: $[X]
- Personal Guaranty: [yes / no / capped]

OPTIONS & RIGHTS
- Renewal: [X x Y years at FMV / fixed]
- Right of First Refusal: [yes/no]
- Termination Right: [yes/no -- conditions]
- Assignment / Sublease: [permitted with consent / restricted]

EXPENSES (NNN)
- CAM: [tenant pro-rata]
- Taxes: [tenant pro-rata]
- Insurance: [tenant carries / pro-rata]
- Utilities: [direct meter / sub-meter]

KEY DEADLINES
[date] -- [milestone -- e.g., LOI response, lease execution, possession]
[date] -- [milestone]
[date] -- [milestone]

RED FLAGS
[Any unusual terms, aggressive language, missing standard provisions]
```

### For a PURCHASE AGREEMENT

```
PURCHASE SUMMARY
---
Property: [address]
Seller: [entity]
Buyer: [entity]
Purchase Price: $[X]
Earnest Money: $[X] due [date]
Closing: [date]

CONTINGENCIES
- Due Diligence: [X days from effective date]
- Financing: [yes/no -- terms]
- Title: [delivery + cure period]
- Environmental: [yes/no]

KEY DEADLINES
[date] -- [milestone]
[date] -- [milestone]

RED FLAGS
[unusual seller representations, broad as-is language, environmental holdback, etc.]
```

---

## Flags to Watch (CRE-specific)

- Personal guaranty without a cap or burn-down schedule
- Indemnity provisions that cap landlord but not tenant (or vice versa)
- Operating expense definitions that include capital expenditures
- Tax escalation with no base year reset
- Co-tenancy clauses that don't actually trigger anything
- Holdover rent at less than 150% of base
- Renewal options with no pre-set rate or formula
- LOI language that is binding when it claims to be non-binding (or vice versa)
- Brokerage commission language that obligates the wrong party
- Notice provisions requiring overnight delivery to multiple parties
