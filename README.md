# Akiva's Context OS

> **The point:** give attention to every lead that comes in, while still running the property management company. AI in the back, you in the front.

AI executive assistant for Akiva Halpern, Atlanta CRE. Built on the Context OS architecture by [Woodworks Realty Studio](https://woodworksrealtystudio.com). You own this repo. It runs locally inside Claude Code. No vendor lock-in, no API keys.

---

## Install (one paste, then one command)

**1. Install Claude Code** if you don't have it: [claude.com/code](https://claude.com/code)

**2. Open Terminal, paste this single line:**

```bash
git clone https://github.com/woodworksrealtystudio-stack/akiva-exec-assistant.git ~/akiva-context-os && cd ~/akiva-context-os && claude
```

That's it. The repo clones to `~/akiva-context-os`, your terminal moves into the folder, and Claude Code opens with the assistant pre-loaded.

**3. Once Claude opens, paste this prompt:**

```
Onboard me. I'm Akiva.
```

Claude will walk you through 10 minutes of questions about your portfolio, market, and tools, and fill in your context files. Every future session starts with Claude already knowing your business.

---

## What You Get -- 18 Skills, 7 Pain-Point Workflows

**Daily operations**
- **Onboarding** -- 10-min interview that populates every context file + seeds wiki entities for your portfolio
- **Lead parser** -- paste any LoopNet email / Voice transcript / Forms response / broker text -> structured lead, follow-up draft, AppFolio guest card instructions
- **Inbox triage** -- "triage my inbox" -> batch processes Outlook, categorizes, drafts replies
- **Tenant FAQ** -- tenant question comes in -> Claude pulls their actual lease + drafts response
- **Maintenance triage** -- maintenance request -> category, vendor draft, tenant ack, ticket log
- **Tour scheduler** -- reads your calendar, proposes 3 times, drafts confirmation, queues the Outlook event
- **Weekly digest** -- Monday-morning operations brief: vacancies, hot leads, leases expiring, maintenance, top 3 priorities

**Deal & document flow**
- **Vacancy marketing** -- branded flyer (PDF/PNG) + 4 segmented email drafts per vacancy
- **Lease extractor** -- builds your queryable lease database -- "show me every lease expiring in 12 months"
- **Contract summary** -- quick one-off lease / PSA summary
- **Comp analysis** -- rent comps, sale comps, cap rates, $/SF
- **Email drafts** -- general email drafting in your voice
- **Follow-up sequences** -- 3-touch plan for any contact

**Research**
- **Market research** -- live web data on submarkets, comps, news (built-in WebSearch)
- **Lead research** -- profile a person / company before a meeting

**Meta / system**
- **Brainstorming** -- structured exploration before you build anything new
- **Skill creator** -- build a new custom skill when a workflow keeps repeating
- **Using-superpowers** -- the framework that ties it all together

---

## Connectors (5 minutes, optional)

To unlock Outlook + Calendar + OneDrive reading, open Claude Code's **Connectors** panel and click Connect on **Microsoft 365**. OAuth into your Microsoft 365 Business account. Done.

Skip if you'd rather paste content in manually for now.

See `docs/mcp-setup.md` for the full walkthrough + what's coming in v2.

---

## Optional: Vacancy Flyer Generation

If you want Claude to render the actual flyer PDF (not just write the copy), install one Python dependency:

```bash
pip3 install Pillow
```

Skip if you don't plan to use the flyer generator.

---

## What v1 Does NOT Do (Yet)

Claude Code's Microsoft 365 connector is **read-only** in v1. That means:

- Claude **drafts** emails -- you copy them into Outlook and send
- Claude **suggests** calendar times -- you create the events
- Claude **tells** you what AppFolio guest card to create -- you click through

This is intentional. Every outbound communication still gets your eyes on it. AI in the back, human in the front.

**v2 (covered by your monthly retainer)** adds the write side -- send / draft / move email, create calendar events, watch folders for new LoopNet inquiries, auto-import to AppFolio. We add it together once v1 has shaped what you actually need.

---

## The Folder Structure

```
~/akiva-context-os/
├── CLAUDE.md           # Top-level instructions Claude reads at session start
├── INSTALL.md          # The paste-in install instructions (this file's quick version)
├── context/            # Who you are, your portfolio, your market, your tools
├── wiki/               # Persistent second brain -- entities, concepts, sources
├── .claude/skills/     # 11 pre-built skills
├── docs/mcp-setup.md   # Connector walkthrough
├── tools/              # Flyer generator + cheat sheet generator
└── output/             # Generated flyers, summaries, drafts land here
```

Open any file. Edit anything. It's your repo.

---

## Questions

Eli Bock -- eli@woodworksrealtystudio.com -- [Woodworks Realty Studio](https://woodworksrealtystudio.com)
