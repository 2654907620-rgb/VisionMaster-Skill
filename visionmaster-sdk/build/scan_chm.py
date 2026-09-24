import os, sys, json
from collections import Counter

base = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\net"
out = []

if not os.path.isdir(base):
    out.append("MISSING: " + base)
else:
    exts = Counter()
    total = 0
    for root, dirs, files in os.walk(base):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            exts[ext] += 1
            total += 1
    out.append("TOTAL FILES: %d" % total)
    out.append("EXT COUNTS: " + json.dumps(exts.most_common(30), ensure_ascii=False))
    out.append("")
    out.append("--- TOP LEVEL ---")
    for name in sorted(os.listdir(base)):
        p = os.path.join(base, name)
        out.append(("DIR  " if os.path.isdir(p) else "FILE ") + name)

    # find toc / hhc / hhk
    out.append("")
    out.append("--- INDEX-LIKE FILES ---")
    for root, dirs, files in os.walk(base):
        for f in files:
            if f.lower().endswith((".hhc", ".hhk", ".hhp", ".htm", ".html")) and any(k in f.lower() for k in ("toc", "index", "content", "default", "main")):
                out.append(os.path.join(root, f))

with open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_scan_net.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))
print("ok")
