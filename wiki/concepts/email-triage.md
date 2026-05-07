---
title: Email Triage
type: concept
tags: [pain-point, workflow, executive-assistant, calendar]
created: 2026-05-06
updated: 2026-05-06
sources: 1
---

# Email Triage

Pain point #3. The "light executive assistant layer" -- calendar coverage, inbox triage, draft replies Akiva reviews before sending.

---

## The Problem

A one-man operator gets pulled in too many directions. Most emails are routine: tenant maintenance request, broker tour confirmation, prospect inquiry, vendor quote. Each one is small but they add up to hours per week.

---

## Target End-State

**Inbox triage:**
- Claude reads new emails (via Claude Code's native Gmail connector)
- Categorizes: urgent / response needed / FYI / spam
- For "response needed," drafts a reply Akiva reviews and sends with one click
- Logs substantive threads to the wiki (tenant correspondence under the tenant entity, broker correspondence under broker entity)

**Calendar:**
- Claude has read access to his Google Calendar (via Claude Code's native Calendar connector)
- Knows what's coming up, can answer "what's on my schedule today?"
- When someone proposes a meeting, suggests times that work
- Schedules with confirmation

---

## Build Path

1. **Day 1 / Demo:** Show the pattern with manual paste -- Akiva pastes an email, Claude drafts a response, Akiva sends.
2. **Day 14:** Native Gmail + Calendar connectors enabled in Claude Code. Claude triages real inbox in batches Akiva runs on demand.
3. **Day 30+:** Background triage runs proactively, Akiva gets a morning summary.

---

## What He Doesn't Want

- Auto-send (he reviews before anything goes out)
- Generic AI-sounding replies (must read like him)
- Mass automation that removes the personal touch

---

## Tooling

- `email-draft` skill -- already drafts in Akiva's voice
- `docs/mcp-setup.md` -- Composio Gmail + Calendar setup
- `[[AppFolio]]` -- substantive tenant correspondence eventually mirrors here

---

## Related

- [[Akiva Halpern]]
- [[AppFolio]]
