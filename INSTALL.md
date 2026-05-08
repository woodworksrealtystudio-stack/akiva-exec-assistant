# Install -- Akiva's Context OS

> **The point:** give attention to every lead while still running the company. AI in the back, you in the front.

Two pastes. Five minutes. Done.

---

## Step 1 -- Install Claude Code

If you don't have it: [claude.com/code](https://claude.com/code) -- download and install.

---

## Step 2 -- Paste this in your Terminal

Open Terminal (Applications -> Utilities -> Terminal on Mac), and paste this single line:

```bash
git clone https://github.com/woodworksrealtystudio-stack/akiva-exec-assistant.git ~/akiva-context-os && cd ~/akiva-context-os && claude
```

Press Enter.

What this does:
1. Clones the repo to `~/akiva-context-os` on your Mac
2. Moves your terminal into that folder
3. Opens Claude Code with your assistant pre-loaded

---

## Step 3 -- Paste this in Claude

Once Claude Code opens, paste this prompt:

```
Onboard me. I'm Akiva.
```

Claude will walk you through about 10 minutes of questions and fill in every context file. After that, every session starts with Claude already knowing your business.

---

## Step 4 (optional, 5 minutes) -- Connect Microsoft 365

To let Claude search your Outlook and read your calendar:

1. Open Claude Code's **Connectors** panel (Settings or sidebar)
2. Find **Microsoft 365**
3. Click **Connect**
4. OAuth into your Microsoft 365 Business account
5. Approve the read-only permissions

Done. Claude can now answer "what's on my calendar today" or "show me unread broker emails."

---

## Step 5 (optional) -- Enable Flyer Generation

If you want Claude to render branded vacancy flyers as PDF + PNG:

```bash
pip3 install Pillow
```

Skip if you won't use it.

---

## Day 1 Things to Try

After onboarding, paste any of these:

- `Generate a vacancy flyer for [address] -- [SF], asking [$rate]/SF NNN`
- `Summarize this lease.` (paste lease text)
- `Draft a follow-up email to the broker who toured 1364 Briar Vista last week.`
- `Research the Toco Hills retail rent market -- what are comparable spaces leasing for?`
- `Add the Cohens to the wiki -- they inquired about Suite 200 yesterday.`
- `What's on my calendar this week?` (after M365 connector is set up)

---

## Questions

Eli Bock -- eli@woodworksrealtystudio.com -- [woodworksrealtystudio.com](https://woodworksrealtystudio.com)
