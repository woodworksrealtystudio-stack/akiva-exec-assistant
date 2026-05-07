---
title: Lead Consolidation
type: concept
tags: [pain-point, workflow, crm]
created: 2026-05-06
updated: 2026-05-07
sources: 1
---

# Lead Consolidation

Pain point #1. From the [[2026-05-01 Intro Call]] and reinforced [[2026-05-07 In-Person Demo]]: every inbound lead needs to land in [[AppFolio]] as a guest card with duplicate detection on phone number.

---

## The Problem

Inbound leads arrive in three different channels:

1. **[[LoopNet]]** -- inquiry emails arriving in [[Outlook]]
2. **[[Google Voice]]** -- inbound calls + texts (voicemails transcribed inside Google Voice, not exported)
3. **[[Microsoft Forms]]** -- his lead-intake form, results emailed to him

None of these auto-log into [[AppFolio]] (his CRM of record). He manually copies contact info, transcribes what was said, and links to the property the prospect was interested in.

---

## The Cost

- Lost leads (forgotten because the message lives in only one inbox)
- Slow follow-up (manual copy-paste before he can respond)
- No single source of truth -- he can't query "every prospect who inquired about X this month"
- Can't onboard a future VA cleanly because there's no canonical pipeline
- AppFolio guest cards get duplicated when the same prospect calls + emails

---

## v1 Workflow (manual hand-off, Microsoft 365 read-only constraint)

```
LoopNet email in Outlook   ─→  "Claude, parse this LoopNet inquiry"  ─→  Wiki entity + draft follow-up
Google Voice transcript    ─→  Akiva pastes (or transcribe skill)     ─→  Wiki entity + draft follow-up
Microsoft Forms response   ─→  Akiva pastes the email                 ─→  Wiki entity + draft follow-up
                                       │
                                       ▼
                          Claude tells Akiva exactly what AppFolio
                          guest card to create (name, phone, property,
                          source, notes). Akiva creates it in AppFolio.
```

Each new lead at v1:
- Logged in `wiki/entities/<prospect>.md` (so context compounds across leads)
- Logged in `context/portfolio.md` Hot Leads section
- A drafted follow-up email ready for Akiva to copy into Outlook and send
- A "create AppFolio guest card with these fields" instruction Akiva can do in 30 seconds

**v1 is intentionally human-in-the-loop on every inbound + outbound.** No tenant or broker ever gets an email Akiva didn't approve.

---

## v2 Workflow (after Outlook MCP add-on + email parser, retainer scope)

```
LoopNet email arrives  ─→  Outlook folder watcher  ─→  Mailparser.io  ─→  Sheets staging
Google Voice text      ─→  Forwarded to Outlook    ─→  same path
Microsoft Forms reply  ─→  Power Automate bridge   ─→  same path
                                       │
                                       ▼
                          Claude triages new entries in the wiki
                          + drafts follow-ups in Outlook drafts folder
                          + weekly CSV export to AppFolio (or live API
                          if AppFolio Plus is in by then)
```

Adds:
- Auto-ingestion from Outlook (no paste-in)
- Mailparser.io ($35-100/mo direct cost) for structured LoopNet parsing
- Weekly AppFolio CSV import (Basic tier path) **OR** AppFolio Plus API (clean path)

---

## v3 Workflow (after phone AI is built)

```
Inbound call to Google Voice number  ─→  Vapi/Retell AI agent
                                              │
                                              ▼
                                    Q&A screening: company, website,
                                    time in business, suite, phone
                                              │
                            ┌─────────────────┴─────────────────┐
                            ▼                                   ▼
                   Qualified           Hand-off to Akiva       Not qualified
                   prospect            (live transfer)          → email digest
                            │                                   │
                            └────────────→  Wiki + AppFolio  ←──┘
```

---

## Related

- [[LoopNet]], [[Google Voice]], [[AppFolio]], [[Outlook]]
- [[Akiva Halpern]]
- [[2026-05-07 In-Person Demo]]
