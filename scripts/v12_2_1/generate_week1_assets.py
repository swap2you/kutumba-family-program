#!/usr/bin/env python3
"""Generate original, simple C1-W1 line-art PNG assets with Pillow."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "11-weekly-program-library" / "first-six-months" / "c1-w1-what-is-kutumba-and-why-are-we-here" / "visuals" / "v12_2_1"
SIZE = 384
CREAM, PLUM, SAFFRON, TEAL = "#FFF8E8", "#5B1933", "#E59B24", "#4F7C78"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    names = ["segoeuib.ttf" if bold else "segoeui.ttf", "arialbd.ttf" if bold else "arial.ttf"]
    for name in names:
        path = Path(r"C:\Windows\Fonts") / name
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def canvas(size: tuple[int, int] = (SIZE, SIZE)):
    image = Image.new("RGB", size, CREAM)
    return image, ImageDraw.Draw(image)


def save(image: Image.Image, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    image.save(OUT / name, "PNG", optimize=True)


def icon_hear() -> None:
    im, d = canvas()
    d.arc((42, 42, 210, 260), 235, 115, fill=PLUM, width=13)
    d.arc((82, 82, 175, 220), 225, 110, fill=TEAL, width=10)
    d.line((130, 185, 130, 245, 105, 278), fill=PLUM, width=11)
    d.polygon([(205, 130), (286, 108), (350, 135), (350, 296), (286, 274), (205, 296)], outline=TEAL, width=10)
    d.line((286, 110, 286, 274), fill=SAFFRON, width=8)
    save(im, "icon-hear.png")


def icon_chant() -> None:
    im, d = canvas()
    beads = [(70 + i * 28, 230 + int(42 * __import__("math").sin(i / 2))) for i in range(10)]
    d.line(beads, fill=PLUM, width=7)
    for x, y in beads:
        d.ellipse((x - 10, y - 10, x + 10, y + 10), outline=SAFFRON, width=6)
    d.line((300, 65, 300, 205), fill=TEAL, width=10)
    d.line((300, 65, 355, 48, 355, 175), fill=TEAL, width=10)
    d.ellipse((266, 188, 307, 225), fill=TEAL)
    d.ellipse((321, 158, 362, 195), fill=TEAL)
    save(im, "icon-chant.png")


def icon_serve() -> None:
    im, d = canvas()
    d.arc((38, 92, 218, 315), 220, 350, fill=PLUM, width=16)
    d.arc((166, 92, 346, 315), 190, 320, fill=TEAL, width=16)
    d.line((62, 262, 142, 302, 197, 252), fill=PLUM, width=16)
    d.line((322, 262, 242, 302, 187, 252), fill=TEAL, width=16)
    d.ellipse((162, 96, 222, 156), outline=SAFFRON, width=10)
    save(im, "icon-serve.png")


def icon_respect() -> None:
    im, d = canvas()
    d.line((42, 170, 192, 55, 342, 170), fill=TEAL, width=13)
    d.rectangle((83, 164, 301, 326), outline=TEAL, width=11)
    d.polygon([(192, 280), (119, 207), (126, 166), (166, 153), (192, 181), (218, 153), (258, 166), (265, 207)], outline=PLUM, fill=None)
    d.line((192, 280, 119, 207), fill=PLUM, width=10)
    d.line((192, 280, 265, 207), fill=PLUM, width=10)
    save(im, "icon-respect.png")


def flower() -> None:
    im, d = canvas((768, 640))
    petals = [((270, 40, 498, 300), "HEAR"), ((470, 200, 735, 430), "SERVE"),
              ((270, 335, 498, 610), "RESPECT"), ((35, 200, 298, 430), "CHANT")]
    for box, label in petals:
        d.ellipse(box, outline=TEAL, width=9)
        b = d.textbbox((0, 0), label, font=font(28, True))
        x = (box[0] + box[2] - (b[2] - b[0])) / 2
        y = (box[1] + box[3] - (b[3] - b[1])) / 2
        d.text((x, y), label, fill=PLUM, font=font(28, True))
    d.ellipse((258, 190, 510, 442), fill=CREAM, outline=SAFFRON, width=11)
    lines = ["Our family helps", "one another", "remember Kṛṣṇa."]
    f = font(20, True)
    y = 250
    for line in lines:
        b = d.textbbox((0, 0), line, font=f)
        d.text((384 - (b[2] - b[0]) / 2, y), line, fill=PLUM, font=f)
        y += 36
    save(im, "flower-bhakti-garden.png")


def compass() -> None:
    im, d = canvas((640, 640))
    c = 320
    d.ellipse((92, 92, 548, 548), outline=TEAL, width=9)
    d.line((c, 100, c, 540), fill=PLUM, width=8)
    d.line((100, c, 540, c), fill=PLUM, width=8)
    d.polygon([(c, 75), (298, 132), (342, 132)], fill=SAFFRON)
    labels = [(c, 28, "HEAR"), (515, 285, "PRACTICE"), (c, 570, "SERVE"), (92, 285, "ASSOCIATE")]
    for x, y, text in labels:
        b = d.textbbox((0, 0), text, font=font(22, True))
        d.text((x - (b[2] - b[0]) / 2, y), text, fill=PLUM, font=font(22, True))
    d.ellipse((288, 288, 352, 352), fill=CREAM, outline=SAFFRON, width=8)
    save(im, "compass-family.png")


def outlines() -> None:
    im, d = canvas((420, 420))
    d.rounded_rectangle((24, 24, 396, 396), radius=48, outline=PLUM, width=12)
    d.line((70, 70, 350, 70), fill=SAFFRON, width=7)
    lines = ["WE HELP EACH OTHER", "REMEMBER KṚṢṆA", "", "Our family helps", "one another", "remember Kṛṣṇa."]
    y = 110
    for i, line in enumerate(lines):
        if not line:
            y += 18
            continue
        f = font(22 if i < 2 else 16, True)
        b = d.textbbox((0, 0), line, font=f)
        d.text((210 - (b[2] - b[0]) / 2, y), line, fill=PLUM, font=f)
        y += 34 if i < 2 else 28
    save(im, "badge-outline.png")
    im, d = canvas((280, 720))
    d.line([(40, 30), (240, 30), (240, 620), (140, 690), (40, 620), (40, 30)], fill=TEAL, width=10)
    lines = ["HEAR", "CHANT", "SERVE", "RESPECT", "", "We help", "each other", "remember", "Kṛṣṇa."]
    y = 70
    for line in lines:
        if not line:
            y += 24
            continue
        f = font(22, True)
        b = d.textbbox((0, 0), line, font=f)
        d.text((140 - (b[2] - b[0]) / 2, y), line, fill=PLUM, font=f)
        y += 48
    save(im, "bookmark-strip.png")
    for name, label, color in (("mat-safe.png", "SAFE", TEAL), ("mat-reset.png", "NEEDS RESET", PLUM)):
        im, d = canvas((640, 320))
        d.rounded_rectangle((25, 25, 615, 295), radius=35, outline=color, width=12)
        b = d.textbbox((0, 0), label, font=font(48, True))
        d.text(((640 - (b[2] - b[0])) / 2, 126), label, fill=color, font=font(48, True))
        save(im, name)


def main() -> int:
    icon_hear(); icon_chant(); icon_serve(); icon_respect(); flower(); compass(); outlines()
    for path in sorted(OUT.glob("*.png")):
        print(path.relative_to(REPO), Image.open(path).size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
