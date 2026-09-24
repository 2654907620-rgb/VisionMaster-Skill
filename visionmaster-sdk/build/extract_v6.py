"""VM 用户手册 模块知识 提取器 v6（定稿）
根治 v5 的两个顽疾：
  1. 用 PyMuPDF 原生 line（而非 y 聚类）重建行，避免 int/image/float 类型词被拆散乱序；
  2. 类型词（int/float/string/image/binary/point/box 等）仅作补充字段，不参与正文。
同时修正 zone 切换顺序，确保「参数配置 / 模块结果」正确切区。
"""
import pymupdf, re, os, json

PDF = r"D:\VisionMaster4.4.0\Applications\Help\CH\Vision Master算法开发平台_用户手册_4.4.3_20251108.pdf"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\extract_v6"
os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(PDF)
toc = doc.get_toc()
mods_toc = [(t, p) for l, t, p in toc if l == 3 and re.match(r"^13\.\d+\.\d+", t)]
print("模块数:", len(mods_toc))

NOISE = ("Vision Master 算法开发平台 用户手册", "用户手册")
TYPES = {"int", "float", "bool", "string", "binary", "double", "image", "point",
         "box", "line", "circle", "region", "struct", "annull", "roi", "void",
         "byte", "long", "short", "array", "matrix", "xml"}

def native_lines(page):
    """按 PyMuPDF 原生 line 还原，保留阅读顺序"""
    out = []
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b["lines"]:
            # 同一 line 内多 span 按 x 排序拼接
            parts = sorted(l["spans"], key=lambda s: s["bbox"][0])
            txt = "".join(s["text"] for s in parts).strip()
            if not txt:
                continue
            if any(n in txt for n in NOISE):
                continue
            if re.fullmatch(r"\d{1,4}", txt):
                continue
            # 纯类型词行（如 "int" "image"）先保留，后续合并到上一条
            bold = any("SimHei" in s["font"] for s in parts)
            out.append({"t": txt, "bold": bold})
    return out

def collect(pg_from, pg_to):
    rows = []
    for p in range(pg_from - 1, min(pg_to, 1204)):
        rows.extend(native_lines(doc[p]))
    return rows

SECTOK = {"参数配置", "运行参数", "模块参数", "模块结果", "结果说明", "结果显示"}
SKIP_ONLY = {"说明", "注意", "示例", "基本参数", "应用场景", "算法原理", "功能简介",
             "使用方法", "术语介绍", "模块介绍", "参数说明", "结果列表", "前后序模块"}
FIGCAP = re.compile(r"^[图表]\s*13-\d+")
EXPLAIN = re.compile(r"^(以下仅介绍|以下介绍|通过配置|基本参数详情|结果显示参数详情|具体如下|如下所示)")
# 过滤：图例名（含"示例""示意图""图"结尾）、章导语（含 "13.xx 标题" 粘连）
FIGNAME = re.compile(r"(示例|示意图|流程图|效果图|对比图|框图|连线图)$")
CHBLURB = re.compile(r"^13\.\d+\s*[\u4e00-\u9fff]")
MODPRINCIPLE = re.compile(r"^(模块原理|模块说明|算法原理|原理介绍|模块介绍)$")
DEFAULTRX = re.compile(r"(默认[值]?[为是]?\s*[\d\.\-~～]+\s*(?:mm|px|ms|度|s|%)?|默认为?\s*[\d\.\-~～]+|默认(?:关闭|开启|启用|禁用|不勾选|勾选))")
RANGERX = re.compile(r"((?:有效)?取值范围[为是]?\s*[\d\.\-~～]+\s*(?:mm|px|度|%)?|(?:有效)?取值范围[为是]?\s*[\d\.]+\s*[~～-]\s*[\d\.]+|(?:有效值范围|取值范围)[为是]?\s*[^，。；]{0,24}|最大可?设置为\s*[\d\.]+|最小可?设置为\s*[\d\.]+)")
ENUMRX = re.compile(r"(支持\s*[A-Za-z0-9\u4e00-\u9fff、/\+]{2,50}|可选[值项]?[为：]?\s*[^，。；]{2,60}|包括\s*[^，。；]{2,60})")
TYPERX = re.compile(r"\b(int|float|bool|string|binary|double|image|point|box|line|circle|region|struct|annull|byte|long|short|array|matrix|xml)\b\s*型?")

