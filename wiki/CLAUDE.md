# CRE Wiki -- Schema

Akiva's persistent second brain for his commercial real estate operation. Everything worth remembering goes here.

---

## Folder Structure

```
wiki/
├── CLAUDE.md       # This file
├── overview.md     # High-level summary of what the wiki knows
├── index.md        # Catalog of all pages
├── log.md          # Append-only operation log
├── entities/       # People (tenants, brokers, prospects), companies, properties, tools
├── concepts/       # Pain-point frameworks, submarket strategies, deal patterns
├── sources/        # Ingested calls, articles, podcasts -- one summary page per source
└── synthesis/      # Comp reports, deal analyses, answered questions
```

---

## Page Types

**Entity pages (`wiki/entities/`):** One page per tenant, broker, prospect, property, vendor, or tool.
- People: name, contact, relationship, key facts, last interaction, open items
- Properties: address, type, SF, units, current tenants, vacancy state
- Tools: what they do, how they fit into Akiva's stack

**Concept pages (`wiki/concepts/`):** One page per framework, submarket, or recurring pattern.
- What it is, why it matters, current state, target end-state

**Source pages (`wiki/sources/`):** One page per ingested raw input (intro call, market report, podcast).
- Original title and date
- Key takeaways
- What entities and concepts this updated

**Synthesis pages (`wiki/synthesis/`):** Reports and analyses.
- Comp reports, vacancy strategies, broker network maps

---

## Page Frontmatter

Every page gets:

```yaml
---
title: Page Title
type: entity | concept | source | synthesis
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## Cross-Reference Style

Use Obsidian-style wiki links: `[[Page Title]]`
Specific section: `[[Page Title#Section]]`
Display text differs: `[[Page Title|display text]]`

---

## Operations

**Add something:** "Add [person/property/topic] to the wiki."

**Find something:** "What do we know about [name/topic]" -- Claude reads the index and finds it.

**After a meeting/tour:** "Update the wiki" -- Claude asks what happened and updates the right pages.

---

## Log Format

Each entry in `wiki/log.md`:

```
## [YYYY-MM-DD] operation | Description
- What was done
- Pages created or updated
```

Operations: `ingest` | `query` | `update` | `lint`
