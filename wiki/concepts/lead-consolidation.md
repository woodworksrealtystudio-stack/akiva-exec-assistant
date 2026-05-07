---
title: Lead Consolidation
type: concept
tags: [pain-point, workflow, crm]
created: 2026-05-06
updated: 2026-05-06
sources: 1
---

# Lead Consolidation

Pain point #1. The first thing Akiva said he wanted automated on the [[2026-05-01 Intro Call]]: every inbound lead needs to land in his CRM.

---

## The Problem

Inbound leads arrive in three different channels:

1. **[[LoopNet]]** -- inquiry emails when prospects view his commercial listings
2. **[[Google Voice]]** -- inbound calls + texts (voicemails transcribed inside Google Voice, not exported)
3. **Direct email** -- referrals, broker outreach, repeat prospects

None of these auto-log into [[AppFolio]] (his CRM of record). He has to manually copy contact info, transcribe what was said, and link to the property the prospect was interested in.

---

## The Cost

- Lost leads (forgotten because the message lives in only one inbox)
- Slow follow-up (manual copy-paste before he can respond)
- No single source of truth -- he can't query "every prospect who inquired about X this month"
- Can't onboard a future VA cleanly because there's no canonical pipeline

---

## Target End-State

```
LoopNet email
     \
Google Voice transcript --→  Parsing layer  --→  AppFolio entry
     /                               +
Direct email                  Wiki entity page
                                     +
                              Draft follow-up to review
```

Each new lead:
- Logged in AppFolio with property, contact, source, timestamp
- Mirrored to a wiki entity page (so context compounds across leads)
- A drafted follow-up email ready for Akiva to review and send

---

## Build Path

1. **Day 1 / Demo:** Manual Claude + paste workflow -- forward LoopNet email, paste Google Voice transcript, Claude logs to wiki and drafts follow-up.
2. **Day 14 / Once setup is stable:** Composio MCP for Gmail watches a folder, auto-parses LoopNet inquiries, creates the entries.
3. **Day 30+:** AppFolio API connection (if exposed) so the wiki and AppFolio stay in sync without manual entry.

---

## Related

- [[LoopNet]], [[Google Voice]], [[AppFolio]]
- [[Akiva Halpern]]
