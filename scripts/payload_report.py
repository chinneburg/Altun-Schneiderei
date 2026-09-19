"""Estimate what a phone actually downloads on first load, vs the old draft.

Counts the HTML, CSS, JS, the two Latin webfonts, the 640w hero and the three
gallery crops that are visible below 1024px.
"""

import glob
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"


def total(pattern: str, exclude: str | None = None) -> int:
    files = glob.glob(str(DIST / pattern))
    if exclude:
        files = [f for f in files if exclude not in os.path.basename(f)]
    return sum(os.path.getsize(f) for f in files)


def smallest(pattern: str, count: int = 1) -> int:
    files = sorted(glob.glob(str(DIST / pattern)), key=os.path.getsize)
    return sum(os.path.getsize(f) for f in files[:count])


rows = [
    ("html", os.path.getsize(DIST / "index.html")),
    ("css", total("_astro/*.css")),
    ("js", total("_astro/*.js")),
    ("fonts (2 latin)", total("_astro/*latin-wght*.woff2", exclude="ext")),
    ("hero (640w)", smallest("_astro/hero*.webp")),
    ("gallery (3 crops)", smallest("_astro/gallery-0[1-3]*.webp", 3)),
]

width = max(len(name) for name, _ in rows)
for name, size in rows:
    print(f"{name:<{width}}  {size / 1024:7.1f} KB")

new = sum(size for _, size in rows)
old = os.path.getsize(ROOT / "nyveo_html_entwurf_Sep-15.html")
print("-" * (width + 12))
print(f"{'new total':<{width}}  {new / 1024:7.1f} KB")
print(f"{'old draft':<{width}}  {old / 1024:7.1f} KB  (single file, everything inline)")
print(f"\nreduction: {100 * (1 - new / old):.0f}%")
