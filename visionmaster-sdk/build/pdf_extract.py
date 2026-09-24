# -*- coding: utf-8 -*-
"""Extract the VM FAQ PDF (V1.8.1) to markdown + report structure."""
import os, json, re
import pymupdf

SRC = r"C:\Users\Administrator\Desktop\VM FAQ手册(V1.8.1)_PDF.pdf"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\pdf_faq"
os.makedirs(OUT, exist_ok=True)

doc = pymupdf.open(SRC)
n = doc.page_count
pages = []
lows = 0
for i in range(n):
    p = doc[i]
    t = p.get_text("text")
    pages.append(t)
    if len(t.strip()) < 30:
        lows += 1

full = "\n\n".join("<!-- page %d -->\n%s" % (i + 1, t) for i, t in enumerate(pages))
with open(os.path.join(OUT, "faq_fulltext.md"), "w", encoding="utf-8") as fh:
    fh.write(full)

# try to get bookmark tree
toc = doc.get_toc(simple=True)
with open(os.path.join(OUT, "_toc.json"), "w", encoding="utf-8") as fh:
    json.dump(toc, fh, ensure_ascii=False, indent=1)

report = {
    "pages": n,
    "low_text_pages": lows,
    "total_chars": len(full),
    "toc_entries": len(toc),
    "toc_sample": toc[:60],
}
with open(os.path.join(OUT, "_report.json"), "w", encoding="utf-8") as fh:
    json.dump(report, fh, ensure_ascii=False, indent=1)
print(json.dumps({"pages": n, "low": lows, "chars": len(full), "toc": len(toc)}, ensure_ascii=False))
