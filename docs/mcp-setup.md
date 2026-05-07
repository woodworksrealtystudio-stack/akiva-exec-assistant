# Connectors -- Microsoft 365 + Google Calendar (Optional)

Claude Code has native connectors that let your assistant **read** your Microsoft 365 data on demand. **No API keys to manage.** This is what lights up "show me unread broker emails" or "what's on my calendar this week."

> **What v1 does:** Reads Outlook / Calendar / OneDrive when you ask. Drafts emails for you to copy and send.
> **What v1 does NOT do:** Auto-send email, watch your inbox, create calendar events. That's v2 (see bottom).

---

## What Each Connector Gives You (v1, read-only)

### Microsoft 365 (recommended -- you live here)
- **Outlook mail:** search and read messages, attachments, threads on demand
- **Outlook calendar:** read upcoming events
- **OneDrive:** read files (leases, financials, drawings)
- **SharePoint:** tenant-wide search if you use it
- **NOT:** Microsoft Forms (form responses are not exposed)

### Google Calendar (optional)
Only if you also use Google Calendar separately. Skip if everything's in Outlook.

---

## How to Connect (5 minutes)

1. Open Claude Code
2. Open the **Connectors** panel (or find it in Settings)
3. Find **Microsoft 365** -> click **Connect**
4. OAuth window opens -> authorize with your Microsoft 365 Business account
5. Grant the consent screen permissions (read-only mail / calendar / files)
6. Done

**Important note on the auth flow:**
- Requires a **Microsoft 365 Business** plan (not personal `@outlook.com`)
- A Global Administrator on your tenant must authorize the connector once before users can connect
- If you're the only admin on your tenant (likely for a one-man op), you authorize yourself

---

## Verify It Works

Ask your assistant:
- "Show me unread emails from last week with 'LoopNet' in the subject."
- "What's on my calendar tomorrow?"
- "Find any OneDrive files mentioning [tenant name] and summarize."

If it returns results, you're connected.

---

## Day-to-Day Workflow (v1)

Because v1 is read-only, the loop is:

1. **You ask** Claude to check your inbox / calendar / files
2. **Claude reads** the relevant items, summarizes, suggests next actions
3. **Claude drafts** any reply, follow-up email, calendar invite, etc.
4. **You copy** the draft into Outlook and send

This is intentional: every outbound communication still gets your eyes on it. **AI in the back, human in the front.** No tenant or broker ever gets an email you didn't approve.

---

## What's Coming in v2 (covered by your monthly retainer)

When you're ready for write-side automation, we add the **Outlook MCP** layer (via Composio or direct Microsoft Graph app registration). That unlocks:

- Send / reply / draft emails directly from the assistant
- Create / update calendar events
- Move and label messages (auto-triage your inbox)
- Watch a folder for new LoopNet inquiries -> auto-process into the wiki + AppFolio
- Microsoft Forms response ingestion (your lead-intake form)

This is a 30-minute add-on we'll do during the retainer phase, once v1 has shaped what you actually need.

---

## What About AppFolio?

AppFolio's basic tier ($300/mo) does **not** expose an API. Two paths:

**Path A -- Stay on Basic tier ($0 extra)**
- Lead consolidation runs through email parsing + weekly CSV import to AppFolio
- Add Mailparser.io (~$35/mo) in v2 to auto-parse LoopNet inquiry emails
- Manual hand-off in v1: Claude tells you what guest card to create, you create it

**Path B -- Upgrade to AppFolio Plus ($1,000/mo more)**
- Real API + webhooks + AppFolio's own Realm-X AI assistant (in-app)
- Clean two-way integration with the Context OS
- Recommended if you want true zero-touch lead consolidation

Decide during the v1 pilot once you see how much daily lead volume actually flows through.

---

## Security

- All OAuth is standard Microsoft / Google -- the assistant never sees your password
- You can revoke any connector instantly from the Connectors panel or your Microsoft / Google account settings
- No data leaves your Claude Code session except what Claude needs to answer your specific question
