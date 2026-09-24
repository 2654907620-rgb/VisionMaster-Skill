# -*- coding: utf-8 -*-
import os, json, re

MD = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_net"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb"

with open(os.path.join(MD, "_index.json"), "r", encoding="utf-8") as fh:
    data = json.load(fh)

idx = data["index"]

def bucket(name):
    lf = name.lower()
    if lf.startswith("class_"): return "class"
    if lf.startswith("group_"): return "group"
    if lf.startswith(("namespace", "struct_", "interface_")): return "ns"
    if lf.startswith("_"): return "guide"
    return "other"

b = {}
for it in idx:
    b.setdefault(bucket(it["src"]), []).append(it)

lines = []
lines.append("### GUIDE (%d)" % len(b.get("guide", [])))
for it in sorted(b.get("guide", []), key=lambda x: -x["chars"]):
    lines.append("%7d  %-70s  %s" % (it["chars"], it["src"], it["title"]))
lines.append("")
lines.append("### OTHER (%d)" % len(b.get("other", [])))
for it in sorted(b.get("other", []), key=lambda x: -x["chars"]):
    lines.append("%7d  %-70s  %s" % (it["chars"], it["src"], it["title"]))
lines.append("")
lines.append("### GROUP (%d)" % len(b.get("group", [])))
for it in sorted(b.get("group", []), key=lambda x: -x["chars"]):
    lines.append("%7d  %-70s  %s" % (it["chars"], it["src"], it["title"]))
lines.append("")
lines.append("### NS/STRUCT (%d)" % len(b.get("ns", [])))
for it in sorted(b.get("ns", []), key=lambda x: -x["chars"]):
    lines.append("%7d  %-70s  %s" % (it["chars"], it["src"], it["title"]))
lines.append("")
lines.append("### CLASS (%d) top 200 by size" % len(b.get("class", [])))
for it in sorted(b.get("class", []), key=lambda x: -x["chars"])[:200]:
    lines.append("%7d  %-70s  %s" % (it["chars"], it["src"], it["title"]))

with open(os.path.join(OUT, "_analysis_net.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print("ok")
