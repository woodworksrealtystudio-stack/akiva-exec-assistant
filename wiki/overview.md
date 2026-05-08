---
title: Overview
type: overview
updated: 2026-05-06
sources: 1
---

# Overview

> **The point of Akiva's Context OS:** give attention to every lead that comes in, while still running the property management company. AI in the back, Akiva in the front.

_High-level synthesis of what the wiki knows. Read this first, then navigate via [[index]] for specifics._

---

## Business Summary

[[Akiva Halpern]] runs a one-man commercial real estate operation out of Toco Hills (Atlanta). He owns and manages his own portfolio of commercial properties and recently got licensed to broker third-party CRE deals on top of that.

He's a heavy ChatGPT user, comfortable with AI in general but new to agentic systems. The point of this assistant: give him an "AI manager" he can run himself, before he ever hires a human VA or leasing agent. Once the system matures, the human hire plugs in on top of it.

---

## Three Pain Points (Pre-Mapped)

1. **[[Lead Consolidation]]** -- Inbound from [[LoopNet]] (Outlook), [[Google Voice]] (calls + texts), and Microsoft Forms all need to land in [[AppFolio]] as the CRM of record. v1 = paste-in workflow + draft follow-ups + AppFolio guest-card instructions. v2 = auto-ingest via Outlook MCP.
2. **[[Vacancy Marketing]]** -- When a space goes vacant: branded flyer + segmented email blast drafts (tenants, brokers, retailers, prospects). Working in v1.
3. **[[Email Triage]]** -- Inbox triage + calendar awareness. v1 = read-only via Microsoft 365 connector. v2 = write side via Outlook MCP.

---

## Tools Stack

- **[[Outlook]]** (Microsoft 365) -- email + calendar of record. Connected v1 via Claude Code's M365 connector (read-only).
- **[[AppFolio]]** -- property management, target CRM of record. Basic tier ($300/mo); Plus tier ($1,300/mo) is v2 decision.
- **OneDrive** -- files. Read-only via M365 connector.
- **Microsoft Forms** -- lead intake form (responses come into Outlook as email).
- **[[LoopNet]]** -- commercial lead source (inquiries arrive via Outlook).
- **[[Google Voice]]** -- inbound calls + texts.
- **[[Matterport]]** -- 3D virtual tours, central to leasing process.
- **Gemini** -- AI photo staging / destaging.
- **ChatGPT** -- daily driver for drafting, lease language, brainstorming.
- **Claude Code** (this) -- the persistent agentic + context layer.

---

## Market

- Primary submarket: Toco Hills, Atlanta (retail-heavy, dense Jewish community, walking-distance demand drivers)
- Secondary: Sandy Springs and surrounding Atlanta CRE
- Specialization expanding from owned-portfolio management into third-party brokerage

---

## Key Relationships

- **[[Eli Bock]]** ([[Woodworks Realty Studio]]) -- built this assistant, primary point of contact for the system

_Tenants, brokers, prospects appear here as Akiva adds them via "add [name] to the wiki."_

---

## Wiki Health

- Pages: 12 (seeded from intro call)
- Last updated: 2026-05-06
- Next action: walk through demo, add live tenants + active vacancies during onboarding interview
