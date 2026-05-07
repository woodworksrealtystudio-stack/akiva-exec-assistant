# MCP Setup -- Gmail and Google Calendar

Connect Claude to your Gmail and Google Calendar so it can triage your inbox, draft replies, and pull calendar context into any conversation. This is what lights up [[Email Triage]] (pain point #3).

---

## What This Unlocks

- Read your inbox and triage threads (urgent / response needed / FYI)
- Draft replies you review before sending
- Read your calendar and answer "what's on my schedule today?"
- Suggest meeting times when someone proposes one
- Save substantive threads to the wiki under the right entity

---

## Setup (Composio)

This setup uses Composio to connect your Google account to Claude Code.

**Step 1: Create a Composio account**

Go to composio.dev and sign up for a free account.

**Step 2: Connect Google**

In the Composio dashboard:
1. Go to "Apps" in the left sidebar
2. Search for "Gmail" and click "Connect"
3. Authorize with your Google account
4. Repeat for "Google Calendar"

**Step 3: Get your API key**

In Composio, go to Settings > API Keys and copy your key.

**Step 4: Add to your .env file**

Create a file called `.env` in this project folder:

```
COMPOSIO_API_KEY=your_key_here
PERPLEXITY_API_KEY=your_perplexity_key_here
```

(Perplexity key is for `tools/research.py` -- get one free at perplexity.ai/settings/api.)

**Step 5: Add Composio MCP to Claude Code**

Add this to your Claude Code settings (or run via Claude Code settings UI):

```json
{
  "mcpServers": {
    "composio": {
      "command": "npx",
      "args": ["-y", "composio-core", "mcp", "--api-key", "your_key_here"]
    }
  }
}
```

**Step 6: Restart Claude Code**

Close and reopen Claude Code. It will now have access to Gmail and Calendar tools.

---

## Verify It Works

Ask Claude:
- "Check my Gmail for any unread messages from brokers."
- "What's on my calendar today?"

If it returns results, you're connected. If not, double-check your API key and restart Claude Code.

---

## Security Note

Your Google account access stays within Composio's OAuth flow -- Claude never sees your password. You can revoke access at any time from your Google account security settings.

---

## Future: AppFolio

When AppFolio exposes a public API (or via a Zapier / make.com bridge), we'll add a similar MCP layer so leads can flow LoopNet → Claude → AppFolio automatically. See [[Lead Consolidation]] in the wiki for the build path.
