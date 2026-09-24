# -*- coding: utf-8 -*-
"""Assemble core CHM pages into a readable bundle + extract status-code tables."""
import os, json, re

MD = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_net"
OUTD = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb"
with open(os.path.join(MD, "_index.json"), "r", encoding="utf-8") as fh:
    idx = json.load(fh)["index"]

def read(src):
    p = os.path.join(MD, src[:-5] + ".md")
    return open(p, "r", encoding="utf-8").read()

def path_of(it):
    return it.get("path") or []

# ---- 1. core bundle: 编程引导 / 示例程序 / 常见问题 / 工具 / 前置章节 ----
core = []
for it in idx:
    p = path_of(it)
    if not p:
        continue
    if p[0] in ("编程引导", "示例程序介绍", "常见问题", "工具") or \
       (p[0] in ("发版说明", "软件许可", "运行环境", "版本激活和升级", "首页", "法律声明")):
        core.append(it)

buf = ["# VisionMaster .NET SDK 开发指南 — 核心章节全文\n"]
for it in core:
    buf.append("\n\n\n<!-- ===== %s | %s ===== -->\n" % (it["src"], " > ".join(path_of(it))))
    buf.append(read(it["src"]))
with open(os.path.join(OUTD, "chm_core.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(buf))

# ---- 2. status codes ----
sc = [it for it in idx if path_of(it) and path_of(it)[0] == "状态码"]
buf2 = ["# VisionMaster 状态码章节全文\n"]
for it in sc:
    buf2.append("\n\n<!-- ===== %s | %s ===== -->\n" % (it["src"], " > ".join(path_of(it))))
    buf2.append(read(it["src"]))
with open(os.path.join(OUTD, "chm_statuscodes_raw.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(buf2))

print("core pages", len(core), "status pages", len(sc))
print("core chars", sum(it["chars"] for it in core), "sc chars", sum(it["chars"] for it in sc))
