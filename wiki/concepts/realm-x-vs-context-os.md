---
title: Realm-X vs. Akiva's Context OS
type: concept
tags: [appfolio, context-os, naming, scope]
created: 2026-05-07
updated: 2026-05-07
---

# Realm-X vs. Akiva's Context OS

Two different systems. They complement each other. Don't confuse them.

---

## AppFolio's Realm-X

**What it is:** AppFolio's built-in AI leasing agent. A feature inside AppFolio's Plus tier (~$1,300/mo).

**What it does:**
- AI leasing chatbot for tenant screening
- Tour scheduling inside AppFolio
- Lease drafting + auto-population in AppFolio
- Tenant Q&A inside the AppFolio portal
- Maintenance ticket suggestions inside AppFolio

**Where it lives:** Inside the AppFolio web UI / mobile app. Tenants and prospects interact with it through AppFolio's interface.

**Cost:** Bundled into AppFolio Plus tier (~$1,000/mo more than basic).

---

## Akiva's Context OS (this system)

**What it is:** A custom AI executive assistant Akiva owns and runs locally inside Claude Code. Built by Woodworks Realty Studio.

**What it does:**
- Reads Akiva's Outlook, Calendar, OneDrive on demand
- Parses any inbound lead from any source -> structured wiki entity + drafted reply + AppFolio guest-card instructions
- Triages his Outlook inbox in batch
- Generates branded vacancy flyers + segmented email blasts
- Builds a queryable lease database in his wiki
- Monday-morning operations digest
- Drafts tenant-FAQ responses citing his actual lease terms
- Categorizes maintenance tickets and drafts vendor + tenant comms
- Schedules tours by reading his calendar
- Pulls market comps + does prospect research via WebSearch
- Maintains his second brain (every tenant, broker, deal, decision)

**Where it lives:** In a GitHub repo Akiva owns, on his own machine, inside Claude Code. No shared servers. He owns every file.

**Cost:** $1,500 setup + $200/mo retainer.

---

## How They Work Together

```
INBOUND
  LoopNet email -> Outlook
  Microsoft Forms -> Outlook
  Google Voice -> SMS / voicemail
                            \
                             v1: Akiva pastes / forwards
                             v2: Outlook MCP auto-watches
                                  \
                                   v
                          [ Akiva's Context OS ]
                          - Parses lead
                          - Drafts follow-up reply
                          - Logs to wiki entity
                          - Outputs AppFolio guest-card spec
                          - Akiva creates the guest card
                                  \
                                   v
                          [ AppFolio + Realm-X ]
                          - Guest card lives in AppFolio
                          - Realm-X handles tour scheduling inside AppFolio
                          - Realm-X drives lease drafting inside AppFolio
                          - Akiva approves and signs
                                  \
                                   v
                          [ Back to Context OS ]
                          - Lease extractor logs the executed lease to wiki
                          - Tenant entity now has full record
                          - Lease database queryable across portfolio
```

---

## The One-Sentence Distinction

- **Realm-X = AI inside AppFolio.**
- **Context OS = AI everywhere else.**

If a workflow is INSIDE AppFolio (tour scheduling in their portal, tenant chatbot on their app, lease auto-fill in their UI), that's Realm-X.

If a workflow is OUTSIDE AppFolio (Outlook, OneDrive, vacancy flyers, Monday digest, market research, the wiki), that's Context OS.

They never duplicate. They never conflict. They reinforce each other.

---

## Why This Matters

Akiva said in the 2026-05-07 demo:
> "I'm a little bit locked into [AppFolio's] ecosystem... I'm not going to not use their built-in AIs already."

Right answer. Don't replace AppFolio. Don't replace Realm-X. The Context OS is the thinking + drafting layer that wraps around them and the wider Microsoft 365 + LoopNet + Google Voice + Matterport stack he uses.

---

## Decision Triggers

When in doubt about which system handles a workflow, use this:

| Workflow | System |
|---|---|
| A prospect texts Akiva's Google Voice number | Context OS (parse + draft) |
| Akiva needs to log into AppFolio to create a guest card | AppFolio + Realm-X (Akiva does this) |
| Akiva wants to know "what should I charge for Suite 200" | Context OS (`pricing-review`) |
| AppFolio needs to send a rent reminder | AppFolio + Realm-X (already runs) |
| Akiva pastes a lease he's negotiating | Context OS (`lease-drafter` for clauses) |
| Akiva wants to send a vacancy flyer to 200 brokers | Context OS (`vacancy-marketing`) |
| Tenant asks "when does my lease end" | Either -- if they ask via AppFolio app, Realm-X. If they email Akiva, Context OS (`tenant-faq`). |

---

## Related

- [[Akiva Halpern]]
- [[AppFolio]]
- [[Outlook]]
