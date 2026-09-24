# -*- coding: utf-8 -*-
import os, re
BASE = r"D:\VisionMaster4.4.0\Applications\Help\CH"
raw = open(os.path.join(BASE, "index.html"), "r", encoding="utf-8", errors="ignore").read()
lines = raw.split("\n")
seg = lines[150] if len(lines) > 150 else raw
out = []
out.append("LINE 151 len=%d" % len(seg))
out.append(seg[:6000])
out.append("")
out.append("--- looking for data-* attributes sample ---")
for m in re.finditer(r"<li[^>]{0,400}>", seg):
    out.append(m.group(0)[:400])
    if len(out) > 30:
        break
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_help_toc_raw.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok")
