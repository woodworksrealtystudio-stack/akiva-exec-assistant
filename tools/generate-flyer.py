#!/usr/bin/env python3
"""
Vacancy flyer generator -- one-page CRE listing flyer.

Usage:
  python3 tools/generate-flyer.py output/flyer.json

flyer.json format:
{
  "property_slug": "1364-briar-vista-suite-200",
  "headline": "2,400 SF Retail Available",
  "address": "1364 Briar Vista Way, Suite 200",
  "submarket": "Toco Hills, Atlanta",
  "asking_rate": "$28/SF NNN",
  "available": "Immediate",
  "highlights": [
    "End-cap with full glass frontage",
    "Pylon signage included",
    "32 parking spaces"
  ],
  "use_types": ["Retail", "Quick-service restaurant", "Service"],
  "matterport_url": "https://my.matterport.com/...",
  "contact": {
    "name": "Akiva Halpern",
    "email": "[email]",
    "phone": "[phone]"
  }
}
"""

import sys
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT  = Path(__file__).resolve().parents[1]
FONTS_DIR  = REPO_ROOT / "brand-assets" / "fonts"
OUTPUT_DIR = REPO_ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# US Letter at 150 DPI
W, H   = 1275, 1650
MARGIN = 96
TEXT_W = W - 2 * MARGIN

# Cream / charcoal / accent palette
CREAM    = (250, 244, 238)
CHARCOAL = (32, 32, 32)
NAVY     = (28, 43, 74)
ACCENT   = (139, 105, 20)
SLATE    = (107, 114, 128)
BORDER   = (210, 200, 185)
WHITE    = (255, 255, 255)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    path = FONTS_DIR / name
    if path.exists():
        return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def F_HEADLINE(size): return font("CormorantGaramond-Bold.ttf", size)
def F_SECTION(size):  return font("DMSans-Medium.ttf", size)
def F_BODY(size):     return font("DMSans-Regular.ttf", size)
def F_LIGHT(size):    return font("DMSans-Light.ttf", size)


def measure(fnt, text):
    bb = fnt.getbbox(text)
    return bb[2] - bb[0], bb[3] - bb[1]


def wrap(text, fnt, max_w):
    words, lines, cur = text.split(), [], []
    for w in words:
        trial = " ".join(cur + [w])
        tw, _ = measure(fnt, trial)
        if tw <= max_w or not cur:
            cur.append(w)
        else:
            lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    return lines


def draw_lines(draw, lines, x, y, fnt, color, line_h):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=color)
        y += line_h
    return y


