"""VM 用户手册模块知识 布局感知提取器 v4
关键：PDF 中「运行参数名」使用 SimHei（黑体）span，说明用 SimSun（宋体）。
据此可精确切出参数名，跨页表格/段落也能正确归属。
输出：结构化 JSON（模块 → 参数表/结果表），供 skill 生成。
"""
import pymupdf, re, os, json, collections

PDF = r"D:\VisionMaster4.4.0\Applications\Help\CH\Vision Master算法开发平台_用户手册_4.4.3_20251108.pdf"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\extract_v4"
os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(PDF)

def spans(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b["lines"]:
            for s in l["spans"]:
                t = s["text"]
                if not t.strip():
                    continue
                out.append({
                    "t": t,
                    "bold": "SimHei" in s["font"] or "Bold" in s["font"],
                    "size": round(s["size"], 1),
                    "y": round(s["bbox"][1], 1),
                    "x": round(s["bbox"][0], 1),
                })
    return out

NOISE = ("Vision Master 算法开发平台 用户手册", "用户手册")

def page_lines(page):
    """把 span 按 y 聚成行"""
    sp = spans(page)
    rows = collections.defaultdict(list)
    for s in sp:
        key = round(s["y"] / 4)
        rows[key].append(s)
    lines = []
    for k in sorted(rows):
        parts = sorted(rows[k], key=lambda z: z["x"])
        txt = "".join(p["t"] for p in parts).strip()
        if not txt or any(n in txt for n in NOISE):
            continue
        if re.fullmatch(r"\d{1,4}", txt):
            continue
        bold_head = next((p["t"].strip() for p in parts if p["bold"] and p["t"].strip()), None)
        size = max(p["size"] for p in parts)
        lines.append({"text": txt, "bold_head": bold_head, "size": size,
                      "bold": any(p["bold"] for p in parts)})
    return lines

# ---- 章节边界（用 PDF 书签，精确） ----
toc = doc.get_toc()
CH = {f"{p}": t for l, t, p in toc if l == 2}   # 二级书签 = 模块
ch13 = [(t, p) for l, t, p in toc if l == 2 and p >= 306]

def module_range(idx):
    start = ch13[idx][1]
    end = ch13[idx+1][1]-1 if idx+1 < len(ch13) else 1204
    return start, end

results = {}
for i, (title, start) in enumerate(ch13):
    end = module_range(i)[1]
    rows = []
    for p in range(start-1, min(end, 1204)):
        rows.extend(page_lines(doc[p]))
    results[title] = {"pdf_from": start, "pdf_to": end, "lines": rows}

json.dump(results, open(os.path.join(OUT, "_raw_lines.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=0)
print(f"模块数 {len(results)}, 总行数 {sum(len(v['lines']) for v in results.values())}")
print("前20个模块:", list(results.keys())[:20])
