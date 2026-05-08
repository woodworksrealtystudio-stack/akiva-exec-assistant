#!/usr/bin/env python3
"""
Woodworks-branded skills cheat sheet -- one-page poster.

Usage:
  python3 tools/generate-cheatsheet.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT  = Path(__file__).resolve().parents[1]
FONTS_DIR  = REPO_ROOT / "brand-assets" / "fonts"
OUTPUT_DIR = REPO_ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# US Letter at 200 DPI for sharp print
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


SKILLS = [
    # group, name, one-line, trigger phrase
    ("DAILY OPS", "onboard",             "Greets you by name. Confirms what's known + fills gaps.",               "\"Onboard me\""),
    ("DAILY OPS", "lead-parser",         "Any lead source -- structured + drafted + AppFolio spec + dedup.",      "Paste a LoopNet / Voice / Forms message"),
    ("DAILY OPS", "inbox-triage",        "Batch Outlook triage -- categorize + draft replies.",                   "\"Triage my inbox\""),
    ("DAILY OPS", "tenant-faq",          "Tenant question -> response that cites their actual lease.",            "Paste tenant message"),
    ("DAILY OPS", "maintenance-triage",  "Maintenance ticket -> vendor draft + tenant ack + log.",                "Paste maintenance request"),
    ("DAILY OPS", "tour-scheduler",      "Reads your calendar, proposes 3 times, drafts confirmation.",           "\"Schedule tour for [name]\""),
    ("DAILY OPS", "weekly-digest",       "Monday brief -- vacancies, leads, leases, top 3 priorities.",           "\"Weekly digest\""),
    ("DEALS",     "vacancy-marketing",   "Branded flyer (PDF/PNG) + 4 segmented email drafts.",                   "\"Vacancy at [address]\""),
    ("DEALS",     "matterport-prep",     "Matterport upload -> flyer-ready photos. Gemini staging prompts.",      "\"Matterport done for [property]\""),
    ("DEALS",     "lease-extractor",     "Builds your lease database. Queryable across all leases.",              "\"Log this lease\""),
    ("DEALS",     "lease-drafter",       "Clauses, redlines, alternative wordings during negotiations.",          "\"Draft a [TI / option / etc.] clause\""),
    ("DEALS",     "pricing-review",      "Internal -- 'is Suite 200 underpriced?' Your lease + market comps.",    "\"Pricing for [tenant or suite]\""),
    ("DEALS",     "contract-summary",    "Quick one-off lease / PSA summary -- terms + red flags.",               "\"Summarize this contract\""),
    ("DEALS",     "comp-analysis",       "Rent comps, sale comps, cap rates, $/SF -- outward.",                   "\"Pull comps for [address]\""),
    ("DEALS",     "email-draft",         "General-purpose email in your voice.",                                  "\"Draft an email to [name]\""),
    ("DEALS",     "follow-up-sequence",  "3-touch plan -- broker, tenant, prospect.",                             "\"Follow up with [name]\""),
    ("RESEARCH",  "market-research",     "Live web search -- submarkets, news (built-in WebSearch).",             "\"Research [topic]\""),
    ("RESEARCH",  "lead-research",       "Profile a person or firm before a meeting.",                            "\"Look up [name]\""),
    ("META",      "brainstorming",       "Structured idea exploration before you build anything.",                "\"Brainstorm with me\""),
    ("META",      "skill-creator",       "Build a new custom skill when a workflow keeps repeating.",             "\"Build a new skill for X\""),
]
# (using-superpowers loads automatically as the framework -- documented in CLAUDE.md, not on the cheatsheet)


def render():
    img  = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)

    # Top + bottom rules
    draw.rectangle([(0, 0), (W, 8)], fill=NAVY)
    draw.rectangle([(0, 8), (W, 12)], fill=ACCENT)
    draw.rectangle([(0, H - 12), (W, H - 8)], fill=ACCENT)
    draw.rectangle([(0, H - 8), (W, H)], fill=NAVY)

    y = 110

    # Eyebrow
    eyebrow = "WOODWORKS REALTY STUDIO  ·  AI EXECUTIVE ASSISTANT"
    eb_fnt = F_SECT(28)
    draw.text((MARGIN, y), eyebrow, font=eb_fnt, fill=ACCENT)
    y += 50

    # Title
    title = "Akiva's Context OS"
    tfnt  = F_HL(140)
    draw.text((MARGIN, y), title, font=tfnt, fill=NAVY)
    y += 156

    # Gold accent
    draw.rectangle([(MARGIN, y), (MARGIN + 110, y + 6)], fill=ACCENT)
    y += 36

    sub = "Twenty skills + the framework. AI in the back, you in the front."
    sfnt = F_BODY(34)
    draw.text((MARGIN, y), sub, font=sfnt, fill=CHARCOAL)
    y += 64

    # Install command box
    install_y = y
    draw.rectangle([(MARGIN, install_y), (W - MARGIN, install_y + 180)], outline=BORDER, width=2)

    inst_label_fnt = F_SECT(24)
    draw.text((MARGIN + 24, install_y + 22), "INSTALL", font=inst_label_fnt, fill=ACCENT)

    inst_lines = [
        "git clone https://github.com/woodworksrealtystudio-stack/akiva-exec-assistant.git ~/akiva-context-os",
        "cd ~/akiva-context-os",
        "claude",
    ]
    inst_fnt = F_BODY(28)
    iy = install_y + 58
    for line in inst_lines:
        draw.text((MARGIN + 24, iy), line, font=inst_fnt, fill=NAVY)
        iy += 38

    y = install_y + 220

    # Two-column layout for skills
    col_gap = 80
    col_w   = (TEXT_W - col_gap) // 2
    col_x_left  = MARGIN
    col_x_right = MARGIN + col_w + col_gap

    # Group skills
    daily_ops = [s for s in SKILLS if s[0] == "DAILY OPS"]
    deals     = [s for s in SKILLS if s[0] == "DEALS"]
    research  = [s for s in SKILLS if s[0] == "RESEARCH"]
    meta      = [s for s in SKILLS if s[0] == "META"]

    col1_y = y
    col2_y = y

    def render_group(group_label, items, x, ystart, col_width, compact=False):
        cy = ystart
        gfnt = F_SECT(22)
        draw.text((x, cy), group_label, font=gfnt, fill=ACCENT)
        cy += 10
        draw.rectangle([(x, cy + 18), (x + 56, cy + 21)], fill=ACCENT)
        cy += 34
        name_size  = 32
        line_step  = 25
        item_gap   = 8
        for _, name, desc, trigger in items:
            name_fnt = F_SEMI(name_size)
            draw.text((x, cy), "·", font=F_BODY(24), fill=ACCENT)
            draw.text((x + 22, cy - 2), name, font=name_fnt, fill=NAVY)
            cy += name_size + 6
            d_fnt = F_BODY(18)
            for ln in wrap(desc, d_fnt, col_width - 24):
                draw.text((x + 22, cy), ln, font=d_fnt, fill=CHARCOAL)
                cy += line_step
            t_fnt = F_LIGHT(17)
            for ln in wrap(trigger, t_fnt, col_width - 24):
                draw.text((x + 22, cy), ln, font=t_fnt, fill=SLATE)
                cy += line_step - 2
            cy += item_gap
        return cy

    # Left column: DAILY OPS (7 skills) -- the most important lane
    col1_y = render_group("DAILY OPERATIONS", daily_ops, col_x_left, col1_y, col_w, compact=True)

    # Right column: DEALS + RESEARCH + META (6 + 2 + 3 = 11 skills)
    col2_y = render_group("DEALS + DOCUMENTS", deals, col_x_right, col2_y, col_w, compact=True)
    col2_y += 12
    col2_y = render_group("RESEARCH", research, col_x_right, col2_y, col_w, compact=True)
    col2_y += 12
    col2_y = render_group("META / SYSTEM", meta, col_x_right, col2_y, col_w, compact=True)

    # Footer note (full width below both columns)
    footer_y = max(col1_y, col2_y) + 24
    if footer_y > H - 200:
        footer_y = H - 200

    draw.rectangle([(MARGIN, footer_y), (W - MARGIN, footer_y + 1)], fill=BORDER)
    note_y = footer_y + 24
    note_fnt = F_LIGHT(20)
    notes = [
        "Built-in tools: WebSearch (live web)  ·  WebFetch (specific URLs)  ·  tools/generate-flyer.py (1-page flyer renderer)",
        "Connector (optional, no API keys): Microsoft 365 -- Outlook + Calendar + OneDrive (read-only in v1, write in v2)",
        "Add-on (v2): Outlook MCP for send / draft / move + folder watching for auto-ingest",
    ]
    for ln in notes:
        draw.text((MARGIN, note_y), ln, font=note_fnt, fill=CHARCOAL)
        note_y += 30

    note_y += 16
    leg_fnt = F_LIGHT(22)
    draw.text((MARGIN, note_y), "Twenty skills + the framework. One Context OS. AI in the back, you in the front.", font=leg_fnt, fill=CHARCOAL)

    # Brand block bottom right
    brand_fnt = F_SEMI(36)
    bw, bh = measure(brand_fnt, "Woodworks Realty Studio")
    draw.text((W - MARGIN - bw, H - 150), "Woodworks Realty Studio", font=brand_fnt, fill=NAVY)
    site_fnt = F_LIGHT(24)
    sw, sh = measure(site_fnt, "woodworksrealtystudio.com")
    draw.text((W - MARGIN - sw, H - 90), "woodworksrealtystudio.com", font=site_fnt, fill=SLATE)

    # Save
    png = OUTPUT_DIR / "akiva-cheatsheet.png"
    pdf = OUTPUT_DIR / "akiva-cheatsheet.pdf"
    img.save(png, "PNG")
    img.convert("RGB").save(pdf, "PDF", resolution=200.0)
    print(f"PNG:{png}")
    print(f"PDF:{pdf}")


if __name__ == "__main__":
    render()
