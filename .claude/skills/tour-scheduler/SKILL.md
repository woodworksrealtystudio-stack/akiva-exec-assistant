---
name: tour-scheduler
description: Schedule a property tour for a qualified prospect. Reads Akiva's Outlook calendar (M365 connector, read-only) to find open windows, drafts the confirmation email with proposed times + Matterport link, and tells Akiva exactly what calendar event to create. Use when Akiva says "schedule a tour for [name]," "set up a showing," or after lead-parser has run on a qualified prospect.
---

# Tour Scheduler

Front-end for the tour-booking workflow. Pulls calendar context, proposes times, drafts the comm, and queues the Outlook event for Akiva to manually create.

---

## Process

1. Identify the prospect (read their wiki entity for context: company, intended use, qualification level).
2. Use the M365 connector to **read** Akiva's Outlook calendar -- find open 60-min windows in the next 7 business days.
3. Avoid early morning (before 9am), late evening (after 5pm), Friday afternoons, and Saturday (Akiva is shomer Shabbos).
4. Propose 3 specific time options.
5. Draft the confirmation email with:
   - Proposed times
   - Property address + suite
   - Matterport link (pull from `wiki/entities/<property>.md` or `context/portfolio.md`)
   - Akiva's contact for day-of
6. Output the **calendar event spec** for Akiva to create in Outlook (because v1 is read-only).
7. Add the prospective tour to `wiki/entities/<prospect-slug>.md` under "Open Items."

---

## Required Inputs

- Prospect name (and a wiki entity should already exist from lead-parser)
- Property + suite

---

## Output Format

```
TOUR SCHEDULING -- [prospect] @ [property suite]
---
Prospect context: [from their wiki entity]
- Company: [...]
- Intended use: [...]
- Qualification level: [Hot / Warm / Tire-kicker]
- Stated SF need: [...]

CALENDAR SCAN (next 7 business days)
- Reviewed Outlook calendar via M365 connector
- Found [N] open 60-min windows that fit the rules

PROPOSED TIMES (in order of preference)
1. [Day, Date, Time] -- [why this slot]
2. [Day, Date, Time]
3. [Day, Date, Time]

DRAFT EMAIL TO PROSPECT
Subject: Tour confirmed -- [property], [suite]

[Greeting using their name]

[2-3 sentences proposing the times. Include Matterport link if available.
Reference what they're touring for -- their stated use.]

[Direct CTA: reply with the time that works.]

[Akiva sign-off]

OUTLOOK CALENDAR EVENT TO CREATE (manually -- v1 read-only)
- Title: Tour -- [prospect] @ [property suite]
- Location: [property address]
- When: [first proposed time -- Akiva picks once they confirm]
- Duration: 60 minutes
- Description: [include Matterport link, prospect phone, their company, what they're looking for]

WIKI UPDATED
- wiki/entities/<prospect>.md -- added "Open: tour proposed for [time options]"

NEXT ACTION
[Akiva sends email + waits for confirm / Akiva proposes alternative if all 3 are no-good]
```

---

## Tone (the email)

- Confident, direct -- proposes a tour as if it's already happening
- Specific times, not "let me know what works" (that creates back-and-forth)
- Always include the Matterport link if available
- Under 100 words
- Sign off as Akiva

---

## Calendar Rules (always apply)

- No tours before 9:00 AM or after 5:00 PM
- No tours Friday after 2:00 PM (Shabbos prep)
- No tours Saturday (Shabbos)
- Holiday awareness if known -- ask Akiva when in doubt
- 60 min default; 90 min if it's a multi-suite tour or anchor space
