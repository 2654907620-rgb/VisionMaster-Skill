# -*- coding: utf-8 -*-
"""Split the status-code chapter into clean reference files + build an index."""
import os, re, json

SRC = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\chm_statuscodes_raw.md"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\status_codes"
os.makedirs(OUT, exist_ok=True)

txt = open(SRC, "r", encoding="utf-8").read()

# split on the page markers
blocks = re.split(r"<!-- ===== (.*?) \| (.*?) ===== -->", txt)
# blocks[0] = preamble; then triples (src, path, body)
items = []
for i in range(1, len(blocks), 3):
    src, path, body = blocks[i], blocks[i + 1], blocks[i + 2]
    items.append((src, path.strip(), body))

MAP = {
    "状态码 > SDK状态码": "01-sdk-status.md",
    "状态码 > 算子状态码（C#） > 正确码": "02-operator-correct.md",
    "状态码 > 算子状态码（C#） > 通用状态码": "03-operator-common.md",
    "状态码 > 算子状态码（C#） > 算法状态码": "04-algorithm-status.md",
    "状态码 > 算子状态码（C#） > 相机相关状态码": "05-camera-status.md",
}

written = []
for src, path, body in items:
    fn = MAP.get(path)
    if not fn:
        continue
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as fh:
        fh.write("<!-- src:%s | path:%s -->\n" % (src, path))
        fh.write(body.strip() + "\n")
    written.append((fn, path, len(body)))

# ---- split the big 算法状态码 into sub-modules ----
algo = [b for s, p, b in items if p.endswith("算法状态码")]
idx_lines = []
if algo:
    body = algo[0]
    # find "## <name>" and "| <subname> | | |" markers
    lines = body.split("\n")
    sections = []          # (level, name, start_line)
    for i, ln in enumerate(lines):
        m = re.match(r"^##\s+(.+?)\s*$", ln)
        if m:
            sections.append((1, m.group(1), i))
            continue
        m2 = re.match(r"^\|\s*([^|]+?)\s*\|\s*\|\s*\|\s*$", ln)
        if m2 and m2.group(1).strip() not in ("名称",):
            nm = m2.group(1).strip()
            if nm and not nm.startswith("---"):
                sections.append((2, nm, i))
    # write per major section
    majors = [s for s in sections if s[0] == 1]
    for j, (lvl, name, start) in enumerate(majors):
        end = majors[j + 1][2] if j + 1 < len(majors) else len(lines)
        chunk = lines[start:end]
        safe = re.sub(r'[\\/:*?"<>|]', "_", name)
        sub = [s for s in sections if s[0] == 2 and start < s[2] < end]
        with open(os.path.join(OUT, "04a-%s.md" % safe), "w", encoding="utf-8") as fh:
            fh.write("<!-- from 04-algorithm-status.md | section: %s -->\n" % name)
            fh.write("\n".join(chunk).strip() + "\n")
        written.append(("04a-%s.md" % safe, name, len("\n".join(chunk))))

# ---- build index ----
codes = re.findall(r"\|\s*([A-Za-z][A-Za-z0-9_\\]{4,})\s*\|\s*(0x[0-9A-Fa-f]+)\s*\|\s*([^|]*)\|", txt)
codes = [(n.replace("\\", ""), v, d) for n, v, d in codes]
prefix = {}
for name, val, desc in codes:
    pfx = name.split("_")
    key = "_".join(pfx[:4]) if len(pfx) > 3 else name
    prefix.setdefault(key, [0, val, val])
    prefix[key][0] += 1
    prefix[key][1] = min(prefix[key][1], val)
    prefix[key][2] = max(prefix[key][2], val)

idx_lines.append("# 状态码索引\n")
idx_lines.append("> 共收录 %d 条状态码。按前缀族聚合如下。完整表格见同目录各文件。\n" % len(codes))
idx_lines.append("| 前缀族 | 条数 | 值域 |")
idx_lines.append("| --- | --- | --- |")
for k in sorted(prefix, key=lambda x: -prefix[x][0]):
    c, lo, hi = prefix[k]
    idx_lines.append("| `%s` | %d | %s – %s |" % (k, c, lo, hi))

idx_lines.append("\n## 文件清单\n")
idx_lines.append("| 文件 | 内容 | 字符数 |")
idx_lines.append("| --- | --- | --- |")
for fn, path, n in sorted(written):
    idx_lines.append("| `%s` | %s | %d |" % (fn, path, n))

with open(os.path.join(OUT, "00-INDEX.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(idx_lines))

print("codes", len(codes), "files", len(written) + 1)
