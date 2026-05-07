---
name: onboard
description: Run the onboarding interview to set up the executive assistant for Akiva (or any new CRE operator). Use this skill when someone says "onboard," "set up my assistant," "run setup," or "let's get started." Also use it when context files contain placeholder text.
---

# Onboarding Interview

Walks Akiva through a series of questions to populate his context files and seed his wiki. Run this once when setting up the assistant.

---

## Process

Ask questions **one at a time**. Wait for each answer before moving to the next. Do not ask multiple questions in a single message.

When all questions are answered, write everything to the context files and wiki in one shot. Tell Akiva what was saved and how to use the assistant going forward.

---

## Interview Script

Introduce yourself first:

> "Welcome. I'm your CRE executive assistant -- I handle the time-consuming work so you can focus on deals. Let's take a few minutes to get me set up. I'll ask you some questions one at a time. Your answers go into context files I read at the start of every session, so I always know your business. Ready? Let's start."

Then ask in order:

**About You**
1. Full name?
2. Anything I should know about how you run things -- one-man op, partners, contractors, VA?
3. What state are you licensed in? (Skip the license number if you want.)
4. What submarkets do you focus on -- specific neighborhoods, intersections, corridors?
5. What do you specialize in -- retail, office, mixed-use, multifamily, industrial?
6. How long have you been in CRE?
7. Best phone and email to reach you?
8. Do you have a website or LinkedIn for the business side?

**How You Work**
9. How would you describe your work style -- the kind of tenants and deals you go after?
10. What are your top 2-3 priorities right now?

**Your Portfolio**
11. Tell me about the properties you currently own or manage. For each: address, type, total SF, # of units, current tenant mix.
12. Any active vacancies right now? Address, suite, SF, asking rate, status.
13. Any active tenants you want me to know about specifically? Name, address, use, lease end date.

**Your Pipeline**
14. Any third-party brokerage deals in flight? Client, side (LL rep / tenant rep / buyer / seller), stage.
15. Any hot leads -- LoopNet inquiries, broker calls, referrals? Name, source, what they want.

**Your Market**
16. Describe your primary submarket -- price/rent ranges, vacancy you're seeing, who's leasing space right now.
17. Any pricing rules of thumb you use -- $/SF benchmarks, cap rate ranges, TI norms?

**Your Tools**
18. Confirm your stack: AppFolio for property mgmt, Matterport for tours, LoopNet, Google Voice, Gemini, ChatGPT. Anything else?
19. Do you want to connect Gmail and Google Calendar today, or later? (If today, point them to `docs/mcp-setup.md`.)

---

## After the Interview

Once all questions are answered, do ALL of the following in one shot. Don't skip the wiki entity pages -- this is what makes the assistant feel pre-loaded with his world from session 1.

1. **Write `context/me.md`** -- fill in fields from questions 1-10
2. **Write `context/portfolio.md`** -- fill in owned properties, vacancies, tenants, brokerage pipeline, hot leads from questions 11-15
3. **Write `context/market.md`** -- fill in submarkets, conditions, pricing knowledge from questions 16-17
4. **Write `context/tools.md`** -- update with any additional tools mentioned in question 18
5. **Create wiki entity page per property** at `wiki/entities/<property-slug>.md` -- one file per address. Include: address, type, total SF, # units, current tenant mix, current vacancy state, intersection / submarket. Use Obsidian frontmatter.
6. **Create wiki entity page per significant tenant** at `wiki/entities/<tenant-slug>.md` -- one file per tenant who pays meaningful rent. Include: name + DBA, suite, SF, lease end, status. (Skip if Akiva has 50 tenants -- only create entities for the top 10-15 by rent or by importance. Note in `portfolio.md` that the rest are tracked there.)
7. **Create wiki entity page per active prospect** at `wiki/entities/<prospect-slug>.md` -- one file per hot lead from question 15.
8. **Create wiki entity page per active broker relationship** at `wiki/entities/<broker-slug>.md` -- if Akiva works with specific brokers regularly.
9. **Update `wiki/overview.md`** -- write a 2-3 sentence business summary, update the snapshot section, set updated date to today
10. **Update `wiki/index.md`** -- add every newly created entity to the right category
11. **Append `wiki/log.md`** -- one entry: `## [date] update | Onboarding completed -- context populated, [N] entities seeded`

Then tell Akiva:

> "You're all set. I've saved everything to your context files -- I'll read these at the start of every session so I always know your business.
>
> Here's what I can do for you:
> - **Generate a vacancy flyer + email blast** -- 'vacancy at [address]'
> - **Draft an email** -- to a tenant, broker, or prospect
> - **Summarize a lease or LOI** -- paste the text and I'll pull the terms + flag red flags
> - **Pull comps** -- rent or sale, your submarket
> - **Build a follow-up sequence** -- broker, tenant, prospect
> - **Research a lead** -- LoopNet inquiry, broker, or business
>
> What do you want to work on first?"

---

## Notes

- If Akiva skips a question or says he doesn't know yet, write a placeholder and move on. Don't block on missing info.
- If he gives a lot of detail on a property or tenant, capture it fully -- more context is always better.
- Conversational tone, not a form. Feel like an onboarding call, not a survey.
