# Akiva's Executive Assistant

A Claude Code project built for Akiva Halpern -- commercial real estate operator in Toco Hills / Sandy Springs, Atlanta. Built by [Woodworks Realty Studio](https://woodworksrealtystudio.com).

This is your AI executive assistant. It lives on your machine, it runs on your terms, and you own every file.

---

## What This Is

A Claude Code project folder with:
- **Pre-built skills** for the workflows that eat your time -- vacancy marketing, lease summaries, broker follow-ups, comp analysis, lead research
- **A wiki** -- your second brain. Tenants, brokers, properties, market knowledge -- all in markdown, all yours
- **Context files** Claude reads automatically so it always knows your business
- **Tools** -- live web research and a flyer generator wired in

---

## Day 1 Setup (5 minutes)

**No API keys required.** Works out of the box.

**1. Install Claude Code** if you don't have it:
- [claude.com/code](https://claude.com/code)

**2. Open this folder in your terminal**
```bash
cd ~/akiva-exec-assistant
claude
```

**3. Run the onboarding interview**

Once Claude is open, type:
```
Onboard me.
```

It'll walk you through 10 minutes of questions -- your portfolio, your market, your tools -- and fill in your context files. After that, every session starts with Claude already knowing your business.

**4. (Optional) Connect Gmail and Calendar**

Open Claude Code's **Connectors** panel. Click Connect on Gmail and Google Calendar to authorize with your Google account. That lights up the inbox triage and calendar features. Skip this if you'd rather paste emails in manually for now.

**5. (Optional) Enable vacancy flyer generation**

If you want Claude to generate branded vacancy flyers, install one Python dependency:
```bash
pip3 install Pillow
```
Skip this if you don't plan to use the flyer generator.

---

## Try These First

- `Generate a vacancy flyer for [address] -- [SF] sqft, asking [$rate]/SF NNN`
- `Summarize this lease and pull every key date.` (paste lease text)
- `Draft a follow-up email to the broker who toured 1364 Briar Vista last week.`
- `Research the Toco Hills retail rent market -- what are comparable spaces leasing for?`

---

## Skills

| Skill | What it does | How to trigger |
|---|---|---|
| Onboarding | Interviews you, populates all context files | "Onboard me" |
| Vacancy Marketing | Flyer + segmented email blast for a vacant space | "Vacancy at [address]" |
| Email Draft | Tenant / broker / prospect emails in your voice | "Draft an email to [name]" |
| Contract Summary | Pulls key terms + dates from a lease or purchase agreement | "Summarize this lease" |
| Comp Analysis | Rent comps, sale comps, cap rates, $/SF | "Pull comps for [address]" |
| Market Research | Live web data on any CRE topic | "Research [topic]" |
| Lead Research | Profiles a LoopNet inquiry or broker rep | "Look up [name]" |
| Follow-Up Sequence | 3-touch plan for brokers, tenants, prospects | "Follow up with [name]" |
| Brainstorming | Structured idea exploration before building anything | "Brainstorm with me" |
| Skill Creator | Build a new custom skill for a workflow that keeps repeating | "Build a new skill for X" |

---

## The Wiki

The `wiki/` folder is your second brain. It ships pre-populated with everything Eli captured from the May 1 intro call. Add to it as you go:

- "Add [tenant name] to the wiki"
- "What do we know about [broker name]?"
- "Update the wiki" (after a meeting or showing)

Open `wiki/overview.md` for the high-level view. Open `wiki/index.md` to see everything.

---

## Optional: Connect Gmail, Calendar, and Drive

Claude Code has native connectors. Open the Connectors panel inside Claude Code to authorize Gmail, Google Calendar, and Drive in a few clicks. No API keys, no third-party service.

Once connected, Claude can:
- Triage your inbox
- Draft replies you review before sending
- Pull your calendar context into any conversation
- Suggest meeting times
- Save flyers and reports to a Drive folder

See `docs/mcp-setup.md` for the walkthrough.

---

## Questions?

Built by [Woodworks Realty Studio](https://woodworksrealtystudio.com).

Eli Bock -- eli@woodworksrealtystudio.com
