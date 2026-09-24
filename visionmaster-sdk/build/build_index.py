# -*- coding: utf-8 -*-
"""Build a compact API index + module catalog from converted CHM markdown."""
import os, json, re

MD = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_net"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb"
with open(os.path.join(MD, "_index.json"), "r", encoding="utf-8") as fh:
    data = json.load(fh)
idx = data["index"]

def brief_of(src):
    p = os.path.join(MD, src[:-5] + ".md")
    try:
        t = open(p, "r", encoding="utf-8").read(4000)
    except Exception:
        return ""
    t = re.sub(r"^<!--.*?-->\n", "", t, flags=re.S)
    t = re.sub(r"^#\s*.*?\n", "", t, flags=re.S)
    lines = [l.strip() for l in t.split("\n") if l.strip()]
    for l in lines:
        if l.startswith(("#", "|", "-", "*", "!", "<!--")):
            continue
        if len(l) < 4:
            continue
        return l[:160]
    return ""

# ---- module catalog: 接口函数 > <大类> > <模块> ----
cat = {}
for it in idx:
    p = it.get("path") or []
    if len(p) >= 3 and p[0] == "接口函数":
        cat.setdefault(p[1], {}).setdefault(p[2], []).append(it)

lines = []
lines.append("# VisionMaster .NET SDK 接口函数目录（按大类/模块）\n")
for big in sorted(cat.keys()):
    mods = cat[big]
    lines.append("\n## %s（%d 个模块）" % (big, len(mods)))
    for mod in sorted(mods.keys()):
        items = mods[mod]
        brief = ""
        for it in items:
            b = brief_of(it["src"])
            if b:
                brief = b
                break
        lines.append("- **%s** — %s" % (mod, brief))

with open(os.path.join(OUT, "_module_catalog.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))

# ---- API index: all class/group pages with path ----
lines2 = []
lines2.append("# 类索引（class_*.html）\n")
n = 0
for it in idx:
    src = it["src"].lower()
    if src.startswith(("class_", "struct_", "interface_", "namespace")):
        p = " > ".join(it.get("path") or [])
        lines2.append("| %s | %s | %s |" % (it["title"] or it["src"], p, it["src"]))
        n += 1
with open(os.path.join(OUT, "_class_index.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines2))
print("ok classes=%d" % n)
