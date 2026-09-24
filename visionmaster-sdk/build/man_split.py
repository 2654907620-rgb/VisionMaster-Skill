"""用户手册 PDF → 分片 MD（供子代理提炼）
策略：按一级章节切；第13章(899页)按二级书签再切
保留印刷页码标记，便于溯源
"""
import pymupdf, re, os, json

SRC = r"D:\VisionMaster4.4.0\Applications\Help\CH\Vision Master算法开发平台_用户手册_4.4.3_20251108.pdf"
DST = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\man_mdparts"
os.makedirs(DST, exist_ok=True)

doc = pymupdf.open(SRC)
n = doc.page_count
toc = doc.get_toc()
pages = {}
for i in range(n):
    pages[i+1] = doc[i].get_text("text")

# 清洗页眉页脚：常见 "Vision Master 算法开发平台 用户手册" 与孤立页码
def clean_page(t):
    lines = t.splitlines()
    out = []
    for ln in lines:
        s = ln.strip()
        if s == "Vision Master 算法开发平台 用户手册":
            continue
        if re.fullmatch(r"[ivxlcdm]{1,6}|\d{1,4}", s):   # 页码
            continue
        out.append(ln)
    return "\n".join(out)

# 一级章节
chapters = [(t, p) for l, t, p in toc if l == 1]

def slug(s):
    s = re.sub(r"[^\w\u4e00-\u9fff]+", "-", s).strip("-")
    return s[:40]

manifest = []
for i, (title, start) in enumerate(chapters):
    end = chapters[i+1][1]-1 if i+1 < len(chapters) else n
    # 取该章下的二级书签做切分（若章节很大）
    subs = [(t, p) for l, t, p in toc if l == 2 and start <= p <= end]
    segs = []
    if len(subs) >= 3 and (end-start) > 60:
        for j, (st, sp) in enumerate(subs):
            se = subs[j+1][1]-1 if j+1 < len(subs) else end
            if se < sp:
                continue
            segs.append((st, sp, se))
    else:
        segs.append((title, start, end))
    for st, sp, se in segs:
        buf = [f"<!-- source: 用户手册V4.4.3 PDF, PDF页 {sp}-{se} -->",
               f"<!-- chapter: {title} > {st} -->", ""]
        for p in range(sp, se+1):
            buf.append(f"\n===== PDF页 {p} =====")
            buf.append(clean_page(pages[p]))
        fn = f"{i+1:02d}-{slug(title)}__{slug(st)}.md"
        open(os.path.join(DST, fn), "w", encoding="utf-8").write("\n".join(buf))
        manifest.append({"file": fn, "chapter": title, "sub": st,
                         "pdf_from": sp, "pdf_to": se, "pages": se-sp+1})

json.dump(manifest, open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_man_manifest.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
lines = [f"共生成 {len(manifest)} 个分片\n"]
for m in manifest:
    lines.append(f"{m['file']:60s} p{m['pdf_from']:5d}-{m['pdf_to']:5d}  {m['pages']:4d}页  {m['chapter']} > {m['sub']}")
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_man_parts_list.txt", "w", encoding="utf-8").write("\n".join(lines))
print("\n".join(lines))
