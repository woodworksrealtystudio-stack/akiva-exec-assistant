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
    ("CRE OPS",    "onboard",             "First-run interview -- populates every context file.",                   "\"Onboard me\""),
    ("CRE OPS",    "email-draft",         "Tenant / broker / prospect emails in your voice.",                       "\"Draft an email to [name]\""),
    ("CRE OPS",    "vacancy-marketing",   "Branded flyer + segmented email blast for any vacant space.",            "\"Vacancy at [address]\""),
    ("CRE OPS",    "contract-summary",    "Lease or PSA summary -- terms, dates, red-flag list.",                   "\"Summarize this lease\""),
    ("CRE OPS",    "comp-analysis",       "Rent comps, sale comps, cap rates, $/SF.",                               "\"Pull comps for [address]\""),
    ("CRE OPS",    "market-research",     "Live Perplexity search -- submarkets, comps, news.",                     "\"Research [topic]\""),
    ("CRE OPS",    "lead-research",       "Profile a LoopNet inquiry, broker rep, or prospect.",                    "\"Look up [name]\""),
    ("CRE OPS",    "follow-up-sequence",  "Touchpoint plan -- broker, tenant, prospect.",                           "\"Follow up with [name]\""),
    ("META",       "using-superpowers",   "Establishes the skills framework -- how this all hangs together.",       "Loads automatically"),
    ("META",       "brainstorming",       "Structured idea exploration before you build anything.",                  "\"Brainstorm with me\""),
    ("META",       "skill-creator",       "Build a new custom skill when a workflow keeps repeating.",              "\"Build a new skill for X\""),
]


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
    eyebrow = "WOODWORKS REALTY STUDIO  ·  CONTEXT OS"
    eb_fnt = F_SECT(28)
    draw.text((MARGIN, y), eyebrow, font=eb_fnt, fill=ACCENT)
    y += 50

    # Title
    title = "Akiva's Skills Cheat Sheet"
    tfnt  = F_HL(124)
    draw.text((MARGIN, y), title, font=tfnt, fill=NAVY)
    y += 138

    # Gold accent
    draw.rectangle([(MARGIN, y), (MARGIN + 110, y + 6)], fill=ACCENT)
    y += 36

    # Subtitle
    sub = "Eleven skills, one Context OS. Type any trigger phrase to invoke."
    sfnt = F_BODY(34)
    draw.text((MARGIN, y), sub, font=sfnt, fill=CHARCOAL)
    y += 64

    # Install command box
    install_y = y
    draw.rectangle([(MARGIN, install_y), (W - MARGIN, install_y + 180)], outline=BORDER, width=2)

    inst_label_fnt = F_SECT(24)
    draw.text((MARGIN + 24, install_y + 22), "INSTALL", font=inst_label_fnt, fill=ACCENT)

    inst_lines = [
        "git clone https://github.com/woodworksrealtystudio-stack/akiva-exec-assistant.git",
        "cd akiva-exec-assistant",
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
    cre_ops = [s for s in SKILLS if s[0] == "CRE OPS"]
    meta    = [s for s in SKILLS if s[0] == "META"]

    # Layout: CRE OPS in left column, META in right column
    col1_y = y
    col2_y = y

    def render_group(group_label, items, x, ystart, col_width):
        cy = ystart
        gfnt = F_SECT(26)
        draw.text((x, cy), group_label, font=gfnt, fill=ACCENT)
        cy += 14
        draw.rectangle([(x, cy + 22), (x + 70, cy + 25)], fill=ACCENT)
        cy += 46
        for _, name, desc, trigger in items:
            # Skill name (semibold serif)
            name_fnt = F_SEMI(48)
            draw.text((x, cy), "·", font=F_BODY(36), fill=ACCENT)
            draw.text((x + 28, cy - 6), name, font=name_fnt, fill=NAVY)
            cy += 60
            # Description
            d_fnt = F_BODY(24)
            for ln in wrap(desc, d_fnt, col_width - 36):
                draw.text((x + 28, cy), ln, font=d_fnt, fill=CHARCOAL)
                cy += 34
            # Trigger
            t_fnt = F_LIGHT(22)
            for ln in wrap(trigger, t_fnt, col_width - 36):
                draw.text((x + 28, cy), ln, font=t_fnt, fill=SLATE)
                cy += 32
            cy += 22
        return cy

    # Left column: 8 CRE OPS skills
    col1_y = render_group("CRE OPERATIONS", cre_ops, col_x_left, col1_y, col_w)

    # Right column: 3 META skills + breathing room for "build your own"
    col2_y = render_group("META / SYSTEM", meta, col_x_right, col2_y, col_w)
    col2_y += 32

    # Side note in right column under META
    note_fnt = F_LIGHT(22)
    note_lines = [
        "Tools (not skills):",
        "  · tools/research.py -- live web data",
        "  · tools/generate-flyer.py -- 1-page flyer",
        "",
        "MCP layer (set up once):",
        "  · Gmail + Google Calendar via Composio",
        "  · See docs/mcp-setup.md",
    ]
    for ln in note_lines:
        draw.text((col_x_right, col2_y), ln, font=note_fnt, fill=SLATE)
        col2_y += 32

    # Footer
    footer_y = max(col1_y, col2_y) + 40
    if footer_y > H - 180:
        footer_y = H - 180

    draw.rectangle([(MARGIN, footer_y), (W - MARGIN, footer_y + 1)], fill=BORDER)
    leg_y = footer_y + 28
    leg_fnt = F_LIGHT(22)
    draw.text((MARGIN, leg_y), "Eleven skills. One Context OS. Built for one operator.", font=leg_fnt, fill=CHARCOAL)

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
