---
name: matterport-prep
description: Walk through the Matterport-to-flyer photo prep workflow. Use when Akiva says "Matterport is uploaded," "I have new photos for [property]," "prep the photos for [vacancy]," or before running vacancy-marketing on a new vacancy. Replaces the manual workflow Akiva described on 5/7 -- download photos, set start location, stage with Gemini, then to flyer.
---

# Matterport Photo Prep

The bridge step between "Matterport is done" and "vacancy flyer goes out." Akiva walked through this verbatim on 5/7:

> "As soon as I get an email saying [Matterport is] uploaded, I'll click on it, I'll download the pictures, I'll download the floor plan, I'll set the start location, and then I'll take the pictures and then I want to throw it into the Nano Banana."

(Nano Banana = Google's AI photo staging tool, Gemini-powered.)

This skill turns that 30-minute manual flow into a 5-minute checklist with drafted comms and the right prompts.

---

## Process

1. Confirm the property + suite that just got uploaded.
2. Walk Akiva through the download checklist (Matterport URL, photo download, floor plan PDF download).
3. For each photo, suggest staging direction: which photos to keep raw, which to push through Gemini for staging/destaging, what staging style fits the listing's target tenant.
4. Generate the Gemini prompts for each photo Akiva wants to enhance.
5. Once photos are ready, hand off to `vacancy-marketing` with the assets in place.
6. Log the prep step to the property's wiki entity.

---

## Required Inputs

- Property + suite (or Matterport URL)
- Target tenant profile (retail / office / restaurant / service -- affects staging style)
- Asking rate (affects whether to stage premium or budget-friendly)

---

## Output Format

```
MATTERPORT PREP -- [property] -- [suite]
---
Matterport URL: [paste / TBD]
Vacancy details: [SF, asking rate, target tenant from wiki]

DOWNLOAD CHECKLIST (do these in Matterport)
1. Download all photos (right-click each in the Matterport app -> Save Image)
2. Download the floor plan PDF
3. Set the "start location" inside Matterport (the angle a prospect lands on)
   -- Akiva's preference: usually the front entrance looking into the main space
4. Note the Matterport public-link URL (you'll embed it in the flyer)

PHOTO TRIAGE -- which to use raw vs. stage with Gemini

[For each photo Akiva uploads or describes:]
- Photo 1 (front entrance): KEEP RAW -- shows actual condition
- Photo 2 (main space): STAGE -- target tenant is QSR, suggest restaurant staging
- Photo 3 (back office): DESTAGE -- previous tenant left clutter, remove for clean white-box look
- Photo 4 (storefront): KEEP RAW -- pylon signage is a selling point as-is
- Photo 5 (parking): KEEP RAW

GEMINI PROMPTS (paste into Gemini for each staged photo)
Photo 2 -- "Restage this commercial retail space as a clean modern QSR with neutral
seating, minimal branding, daylight from windows. Keep the existing floor plan and
walls intact. No people."

Photo 3 -- "Remove all furniture, debris, and cardboard boxes from this commercial
space. Show the empty white-box condition with clean walls and floors."

[etc.]

FLYER ASSETS READY (when done)
- 5 photos staged + 1 raw cover
- Floor plan PDF
- Matterport URL
- Asking rate from portfolio.md

NEXT ACTION
Run `vacancy-marketing` with these assets -> generates the flyer + 4 segmented email drafts.

WIKI UPDATE
- wiki/entities/<property>.md: noted "Matterport tour completed [date], assets staged."
```

---

## Staging Style Cheat Sheet

| Target tenant | Style direction |
|---|---|
| QSR / restaurant | Light, clean, daylight, minimal branding, casual seating |
| Service retail (salon, dry cleaner, nail) | Clean white walls, neutral, single counter, organized |
| Office / professional | Sparse, white desks, daylight, no clutter |
| Medical / dental | Sterile feel, clean, white-on-white |
| Specialty retail | Match the brand if known (target tenant has aesthetic) |
| White-box / shell | DESTAGE everything, just empty space |

---

## Why This Skill Exists

Without this, every vacancy starts with a 30-minute manual photo-prep step that Akiva does himself. With it, the photos are ready in 5 minutes and `vacancy-marketing` runs immediately. That's the difference between a same-day flyer and a 3-day delay.