def is_param_name(txt):
    s = txt.strip()
    if not s or len(s) > 20:
        return False
    if s in SECTOK or s in SKIP_ONLY or FIGCAP.match(s):
        return False
    if FIGNAME.search(s) or CHBLURB.match(s) or MODPRINCIPLE.match(s):
        return False
    if s.startswith(("图", "表", "●", "○", "◆")):
        return False
    if re.match(r"^[a-zA-Z]{1,7}$", s) and s.lower() in TYPES:
        return False  # 纯类型词
    if re.match(r"^\d", s):
        return False
    if s.endswith(("。", "，", "；", "：", "）", ")")):
        return False
    if "。" in s or "，" in s:
        return False
    if not re.search(r"[\u4e00-\u9fff]", s):
        return False
    return True

def new_item(name):
    return {"name": name, "desc": "", "default": "", "range": "", "enum": "", "types": ""}

def parse(rows):
    m = {"params": [], "results": [], "intro": [], "notes": []}
    zone, cur = None, None
    intro_closed = False
    for i, l in enumerate(rows):
        t = l["t"].strip()
        if not t:
            continue
        if t in SECTOK or t in ("模块结果", "结果说明", "结果显示"):
            zone = "params" if t in ("参数配置", "运行参数", "模块参数") else "results"
            cur = None
            intro_closed = True
            continue
        if FIGCAP.match(t) or MODPRINCIPLE.match(t):
            continue
        if EXPLAIN.match(t) or CHBLURB.match(t):
            continue
        if t in SKIP_ONLY:
            zone, cur = (zone, None) if zone else (None, None)
            continue
        if re.match(r"^[●○◆]", t):
            continue
        # 参数名的续行若只是纯类型词，补到上一条
        if re.fullmatch(r"[a-zA-Z ]{1,10}", t) and t.strip().lower() in TYPES:
            if cur is not None:
                cur["desc"] += t
            continue
        if zone in ("params", "results"):
            if is_param_name(t):
                cur = new_item(t)
                m[zone].append(cur)
            elif cur is not None:
                cur["desc"] += t
            elif not intro_closed:
                m["intro"].append(t)
            else:
                m["notes"].append(t)
        else:
            m["intro"].append(t)
    for b in ("params", "results"):
        for it in m[b]:
            d = it["desc"]
            it["default"] = " ; ".join(x.strip() for x in (x.group(0).strip() for x in DEFAULTRX.finditer(d)) if x)
            it["range"] = " ; ".join(x.strip() for x in (x.group(0).strip() for x in RANGERX.finditer(d)) if x)
            it["enum"] = " ; ".join(x.strip() for x in (x.group(0).strip() for x in ENUMRX.finditer(d)) if x)
            it["types"] = " ".join(sorted(set(TYPERX.findall(d))))
    return m

allmods, summary = {}, []
for i, (title, pg) in enumerate(mods_toc):
    end = mods_toc[i+1][1] - 1 if i+1 < len(mods_toc) else 1204
    m = parse(collect(pg, end))
    allmods[title] = {"pdf_from": pg, "pdf_to": end, **m}
    summary.append(f"{title:32s} 参数{len(m['params']):3d} 结果{len(m['results']):3d}")

json.dump(allmods, open(os.path.join(OUT, "_modules.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(OUT, "_summary.txt"), "w", encoding="utf-8").write("\n".join(summary))
print("\n".join(summary))
