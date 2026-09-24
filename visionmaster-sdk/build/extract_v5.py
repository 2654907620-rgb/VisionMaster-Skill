"""VM 用户手册 模块知识 提取器 v5（最终版）
基于真实排版规律：
  · 参数名 = 独占一行的短行（下一行为其说明），说明常含「默认值为 0.5」「取值范围为 1~1000」等
  · 参数名与说明若同处一行，则以「参数名」后紧跟说明的形式出现
  · 数字/范围由 Roboto 字体标注（可用于抽取默认值/范围）
策略：先在 span 级重建行，行内用 Roboto 数字抽取「默认值/取值范围/单位」；
      再用「短行 + 后续长行」判定参数名，跨页续接。
"""
import pymupdf, re, os, json, collections

PDF = r"D:\VisionMaster4.4.0\Applications\Help\CH\Vision Master算法开发平台_用户手册_4.4.3_20251108.pdf"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\extract_v5"
os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(PDF)
toc = doc.get_toc()

# 三级书签 = 模块（13.x.y）
mods_toc = [(l, t, p) for l, t, p in toc if l == 3 and re.match(r"^13\.\d+\.\d+", t)]
print("三级书签模块数:", len(mods_toc))

NOISE = ("Vision Master 算法开发平台 用户手册", "用户手册")

def lines_of(page):
    sp = []
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b["lines"]:
            for s in l["spans"]:
                if s["text"].strip():
                    sp.append(s)
    rows = collections.defaultdict(list)
    for s in sp:
        rows[round(s["bbox"][1] / 4)].append(s)
    out = []
    for k in sorted(rows):
        parts = sorted(rows[k], key=lambda z: (round(z["bbox"][1], 0), z["bbox"][0]))
        txt = "".join(p["text"] for p in parts).strip()
        if not txt or any(n in txt for n in NOISE):
            continue
        if re.fullmatch(r"\d{1,4}", txt):
            continue
        out.append({"t": txt,
                    "x0": round(parts[0]["bbox"][0], 1),
                    "bold": any("SimHei" in p["font"] for p in parts)})
    return out

# 收集每个模块的行
raw = {}
for i, (lvl, title, pg) in enumerate(mods_toc):
    end = mods_toc[i+1][2]-1 if i+1 < len(mods_toc) else 1204
    rows = []
    for p in range(pg-1, min(end, 1204)):
        rows.extend(lines_of(doc[p]))
    raw[title] = {"pdf_from": pg, "pdf_to": end, "rows": rows}

SECTOK = ("参数配置", "运行参数", "模块参数", "模块结果", "结果说明", "结果显示",
          "使用方法", "注意事项", "基本参数", "功能简介", "应用场景", "算法原理",
          "说明", "注意", "示例", "参数说明", "结果列表")
FIGCAP = re.compile(r"^[图表]\s*13-\d+")
DEFAULTRX = re.compile(r"(默认[值]?[为是]?\s*[\d\.\-~～]+\s*(?:mm|px|ms|度|%)?|默认为?\s*[\d\.\-~～]+|默认(?:关闭|开启|启用|禁用))")
RANGERX = re.compile(r"((?:有效)?取值范围[为是]?\s*[\d\.\-~～°]+\s*(?:mm|px|度|%)?|(?:有效)?取值范围[为是]?\s*[\d\.]+\s*[~～-]\s*[\d\.]+|有效值范围[为是]?\s*[\d\.]+\s*[~～-]\s*[\d\.]+|最大可?设置为\s*[\d\.]+|最小可?设置为\s*[\d\.]+)")
ENUMRX = re.compile(r"(支持\s*[A-Za-z0-9\u4e00-\u9fff、/\+]{2,50}|可选[值项]?[为：]?\s*[^，。；]{2,60}|包括\s*[^，。；]{2,60})")
EXPLAIN = re.compile(r"^(?:以下仅介绍|以下介绍|通过配置|基本参数详情|结果显示参数详情)")

def is_param_line(txt, rows, i):
    """判定该行是否为参数名行"""
    s = txt.strip()
    if not s or len(s) > 18:
        return False
    if s in SECTOK or FIGCAP.match(s) or s.startswith(("图", "表", "●", "○", "示例")):
        return False
    if re.match(r"^\d", s) or s.endswith(("。", "，", "；", "：", "）", ")")):
        return False
    if "。" in s or "，" in s:
        return False
    if not re.search(r"[\u4e00-\u9fff]", s):
        return False
    # 下一行应是较长的说明或含默认值线索（也允许参数名后紧跟说明在同段）
    return True

def split_inline(txt):
    """一行里「参数名+说明」粘连：参数名≤14字且紧跟说明"""
    m = re.match(r"^([\u4e00-\u9fffA-Za-z0-9_/（）\-～ ]{2,16}?)(?=(?:指|设|开|选|表|当|用|默|范|单|的|为|是|：))(.{6,})$", txt)
    if m:
        n = m.group(1).strip()
        if len(n) <= 14 and not re.search(r"[，。；]", n) and n not in SECTOK:
            return n, m.group(2).strip()
    return None

def parse_mod(rows):
    mod = {"params": [], "results": [], "intro": [], "notes": []}
    zone, cur = None, None
    i = 0
    while i < len(rows):
        l = rows[i]
        t = l["t"].strip()
        i += 1
        if not t:
            continue
        if t in SECTOK:
            if t in ("参数配置", "运行参数", "模块参数"):
                zone, cur = "params", None
            elif t in ("模块结果", "结果说明", "结果显示"):
                zone, cur = "results", None
            else:
                zone, cur = "notes", None
            continue
        if FIGCAP.match(t) or re.match(r"^[●○]", t):
            continue
        if EXPLAIN.match(t):
            continue
        if zone in ("params", "results"):
            if is_param_line(t, rows, i-1):
                cur = {"name": t, "desc": "", "default": "", "range": "", "enum": "",
                       "types": "", "unit": ""}
                mod[zone].append(cur)
                continue
            if cur is None:
                # 参数名与说明同段
                si = split_inline(t)
                if si:
                    cur = {"name": si[0], "desc": si[1], "default": "", "range": "",
                           "enum": "", "types": "", "unit": ""}
                    mod[zone].append(cur); continue
                mod["intro"].append(t); continue
            cur["desc"] += t
        else:
            (mod["intro"] if zone is None else mod["notes"]).append(t)
    # 抽字段（也要对「说明」段做无参名内联切分）
    for b in ("params", "results"):
        fixed = []
        for it in mod[b]:
            d = it["desc"]
            it["default"] = " ; ".join(x.strip() for x in (m.group(0).strip() for m in DEFAULTRX.finditer(d)) if x)
            it["range"] = " ; ".join(x.strip() for x in (m.group(0).strip() for m in RANGERX.finditer(d)) if x)
            it["enum"] = " ; ".join(x.strip() for x in (m.group(0).strip() for m in ENUMRX.finditer(d)) if x)
            fixed.append(it)
        mod[b] = fixed
    return mod

allmods, summary = {}, []
for title, meta in raw.items():
    mod = parse_mod(meta["rows"])
    allmods[title] = {"pdf_from": meta["pdf_from"], "pdf_to": meta["pdf_to"], **mod}
    summary.append(f"{title:34s} 参数{len(mod['params']):3d} 结果{len(mod['results']):3d}")

json.dump(allmods, open(os.path.join(OUT, "_modules.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
open(os.path.join(OUT, "_summary.txt"), "w", encoding="utf-8").write("\n".join(summary))
print("\n".join(summary))
