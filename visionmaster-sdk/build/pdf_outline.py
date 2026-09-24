# -*- coding: utf-8 -*-
"""Outline detection for the VM FAQ PDF."""
import os, re, json

P = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\pdf_faq\faq_fulltext.md"
with open(P, "r", encoding="utf-8") as fh:
    txt = fh.read()

pages = re.split(r"<!-- page (\d+) -->\n", txt)
# pages[0] is preamble; then pairs
pairs = []
for i in range(1, len(pages), 2):
    num = int(pages[i]); body = pages[i + 1]
    pairs.append((num, body))

lines = []
lines.append("PAGES: %d" % len(pairs))
lines.append("=== FIRST 3 PAGES ===")
for num, body in pairs[:3]:
    lines.append("--- page %d ---" % num)
    lines.append(body[:2500])

# heading candidate patterns
pat = re.compile(r"^\s*(\d+(?:\.\d+){0,3})[\.\s、]+\S")
pat2 = re.compile(r"^\s*第[一二三四五六七八九十百零\d]+[章节部分]\s*\S*")
heads = []
for num, body in pairs:
    for ln in body.split("\n"):
        s = ln.strip()
        if not s or len(s) > 60:
            continue
        if pat.match(s) or pat2.match(s):
            heads.append((num, s))
lines.append("")
lines.append("=== HEADING CANDIDATES (%d) ===" % len(heads))
for num, s in heads:
    lines.append("p%-5d %s" % (num, s))

with open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_faq_outline.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print("ok", len(heads))
