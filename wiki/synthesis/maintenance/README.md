# Maintenance Log

Every maintenance ticket processed through the `maintenance-triage` skill lands here as a structured markdown file.

Filename convention: `YYYY-MM-DD-<property-slug>-<short-desc>.md`

Once populated, query via Claude:
- "What's open maintenance right now?"
- "How many tickets did we close last month?"
- "What does it usually cost when [tenant] reports HVAC?"
- "Which property has the most maintenance tickets this year?"

See `.claude/skills/maintenance-triage/SKILL.md` for the schema.
