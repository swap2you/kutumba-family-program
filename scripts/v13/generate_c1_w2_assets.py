#!/usr/bin/env python3
"""Generate original C1-W2 V13 line-art PNG assets with Pillow."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[2]
OUT = (
    REPO
    / "11-weekly-program-library"
    / "first-six-months"
    / "c1-w2-i-am-not-this-body"
    / "visuals"
    / "v13"
)
CREAM, PLUM, SAFFRON, TEAL = "#FFF8E8", "#5B1933", "#E59B24", "#4F7C78"


def font(size: int, bold: bool = False):
    names = ["segoeuib.ttf" if bold else "segoeui.ttf", "arialbd.ttf" if bold else "arial.ttf"]
    for name in names:
        path = Path(r"C:\Windows\Fonts") / name
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def canvas(size=(768, 512)):
    image = Image.new("RGB", size, CREAM)
    return image, ImageDraw.Draw(image)


def save(image: Image.Image, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    image.save(OUT / name, "PNG", optimize=True)
    print("wrote", OUT / name)


def silhouette(d, cx, cy, scale, color=PLUM):
    # head
    r = int(28 * scale)
    d.ellipse((cx - r, cy - 110 * scale, cx + r, cy - 110 * scale + 2 * r), outline=color, width=6)
    # body
    d.line((cx, cy - 110 * scale + 2 * r, cx, cy + 40 * scale), fill=color, width=8)
    # arms
    d.line((cx - 45 * scale, cy - 20 * scale, cx + 45 * scale, cy - 20 * scale), fill=color, width=7)
    # legs
    d.line((cx, cy + 40 * scale, cx - 35 * scale, cy + 110 * scale), fill=color, width=7)
    d.line((cx, cy + 40 * scale, cx + 35 * scale, cy + 110 * scale), fill=color, width=7)


def life_stage_sequence() -> None:
    im, d = canvas((900, 420))
    labels = [("CHILD", 0.75), ("YOUTH", 1.0), ("ELDER", 0.95)]
    xs = [150, 450, 750]
    for (label, scale), x in zip(labels, xs):
        silhouette(d, x, 200, scale, TEAL if label != "YOUTH" else PLUM)
        b = d.textbbox((0, 0), label, font=font(26, True))
        d.text((x - (b[2] - b[0]) / 2, 340), label, fill=PLUM, font=font(26, True))
    for x in (300, 600):
        d.polygon([(x - 20, 200), (x + 20, 200), (x, 220)], fill=SAFFRON)
        d.line((x - 50, 190, x + 50, 190), fill=SAFFRON, width=6)
    save(im, "life-stage-sequence.png")


def care_self_craft() -> None:
    im, d = canvas((900, 600))
    # left Care panel
    d.rectangle((40, 40, 430, 480), outline=TEAL, width=8)
    d.text((160, 55), "CARE", fill=TEAL, font=font(36, True))
    d.ellipse((170, 130, 300, 280), outline=PLUM, width=7)  # head-ish
    d.rectangle((185, 280, 285, 420), outline=PLUM, width=7)
    # right Self panel
    d.rectangle((470, 40, 860, 480), outline=SAFFRON, width=8)
    d.text((640, 55), "SELF", fill=SAFFRON, font=font(36, True))
    d.polygon(
        [(665, 360), (560, 250), (575, 200), (630, 185), (665, 230), (700, 185), (755, 200), (770, 250)],
        outline=PLUM,
        width=7,
    )
    d.text((250, 520), "My body changes; I continue as the conscious self.", fill=PLUM, font=font(22, True))
    save(im, "care-self-craft.png")
    save(im, "care-self-card.png")


def life_stage_singles() -> None:
    for label, scale, name in (("CHILD", 0.75, "life-stage-child.png"), ("YOUTH", 1.0, "life-stage-youth.png"), ("ELDER", 0.95, "life-stage-elder.png")):
        im, d = canvas((384, 420))
        silhouette(d, 192, 180, scale, TEAL if label != "YOUTH" else PLUM)
        b = d.textbbox((0, 0), label, font=font(28, True))
        d.text((192 - (b[2] - b[0]) / 2, 340), label, fill=PLUM, font=font(28, True))
        save(im, name)


def _center_text(d, box, text, fill, fnt):
    x1, y1, x2, y2 = box
    b = d.textbbox((0, 0), text, font=fnt)
    x = (x1 + x2 - (b[2] - b[0])) / 2
    y = (y1 + y2 - (b[3] - b[1])) / 2
    d.text((x, y), text, fill=fill, font=fnt)


def memory_phrase_mat() -> None:
    im, d = canvas((1000, 600))
    bands = [
        (40, 60, 960, 180, "My body changes;"),
        (40, 210, 960, 330, "I continue"),
        (40, 360, 960, 480, "as the conscious self."),
    ]
    colors = [TEAL, PLUM, SAFFRON]
    for (x1, y1, x2, y2, text), color in zip(bands, colors):
        d.rounded_rectangle((x1, y1, x2, y2), radius=24, outline=color, width=8)
        _center_text(d, (x1, y1, x2, y2), text, PLUM, font(40, True))
    d.text((220, 520), "Care for the body. Don't tease bodies.", fill=TEAL, font=font(22, True))
    save(im, "memory-phrase-mat.png")
    save(im, "memory-mat.png")


def care_self_diagram() -> None:
    im, d = canvas((900, 560))
    boxes = [
        (60, 60, 840, 150, "Body stages: child -> youth -> elder"),
        (60, 220, 840, 310, "Conscious self continues"),
        (60, 390, 420, 500, "Kind speech"),
        (480, 390, 840, 500, "Responsible care"),
    ]
    for x1, y1, x2, y2, text in boxes:
        d.rounded_rectangle((x1, y1, x2, y2), radius=18, outline=PLUM, width=6)
        _center_text(d, (x1, y1, x2, y2), text, PLUM, font(24, True))
    d.line((450, 150, 450, 220), fill=SAFFRON, width=8)
    d.line((450, 310, 450, 350), fill=SAFFRON, width=8)
    d.line((240, 350, 660, 350), fill=SAFFRON, width=8)
    d.line((240, 350, 240, 390), fill=SAFFRON, width=8)
    d.line((660, 350, 660, 390), fill=SAFFRON, width=8)
    save(im, "care-self-diagram.png")
    save(im, "body-self-diagram.png")


def kind_speech_icons() -> None:
    im, d = canvas((800, 220))
    # speech bubble
    d.ellipse((40, 40, 160, 140), outline=TEAL, width=7)
    d.polygon([(70, 130), (55, 175), (100, 140)], outline=TEAL, width=7)
    # heart
    d.polygon([(280, 150), (220, 90), (230, 55), (265, 45), (290, 75), (315, 45), (350, 55), (360, 90)], outline=PLUM, width=7)
    # water glass
    d.polygon([(470, 50), (510, 50), (500, 170), (480, 170)], outline=SAFFRON, width=7)
    d.line((478, 100, 502, 100), fill=TEAL, width=5)
    # repair handshake arcs
    d.arc((600, 40, 760, 180), 200, 340, fill=PLUM, width=8)
    d.arc((600, 40, 760, 180), 20, 160, fill=TEAL, width=8)
    save(im, "kind-speech-icons.png")


def main() -> None:
    life_stage_sequence()
    life_stage_singles()
    care_self_craft()
    memory_phrase_mat()
    care_self_diagram()
    kind_speech_icons()


if __name__ == "__main__":
    main()
