"""把 extract_v6 的结构化模块数据渲染成 skill 参考文件
产出：
  11-modules-params/00-INDEX.md        模块总索引（按大类分组，标注页范围）
  11-modules-params/<大类>.md          每个模块的参数表 + 结果表
同时更新 04-modules-catalog.md 的索引指向。
"""
import json, re, os, collections

SRC = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\extract_v6\_modules.json"
DST = r"C:\Users\Administrator\.workbuddy\skills\visionmaster-sdk\references\11-modules-params"
os.makedirs(DST, exist_ok=True)
D = json.load(open(SRC, encoding="utf-8"))

# 大类名：13.x 的章名（从 TOC 一级/二级标题推）。这里用固定映射（对齐 VM 模块树）
CAT = {
    "13.1": "采集", "13.2": "定位", "13.3": "测量", "13.4": "识别",
    "13.5": "缺陷检测", "13.6": "边缘学习", "13.7": "深度学习", "13.8": "标定",
    "13.9": "运算", "13.10": "图像处理", "13.11": "颜色处理", "13.12": "拆分组合",
    "13.13": "图形生成", "13.14": "逻辑工具", "13.15": "通信",
}

def cat_of(title):
    m = re.match(r"^(13\.\d+)\.", title)
    return CAT.get(m.group(1), "其他") if m else "其他"

groups = collections.defaultdict(list)
for title, v in D.items():
    groups[cat_of(title)].append((title, v))

def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()

# 从 04-modules-catalog.md 抽模块一句话职责
CATALOG = r"C:\Users\Administrator\.workbuddy\skills\visionmaster-sdk\references\04-modules-catalog.md"
DESC = {}
try:
    cur_cat = None
    for ln in open(CATALOG, encoding="utf-8"):
        s = ln.strip()
        m = re.match(r"^##\s*(.+?)（\d+\s*个模块）", s)
        if m:
            cur_cat = m.group(1)
            continue
        m = re.match(r"^-\s*\*\*(.+?)\*\*\s*—\s*(.+)$", s)
        if m:
            DESC[m.group(1).strip()] = m.group(2).strip()
except Exception as e:
    print("catalog 读取失败:", e)

def clean_desc(d):
    """清理粘连的图注/类型词残留"""
    d = re.sub(r"(图|表)\s*13-\d+\s*[\u4e00-\u9fff]*", "", d)
    d = re.sub(r"13\.\d+\s*[\u4e00-\u9fff]{2,}[^。]{0,60}?是对", "。", d)
    d = re.sub(r"\s{2,}", " ", d)
    return d.strip("。；， ")[:400]

lines_idx = ["# 模块参数与结果参考（官方《VM 用户手册 V4.4.3》第 13 章全量）", ""]
lines_idx += [f"> 覆盖 15 大类 · **{len(D)} 个算法模块** · "
              f"**{sum(len(v['params']) for v in D.values())} 条参数** · "
              f"**{sum(len(v['results']) for v in D.values())} 条结果输出**", "",
              "> 每行：`模块` → 参数数 / 结果数 / 手册 PDF 页范围。点进大类文件看参数全表。", ""]

for cat in ["采集","定位","测量","识别","缺陷检测","边缘学习","深度学习","标定","运算",
            "图像处理","颜色处理","拆分组合","图形生成","逻辑工具","通信"]:
    if cat not in groups:
        continue
    items = sorted(groups[cat], key=lambda x: x[0])
    fn = f"{cat}.md"
    o = [f"# {cat} 模块参数与结果（VM 用户手册 V4.4.3）", "",
         f"共 {len(items)} 个模块。来源：官方用户手册第 13 章对应小节。", ""]
    for title, v in items:
        o.append(f"## {title}")
        o.append(f"*手册 PDF {v['pdf_from']}–{v['pdf_to']} 页*")
        o.append("")
        nm_short = title.split(" ", 1)[1] if " " in title else title
        if nm_short in DESC and not DESC[nm_short].startswith("（原文"):
            o.append(f"> {DESC[nm_short]}")
            o.append("")
        if v["params"]:
            o.append(f"**参数（{len(v['params'])}）**")
            o.append("")
            o.append("| 参数名 | 说明 | 默认值 | 取值范围/枚举 |")
            o.append("|---|---|---|---|")
            for p in v["params"]:
                desc = clean_desc(p["desc"])
                extra = " / ".join(x for x in (p["range"], p["enum"]) if x)
                o.append(f"| **{esc(p['name'])}** | {esc(desc)} | {esc(p['default']) or '—'} | {esc(extra) or '—'} |")
            o.append("")
        if v["results"]:
            o.append(f"**输出结果（{len(v['results'])}）**")
            o.append("")
            o.append("| 结果名 | 类型 | 说明 |")
            o.append("|---|---|---|")
            for p in v["results"]:
                desc = clean_desc(p["desc"])
                o.append(f"| **{esc(p['name'])}** | `{esc(p['types']) or '—'}` | {esc(desc)} |")
            o.append("")
        o.append(f"[← 返回总索引](00-INDEX.md) · [→ 模块职责速览](../04-modules-catalog.md)")
        o.append("")
    open(os.path.join(DST, fn), "w", encoding="utf-8").write("\n".join(o))
    lines_idx.append(f"### {cat}（{len(items)} 模块）")
    lines_idx.append("")
    lines_idx.append("| 模块 | 参数 | 结果 | 手册页 |")
    lines_idx.append("|---|---|---|---|")
    for title, v in items:
        nm = title.split(" ", 1)[1] if " " in title else title
        lines_idx.append(f"| [{nm}]({fn}#{title.replace(' ','-')}) | {len(v['params'])} | {len(v['results'])} | {v['pdf_from']} |")
    lines_idx.append("")

open(os.path.join(DST, "00-INDEX.md"), "w", encoding="utf-8").write("\n".join(lines_idx))
print("写出大类文件:", len(groups))
for c, it in sorted(groups.items()):
    print(f"  {c:8s} {len(it):3d} 模块  {sum(len(v['params']) for _,v in it):4d} 参数  {sum(len(v['results']) for _,v in it):4d} 结果")
