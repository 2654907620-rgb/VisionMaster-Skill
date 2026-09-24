"""按 PDF 真实排版提炼模块参数：参数名短行 + 说明段落（含默认值/范围）
VM 用户手册的「运行参数」实际是：参数名单独占行 → 说明段落（含默认值、取值范围、枚举）
所以不能指望表格，要做「短行=参数名，长行=说明」的状态机，并把默认值/范围抽成字段
"""
import re, os, json

SRC = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\man_mdparts"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\extract_mod2"
os.makedirs(OUT, exist_ok=True)

NOISE = re.compile(r"^\s*(Vision Master 算法开发平台 用户手册|用户手册|第13章 模块使用参考)\s*$")
FIGCAP = re.compile(r"^\s*图\s*13-\d+")
PAGEMARK = re.compile(r"^\s*=====\s*PDF页\s*\d+\s*=====\s*$")

def load(name):
    t = open(os.path.join(SRC, name), encoding="utf-8", errors="ignore").read()
    return [ln.rstrip() for ln in t.splitlines()]

def merge_paras(lines):
    """PDF 断行合并：中文行尾无标点则与下一行拼接"""
    out, buf = [], ""
    for ln in lines:
        s = ln.strip()
        if not s or PAGEMARK.match(s) or NOISE.match(s) or FIGCAP.match(s):
            if buf: out.append(buf); buf=""
            if PAGEMARK.match(s): out.append(s)
            continue
        if not buf:
            buf = s
        else:
            prev_end = buf[-1]
            if prev_end in "。：；！？)）】" or len(buf) > 90:
                out.append(buf); buf = s
            else:
                buf += s
    if buf: out.append(buf)
    return out

def split_modules(lines, prefix):
    pat = re.compile(rf"^{re.escape(prefix)}\.(\d+)\s+(\S.*)$")
    idx = [(i, m.group(1), m.group(2).strip()) for i, ln in enumerate(lines) if (m := pat.match(ln.strip()))]
    return [(n, nm, lines[i: (idx[j+1][0] if j+1 < len(idx) else len(lines))])
            for j, (i, n, nm) in enumerate(idx)]

# 参数名特征：短、无句号、不以下列词开头
STOP_HEAD = ("说明", "注意", "示例", "模块结果", "参数配置", "使用方法", "功能", "应用", "算法", "典型", "文档", "结果")
def is_param_name(s):
    if len(s) > 16 or not s:
        return False
    if s.endswith(("。", "，", "：", "；")):
        return False
    if s.startswith(STOP_HEAD) or s.startswith("图") or s.startswith("表"):
        return False
    if re.match(r"^\d", s):
        return False
    return bool(re.search(r"[\u4e00-\u9fff]", s))

DEFAULT = re.compile(r"(默认[为是]?\s*[^。；，,]{0,24}|默认为\s*[\d\.]+|取值范围[为是]?\s*[^。；]{0,60}|最大可?设置为\s*[\d\.]+|最小可?设置为\s*[\d\.]+)")
ENUM = re.compile(r"(支持\s*[A-Za-z0-9\u4e00-\u9fff、/]{2,60}|可选[值为]?\s*[^。；]{2,60}|包括\s*[^。；]{2,60})")
UNITTYPE = re.compile(r"((?:int|float|bool|string|binary|double|枚举|整型|浮点|布尔|字符串|数值)型?)")

def parse_module(name, block):
    body = merge_paras(block)
    res = {"name": name, "intro": [], "params": [], "results": [], "notes": []}
    mode = "intro"
    cur = None
    for s in body:
        if PAGEMARK.match(s):
            continue
        if re.match(r"^(参数配置|运行参数)", s):
            mode = "param"; cur=None; continue
        if re.match(r"^(模块结果|结果说明)", s):
            mode = "result"; cur=None; continue
        if re.match(r"^(说明|注意)", s):
            mode = "note"; continue
        if mode == "param" and is_param_name(s):
            cur = {"name": s, "desc": []}
            res["params"].append(cur)
            continue
        if mode == "result" and is_param_name(s):
            cur = {"name": s, "desc": []}
            res["results"].append(cur)
            continue
        if cur is not None:
            cur["desc"].append(s)
        else:
            (res["intro"] if mode == "intro" else res["notes"]).append(s)

    # 抽字段
    for bucket in (res["params"], res["results"]):
        for it in bucket:
            d = " ".join(it["desc"])
            it["text"] = d
            it["default"] = "；".join(m.group(0).strip() for m in DEFAULT.finditer(d))
            it["enum"] = "；".join(m.group(0).strip() for m in ENUM.finditer(d))
            it["types"] = " ".join(sorted(set(m.group(0) for m in UNITTYPE.finditer(d))))
    return res

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

TITLES = {
 "20-mod-edge-learning":"边缘学习","21-mod-deep-learning":"深度学习","22-mod-calibration":"标定",
 "23-mod-arithmetic":"运算","24-mod-image-process":"图像处理","25-mod-color":"颜色处理",
 "26-mod-split-merge":"拆分组合","27-mod-graphic-gen":"图形生成","28-mod-logic-tool":"逻辑工具",
 "29-mod-communication":"通信"}

alljson = {}
summary=[]
for fn, prefix, tag in JOBS:
    mods = split_modules(load(fn), prefix)
    parsed = [parse_module(nm, blk) for _, nm, blk in mods]
    alljson[tag] = {"prefix": prefix, "title": TITLES[tag], "modules": parsed}
    np = sum(len(m["params"]) for m in parsed)
    nr = sum(len(m["results"]) for m in parsed)
    nd = sum(1 for m in parsed for p in m["params"] if p["default"])
    summary.append(f"{tag:26s} 模块{len(parsed):3d}  参数{np:4d}  结果{nr:4d}  含默认值{nd:4d}")

json.dump(alljson, open(os.path.join(OUT, "_parsed.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_parsed_summary.txt","w",encoding="utf-8").write("\n".join(summary))
print("\n".join(summary))
