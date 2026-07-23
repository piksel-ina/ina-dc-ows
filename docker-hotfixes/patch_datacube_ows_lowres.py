from __future__ import annotations

import glob
from pathlib import Path

candidates = glob.glob("/app/.venv/lib/python*/site-packages/datacube_ows/loading.py")
if len(candidates) != 1:
    raise RuntimeError(f"Expected exactly one loading.py candidate, got: {candidates}")

target = Path(candidates[0])
text = target.read_text()

old = "queries = ProductBandQuery.style_queries(self.style)"
new = "queries = ProductBandQuery.style_queries(self.style, self.resource_limited)"

count = text.count(old)
if count != 3:
    raise RuntimeError(
        f"Expected 3 style query call sites in {target}, found {count}"
    )

text = text.replace(old, new)

target.write_text(text)
print(f"Patched {target}")
