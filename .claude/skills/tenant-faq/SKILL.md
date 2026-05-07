---
name: tenant-faq
description: Draft a response to a common tenant question -- rent, lease, maintenance, billing, neighbor, building, complaint. Reads the lease database and the tenant's wiki page so the response is specific to their actual lease and history. Use when Akiva pastes a tenant message, says "respond to this tenant," or describes a tenant question.
---

# Tenant FAQ

Drafts tenant-facing email/text responses to recurring questions. Pulls the tenant's actual lease terms from `wiki/synthesis/leases/` so answers reference the right SF, rent, dates, and clauses -- not generic boilerplate.

---

## Process

1. Identify the tenant from the message (sender, salutation, or Akiva's prompt).
2. Read `wiki/entities/<tenant-slug>.md` for context.
3. Read `wiki/synthesis/leases/<lease>.md` for the actual lease terms.
4. Identify the question category (see below).
5. Draft a response in Akiva's voice that's accurate to their specific lease.
6. Log the correspondence to the tenant's entity page.
7. Flag if the issue needs Akiva's actual judgment (legal, dispute, sensitive).

---

## Question Categories + Response Templates

### Rent / billing
- When is rent due? -> Pull from lease + grace period
- Why is my CAM higher this year? -> Pull from operating expense clause
- Can I pay late? -> Reference late fee policy + Akiva's relationship-based stance
- Where do I send payment? -> AppFolio portal link

### Lease
- When does my lease end? -> Pull from lease
- Renewal options? -> Pull renewal clause
- Can I sublease? -> Pull assignment clause
- Can I change the use? -> Pull permitted use clause + flag for Akiva approval

### Maintenance
- Something is broken -> Route to `maintenance-triage`
- Whose responsibility -- LL or tenant? -> Pull from lease

### Neighbors / building
- Noise complaint about another tenant -> Acknowledge, gather details, flag for Akiva
- HVAC / common area issue -> Route to `maintenance-triage`

### Sensitive (always flag for Akiva, don't auto-draft a final answer)
- Eviction / non-payment dispute
- Lease violation accusation
- Insurance claim
- Anything mentioning attorney / lawyer / lawsuit

---

## Output Format

```
TENANT MESSAGE FROM: [tenant name @ property]
QUESTION CATEGORY: [rent / lease / maintenance / building / sensitive]
LEASE CONTEXT: [pulled from wiki/synthesis/leases/<file>.md]
   - Term ends: [date]
   - Base rent: $[X]/SF [type]
   - [other relevant terms]

DRAFT RESPONSE
---
Subject: [specific]

[2-3 short paragraphs in Akiva's voice -- references their actual lease,
gives the specific answer, sets a clear next step]

WIKI UPDATED
- Logged correspondence to wiki/entities/<tenant-slug>.md

[FLAG if sensitive: "This involves [legal / dispute / etc.] -- review carefully and consider
forwarding to attorney before responding."]
```

---

## Tone

- Warm but direct -- treat tenants like long-term partners (Akiva's style: relationship-based)
- Reference the specific term / dollar / date from their lease
- Never make up a clause that's not in the lease -- if unsure, say "I'll need to check the lease and get back to you"
- Akiva's stance on late fees: relationship-first. He has 50 tenants and traditionally never charges late fees. Match that posture unless he says otherwise.
