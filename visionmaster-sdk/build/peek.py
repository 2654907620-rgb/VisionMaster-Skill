# -*- coding: utf-8 -*-
import re
P = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\pdf_faq\faq_fulltext.md"
txt = open(P, "r", encoding="utf-8").read()
parts = re.split(r"<!-- page (\d+) -->\n", txt)
pages = {}
for i in range(1, len(parts), 2):
    pages[int(parts[i])] = parts[i + 1]
out = []
for n in list(range(5, 26)):
    t = pages.get(n, "")
    out.append("===== PDF page %d  (chars=%d) =====" % (n, len(t.strip())))
    out.append(t.strip()[:900])
    out.append("")
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_peek_5_25.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok")
