"""VM 用户手册模块参数/结果 精确解析器 v3
关键发现：PDF 里「参数名」与「说明」**直接相连**（无空格），如
   「通道下限指定颜色空间内，用来存储、传递与颜色相关的图像信息的通道抽取像素的最小值。」
   「颜色空间支持RGB、HSV、HSI 三种颜色空间，...」
所以先按标点断句成句，再用「句首短名词 + 后续解释」拆分。
"""
import re, os, json

SRC = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\man_mdparts"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\extract_mod3"
os.makedirs(OUT, exist_ok=True)

NOISE = re.compile(r"^\s*(Vision Master 算法开发平台 用户手册|用户手册)\s*$")
FIGCAP = re.compile(r"^\s*图\s*13-\d+")
PAGEMARK = re.compile(r"^\s*=====\s*PDF页\s*\d+\s*=====\s*$")
HEADNUM = re.compile(r"^\s*\d+(\.\d+)+\s")
SECTION = re.compile(r"^(参数配置|运行参数|模块结果|结果说明|使用方法|功能简介|注意事项|说明|注意|示例)")

def load(name):
    t = open(os.path.join(SRC, name), encoding="utf-8", errors="ignore").read()
    return [ln.rstrip() for ln in t.splitlines()]

def clean(lines):
    keep = []
    for ln in lines:
        s = ln.strip()
        if not s or NOISE.match(s) or FIGCAP.match(s):
            continue
        keep.append(s)
    return keep

def join_lines(lines):
    """只做必要的断行拼接：行尾是中文字且无终止标点，则与下一行相接"""
    out, buf = [], ""
    for s in lines:
        if PAGEMARK.match(s):
            if buf: out.append(buf); buf = ""
            continue
        if not buf:
            buf = s; continue
        if buf[-1] in "。：；！？)）】”" or len(buf) > 120:
            out.append(buf); buf = s
        else:
            buf += s
    if buf: out.append(buf)
    return out

def split_sentences(text):
    """按中文标点切句，保留标点"""
    parts = re.split(r"(?<=[。；！？])", text)
    return [p.strip() for p in parts if p.strip()]

# 参数行特征：整行 = 名词短语 + 说明（名词短语 ≤ 14 字，且不含逗号）
def try_split_named(s):
    m = re.match(r"^([\u4e00-\u9fffA-Za-z0-9_/（）\(\)\-～~ ]{2,20}?)(?=[指支表当用设开选默范单同，。])(.{6,})$", s)
    if not m:
        return None
    name, desc = m.group(1).strip(), m.group(2).strip()
    if len(name) > 14 or re.search(r"[，。；：]", name):
        return None
    if name in ("说明", "注意", "示例", "使用方法", "参数配置", "模块结果"):
        return None
    return name, desc

DEFAULT = re.compile(r"(默认[值]?[为是]?\s*[^。；，]{0,30}|默认为\s*[\d\.]+|[^，。；]{0,12}默认为\s*[\d\.]+|最大可?设置为\s*[\d\.]+|最小可?设置为\s*[\d\.]+|取值范围为?\s*[^。；]{0,50})")
ENUMS = re.compile(r"(支持\s*[A-Za-z0-9\u4e00-\u9fff、/\+]{2,50}|可选[值为]?[：]?\s*[^。；]{2,60}|包括\s*[^。；]{2,60})")
TYPES = re.compile(r"((?:int|float|bool|string|binary|double|annull|box|point|line|circle|region|struct|枚举|整型|浮点|布尔|字符串|数值|型))")
UNIT = re.compile(r"(ms|mm|px|度|像素|百分比|%)")

