"""Print specific draft lines in full, for copy that the truncated dumps cut off."""

import pathlib
import sys

DRAFT = pathlib.Path(__file__).resolve().parent.parent / "nyveo_html_entwurf_Sep-15.html"
lines = DRAFT.read_text(encoding="utf-8").splitlines()

for arg in sys.argv[1:]:
    n = int(arg)
    print(f"--- {n} ---")
    print(lines[n - 1].strip())