def render(data: dict) -> Path:
    img  = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)

    # Top + bottom rules
    draw.rectangle([(0, 0), (W, 6)], fill=NAVY)
    draw.rectangle([(0, 6), (W, 9)], fill=ACCENT)
    draw.rectangle([(0, H - 9), (W, H - 6)], fill=ACCENT)
    draw.rectangle([(0, H - 6), (W, H)], fill=NAVY)

    y = 80

    # Eyebrow -- submarket
    eyebrow = data.get("submarket", "Atlanta CRE").upper()
    eb_fnt = F_SECTION(22)
    ebw, ebh = measure(eb_fnt, eyebrow)
    # Letterspaced effect with accent dot
    draw.text((MARGIN, y), eyebrow, font=eb_fnt, fill=ACCENT)
    y += ebh + 8

    # Headline -- "2,400 SF Retail Available"
    hl_fnt = F_HEADLINE(96)
    hl_lines = wrap(data["headline"], hl_fnt, TEXT_W)
    hl_h = round(96 * 1.05)
    y = draw_lines(draw, hl_lines, MARGIN, y, hl_fnt, NAVY, hl_h)
    y += 8

    # Gold accent bar
    draw.rectangle([(MARGIN, y), (MARGIN + 80, y + 5)], fill=ACCENT)
    y += 36

    # Address line
    addr_fnt = F_SECTION(34)
    draw.text((MARGIN, y), data["address"], font=addr_fnt, fill=CHARCOAL)
    y += 50

    # Stats row -- rate + availability
    stats = [
        ("ASKING", data.get("asking_rate", "")),
        ("AVAILABLE", data.get("available", "")),
        ("USE", " · ".join(data.get("use_types", []))[:48]),
    ]
    col_w = TEXT_W // 3
    for i, (label, value) in enumerate(stats):
        col_x = MARGIN + i * col_w
        lf = F_LIGHT(20)
        draw.text((col_x, y), label, font=lf, fill=SLATE)
        vf = F_SECTION(28)
        draw.text((col_x, y + 28), value, font=vf, fill=NAVY)
    y += 90

    # Divider
    draw.rectangle([(MARGIN, y), (W - MARGIN, y + 1)], fill=BORDER)
    y += 36

    # Highlights section
    sec_fnt = F_SECTION(22)
    draw.text((MARGIN, y), "PROPERTY HIGHLIGHTS", font=sec_fnt, fill=ACCENT)
    y += 36

    hl_body_fnt = F_BODY(28)
    hl_lh = round(28 * 1.6)
    bullet_size = 6
    for item in data.get("highlights", [])[:8]:
        draw.ellipse(
            [(MARGIN + 4, y + 14), (MARGIN + 4 + bullet_size, y + 14 + bullet_size)],
            fill=ACCENT,
        )
        for i, ln in enumerate(wrap(item, hl_body_fnt, TEXT_W - 32)):
            draw.text((MARGIN + 28, y), ln, font=hl_body_fnt, fill=CHARCOAL)
            y += hl_lh
        y += 4

    y += 24

    # Matterport link block (if provided)
    if data.get("matterport_url"):
        draw.rectangle([(MARGIN, y), (W - MARGIN, y + 1)], fill=BORDER)
        y += 32
        mp_label_fnt = F_SECTION(22)
        draw.text((MARGIN, y), "VIRTUAL TOUR", font=mp_label_fnt, fill=ACCENT)
        y += 32
        mp_fnt = F_BODY(24)
        url = data["matterport_url"]
        if len(url) > 70:
            url = url[:67] + "..."
        draw.text((MARGIN, y), url, font=mp_fnt, fill=NAVY)
        y += 56

    # Contact block at the bottom
    contact_y = H - 320
    draw.rectangle([(MARGIN, contact_y), (W - MARGIN, contact_y + 1)], fill=BORDER)

    contact_label_fnt = F_SECTION(22)
    draw.text((MARGIN, contact_y + 28), "CONTACT", font=contact_label_fnt, fill=ACCENT)

    contact = data.get("contact", {})
    name_fnt = F_HEADLINE(54)
    draw.text((MARGIN, contact_y + 64), contact.get("name", ""), font=name_fnt, fill=NAVY)

    line_fnt = F_BODY(26)
    cy = contact_y + 138
    if contact.get("email"):
        draw.text((MARGIN, cy), contact["email"], font=line_fnt, fill=CHARCOAL)
        cy += 38
    if contact.get("phone"):
        draw.text((MARGIN, cy), contact["phone"], font=line_fnt, fill=CHARCOAL)
        cy += 38

    # Footer
    foot_fnt = F_LIGHT(18)
    foot_txt = "Built with Woodworks Realty Studio  ·  woodworksrealtystudio.com"
    fw, fh = measure(foot_fnt, foot_txt)
    draw.text(((W - fw) // 2, H - 56), foot_txt, font=foot_fnt, fill=SLATE)

    # Save
    slug = data.get("property_slug", "vacancy")
    png_path = OUTPUT_DIR / f"flyer-{slug}.png"
    pdf_path = OUTPUT_DIR / f"flyer-{slug}.pdf"
    img.save(png_path, "PNG")
    img.convert("RGB").save(pdf_path, "PDF", resolution=150.0)
    print(f"FLYER_GENERATED:{png_path}")
    print(f"FLYER_PDF:{pdf_path}")
    return png_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/generate-flyer.py output/flyer.json")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        data = json.load(f)
    render(data)
