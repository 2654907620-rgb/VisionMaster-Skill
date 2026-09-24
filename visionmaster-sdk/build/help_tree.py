# -*- coding: utf-8 -*-
import os, json
BASE = r"D:\VisionMaster4.4.0\Applications\Help\CH"
out = []
out.append("=== daksys-webhelp tree (depth<=3) ===")
root = os.path.join(BASE, "daksys-webhelp")
for dp, dn, fn in os.walk(root):
    depth = dp[len(root):].count(os.sep)
    if depth > 3:
        dn[:] = []
        continue
    out.append("DIR " + "." * depth + " " + (dp[len(root):] or "\\") + "  (%d files)" % len(fn))
    if depth <= 2:
        for f in sorted(fn)[:25]:
            out.append("    " + f)

out.append("")
out.append("=== candidate TOC / index files in CH ===")
for dp, dn, fn in os.walk(BASE):
    for f in fn:
        lf = f.lower()
        if any(k in lf for k in ("toc", "index", "whx", "search", "context-help-map", "home")):
            out.append(os.path.join(dp, f).replace(BASE, "."))
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_help_tree.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok")
