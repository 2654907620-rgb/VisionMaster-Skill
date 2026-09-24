# -*- coding: utf-8 -*-
import os, json
MD = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_net"
idx = json.load(open(os.path.join(MD, "_index.json"), "r", encoding="utf-8"))["index"]
want = []
for it in idx:
    p = it.get("path") or []
    if not p:
        continue
    joined = " > ".join(p)
    if joined in ("编程引导 > 配置流程 > WPF框架", "编程引导 > 配置流程 > WinForm框架",
                  "编程引导 > 配置流程 > 动态库介绍及添加说明",
                  "编程引导 > 方案相关操作", "编程引导 > 模块相关操作", "编程引导 > 流程相关操作",
                  "编程引导 > Group相关操作", "编程引导 > 全局模块相关操作",
                  "编程引导 > 控件相关调用", "编程引导 > 事件 > 事件设置方法",
                  "编程引导 > 事件 > 事件类型"):
        want.append(it)
buf = []
for it in want:
    buf.append("\n\n<!-- ===== %s ===== -->\n" % " > ".join(it["path"]))
    buf.append(open(os.path.join(MD, it["src"][:-5] + ".md"), "r", encoding="utf-8").read())
out = "\n".join(buf)
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_core_objects_src.md", "w", encoding="utf-8").write(out)
print("pages", len(want), "chars", len(out))
