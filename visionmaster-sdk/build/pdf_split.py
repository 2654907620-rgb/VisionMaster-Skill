# -*- coding: utf-8 -*-
"""Split the FAQ fulltext into logical parts for distillation."""
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
    ("01-nav-and-readme", "导航/版本更新记录/开发模式必读", 1, 7),
    ("02-ch1-software-usage", "第1章 VM软件使用（含环境配置/工具/全局模块/通讯）", 8, 217),
    ("03-ch2-sdk-dev-v40", "第2章 VM二次开发（VM4.0：环境配置/模块API/控件嵌入/结果获取/全局工具）", 218, 386),
    ("04-vm42-usage-and-sdk", "VM4.2 章节（常用工具和配置修改 + VM4.2 第1章/第2章）", 387, 597),
    ("05-ch3-operator-sdk", "第3章 算子SDK开发（公共工具/模块工具/控件嵌入）", 598, 702),
    ("06-ch4-algo-module", "第4章 算法模块开发（开发配置/OpenCV/Halcon联合/异常处理）", 703, 800),
    ("07-topic-cert-and-cases", "专题：认证教程 + VM应用案例", 801, 995),
    ("08-topic-guiding-and-sdk-cases", "专题：定位引导专题 + VM开发案例", 996, 1112),
    ("09-image-conversion", "专题：图像转换（C# / C++ 与各图像类型互转）", 1113, 1288),
    ("10-version-updates", "专题：版本更新（多版本切换/4.2/4.3 更新说明）", 1289, 1391),
    ("11-toolbox", "专题：宝藏工具合集（问题采集助手/定位精度评估/服务管家）", 1392, maxp),
]

manifest = []
for name, desc, a, b in RANGES:
    buf = []
    for n in range(a, b + 1):
        if n in pages:
            buf.append("<!-- page %d -->\n%s" % (n, pages[n]))
    body = "\n".join(buf)
    with open(os.path.join(OUT, name + ".md"), "w", encoding="utf-8") as fh:
        fh.write("# %s\n<!-- pages %d-%d -->\n\n%s" % (desc, a, b, body))
    manifest.append({"file": name + ".md", "desc": desc, "pages": "%d-%d" % (a, b), "chars": len(body)})

with open(os.path.join(OUT, "_manifest.json"), "w", encoding="utf-8") as fh:
    json.dump(manifest, fh, ensure_ascii=False, indent=1)
for m in manifest:
    print(m["file"], m["pages"], m["chars"])
