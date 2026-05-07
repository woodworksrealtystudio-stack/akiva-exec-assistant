# Tools

Akiva's existing tech stack. Reference this when drafting workflows or recommending automations.

---

## AppFolio
**What it is:** Property management software -- the source of truth for tenants, leases, payments, maintenance.
**Tier:** [current tier -- update during onboarding]
**Note:** Upper tier has built-in AI / automation, but the goal is to layer Claude on top so the workflows stay open and tweakable, not locked in vendor UI.
**Where it fits:** CRM of record. Everything from leads on through to active tenants should land here.

---

## LoopNet
**What it is:** "Zillow for commercial" -- Akiva gets lead emails when a prospect inquires about one of his listings.
**Pain point:** Inquiries arrive in email, not in AppFolio. Goal: parse LoopNet emails → log in AppFolio + portfolio.md.

---

## Google Voice
**What it is:** Inbound call + text channel.
**Pain point:** Voicemails + texts don't auto-log anywhere. Goal: transcribe voicemails, capture text threads, log in AppFolio + portfolio.md.

---

## Matterport
**What it is:** AI-powered 3D virtual tours of properties. Central to Akiva's leasing process.
**Where it fits:** Every available space gets a Matterport. Link is included in every flyer + listing email.

---

## Gemini (Google)
**What it is:** Used for AI photo staging / destaging on listing photos.
**Where it fits:** Property photo prep before flyers go out.

---

## ChatGPT
**What it is:** Akiva's daily driver -- drafting, email replies, lease language, brainstorming, personal growth.
**Where it fits:** Claude Code (this assistant) is the agentic layer on top of where ChatGPT sits today.

---

## Email
**Pain point:** Multiple lead sources land in email. Goal: triage in inbox, draft replies, log substance in AppFolio.

---

## Future / To-Add

- CRM: AppFolio (already in place)
- Calendar: Google Calendar -- connect via Claude Code Connectors (see `docs/mcp-setup.md`)
- Email: Gmail -- connect via Claude Code Connectors
