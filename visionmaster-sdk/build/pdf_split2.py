# -*- coding: utf-8 -*-
"""Split the FAQ fulltext into logical parts (corrected page offset: PDF page = printed page + 9)."""
import os, re, json

SRC = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\pdf_faq\faq_fulltext.md"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\faq_parts"
os.makedirs(OUT, exist_ok=True)

with open(SRC, "r", encoding="utf-8") as fh:
    txt = fh.read()
parts = re.split(r"<!-- page (\d+) -->\n", txt)
pages = {}
for i in range(1, len(parts), 2):
    pages[int(parts[i])] = parts[i + 1]
maxp = max(pages)

RANGES = [
    ("01-nav-and-readme", "法律声明/导航/运行环境/使用说明/版本更新记录/VM开发模式必读", 10, 16),
    ("07a-cert-tutorials", "专题·认证教程（VM4.2/4.3 中级教程：SDK开发/算子SDK/算法模块/标定定位）", 810, 945),
    ("08-cases-and-guiding", "专题·VM应用案例 + 定位引导专题 + VM开发案例", 946, 1121),
    ("09-image-conversion", "专题·图像转换（C#/C++ 与各图像类型互转）", 1122, 1297),
    ("10-version-updates", "专题·版本更新（多版本切换 / 4.2 / 4.3 更新说明）", 1298, 1400),
    ("11-toolbox", "专题·宝藏工具合集（问题采集助手/定位精度评估/服务管家）", 1401, maxp),
    ("12-ch4-tail", "第4章尾部（4.3.1 结束 + 4.4 异常处理）", 801, 809),
]

manifest = []
for name, desc, a, b in RANGES:
    buf = []
    for n in range(a, b + 1):
        if n in pages:
            buf.append("<!-- page %d -->\n%s" % (n, pages[n]))
    body = "\n".join(buf)
    with open(os.path.join(OUT, name + ".md"), "w", encoding="utf-8") as fh:
        fh.write("# %s\n<!-- pdf pages %d-%d -->\n\n%s" % (desc, a, b, body))
    manifest.append({"file": name + ".md", "desc": desc, "pdf_pages": "%d-%d" % (a, b), "chars": len(body)})

with open(os.path.join(OUT, "_manifest.json"), "w", encoding="utf-8") as fh:
    json.dump(manifest, fh, ensure_ascii=False, indent=1)
print("done")
