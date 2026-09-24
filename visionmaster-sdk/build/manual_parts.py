"""用户手册 PDF: 书签全文导出 + 按章分片"""
import pymupdf, re, os, json

SRC = r"D:\VisionMaster4.4.0\Applications\Help\CH\Vision Master算法开发平台_用户手册_4.4.3_20251108.pdf"
OUTD = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\man_parts"
os.makedirs(OUTD, exist_ok=True)
doc = pymupdf.open(SRC)
n = doc.page_count
toc = doc.get_toc()

lines = [f"总页数 {n}, 书签 {len(toc)} 条\n"]
for lvl, title, pg in toc:
    lines.append(f"{'  '*(lvl-1)}[p{pg}] {title}")
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_manual_bookmarks.txt", "w", encoding="utf-8").write("\n".join(lines))

# 找一级（章）书签的页码范围
chapters = [(t, p) for l, t, p in toc if l == 1]
lines2 = [f"=== 一级章节 {len(chapters)} 章 ==="]
for i, (t, p) in enumerate(chapters):
    end = chapters[i+1][1]-1 if i+1 < len(chapters) else n
    lines2.append(f"p{p:5d} - p{end:5d}  ({end-p+1:4d} 页)  {t}")
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_manual_chapters.txt", "w", encoding="utf-8").write("\n".join(lines2))
print("\n".join(lines2))