def parse(name, block, prefix):
    lines = join_lines(clean(block))
    # 去掉模块自身编号标题行
    lines = [l for l in lines if not HEADNUM.match(l)]
    mod = {"name": name, "intro": [], "param_notes": [], "params": [],
           "results": [], "notes": [], "raw_paragraphs": []}
    mode = "intro"
    for s in lines:
        st = s.strip()
        if HEADNUM.match(st):
            continue
        if re.match(r"^(参数配置|运行参数)", st):
            mode = "param"; continue
        if re.match(r"^(模块结果|结果说明)", st):
            mode = "result"; continue
        if re.match(r"^(说明|注意)$", st):
            mode = "note"; continue
        if re.match(r"^(基本参数|结果显示)", st):
            continue
        if mode == "intro":
            mod["intro"].append(st[:400])
            continue
        if mode == "note":
            mod["notes"].append(st[:300])
            continue
        # param / result 区：逐句，首句尝试拆「名+说明」
        b = "params" if mode == "param" else "results"
        for sent in split_sentences(st):
            nm = try_split_named(sent)
            if nm:
                n_, d_ = nm
                mod[b].append({"name": n_, "desc": d_})
            else:
                # 归属到上一条的 desc 补充
                if mod[b]:
                    mod[b][-1]["desc"] += sent
                else:
                    mod["raw_paragraphs"].append(sent[:300])
        # 整行未被切句时（无标点），也尝试拆分
        if st and not re.search(r"[。；！？]", st):
            nm = try_split_named(st)
            if nm and (not mod[b] or mod[b][-1]["name"] != nm[0]):
                mod[b].append({"name": nm[0], "desc": nm[1]})
    # 抽字段
    for b in ("params", "results"):
        for it in mod[b]:
            d = it["desc"]
            it["default"] = " / ".join(m.group(0).strip() for m in DEFAULT.finditer(d))
            it["enum"] = " / ".join(m.group(0).strip() for m in ENUMS.finditer(d))
            it["types"] = " ".join(sorted(set(x[0] for x in TYPES.findall(d))))
            it["unit"] = " ".join(sorted(set(x[0] for x in UNIT.findall(d))))
    return mod

JOBS = [
    ("14-第13章-模块使用参考__13-6-边缘学习.md", "13.6", "20-mod-edge-learning"),
    ("14-第13章-模块使用参考__13-7-深度学习.md", "13.7", "21-mod-deep-learning"),
    ("14-第13章-模块使用参考__13-8-标定.md", "13.8", "22-mod-calibration"),
    ("14-第13章-模块使用参考__13-9-运算.md", "13.9", "23-mod-arithmetic"),
    ("14-第13章-模块使用参考__13-10-图像处理.md", "13.10", "24-mod-image-process"),
    ("14-第13章-模块使用参考__13-11-颜色处理.md", "13.11", "25-mod-color"),
    ("14-第13章-模块使用参考__13-12-拆分组合.md", "13.12", "26-mod-split-merge"),
    ("14-第13章-模块使用参考__13-13-图形生成.md", "13.13", "27-mod-graphic-gen"),
    ("14-第13章-模块使用参考__13-14-逻辑工具.md", "13.14", "28-mod-logic-tool"),
    ("14-第13章-模块使用参考__13-15-通信.md", "13.15", "29-mod-communication"),
]
TITLES = {"20-mod-edge-learning":"边缘学习","21-mod-deep-learning":"深度学习","22-mod-calibration":"标定",
 "23-mod-arithmetic":"运算","24-mod-image-process":"图像处理","25-mod-color":"颜色处理",
 "26-mod-split-merge":"拆分组合","27-mod-graphic-gen":"图形生成","28-mod-logic-tool":"逻辑工具",
 "29-mod-communication":"通信"}

def split_modules(lines, prefix):
    pat = re.compile(rf"^{re.escape(prefix)}\.(\d+)\s+(\S.*)$")
    idx = [(i, m.group(1), m.group(2).strip()) for i, ln in enumerate(lines) if (m := pat.match(ln.strip()))]
    return [(n, nm, lines[i:(idx[j+1][0] if j+1 < len(idx) else len(lines))])
            for j,(i,n,nm) in enumerate(idx)]

allj, summary = {}, []
for fn, prefix, tag in JOBS:
    mods = split_modules(load(fn), prefix)
    parsed = [parse(nm, blk, prefix) for _, nm, blk in mods]
    allj[tag] = {"prefix": prefix, "title": TITLES[tag], "modules": parsed}
    np = sum(len(m["params"]) for m in parsed)
    nr = sum(len(m["results"]) for m in parsed)
    nd = sum(1 for m in parsed for p in m["params"] if p["default"])
    summary.append(f"{tag:26s} 模块{len(parsed):3d} 参数{np:4d} 结果{nr:4d} 含默认值{nd:4d}")

json.dump(allj, open(os.path.join(OUT,"_parsed.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_parsed3_summary.txt","w",encoding="utf-8").write("\n".join(summary))
print("\n".join(summary))
