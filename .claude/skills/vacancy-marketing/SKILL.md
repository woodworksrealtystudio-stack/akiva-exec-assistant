---
name: vacancy-marketing
description: Generate a branded vacancy flyer and segmented email blast when a commercial space becomes available. Use this skill whenever Akiva says "vacancy at [address]," "space available," "new listing," "make a flyer," or asks for marketing on a vacant suite.
---

# Vacancy Marketing

When a space goes vacant, this skill produces two things:
1. A branded one-page vacancy flyer (PDF + PNG)
2. A segmented email blast to the right list (tenants, brokers, retailers, prospects)

This is the production pipeline for pain point #2 -- vacancy marketing automation.

---

## Process

1. Read `context/portfolio.md` for the property + suite context.
2. Ask for any missing details (see Required Inputs below).
3. Write the flyer content to `output/flyer.json`.
4. Run the flyer generator: `python3 tools/generate-flyer.py output/flyer.json`
5. Draft the email blast (one version per audience segment).
6. Log the vacancy push to `wiki/log.md`.

---

## Required Inputs

- Property address + suite #
- Total SF (and divisible if applicable)
- Asking rate ($/SF NNN, modified gross, or FSG)
- Use type (retail, office, restaurant, mixed-use, etc.)
- Available date
- Key features (frontage, parking, signage, traffic count, anchor co-tenants, build-out condition, demising state)
- Target tenant profile (1-2 sentences)
- Matterport link (if available)
- Photos (in `brand-assets/` or referenced)

---

## Flyer JSON Structure

Write to `output/flyer.json`:

```json
{
  "property_slug": "1364-briar-vista-suite-200",
  "headline": "2,400 SF Retail Available",
  "address": "1364 Briar Vista Way, Suite 200",
  "submarket": "Toco Hills, Atlanta",
  "asking_rate": "$28/SF NNN",
  "available": "Immediate",
  "highlights": [
    "End-cap with full glass frontage",
    "Pylon signage included",
    "32 parking spaces",
    "Co-tenants: [list]",
    "Traffic count: [X] VPD"
  ],
  "use_types": ["Retail", "Quick-service restaurant", "Service"],
  "matterport_url": "https://my.matterport.com/...",
  "contact": {
    "name": "Akiva Halpern",
    "email": "[email]",
    "phone": "[phone]"
  }
}
```

Then run:
```bash
python3 tools/generate-flyer.py output/flyer.json
```

The generator outputs `output/flyer.pdf` and `output/flyer.png`.

---

## Email Blast -- Segmented

Draft one tailored version per segment. Each version reuses the same flyer attachment but leads with what that audience cares about.

### Segment 1 -- Brokers
- Lead: address, SF, rate, commission terms
- Body: 2-3 lines on highlights, Matterport link, asking they share with active tenant reps
- CTA: "Tour available -- DM me a time"

### Segment 2 -- Existing tenants (in nearby owned properties)
- Lead: "Space coming available next door / in the area"
- Body: relevant for expansion or referral to their network
- CTA: "Reply if you know someone"

### Segment 3 -- Retailers / direct prospects
- Lead: lifestyle / location pitch ("[neighborhood] foot traffic, anchor co-tenants")
- Body: highlights + Matterport
- CTA: "Tour Thursday / let me know what works"

### Segment 4 -- General prospect list (broad)
- Lead: SF + use + rate
- Body: short -- one paragraph, link to flyer + Matterport
- CTA: "Reply for a tour"

---

## Tone (every audience)

- Operator voice -- not marketing-speak
- Specifics over adjectives -- never "stunning" or "prime location"
- Lead with the numbers brokers and prospects scan for: SF, rate, frontage, parking
- Matterport link in every email
- "AI should be invisible" -- never sound like AI wrote it
