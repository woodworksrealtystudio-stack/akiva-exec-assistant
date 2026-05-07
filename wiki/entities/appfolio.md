---
title: AppFolio
type: entity
tags: [tool, crm, property-management]
created: 2026-05-06
updated: 2026-05-06
---

# AppFolio

Akiva's property management software. Source of truth for tenants, leases, payments, maintenance.

---

## What It Is

Property management platform with built-in CRM, accounting, maintenance ticketing, and (on the upper tier) AI / automation features.

---

## How It Fits Into Akiva's Stack

**Target end-state:** AppFolio is the CRM of record. Every lead -- whether it comes in via [[LoopNet]], [[Google Voice]], or direct email -- should land in AppFolio.

**Current state:** Lead data lives in inboxes and texts; AppFolio has the active tenants but not the inbound pipeline.

**Why he's not on AppFolio's upper tier:** Their AI / automation is "their stuff, not as open as using my own, or like, using Claw, or ChatGPT" (from intro call). He wants tweakable, not vendor-locked.

---

## Open Questions

- What tier is he currently on?
- Does AppFolio have a public API + webhook surface? (Confirm before designing the lead-consolidation pipeline.)
- What's already configured re: tenant comms templates, maintenance tickets, payment reminders?

---

## Related

- [[Lead Consolidation]] -- the workflow this entity is the destination of
- [[Akiva Halpern]]
