# -*- coding: utf-8 -*-
"""Split help_bundles C and F into per-category files (by trail level-2 under 模块使用参考)."""
import os, re, io, json

KB = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb"
BD = os.path.join(KB, "help_bundles")
OUT = os.path.join(KB, "help_parts")
os.makedirs(OUT, exist_ok=True)

MARK = re.compile(r"^<!--\s*=====\s*([^|]+?)\s*\|\s*(.*?)\s*=====\s*-->\s*$", re.M)

def split_bundle(fn):
    p = os.path.join(BD, fn)
    raw = io.open(p, "r", encoding="utf-8", errors="replace").read()
    ms = list(MARK.finditer(raw))
    if not ms:
        print("NO MARKS in", fn)
        return
    blocks = []
    for i, m in enumerate(ms):
        start = m.start()
        end = ms[i + 1].start() if i + 1 < len(ms) else len(raw)
        blocks.append((m.group(2).strip(), raw[start:end]))
    groups = {}
    order = []
    for trail, body in blocks:
        parts = [x.strip() for x in trail.split(">")]
        if parts and parts[0] == "模块使用参考" and len(parts) >= 2:
            cat = parts[1]
        else:
            cat = parts[0] if parts else "其他"
        if cat not in groups:
            groups[cat] = []
            order.append(cat)
        groups[cat].append(body)
    print("== %s ==" % fn)
    for cat in order:
        txt = "\n".join(groups[cat])
        safe = {"定位": "locate", "图像处理": "imgproc", "图形生成": "shape",
                "识别": "recog", "缺陷检测": "defect", "边缘学习": "edgeln", "深度学习": "dl"}.get(cat, cat)
        outp = os.path.join(OUT, "%s-%s.md" % (fn[0], safe))
        io.open(outp, "w", encoding="utf-8").write(txt)
        n = len(groups[cat])
        print("  %-8s pages=%3d chars=%7d -> %s" % (cat, n, len(txt), os.path.basename(outp)))

split_bundle("C-mod-locate-imgproc.md")
split_bundle("F-mod-recog-dl-edge.md")
print("DONE")
