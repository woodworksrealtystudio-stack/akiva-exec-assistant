---
title: Google Voice
type: entity
tags: [tool, lead-source, communication]
created: 2026-05-06
updated: 2026-05-06
---

# Google Voice

Akiva's inbound call + text channel. Where the unscheduled lead-flow lives.

---

## What It Is

Google's VoIP service. Inbound calls hit Google Voice; he gets transcribed voicemails + texts in the Google Voice inbox.

---

## How It Fits Into Akiva's Stack

**Lead flow:** Inbound call or text → Google Voice → currently lives only in Google Voice → goal: log substance into [[AppFolio]] + [[portfolio.md]] automatically.

---

## Pain Points

- Voicemail transcripts are siloed in Google Voice, not in any CRM
- Text threads with prospects don't auto-log
- No followup task generation when a new prospect calls
- Easy to lose track of which prospect called about which property

---

## Opportunity

- Use Claude to parse Google Voice transcripts (forward emails or paste) and propose AppFolio entries
- Tie inbound call to property listing if the caller references an address
- Auto-generate a follow-up draft for Akiva to review

---

## Related

- [[Lead Consolidation]] -- framework this feeds into
- [[AppFolio]] -- destination
- [[Akiva Halpern]]
