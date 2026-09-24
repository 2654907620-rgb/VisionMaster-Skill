# -*- coding: utf-8 -*-
"""Parse FAQ PDF table-of-contents (pages 2..10) into a structured outline."""
import os, re, json

P = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\pdf_faq\faq_fulltext.md"
with open(P, "r", encoding="utf-8") as fh:
    txt = fh.read()
parts = re.split(r"<!-- page (\d+) -->\n", txt)
pairs = {}
for i in range(1, len(parts), 2):
    pairs[int(parts[i])] = parts[i + 1]

toc_text = "\n".join(pairs.get(n, "") for n in range(2, 12))

# TOC line pattern:  "1.2.3 <title> ..... 57"
entries = []
for ln in toc_text.split("\n"):
    s = ln.strip()
    if not s:
        continue
    m = re.match(r"^(\d+(?:\.\d+){0,3})\s+(.+?)[\s.·]{2,}(\d{1,4})\s*$", s)
    if not m:
        m2 = re.match(r"^(.+?)[\s.·]{4,}(\d{1,4})\s*$", s)
        if m2:
            entries.append({"num": "", "title": m2.group(1).strip(), "page": int(m2.group(2)), "raw": s})
        continue
    entries.append({"num": m.group(1), "title": m.group(2).strip(), "page": int(m.group(3)), "raw": s})

out = []
out.append("TOC ENTRIES: %d" % len(entries))
for e in entries:
    out.append("%-10s %-90s p%s" % (e["num"], e["title"], e["page"]))
with open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_faq_toc.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))
with open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\pdf_faq\_toc_parsed.json", "w", encoding="utf-8") as fh:
    json.dump(entries, fh, ensure_ascii=False, indent=1)
print("ok", len(entries))
