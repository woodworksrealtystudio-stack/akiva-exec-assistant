# Lease Database

Every lease processed through the `lease-extractor` skill lands here as a structured markdown file.

Filename convention: `<address-slug>-<suite>.md` (e.g., `1364-briar-vista-suite-200.md`)

Once populated, query the database via Claude:
- "Show me every lease expiring in the next 12 months"
- "Which tenants have uncapped personal guaranties"
- "What's our average $/SF NNN across the portfolio"
- "Which leases have free rent burning off this year"

See `.claude/skills/lease-extractor/SKILL.md` for the schema.
