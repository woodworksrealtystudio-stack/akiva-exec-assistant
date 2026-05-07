---
name: inbox-triage
description: Triage Akiva's Outlook inbox in batch -- reads unread / recent emails via the Microsoft 365 connector, categorizes them, and drafts replies for the response-needed bucket. Use when Akiva says "triage my inbox," "what's in my email," "go through my email," or asks about a specific time window of email.
---

# Inbox Triage

Batch processes Akiva's Outlook inbox. Categorizes, summarizes, drafts replies he reviews and sends from Outlook himself.

---

## Process

1. Use the Microsoft 365 connector to search his Outlook inbox per the criteria given (default: unread in the last 24 hours).
2. For each thread, classify into one of:
   - **Lead inquiry** -- LoopNet, Forms, broker referral, direct prospect (route through `lead-parser` skill)
   - **Tenant comm** -- existing tenant, route through `tenant-faq` skill if it's a common question
   - **Maintenance** -- maintenance request, route through `maintenance-triage` skill
   - **Broker / vendor / partner** -- needs response, draft via `email-draft` skill
   - **FYI** -- informational, no response needed, log if substantive
   - **Spam / ignore** -- skip
3. Output a one-page summary with priorities and drafted replies stacked in order.
4. Log substantive threads to the right wiki entity page (tenant correspondence under tenant entity, broker correspondence under broker entity).

---

## Required Inputs

- Time window (default: unread in last 24 hours, or "since yesterday morning")
- Optional filter (sender, subject keyword, folder)

---

## Output Format

```
INBOX TRIAGE -- <window>
---
Total threads scanned: [N]
Needs response: [N]   FYI: [N]   Skipped: [N]

PRIORITY ORDER
---
1. [URGENT TAG if applicable] From [Sender] -- [Subject]
   Thread summary: [2 sentences]
   Recommended action: [Reply / Lead-parse / Maintenance-triage / Wiki log]
   Drafted reply: [if applicable, full draft to copy into Outlook]

2. From ... -- ...
   ...

[continue for each thread]

WIKI UPDATES MADE
- [tenant entity] - logged correspondence about [topic]
- [broker entity] - logged correspondence about [topic]

QUEUED FOR DEDICATED SKILLS
- 2 LoopNet inquiries -- run `lead-parser` on each (paste below)
- 1 maintenance request -- run `maintenance-triage`
```

---

## Tone (drafted replies)

- Akiva's voice -- direct, operator, professional
- Under 100 words per reply
- Specific addresses + dates + numbers
- No filler / corporate language

---

## Read-Only Constraint Reminder

The M365 connector is read-only in v1. This skill drafts replies for Akiva to copy into Outlook and send. It does **not** auto-send, move, or label messages.
