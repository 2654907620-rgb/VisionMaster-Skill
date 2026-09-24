# -*- coding: utf-8 -*-
"""把 VM 应用帮助文档按主题打成 bundle，供子代理逐个提炼。"""
import os, json

D = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\help_md"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\help_bundles"
os.makedirs(OUT, exist_ok=True)

idx = json.load(open(os.path.join(D, "_index.json"), "r", encoding="utf-8"))["index"]
toc = json.load(open(os.path.join(D, "_toc.json"), "r", encoding="utf-8"))
# preserve TOC order
order = {}
for e in toc:
    if e["href"] and e["href"] not in order:
        order[e["href"]] = len(order)
idx_sorted = sorted(idx, key=lambda it: order.get(it["src"], 10 ** 6))

def sel(pred):
    return [it for it in idx_sorted if pred(it.get("path") or [])]

GROUPS = [
    ("A-overview-and-setup", "概览 · 方案搭建",
     lambda p: p and (p[0] in ("前言", "法律声明", "发版说明", "产品概述", "快速入门")
                      or p[0].startswith("方案搭建"))),
    ("B-debug-tools-troubleshoot", "调试运行 · 通用设置 · 工具 · 问题排查",
     lambda p: p and (p[0] in ("方案调试与运行", "软件通用设置", "工具介绍", "问题排查", "常见问题"))),
    ("C-mod-locate-imgproc", "模块参考：定位 / 图像处理 / 图形生成",
     lambda p: len(p) >= 2 and p[0] == "模块使用参考" and p[1] in ("定位", "图像处理", "图形生成")),
    ("D-mod-logic-comm-acq", "模块参考：逻辑工具 / 通信 / 采集 / 拆分组合",
     lambda p: len(p) >= 2 and p[0] == "模块使用参考" and p[1] in ("逻辑工具", "通信", "采集", "拆分组合")),
    ("E-mod-measure-calc-calib", "模块参考：测量 / 运算 / 标定 / 颜色处理",
     lambda p: len(p) >= 2 and p[0] == "模块使用参考" and p[1] in ("测量", "运算", "标定", "颜色处理")),
    ("F-mod-recog-dl-edge", "模块参考：识别 / 缺陷检测 / 深度学习 / 边缘学习",
     lambda p: len(p) >= 2 and p[0] == "模块使用参考" and p[1] in ("识别", "缺陷检测", "深度学习", "边缘学习")),
]

manifest = []
for name, desc, pred in GROUPS:
    items = sel(pred)
    buf = ["# %s\n<!-- VM 应用帮助文档（CH WebHelp）分片，共 %d 页 -->\n" % (desc, len(items))]
    for it in items:
        p = os.path.join(D, it["src"][:-5] + ".md")
        buf.append("\n\n<!-- ===== %s | %s ===== -->\n" % (it["src"], " > ".join(it.get("path") or [])))
        buf.append(open(p, "r", encoding="utf-8").read())
    body = "\n".join(buf)
    with open(os.path.join(OUT, name + ".md"), "w", encoding="utf-8") as fh:
        fh.write(body)
    manifest.append({"file": name + ".md", "desc": desc, "pages": len(items), "chars": len(body)})
    print(name, len(items), len(body))

# sanity: any page not covered?
covered = set()
for name, desc, pred in GROUPS:
    for it in sel(pred):
        covered.add(it["src"])
missed = [it for it in idx if it["src"] not in covered]
print("MISSED:", [(it["src"], it.get("path")) for it in missed][:30])
json.dump(manifest, open(os.path.join(OUT, "_manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
