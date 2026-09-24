# -*- coding: utf-8 -*-
import os, re
BASE = r"D:\VisionMaster4.4.0\Applications\Help\CH"
out = []
# search all files for a TOC-ish data source
cands = []
for dp, dn, fn in os.walk(BASE):
    for f in fn:
        lf = f.lower()
        if lf.endswith((".js", ".json", ".xml", ".html")) and any(k in lf for k in ("toc", "nav", "tree", "map", "index")):
            cands.append(os.path.join(dp, f))
out.append("CANDIDATES (%d):" % len(cands))
for c in cands:
    out.append("  " + c.replace(BASE, ".") + "  %d" % os.path.getsize(c))

out.append("")
# inspect wt_index.js and toc.js for data source hints
for rel in [r"daksys-webhelp\template\resources\js\wt_index.js",
            r"daksys-webhelp\resources\js\toc.js"]:
    p = os.path.join(BASE, rel)
    if not os.path.exists(p):
        out.append("MISS " + rel); continue
    t = open(p, "rb").read().decode("utf-8", errors="ignore")
    out.append("=" * 20 + " " + rel + " (%d) " % len(t) + "=" * 20)
    for m in re.finditer(r"[^\n]*(?:\.html|\.json|\.xml|toc|zNodes|ajax|getJSON|load\()[^\n]*", t, re.I):
        s = m.group(0).strip()
        if len(s) < 300:
            out.append("  " + s)
    out.append("")
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_help_toc_probe.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok")
