---
title: Email Triage
type: concept
tags: [pain-point, workflow, executive-assistant, calendar]
created: 2026-05-06
updated: 2026-05-07
sources: 2
---

# Email Triage

Pain point #3. The "light executive assistant layer" -- inbox triage, calendar awareness, draft replies Akiva reviews before sending.

---

## The Problem

A one-man operator gets pulled in too many directions. Most emails are routine: tenant maintenance request, broker tour confirmation, prospect inquiry, vendor quote. Each one is small but they add up to hours per week.

Akiva lives in **Outlook**, not Gmail. Calendar is also Outlook.

---

## v1 Workflow (Microsoft 365 read-only)

**Inbox triage:**
- Akiva says "triage my inbox" or "show me unread broker emails this week"
- Claude reads via the Microsoft 365 connector, summarizes, categorizes
- For "needs response," Claude drafts a reply Akiva copies into Outlook + sends
- Substantive threads get logged to the wiki under the right entity (tenant, broker)

**Calendar:**
- Claude has read access to Outlook Calendar
- Answers "what's on my schedule today?" / "do I have anything Friday?"
- When someone proposes a meeting, Claude suggests times Akiva offers back manually
- Akiva creates the actual calendar event himself

---

## v2 Workflow (after Outlook MCP add-on, retainer scope)

- Auto-watch a folder for new messages -> proactive morning triage digest
- Claude moves spam / FYI to subfolders directly
- Drafts saved to Outlook Drafts folder (Akiva still reviews + sends)
- Calendar events created directly when Akiva approves a suggested time

---

## What Akiva Doesn't Want

- Auto-send (he reviews before anything goes out -- v1 + v2 both honor this)
- Generic AI-sounding replies (must read like him)
- Mass automation that removes the personal touch with tenants and brokers

---

## Tooling

- `email-draft` skill -- drafts in Akiva's voice
- Microsoft 365 connector -- read-only inbox + calendar + OneDrive
- `docs/mcp-setup.md` -- 5-minute connect walkthrough

---

## Related

- [[Akiva Halpern]]
- [[Outlook]]
- [[AppFolio]]
