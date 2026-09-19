"""Lift the <style> block out of the Sep-15 draft into src/styles/global.css.

Copies the rules verbatim (only removing the shared 8-space indent that came
from being nested in <head>), so the extracted stylesheet is byte-comparable
with the draft and the design cannot drift during the move.
"""

import pathlib
import textwrap

ROOT = pathlib.Path(__file__).resolve().parent.parent
DRAFT = ROOT / "nyveo_html_entwurf_Sep-15.html"
OUT = ROOT / "src" / "styles" / "global.css"

lines = DRAFT.read_text(encoding="utf-8").splitlines()

start = next(i for i, line in enumerate(lines) if line.strip() == "<style>")
end = next(i for i, line in enumerate(lines) if line.strip() == "</style>")

css = textwrap.dedent("\n".join(lines[start + 1 : end])).strip() + "\n"

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(css, encoding="utf-8")

print(f"{OUT.relative_to(ROOT)}  {len(css.splitlines())} lines  {len(css) / 1024:.1f} KB")
