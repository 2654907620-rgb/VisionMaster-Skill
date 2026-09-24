# -*- coding: utf-8 -*-
import os, json, re
from collections import Counter, defaultdict

MD = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_net"
OUTDIR = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb"
with open(os.path.join(MD, "_index.json"), "r", encoding="utf-8") as fh:
    data = json.load(fh)
idx = data["index"]

# top level structure
lvl = defaultdict(Counter)
for it in idx:
    p = it.get("path") or []
    if p:
        lvl[1][p[0]] += 1
    if len(p) > 1:
        lvl[2][p[0] + " > " + p[1]] += 1
    if len(p) > 2:
        lvl[3][p[0] + " > " + p[1] + " > " + p[2]] += 1

lines = []
lines.append("## L1 (top of TOC)")
for k, v in lvl[1].most_common():
    lines.append("%5d  %s" % (v, k))
lines.append("")
lines.append("## L2")
for k, v in lvl[2].most_common():
    lines.append("%5d  %s" % (v, k))
lines.append("")
lines.append("## L3")
for k, v in lvl[3].most_common():
    lines.append("%5d  %s" % (v, k))

with open(os.path.join(OUTDIR, "_toc_levels.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print("ok")
