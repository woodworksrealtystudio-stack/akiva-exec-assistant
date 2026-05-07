---
title: Vacancy Marketing
type: concept
tags: [pain-point, workflow, marketing, leasing]
created: 2026-05-06
updated: 2026-05-06
sources: 1
---

# Vacancy Marketing

Pain point #2. From the [[2026-05-01 Intro Call]]: "When a space becomes available, I need to create a new flyer, and then I need to send that flyer to my email list of tenants, brokers, retailers, people who are looking for space."

---

## The Problem

When a vacancy occurs, Akiva manually:
1. Creates a one-page flyer (graphics, copy, photos, Matterport link)
2. Pulls together a recipient list (tenants, brokers, retailers, prospects)
3. Drafts an email per audience segment (or sends one generic email and loses precision)
4. Sends, tracks responses, follows up

The whole workflow currently lives in his head + email + design tools.

---

## Target End-State

When a space goes vacant, Akiva tells Claude:
> "Vacancy at [address] -- [SF], [asking rate], [available date]. Run vacancy marketing."

Claude:
1. Reads the property entity from the wiki for full context
2. Generates a branded flyer (PDF + PNG) via `tools/generate-flyer.py`
3. Drafts 4 email versions (brokers / existing tenants / retailers / general prospects)
4. Suggests recipient list from the wiki + existing tenant database
5. Logs the vacancy push to the wiki

Akiva reviews each draft and sends.

---

## Audience Segments

| Segment | What they care about | CTA |
|---|---|---|
| Brokers | SF, rate, commission, neighbors | "Tour available -- DM me a time" |
| Existing tenants in nearby owned properties | Expansion, referral | "Reply if you know someone" |
| Retailers / direct prospects | Foot traffic, anchor co-tenants, lifestyle pitch | "Tour Thursday / let me know" |
| General prospect list | SF + use + rate, brief | "Reply for a tour" |

---

## Tone Rules (every audience)

- Operator voice -- not marketing-speak
- Specifics over adjectives -- never "stunning" or "prime location"
- Lead with numbers brokers and prospects scan for: SF, rate, frontage, parking
- [[Matterport]] link in every email
- "AI should be invisible"

---

## Tooling

- `[vacancy-marketing](.claude/skills/vacancy-marketing/SKILL.md)` skill
- `tools/generate-flyer.py` -- HTML / PIL one-page flyer renderer
- `[[Matterport]]` -- virtual tour link, included in every flyer

---

## Related

- [[Akiva Halpern]]
- [[Matterport]]
