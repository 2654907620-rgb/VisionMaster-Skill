# -*- coding: utf-8 -*-
"""Parse the Oxygen WebHelp TOC embedded in CH/index.html (ul.menu_toc_ul)."""
import os, re, json
from bs4 import BeautifulSoup

BASE = r"D:\VisionMaster4.4.0\Applications\Help\CH"
KB = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb"

raw = open(os.path.join(BASE, "index.html"), "r", encoding="utf-8", errors="ignore").read()
soup = BeautifulSoup(raw, "lxml")
root = soup.find("ul", class_=lambda c: c and "menu_ul" in c)
out = []
if root is None:
    out.append("NO menu_ul FOUND")
    classes = set()
    for ul in soup.find_all("ul"):
        cl = ul.get("class")
        if cl:
            classes.update(cl)
    out.append("UL CLASSES: " + ", ".join(sorted(classes)))
else:
    out.append("FOUND " + " ".join(root.get("class")))
    entries = []

    def walk(ul, depth, trail):
        for li in ul.find_all("li", recursive=False):
            a = li.find("a", recursive=False)
            name = ""
            href = ""
            if a is not None:
                name = a.get_text(" ", strip=True)
                href = (a.get("href") or "").strip()
            sub = li.find("ul", recursive=False)
            mytrail = trail + [name] if name else trail
            if name:
                entries.append({"depth": depth, "name": name, "href": href, "trail": list(mytrail)})
            if sub is not None:
                walk(sub, depth + 1, mytrail)

    walk(root, 0, [])
    out.append("ENTRIES: %d" % len(entries))
    for e in entries:
        out.append("%s%s  ->  %s" % ("  " * e["depth"], e["name"], e["href"]))
    json.dump(entries, open(os.path.join(KB, "_help_toc.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

open(os.path.join(KB, "_help_toc.txt"), "w", encoding="utf-8").write("\n".join(out))
print("ok")
