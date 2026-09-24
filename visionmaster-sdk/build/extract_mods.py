"""从分片里按模块抽取「参数表 + 结果 + 说明」原文，压缩为提炼可读格式（供人工/模型提炼）"""
import re, os, sys, json

SRC = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\man_mdparts"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\extract_mod"
os.makedirs(OUT, exist_ok=True)

NOISE = re.compile(
    r"^\s*(Vision Master 算法开发平台 用户手册|用户手册|第13章 模块使用参考|第\s*13\s*章)\s*$")

def load(name):
    p = os.path.join(SRC, name)
    t = open(p, encoding="utf-8", errors="ignore").read()
    lines = [ln for ln in t.splitlines() if not NOISE.match(ln)]
    return lines

def split_modules(lines, prefix):
    """按 ^prefix.N 切模块"""
    idx = []
    pat = re.compile(rf"^\s*{re.escape(prefix)}\.(\d+)\s+(\S.*)$")
    for i, ln in enumerate(lines):
        m = pat.match(ln)
        if m:
            idx.append((i, m.group(1), m.group(2).strip()))
    mods = []
    for j, (i, num, name) in enumerate(idx):
        end = idx[j+1][0] if j+1 < len(idx) else len(lines)
        mods.append((num, name, lines[i:end]))
    return mods

def compress(block):
    """把模块正文压成 参数区 + 结果区，去掉长段落解释"""
    out = []
    in_tbl = False
    for ln in block:
        s = ln.rstrip()
        if s.strip().startswith("|"):
            in_tbl = True
            out.append(s)
            continue
        if in_tbl and not s.strip():
            in_tbl = False
            out.append("")
            continue
        # 保留参数/结果相关标题与列表
        if re.search(r"(参数|结果|输出|输入|说明|注意|默认|范围|单位|含义|可选)", s):
            out.append(s)
        elif re.match(r"^\s*[\*\-\u25cf\u25cb]", s) and len(s.strip()) < 120:
            out.append(s)
        elif re.match(r"^\s*\d+(\.\d+)+\s+\S", s.strip()):
            out.append(s)
        elif s.strip() and len(s.strip()) < 60 and not s.strip().endswith("。"):
            out.append(s)
    return out

JOBS = [
    ("14-第13章-模块使用参考__13-6-边缘学习.md", "13.6", "20-edge"),
    ("14-第13章-模块使用参考__13-7-深度学习.md", "13.7", "21-dl"),
    ("14-第13章-模块使用参考__13-8-标定.md", "13.8", "22-calib"),
    ("14-第13章-模块使用参考__13-9-运算.md", "13.9", "23-arith"),
    ("14-第13章-模块使用参考__13-10-图像处理.md", "13.10", "24-imgproc"),
    ("14-第13章-模块使用参考__13-11-颜色处理.md", "13.11", "25-color"),
    ("14-第13章-模块使用参考__13-12-拆分组合.md", "13.12", "26-split"),
    ("14-第13章-模块使用参考__13-13-图形生成.md", "13.13", "27-graphic"),
    ("14-第13章-模块使用参考__13-14-逻辑工具.md", "13.14", "28-logic"),
    ("14-第13章-模块使用参考__13-15-通信.md", "13.15", "29-comm"),
]

summary = []
for fn, prefix, tag in JOBS:
    lines = load(fn)
    mods = split_modules(lines, prefix)
    buf = []
    for num, name, block in mods:
        comp = compress(block)
        buf.append(f"\n{'='*70}")
        buf.append(f"### {prefix}.{num} {name}")
        buf.append(f"{'='*70}")
        buf.extend(comp)
    txt = "\n".join(buf)
    open(os.path.join(OUT, f"{tag}.txt"), "w", encoding="utf-8").write(txt)
    summary.append(f"{tag:12s} 模块 {len(mods):3d} 个  压缩后 {len(txt):7d} 字符  原始 {sum(len(b) for _,_,b in mods):8d}")

open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_extract_summary.txt", "w", encoding="utf-8").write("\n".join(summary))
print("\n".join(summary))
