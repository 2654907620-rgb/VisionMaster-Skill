# -*- coding: utf-8 -*-
"""Summarize help_bundles: list pages + trail (2 levels) per bundle."""
import os, re, io, json

KB = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb"
BD = os.path.join(KB, "help_bundles")

MARK = re.compile(r"<!--\s*=====\s*([^|]+?)\s*\|\s*(.*?)\s*=====\s*-->")

out = []
for fn in sorted(os.listdir(BD)):
    if not fn.endswith(".md"):
        continue
    p = os.path.join(BD, fn)
    raw = io.open(p, "r", encoding="utf-8", errors="replace").read()
    out.append("=" * 70)
    out.append("FILE: %s   chars=%d" % (fn, len(raw)))
    out.append("=" * 70)
    found = MARK.findall(raw)
    out.append("PAGES: %d" % len(found))
    trails = []
    for guid, trail in found:
        parts = [x.strip() for x in trail.split(">")]
        key = " > ".join(parts[:3]) if len(parts) >= 3 else trail.strip()
        if not trails or trails[-1] != key:
            trails.append(key)
    # dedupe consecutive
    out.append("--- outline (3-level, consecutive-dedup) ---")
    for t in trails:
        out.append("  " + t)
    out.append("")

txt = "\n".join(out)
io.open(os.path.join(KB, "_bundle_outline.txt"), "w", encoding="utf-8").write(txt)
print("OK bytes=%d" % len(txt))
