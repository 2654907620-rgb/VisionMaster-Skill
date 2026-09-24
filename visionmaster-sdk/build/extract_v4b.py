"""阶段2：从布局行中切出「模块 → 参数表/结果表」
参数名 = 行首黑体 span（bold_head），其后的宋体内容为说明。
支持多行说明续接、跨页。
"""
import json, re, os

RAW = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\extract_v4\_raw_lines.json"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\extract_v4"
raw = json.load(open(RAW, encoding="utf-8"))

CH13 = [k for k in raw if re.match(r"^13\.\d+\s", k)]

# 模块小节标题：形如 "13.11.1 颜色抽取"（独立成行，黑体）
MODSEC = re.compile(r"^13\.(\d+)\.(\d+)\s+(.+)$")
SECTOK = re.compile(r"^(参数配置|运行参数|模块结果|结果说明|使用方法|注意事项|说明|注意|基本参数|结果显示|模块参数|功能简介)\s*$")

def is_para_head(l):
    """参数名行：有黑体开头，且该黑体片段较短，且整行不只是标题"""
    bh = l.get("bold_head")
    if not bh:
        return None
    if len(bh) > 18:
        return None
    if bh.startswith(("图", "表", "说明", "注意", "示例", "●")):
        return None
    if re.match(r"^\d", bh):
        return None
    return bh

def build(rows):
    """rows: [{text,bold_head,size,bold}]  返回模块列表"""
    mods = []
    cur_mod = None
    zone = None          # param / result
    cur_item = None
    for l in rows:
        t = l["text"].strip()
        if not t:
            continue
        m = MODSEC.match(t)
        if m and l["bold"] and l["size"] >= 13:
            cur_mod = {"prefix": f"13.{m.group(1)}.{m.group(2)}", "name": m.group(3).strip(),
                       "params": [], "results": [], "intro": [], "notes": []}
            mods.append(cur_mod)
            zone, cur_item = None, None
            continue
        if cur_mod is None:
            continue
        if SECTOK.match(t):
            s = t.strip()
            if s in ("参数配置", "运行参数", "模块参数"):
                zone, cur_item = "params", None
            elif s in ("模块结果", "结果说明", "结果显示"):
                zone, cur_item = "results", None
            else:
                zone, cur_item = "notes", None
            continue
        head = is_para_head(l)
        # 说明区续接
        if head and zone in ("params", "results"):
            cur_item = {"name": head, "desc": t[len(head):].strip()}
            cur_mod[zone].append(cur_item)
            continue
        if cur_item is not None and zone in ("params", "results"):
            # 续行：仍属上一条说明（排除图注/表注）
            if not re.match(r"^[图表]\s*13-", t):
                cur_item["desc"] += t
            continue
        if zone in ("params", "results"):
            # 无黑体头的说明行 → 归到 intro/note
            (cur_mod["notes"] if zone == "notes" else cur_mod["intro"]).append(t)
        else:
            cur_mod["intro" if zone is None else "notes"].append(t)
    return mods

out = {}
for ck in CH13:
    mods = build(raw[ck]["lines"])
    out[ck] = {"title": ck, "pdf_from": raw[ck]["pdf_from"], "pdf_to": raw[ck]["pdf_to"],
               "modules": mods}
    np = sum(len(m["params"]) for m in mods)
    nr = sum(len(m["results"]) for m in mods)
    print(f"{ck:20s} 模块{len(mods):3d} 参数{np:4d} 结果{nr:4d}")

json.dump(out, open(os.path.join(OUT, "_modules.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
