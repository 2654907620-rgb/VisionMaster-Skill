# -*- coding: utf-8 -*-
import re
P = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\pdf_faq\faq_fulltext.md"
txt = open(P, "r", encoding="utf-8").read()
parts = re.split(r"<!-- page (\d+) -->\n", txt)
pages = {}
for i in range(1, len(parts), 2):
    pages[int(parts[i])] = parts[i + 1]

landmarks = [
    r"^法律声明\s*$", r"^导航\s*$", r"^版本更新记录\s*$", r"^VM 开发模式必读\s*$",
    r"VM4\.0（应用&VM SDK 开发）", r"VM4\.2（应用&VM SDK 开发）",
    r"VM 4\.x （算子SDK 和算法模块开发）", r"VM4\.2 手册查找必读",
    r"常用工具和配置修改", r"^第1 章 VM 软件使用", r"^第2 章 VM 二次开发",
    r"^第3 章 算子SDK 开发", r"^第4 章 算法模块开发", r"^专题\s*$",
    r"^1 认证教程", r"^2\.1 VM 应用案例", r"^2\.2 定位引导专题", r"^2\.3 VM 开发案例",
    r"^3 图像转换", r"^4 版本更新", r"^5 宝藏工具合集",
]
out = []
for pat in landmarks:
    rx = re.compile(pat, re.M)
    hits = []
    for n in sorted(pages):
        if rx.search(pages[n]):
            hits.append(n)
    out.append("%-45s -> %s" % (pat, hits[:8]))
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_landmarks.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok")
