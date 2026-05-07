#!/usr/bin/env python3
"""
SOW + Price Card -- two-page Woodworks-branded PDF for Akiva.

Page 1: Scope (v1 / v2 / v3) and pricing
Page 2: Install instructions

Usage:
  python3 tools/generate-sow.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT  = Path(__file__).resolve().parents[1]
FONTS_DIR  = REPO_ROOT / "brand-assets" / "fonts"
OUTPUT_DIR = REPO_ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# US Letter at 200 DPI
W, H   = 1700, 2200
MARGIN = 110
TEXT_W = W - 2 * MARGIN

CREAM    = (250, 244, 238)
NAVY     = (28, 43, 74)
ACCENT   = (139, 105, 20)
CHARCOAL = (32, 32, 32)
SLATE    = (107, 114, 128)
BORDER   = (210, 200, 185)


def font(name, size):
    return ImageFont.truetype(str(FONTS_DIR / name), size)


def F_HL(s):    return font("CormorantGaramond-Bold.ttf", s)
def F_SEMI(s):  return font("CormorantGaramond-SemiBold.ttf", s)
def F_SECT(s):  return font("DMSans-Medium.ttf", s)
def F_BODY(s):  return font("DMSans-Regular.ttf", s)
def F_LIGHT(s): return font("DMSans-Light.ttf", s)


def measure(fnt, txt):
    bb = fnt.getbbox(txt)
    return bb[2] - bb[0], bb[3] - bb[1]


def wrap(text, fnt, max_w):
    words, lines, cur = text.split(), [], []
    for w in words:
        trial = " ".join(cur + [w])
        if measure(fnt, trial)[0] <= max_w or not cur:
            cur.append(w)
        else:
            lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    return lines


def chrome(draw):
    draw.rectangle([(0, 0), (W, 8)], fill=NAVY)
    draw.rectangle([(0, 8), (W, 12)], fill=ACCENT)
    draw.rectangle([(0, H - 12), (W, H - 8)], fill=ACCENT)
    draw.rectangle([(0, H - 8), (W, H)], fill=NAVY)


def render_page1():
    img  = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)
    chrome(draw)

    y = 110

    # Eyebrow
    eb = "WOODWORKS REALTY STUDIO  ·  STATEMENT OF WORK"
    draw.text((MARGIN, y), eb, font=F_SECT(28), fill=ACCENT)
    y += 50

    # Title
    title = "Akiva's Context OS"
    draw.text((MARGIN, y), title, font=F_HL(140), fill=NAVY)
    y += 162

    # Subtitle
    draw.rectangle([(MARGIN, y), (MARGIN + 110, y + 6)], fill=ACCENT)
    y += 32
    draw.text((MARGIN, y), "AI executive assistant for one-man CRE -- 30-day pilot.", font=F_BODY(34), fill=CHARCOAL)
    y += 60
    draw.text((MARGIN, y), "Built by Woodworks Realty Studio. You own the repo.", font=F_BODY(28), fill=SLATE)
    y += 60

    # Pricing block
    pbox_top = y
    draw.rectangle([(MARGIN, pbox_top), (W - MARGIN, pbox_top + 300)], outline=BORDER, width=2)

    # Setup column
    col1_x = MARGIN + 36
    draw.text((col1_x, pbox_top + 32), "SETUP", font=F_SECT(26), fill=ACCENT)
    draw.text((col1_x, pbox_top + 72), "$1,500", font=F_HL(108), fill=NAVY)
    draw.text((col1_x, pbox_top + 200), "One-time. Repo handed off,", font=F_BODY(24), fill=CHARCOAL)
    draw.text((col1_x, pbox_top + 232), "context populated, you're", font=F_BODY(24), fill=CHARCOAL)
    draw.text((col1_x, pbox_top + 262), "running the system.", font=F_BODY(24), fill=CHARCOAL)

    # Retainer column
    col2_x = MARGIN + (TEXT_W // 2) + 36
    draw.text((col2_x, pbox_top + 32), "MONTHLY RETAINER", font=F_SECT(26), fill=ACCENT)
    draw.text((col2_x, pbox_top + 72), "$200", font=F_HL(108), fill=NAVY)
    draw.text((col2_x, pbox_top + 200), "Per month. Tweaks, new skills,", font=F_BODY(24), fill=CHARCOAL)
    draw.text((col2_x, pbox_top + 232), "v2 build-outs, monthly check-in.", font=F_BODY(24), fill=CHARCOAL)
    draw.text((col2_x, pbox_top + 262), "Cancel anytime.", font=F_BODY(24), fill=CHARCOAL)

    y = pbox_top + 340

    # v1 scope
    draw.text((MARGIN, y), "WHAT v1 SHIPS NOW (covered by setup)", font=F_SECT(28), fill=ACCENT)
    y += 14
    draw.rectangle([(MARGIN, y + 18), (MARGIN + 80, y + 21)], fill=ACCENT)
    y += 46

    v1_items = [
        ("Onboarding", "10-min Q&A -- context files filled + wiki entities seeded for your portfolio"),
        ("Lead parser", "Paste any lead source -- structured + drafted reply + AppFolio guest-card instructions"),
        ("Inbox triage", "Batch-read Outlook (M365 connector) -- categorize + draft replies"),
        ("Tenant FAQ", "Pulls actual lease terms + drafts tenant-facing response"),
        ("Maintenance triage", "Categorize + draft vendor RFQ + tenant ack + log to maintenance database"),
        ("Tour scheduler", "Reads your Outlook calendar, proposes 3 times, drafts confirmation"),
        ("Weekly digest", "Monday brief: vacancies + hot leads + leases expiring + top 3 priorities"),
        ("Vacancy marketing", "Branded flyer (PDF + PNG) + 4 segmented email drafts per vacancy"),
        ("Lease database", "Every lease processed lands as queryable entry in wiki"),
        ("Comp analysis", "Rent comps, sale comps, cap rates, $/SF"),
        ("Market + lead research", "Live web search + prospect profiling (built-in WebSearch)"),
        ("Wiki second brain", "Tenants, brokers, properties, deals -- compounds over time"),
        ("Custom skill creation", "Spot a workflow, build a skill for it -- you own every skill"),
    ]

    body_fnt = F_BODY(24)
    light_fnt = F_LIGHT(22)
    name_fnt = F_SEMI(34)
    for name, desc in v1_items:
        draw.text((MARGIN + 4, y), "·", font=F_BODY(28), fill=ACCENT)
        draw.text((MARGIN + 28, y - 4), name, font=name_fnt, fill=NAVY)
        nw, _ = measure(name_fnt, name)
        draw.text((MARGIN + 36 + nw, y + 4), "-- " + desc, font=light_fnt, fill=CHARCOAL)
        y += 42

    y += 16

    # v2 / v3
    draw.text((MARGIN, y), "WHAT THE RETAINER UNLOCKS (v2 add-ons, when ready)", font=F_SECT(28), fill=ACCENT)
    y += 14
    draw.rectangle([(MARGIN, y + 18), (MARGIN + 80, y + 21)], fill=ACCENT)
    y += 46

    v2_items = [
        "Outlook write side -- send / draft / move email, create calendar events",
        "LoopNet inbox auto-ingest -- new inquiries land in the wiki + AppFolio queue automatically",
        "AppFolio integration -- Plus tier API ($1,000/mo direct to AppFolio) OR Mailparser + CSV path",
        "Microsoft Forms response auto-capture",
        "v3 future: AI phone screening (Vapi/Retell), corporate management business expansion",
    ]
    for item in v2_items:
        draw.text((MARGIN + 4, y), "·", font=F_BODY(28), fill=SLATE)
        for ln in wrap(item, body_fnt, TEXT_W - 32):
            draw.text((MARGIN + 28, y + 2), ln, font=body_fnt, fill=CHARCOAL)
            y += 36
        y += 4

    # Footer
    foot = "Woodworks Realty Studio  ·  Eli Bock  ·  eli@woodworksrealtystudio.com  ·  woodworksrealtystudio.com"
    fw, _ = measure(F_LIGHT(20), foot)
    draw.text(((W - fw) // 2, H - 60), foot, font=F_LIGHT(20), fill=SLATE)
    draw.text((W - MARGIN - 80, 28), "Page 1 / 2", font=F_LIGHT(20), fill=SLATE)

    return img


def render_page2():
    img  = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)
    chrome(draw)

    y = 110

    eb = "WOODWORKS REALTY STUDIO  ·  INSTALL"
    draw.text((MARGIN, y), eb, font=F_SECT(28), fill=ACCENT)
    y += 50

    title = "Get Set Up"
    draw.text((MARGIN, y), title, font=F_HL(140), fill=NAVY)
    y += 162

    draw.rectangle([(MARGIN, y), (MARGIN + 110, y + 6)], fill=ACCENT)
    y += 32

    intro = "Two pastes. Five minutes. Done."
    draw.text((MARGIN, y), intro, font=F_BODY(34), fill=CHARCOAL)
    y += 80

    # Step 1
    draw.text((MARGIN, y), "1.  INSTALL CLAUDE CODE", font=F_SECT(28), fill=ACCENT)
    y += 50
    draw.text((MARGIN, y), "Download from claude.com/code if you don't have it.", font=F_BODY(28), fill=CHARCOAL)
    y += 80

    # Step 2
    draw.text((MARGIN, y), "2.  PASTE THIS IN TERMINAL", font=F_SECT(28), fill=ACCENT)
    y += 50

    cmd_box_top = y
    draw.rectangle([(MARGIN, cmd_box_top), (W - MARGIN, cmd_box_top + 90)], outline=BORDER, width=2, fill=(244, 240, 232))
    cmd = "git clone https://github.com/woodworksrealtystudio-stack/akiva-exec-assistant.git ~/akiva-context-os && cd ~/akiva-context-os && claude"
    cmd_fnt = F_BODY(22)
    cy = cmd_box_top + 28
    for ln in wrap(cmd, cmd_fnt, TEXT_W - 60):
        draw.text((MARGIN + 30, cy), ln, font=cmd_fnt, fill=NAVY)
        cy += 32
    y = cmd_box_top + 130

    # Step 3
    draw.text((MARGIN, y), "3.  PASTE THIS IN CLAUDE", font=F_SECT(28), fill=ACCENT)
    y += 50
    p_box_top = y
    draw.rectangle([(MARGIN, p_box_top), (W - MARGIN, p_box_top + 70)], outline=BORDER, width=2, fill=(244, 240, 232))
    draw.text((MARGIN + 30, p_box_top + 22), "Onboard me. I'm Akiva.", font=F_BODY(26), fill=NAVY)
    y = p_box_top + 110

    # What happens next
    draw.text((MARGIN, y), "WHAT HAPPENS NEXT", font=F_SECT(28), fill=ACCENT)
    y += 14
    draw.rectangle([(MARGIN, y + 18), (MARGIN + 80, y + 21)], fill=ACCENT)
    y += 46

    next_items = [
        "Claude walks you through 10 minutes of questions -- portfolio, market, tools, priorities.",
        "Every context file is filled in. The wiki seeds with your portfolio and your three pain points.",
        "From there, every session starts with Claude already knowing your business.",
    ]
    for item in next_items:
        draw.text((MARGIN + 4, y), "·", font=F_BODY(28), fill=ACCENT)
        for ln in wrap(item, F_BODY(26), TEXT_W - 32):
            draw.text((MARGIN + 28, y), ln, font=F_BODY(26), fill=CHARCOAL)
            y += 38
        y += 8

    y += 16

    # Optional: connect Microsoft 365
    draw.text((MARGIN, y), "OPTIONAL -- CONNECT MICROSOFT 365 (5 minutes)", font=F_SECT(28), fill=ACCENT)
    y += 14
    draw.rectangle([(MARGIN, y + 18), (MARGIN + 80, y + 21)], fill=ACCENT)
    y += 46

    m365_lines = [
        "Open Claude Code's Connectors panel.",
        "Click Connect on Microsoft 365.",
        "OAuth into your business account, approve read-only permissions.",
        "Done -- ask Claude 'what's on my calendar' or 'show me unread broker emails.'",
    ]
    for item in m365_lines:
        draw.text((MARGIN + 4, y), "·", font=F_BODY(26), fill=SLATE)
        draw.text((MARGIN + 28, y - 2), item, font=F_BODY(26), fill=CHARCOAL)
        y += 40

    y += 24

    # Try these first
    draw.text((MARGIN, y), "TRY THESE FIRST", font=F_SECT(28), fill=ACCENT)
    y += 14
    draw.rectangle([(MARGIN, y + 18), (MARGIN + 80, y + 21)], fill=ACCENT)
    y += 46

    examples = [
        "\"Generate a vacancy flyer for [address] -- [SF], asking [$rate]/SF NNN.\"",
        "\"Summarize this lease and pull every key date.\"",
        "\"Draft a follow-up email to the broker who toured 1364 Briar Vista last week.\"",
        "\"Research the Toco Hills retail rent market.\"",
    ]
    for ex in examples:
        draw.text((MARGIN + 4, y), "·", font=F_BODY(26), fill=ACCENT)
        for ln in wrap(ex, F_BODY(24), TEXT_W - 32):
            draw.text((MARGIN + 28, y), ln, font=F_BODY(24), fill=CHARCOAL)
            y += 34
        y += 6

    # Footer
    foot = "Eli Bock  ·  eli@woodworksrealtystudio.com  ·  woodworksrealtystudio.com"
    fw, _ = measure(F_LIGHT(20), foot)
    draw.text(((W - fw) // 2, H - 60), foot, font=F_LIGHT(20), fill=SLATE)
    draw.text((W - MARGIN - 80, 28), "Page 2 / 2", font=F_LIGHT(20), fill=SLATE)

    return img


def render():
    p1 = render_page1()
    p2 = render_page2()
    pdf = OUTPUT_DIR / "akiva-sow.pdf"
    p1.save(pdf, "PDF", resolution=200.0, save_all=True, append_images=[p2])
    p1_png = OUTPUT_DIR / "akiva-sow-p1.png"
    p2_png = OUTPUT_DIR / "akiva-sow-p2.png"
    p1.save(p1_png, "PNG")
    p2.save(p2_png, "PNG")
    print(f"PDF:{pdf}")
    print(f"PNG1:{p1_png}")
    print(f"PNG2:{p2_png}")


if __name__ == "__main__":
    render()
