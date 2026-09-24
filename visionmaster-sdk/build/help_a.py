# -*- coding: utf-8 -*-
import os, re
BASE = r"D:\VisionMaster4.4.0\Applications\Help\CH"
raw = open(os.path.join(BASE, "index.html"), "r", encoding="utf-8", errors="ignore").read()
seg = raw.split("\n")[150]
out = []
ms = list(re.finditer(r"<a\b[^>]*>.*?</a>", seg, re.S))
out.append("A COUNT: %d" % len(ms))
for m in ms[:12]:
    out.append(m.group(0)[:500])
    out.append("")
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_help_a.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok")
