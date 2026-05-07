---
name: lead-parser
description: Parse a new lead from any source -- LoopNet inquiry email, Microsoft Forms response, Google Voice voicemail/text, broker referral, direct email -- into a structured wiki entry, draft follow-up email, and AppFolio guest card instructions. Use whenever Akiva pastes a lead-source message or forwards an inquiry. Triggers on phrases like "new lead," "LoopNet inquiry," "form submission," "got a voicemail from a prospect," or any pasted lead text.
---

# Lead Parser

The single workflow for turning any inbound lead into a logged, drafted, ready-to-act-on package. Covers pain point #1 (lead consolidation) at v1 read-only level.

---

## Process

1. Read `context/portfolio.md` and the wiki to check for existing entity / duplicate.
2. Extract structured fields from the input (handles LoopNet email format, Microsoft Forms notification email, Google Voice transcript, raw broker text).
3. Check for **duplicate** by phone number first, then by email. Flag if a guest card likely already exists.
4. Create or update the wiki entity at `wiki/entities/<lead-slug>.md`.
5. Append to `context/portfolio.md` Hot Leads table.
6. Draft a follow-up email in Akiva's voice.
7. Output the **AppFolio guest card instructions** -- exact field values to paste / type into AppFolio.
8. Suggest the next action (tour offer, more qualification, broker handoff).

---

## Required Inputs

- The raw lead message (LoopNet email, Forms notification, Voice transcript, broker text -- paste or describe source)
- Property / suite the lead is asking about (if not in the message)

---

## Output Format

```
LEAD CAPTURED
---
Name: [extracted]
Company: [extracted or "Unknown"]
Phone: [extracted]
Email: [extracted]
Source: [LoopNet / Microsoft Forms / Google Voice / Broker / Direct]
Property of interest: [address + suite]
Date received: [date]
Duplicate check: [No prior record / DUPLICATE: existing entity at <slug>]

QUALIFICATION (from message)
- Use case: [retail / office / etc.]
- Stated SF need: [if mentioned]
- Timeline: [if mentioned]
- Anything else they said: [verbatim notes]

WIKI UPDATED
- Entity: wiki/entities/<slug>.md  (created / updated)
- Hot lead added to context/portfolio.md
- Source logged to wiki/sources/<date>-<slug>-<source>.md

DRAFT FOLLOW-UP EMAIL
Subject: [specific]
[2-4 short paragraphs in Akiva's voice -- copy into Outlook + send]

APPFOLIO GUEST CARD -- create with these fields
- First name: [...]
- Last name: [...]
- Phone: [...]
- Email: [...]
- Property: [address]
- Source: [LoopNet / Web Form / Phone / Referral]
- Notes: [one-paragraph summary of what they want]
- Tag: [Hot / Warm / Tire-kicker -- based on qualification]

NEXT ACTION
[Tour offer with 3 times / send tenant questionnaire / hand-off to broker / etc.]
```

---

## Source-Specific Parsing

### LoopNet inquiry email
- Sender format: `LoopNet <inquiries@loopnet.com>`
- Body has structured fields: prospect name, company, phone, email, property, message
- Property URL in body -> infer address from listing

### Microsoft Forms response (notification email)
- Sender: typically `noreply@notify.microsoft.com` or `forms-reply@microsoft.com`
- Body has Q-and-A pairs per form question
- Akiva's form usually asks: company, website, time in business, suite, phone, intended use

### Google Voice transcript
- Forwarded voicemail email or pasted transcript
- Phone number from the metadata
- Caller ID may not be the actual prospect name -- mark as "Unknown -- requested name in follow-up"

### Broker text / referral
- Free-form, no structure
- Extract everything possible, flag whatever is missing

---

## Duplicate Detection

Always check the wiki + `context/portfolio.md` for:
1. Same phone number (primary key)
2. Same email
3. Same company name

If duplicate found:
- DO NOT create a new wiki entity -- update the existing one with the new touchpoint
- Tell Akiva: "DUPLICATE: this prospect already has a record at <path>. Updated with this new inquiry. AppFolio likely has a guest card already -- modify the existing one, don't create a new one."

---

## Tone (the follow-up draft)

- Operator voice -- direct, professional, under 100 words
- Reference the specific property + suite + their stated use
- Offer one clear next step (tour Thursday at 2pm OR send the leasing packet)
- No "thank you for your interest in our property"
- No exclamation points
- Sign off as Akiva
