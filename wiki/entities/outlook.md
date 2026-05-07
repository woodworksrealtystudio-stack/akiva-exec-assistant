---
title: Outlook
type: entity
tags: [tool, email, microsoft-365]
created: 2026-05-07
updated: 2026-05-07
---

# Outlook (Microsoft 365)

Akiva's email + calendar of record. Lives inside Microsoft 365 Business.

---

## How Akiva Uses It

- Email: every external comm (tenants, brokers, prospects, vendors, attorneys) goes through Outlook
- Calendar: every meeting, tour, deadline
- LoopNet inquiries land in Outlook
- Microsoft Forms responses land as email notifications in Outlook
- Voicemail-to-email forwarding from [[Google Voice]] also lands here

---

## How This Assistant Connects (v1)

Claude Code's native Microsoft 365 connector -- **read-only**.

What v1 can do:
- Search messages by sender / subject / date / content
- Read full message bodies + attachments
- Read calendar events
- Read OneDrive files

What v1 cannot do:
- Send / draft / reply / move / delete email
- Create / update / cancel calendar events
- Write to OneDrive

---

## v2 Add-On (retainer scope)

Add the Outlook MCP layer (Composio or direct Microsoft Graph app registration) to unlock:
- Send / draft / reply / move email
- Create / update calendar events
- Folder watching for auto-triage

See `docs/mcp-setup.md` for current state and the v2 path.

---

## Related

- [[Akiva Halpern]]
- [[Email Triage]]
- [[Lead Consolidation]]
- [[AppFolio]]
