# -*- coding: utf-8 -*-
import os, json
from collections import Counter, defaultdict
D = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\help_md"
data = json.load(open(os.path.join(D, "_index.json"), "r", encoding="utf-8"))
idx = data["index"]
lvl = [Counter(), Counter(), Counter()]
for it in idx:
    p = it.get("path") or []
    for i in range(3):
        if len(p) > i:
            lvl[i][">".join(p[:i + 1])] += 1
out = []
out.append("count=%d chars=%d" % (data["count"], data["total_chars"]))
out.append("")
for i in range(3):
    out.append("=== L%d ===" % (i + 1))
    for k, v in sorted(lvl[i].items()):
        out.append("%4d  %s" % (v, k))
    out.append("")
out.append("=== LARGEST PAGES ===")
for it in sorted(idx, key=lambda x: -x["chars"])[:30]:
    out.append("%6d  %s | %s" % (it["chars"], " > ".join(it.get("path") or []), it["src"]))
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_help_analysis.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok")
