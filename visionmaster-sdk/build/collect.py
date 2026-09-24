# -*- coding: utf-8 -*-
import re, os, glob
KB = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb"
# 1) full text of PDF pages 10-16
txt = open(os.path.join(KB, "pdf_faq", "faq_fulltext.md"), "r", encoding="utf-8").read()
parts = re.split(r"<!-- page (\d+) -->\n", txt)
pages = {}
for i in range(1, len(parts), 2):
    pages[int(parts[i])] = parts[i + 1]
buf = []
for n in range(10, 17):
    buf.append("\n=========== PDF page %d ===========\n" % n)
    buf.append(pages.get(n, "").strip())
open(os.path.join(KB, "_nav_pages_10_16.txt"), "w", encoding="utf-8").write("\n".join(buf))

# 2) headings of all distilled files
out = []
for f in sorted(glob.glob(os.path.join(KB, "distill", "*.md"))):
    t = open(f, "r", encoding="utf-8").read()
    out.append("\n########## %s  (%d chars) ##########" % (os.path.basename(f), len(t)))
    for ln in t.split("\n"):
        if re.match(r"^#{1,3} ", ln):
            out.append(ln.strip())
open(os.path.join(KB, "_distill_headings.txt"), "w", encoding="utf-8").write("\n".join(out))
print("ok")
