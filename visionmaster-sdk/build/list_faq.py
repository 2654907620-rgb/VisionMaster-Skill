# -*- coding: utf-8 -*-
import json
P = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_net\_index.json"
idx = json.load(open(P, "r", encoding="utf-8"))["index"]
out = []
for it in idx:
    p = it.get("path") or []
    if p and p[0] in ("常见问题", "工具", "状态码", "编程引导", "示例程序介绍"):
        out.append("%-10s | %-40s | %s" % (it["src"][:10], " > ".join(p), it["title"]))
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_faq_list.txt", "w", encoding="utf-8").write("\n".join(out))
print("n=", len(out))
