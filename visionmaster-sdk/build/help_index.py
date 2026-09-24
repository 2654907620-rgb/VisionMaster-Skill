# -*- coding: utf-8 -*-
import os, re
BASE = r"D:\VisionMaster4.4.0\Applications\Help\CH"
out = []
# root html list
htmls = sorted([f for f in os.listdir(BASE) if f.lower().endswith((".html", ".htm"))])
out.append("ROOT HTML COUNT: %d" % len(htmls))
out.append("NON-GUID html: " + ", ".join([f for f in htmls if not f.upper().startswith("GUID")]))
out.append("")
for name in ("index.html", "search.html", "indexTerms.html"):
    p = os.path.join(BASE, name)
    if not os.path.exists(p):
        continue
    t = open(p, "rb").read().decode("utf-8", errors="ignore")
    out.append("=" * 20 + " " + name + " (%d bytes) " % len(t) + "=" * 20)
    out.append(t[:4000])
    out.append("")
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_help_index.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok", len(htmls))
