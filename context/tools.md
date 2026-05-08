# Tools

Akiva's existing tech stack. Reference this when drafting workflows or recommending automations.

---

## AppFolio
**What it is:** Property management software -- the source of truth for tenants, leases, payments, maintenance.
**Tier:** Basic ($300/mo). Plus tier ($1,300/mo) unlocks the API + AppFolio's own Realm-X AI assistant.
**Note:** Plus has built-in AI / automation (their Realm-X = AI leasing agent inside AppFolio). v1 of this Context OS works without Plus -- manual hand-off for AppFolio writes. v2 decision: stay on Basic + Mailparser workaround, or upgrade to Plus for API.
**Where it fits:** CRM of record. Every lead from any source eventually lands here as a guest card.

---

## Outlook (Microsoft 365)
**What it is:** Akiva's email + calendar of record. **Not** Gmail.
**Connection:** Claude Code's native Microsoft 365 connector -- read-only access to mail + calendar + OneDrive.
**v1 capability:** Search and read inbox + calendar on demand. Draft replies for Akiva to send manually.
**v2 unlock:** Outlook MCP layer for send / reply / move / folder watching.

---

## OneDrive
**What it is:** File storage, all his leases, drawings, financial docs.
**Connection:** Read-only via the Microsoft 365 connector.
**v1:** Claude can find and summarize a lease or document by name on demand.
**v2:** Write back -- save generated flyers, summaries, reports directly to OneDrive folders.

---

## Microsoft Forms
**What it is:** His lead-intake form. Prospects answer the same questions a leasing agent would ask: company, website, time in business, suite, phone.
**Connection:** **Not exposed by Claude Code's M365 connector in v1.**
**v1 workaround:** Akiva pastes form responses (or forwards the notification email) -- Claude logs to wiki and drafts follow-up.
**v2:** Direct Microsoft Graph API or Power Automate bridge to capture form submissions automatically.

---

## LoopNet
**What it is:** "Zillow for commercial." Lead inquiries arrive via email to Akiva's Outlook.
**v1 workflow:** Akiva pastes the LoopNet inquiry email or asks Claude to find recent ones in his inbox -- Claude logs to wiki + drafts response.
**v2:** Outlook folder watcher auto-ingests every LoopNet inquiry into the wiki + (Mailparser route) into a Sheets staging area for weekly AppFolio CSV import.

---

## Google Voice
**What it is:** Inbound call + text channel. Voicemails transcribed in Google Voice.
**v1 workflow:** Akiva forwards voicemails / pastes text threads to Claude. Transcribe skill handles audio if needed. Claude logs to wiki + drafts response.
**v2 / v3:** Direct integration via Twilio port-out + Vapi/Retell for the phone AI Akiva wants (separate scope).

---

## Matterport
**What it is:** AI-powered 3D virtual tours of properties. Central to leasing.
**Where it fits:** Every available space gets a Matterport tour. URL goes in every flyer + listing email.
**v1:** No direct integration; Akiva pastes the Matterport URL into the vacancy-marketing skill input.

---

## Gemini (Google)
**What it is:** Used for AI photo staging / destaging on listing photos.
**Where it fits:** Property photo prep before flyers go out. Outside of this assistant -- Akiva runs Gemini directly.

---

## DocuSign
**What it is:** Contract signing. Migrating into AppFolio over time.
**v1:** Out of scope. v2 maybe.

---

## Microsoft To-Do, Trello
**What it is:** Task tracking, both legacy. Migrating away into AppFolio.
**v1:** Out of scope.

---

## ChatGPT
**What it is:** Akiva's daily driver -- drafting, email replies, lease language, brainstorming, personal growth.
**Where it fits:** Claude Code (this assistant) is the agentic / persistent-context layer. ChatGPT stays useful for ad-hoc consumer-AI questions.

---

## SketchUp
**What it is:** 3D modeling for property redesigns / TI scoping.
**v1:** Out of scope.

---

## Social Media Bot (already running -- don't duplicate)
**What it is:** Akiva already has a bot that automatically posts to his social media accounts.
**v1:** Out of scope. This Context OS does NOT post social. Don't suggest building social posting -- it's already covered.

---

## Future / To-Add Decisions

- **AppFolio Plus upgrade** -- $1,000/mo more for API access + their Realm-X AI. Decide in v2.
- **Mailparser.io** -- $35-100/mo for LoopNet email parsing -> Sheets -> CSV import. v2 alternative if staying on AppFolio Basic.
- **Composio Outlook MCP** -- v2 add-on for Outlook write capability.
- **Vapi or Retell** -- v3 for AI phone screening.
