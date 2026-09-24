"""解析用户手册 PDF 目录与章节地标，确定分片边界"""
import pymupdf, re, os, json

SRC = r"D:\VisionMaster4.4.0\Applications\Help\CH\Vision Master算法开发平台_用户手册_4.4.3_20251108.pdf"
doc = pymupdf.open(SRC)
n = doc.page_count
pages = [doc[i].get_text("text") for i in range(n)]

out = []
def w(s=""): out.append(str(s))

w(f"总页数 {n}")
w()
# 1. 尝试书签
toc = doc.get_toc()
w(f"=== 内置书签: {len(toc)} 条 ===")
for lvl, title, pg in toc[:60]:
    w(f"{'  '*(lvl-1)}{title}  ....  p{pg}")
w()

# 2. 从目录页解析（找含 "目录" 的页）
w("=== 目录页探测 ===")
for i in range(min(40, n)):
    t = pages[i]
    if re.search(r"目\s*录", t[:200]):
        w(f"--- PDF p{i+1} 含目录 ---")
        for ln in t.splitlines()[:45]:
            if ln.strip(): w("   " + ln.strip())
        w()

# 3. 章标题地标反查
w("=== 章级地标反查（真实 PDF 页码） ===")
pat = re.compile(r"^\s*(第\s*[0-9一二三四五六七八九十]+\s*章)\s*(.{0,40})", re.M)
found = {}
for i, t in enumerate(pages, 1):
    for m in pat.finditer(t[:600]):
        key = m.group(1).replace(" ", "") + " " + m.group(2).strip()[:30]
        if key not in found:
            found[key] = i
for k, v in list(found.items())[:60]:
    w(f"p{v:5d}  {k}")
w()
# 4. 节级地标
w("=== 节级地标（形如 1.2.3 标题）抽样 ===")
pat2 = re.compile(r"^\s*(\d{1,2}(?:\.\d{1,2}){1,3})\s+(\S.{0,40})", re.M)
secs = []
for i, t in enumerate(pages, 1):
    for m in pat2.finditer(t[:800]):
        secs.append((i, m.group(1), m.group(2).strip()[:40]))
w(f"共发现节标题 {len(secs)} 条")
for s in secs[:50]:
    w(f"p{s[0]:5d}  {s[1]}  {s[2]}")

open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_manual_toc.txt", "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out[:120]))
