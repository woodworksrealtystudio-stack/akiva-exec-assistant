---
name: weekly-digest
description: Generate a Monday-morning operations digest -- open vacancies, leads needing follow-up, leases expiring soon, maintenance tickets open, calendar week ahead, prioritized action list. Use when Akiva says "weekly digest," "Monday brief," "what's the week look like," or any morning-routine kickoff phrase.
---

# Weekly Digest

The Monday-morning command center brief. Pulls everything from the wiki + Outlook calendar (M365 read) into a one-page operations summary so Akiva starts the week knowing exactly what to focus on.

---

## Process

1. Read the wiki:
   - `context/portfolio.md` -- active vacancies, hot leads
   - `wiki/synthesis/leases/*.md` -- find any expiring in the next 90 days
   - `wiki/synthesis/maintenance/*.md` -- any open tickets
   - `wiki/entities/*.md` -- any prospect with "Open Items" or last-touched > 7 days
2. Read the Outlook calendar via M365 connector for the upcoming week.
3. Pull recent activity from `wiki/log.md` (last 7 days).
4. Synthesize into the digest format below.
5. Identify the top 3 priorities for the week.

---

## Output Format

```
WEEKLY DIGEST -- Week of [Monday date]
================================================

CALENDAR
- [Day]: [event title @ time -- 1-line note]
- [Day]: ...
- [Conflicts / busy days flagged]

VACANCIES
- [address suite]: [SF] @ $[X]/SF -- [days vacant] -- [N] active prospects
- [address suite]: ...

HOT LEADS NEEDING TOUCH
- [name @ company]: last contact [date] -- [next action]
- [name @ company]: ...

LEASES EXPIRING (next 90 days)
- [tenant @ property]: expires [date] -- [N] days out -- [renewal status]
- [tenant @ property]: ...

OPEN MAINTENANCE
- [property -- issue]: opened [date] -- [vendor status]
- [property -- issue]: ...

LAST WEEK'S ACTIVITY (from wiki log)
- [date]: [what happened]
- [date]: ...

TOP 3 PRIORITIES THIS WEEK
1. [most leveraged action -- usually a vacancy with hot leads]
2. [renewal conversation that has to happen]
3. [the thing that, if you don't do it, becomes a problem]

================================================
```

---

## Tone

- Operator brief -- numbers, addresses, names, dates
- No corporate filler
- Top 3 priorities should be concrete actions (call X, send Y, decide Z), not generic ("focus on leasing")
- Surface what's URGENT and what's IMPORTANT separately if it matters
- Flag anything that looks like it's been sitting too long without action

---

## Cadence

- Run Mondays as the week-start brief
- Akiva can also ask "mid-week digest" Wednesday or Friday EOD digest if useful
- Eventually (v2) this can be auto-generated and emailed to him via Outlook MCP every Monday at 7am
