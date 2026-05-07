---
name: maintenance-triage
description: Triage a maintenance request from a tenant. Categorizes the issue, drafts the vendor RFQ / dispatch email, drafts the tenant acknowledgment, logs to wiki/synthesis/maintenance/. Use when Akiva pastes a maintenance message, forwards an AppFolio maintenance ticket, or describes a tenant maintenance issue.
---

# Maintenance Triage

Front-end triage for any maintenance request. Categorizes the issue, drafts the vendor email, drafts the tenant acknowledgment, builds the maintenance log.

---

## Process

1. Identify tenant + property from the message.
2. Categorize the issue (see categories below).
3. Determine LL vs Tenant responsibility (read `wiki/synthesis/leases/<lease>.md` for the relevant clause).
4. Draft the vendor dispatch email (which vendor, scope, urgency).
5. Draft the tenant acknowledgment email (acknowledges, sets timeline expectation).
6. Log the ticket to `wiki/synthesis/maintenance/YYYY-MM-DD-<property>-<short-desc>.md`.
7. Flag urgency level for Akiva.

---

## Categories

### Mechanical
- HVAC (heat / cool / ventilation)
- Plumbing (leak, blockage, water heater)
- Electrical (outlet, circuit, lights)
- Refrigeration (commercial coolers / freezers)

### Structural
- Roof leak
- Window / door / lock
- Floor / wall damage
- Foundation / settling

### Building systems
- Fire / life safety (always urgent)
- Security (door access, cameras)
- Elevator / lift

### Cosmetic / Tenant-responsibility
- Paint, light bulbs, minor scuffs
- Most cosmetic items are tenant responsibility per standard CRE leases

### Common area / Multi-tenant
- Parking lot, exterior lights, signage
- Landscaping
- Trash / dumpster

### Code / Compliance
- ADA, fire code, health department
- Always involves Akiva's judgment + flag

---

## Urgency Triage

- **EMERGENCY** -- water actively flooding, electrical fire risk, HVAC out in extreme weather, fire/life safety. Same-day vendor dispatch.
- **HIGH** -- HVAC partial, water heater out, security breach. 24-48 hour resolution.
- **NORMAL** -- non-urgent functional issues. 3-5 day resolution.
- **LOW** -- cosmetic, scheduled batch with other work.

---

## Output Format

```
MAINTENANCE TICKET
---
Tenant: [name @ property]
Issue: [one-line description]
Category: [from above]
Urgency: [EMERGENCY / HIGH / NORMAL / LOW]
LL/Tenant responsibility: [LL responsible / Tenant responsible / Disputed -- flag for Akiva]
Lease clause: [pulled verbatim from wiki/synthesis/leases/<file>.md]

DRAFT VENDOR EMAIL
To: [suggested vendor based on category, or "TBD -- which vendor?"]
Subject: [specific]
[Vendor-facing email -- scope, address, tenant contact, urgency]

DRAFT TENANT ACKNOWLEDGMENT
Subject: [specific]
[Tenant-facing email -- acknowledged, vendor dispatched, timeline]

WIKI LOG
- Created wiki/synthesis/maintenance/YYYY-MM-DD-<slug>.md

NEXT ACTION
[Akiva approves vendor email + sends / Akiva needs to make a call on responsibility / Akiva needs to call tenant directly]
```

---

## Wiki Maintenance Log Format

`wiki/synthesis/maintenance/YYYY-MM-DD-<property>-<short-desc>.md`:

```yaml
---
title: Maintenance -- [property] -- [issue]
type: synthesis
tags: [maintenance, [property-slug], [tenant-slug]]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: open / dispatched / closed
---

# Maintenance -- [property] -- [issue]

## Reported
- Date: [YYYY-MM-DD]
- Tenant: [name]
- Channel: [AppFolio ticket / email / text / phone]
- Description: [verbatim or paraphrased]

## Categorization
- Category: [...]
- Urgency: [...]
- Responsibility: [LL / Tenant / Disputed]
- Lease clause: [verbatim]

## Action Taken
- Vendor dispatched: [name / TBD]
- Vendor contact: [...]
- Estimated cost: [if known]
- Tenant acknowledged: [date]

## Resolution
- Date closed: [if closed]
- Final cost: [...]
- Notes: [...]
```
