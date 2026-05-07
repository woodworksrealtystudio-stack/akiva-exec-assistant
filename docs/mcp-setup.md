# Connectors -- Gmail, Google Calendar, Drive

Claude Code has native connectors for Google Workspace, GitHub, and other services. Use those instead of wiring up third-party MCP layers. **No API keys to manage.**

This is what lights up [[Email Triage]] (pain point #3) and gives Claude visibility into your calendar.

---

## What You Can Connect

Inside Claude Code, you can connect any of these natively:

- **Gmail** -- read, draft, send, label
- **Google Calendar** -- read events, create events, suggest times
- **Google Drive** -- read and write docs, sheets, folders
- **GitHub** -- only relevant if you're managing other repos

You pick what you want. None of them are required to use this assistant -- the assistant works fully offline against your local files. Connectors just expand what it can reach.

---

## How to Connect (Claude Code)

1. Open Claude Code
2. Open the **Connectors** panel (or run `/connectors`)
3. Pick the service you want -- start with Gmail and Google Calendar
4. Click "Connect" -- Claude opens a Google OAuth window
5. Authorize with your Google account
6. Done -- Claude can now use that service in any session

Repeat for any other service you want to add. You can revoke any connector at any time.

---

## Recommended for Akiva (in order)

**Start with these two:**
- **Gmail** -- so Claude can triage your inbox and draft replies you review
- **Google Calendar** -- so Claude knows what's on your schedule and can suggest meeting times

**Add later if useful:**
- **Google Drive** -- if you want Claude to save vacancy flyers, deal summaries, or comp reports straight to a Drive folder

---

## Verify It Works

Once connected, ask Claude:
- "Check my Gmail for any unread broker emails."
- "What's on my calendar tomorrow?"

If it returns results, you're connected. If not, re-open the Connectors panel and reconnect.

---

## Security

- All OAuth happens through Google's standard flow -- Claude never sees your password
- You can revoke any connector instantly from the Connectors panel or from your Google account settings
- Substantive email or calendar threads can be mirrored into your wiki (under the right entity page) if you ask Claude to

---

## What About AppFolio?

AppFolio doesn't have a native Claude Code connector yet. For now:
- Forward LoopNet inquiry emails into Claude (paste or via Gmail connector once it's set up)
- Claude logs the lead to `[[portfolio.md]]` and the wiki, drafts a follow-up
- You manually copy the substance into AppFolio at end-of-day

When AppFolio exposes a public API (or via a simple bridge), we'll add it. See [[Lead Consolidation]] in the wiki for the build path.
