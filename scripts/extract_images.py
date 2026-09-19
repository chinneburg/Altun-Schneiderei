"""Extract the base64-embedded JPEGs from the Sep-15 HTML draft into real files.

The draft carries 7 images inline as data: URIs inside CSS url(...) values,
which accounts for ~94% of the file size. This pulls them out so the build
can optimise and cache them normally.
"""

import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DRAFT = ROOT / "nyveo_html_entwurf_Sep-15.html"
OUT = ROOT / "src" / "assets" / "images"

# First match is the hero background, the rest are the gallery band in order.
NAMES = [
    "hero",
    "gallery-01",
    "gallery-02",
    "gallery-03",
    "gallery-04",
    "gallery-05",
    "gallery-06",
]

PATTERN = re.compile(r"data:image/(?P<ext>[a-z]+);base64,(?P<data>[A-Za-z0-9+/=]+)")


def main() -> None:
    html = DRAFT.read_text(encoding="utf-8")
    matches = list(PATTERN.finditer(html))
    if len(matches) != len(NAMES):
        raise SystemExit(f"expected {len(NAMES)} images, found {len(matches)}")

    OUT.mkdir(parents=True, exist_ok=True)
    for name, match in zip(NAMES, matches):
        raw = base64.b64decode(match.group("data"))
        path = OUT / f"{name}.jpg"
        path.write_bytes(raw)
        print(f"{path.relative_to(ROOT)}  {len(raw) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
