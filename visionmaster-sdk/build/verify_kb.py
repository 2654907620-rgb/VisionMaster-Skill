"""验收 visionmaster-sdk skill 知识库（只读）"""
import os, re, io, sys

BASE = r"C:\Users\Administrator\.workbuddy\skills\visionmaster-sdk"
REF = os.path.join(BASE, "references")
out = []
def w(s=""):
    out.append(str(s))

w("=== visionmaster-sdk 知识库验收 ===")
w()

# 1. 各层文件数与体积
layers = {
    "00-10 提炼层(顶层)": None,
    "05-api": os.path.join(REF, "05-api"),
    "06-status-codes": os.path.join(REF, "06-status-codes"),
    "08-faq-manual": os.path.join(REF, "08-faq-manual"),
    "10-app-manual": os.path.join(REF, "10-app-manual"),
    "fulltext/sdk-guide": os.path.join(REF, "fulltext", "sdk-guide"),
    "fulltext/faq": os.path.join(REF, "fulltext", "faq"),
    "fulltext/app-help": os.path.join(REF, "fulltext", "app-help"),
}
w("--- 1. 各层规模 ---")
total_bytes = 0
total_files = 0
for name, d in layers.items():
    if d is None:
        continue
    n = 0; b = 0
    for root, _, files in os.walk(d):
        for f in files:
            if f.lower().endswith((".md", ".json")):
                n += 1
                try: b += os.path.getsize(os.path.join(root, f))
                except OSError: pass
    total_bytes += b; total_files += n
    w(f"{name:24s} files={n:5d}  size={b/1024/1024:7.2f} MB")

# 顶层 md
top = [f for f in os.listdir(REF) if f.endswith(".md")]
tb = sum(os.path.getsize(os.path.join(REF, f)) for f in top)
w(f"{'顶层提炼页':24s} files={len(top):5d}  size={tb/1024/1024:7.2f} MB")
total_files += len(top); total_bytes += tb
w(f"{'合计':24s} files={total_files:5d}  size={total_bytes/1024/1024:7.2f} MB")
w()

# 2. 面包屑覆盖（排除 -members 空壳页）
w("--- 2. 面包屑路径覆盖 ---")
for lay, sub in (("sdk-guide", "fulltext/sdk-guide"), ("app-help", "fulltext/app-help")):
    d = os.path.join(REF, *sub.split("/"))
    tot = 0; have = 0; shell = 0
    for f in os.listdir(d):
        if not f.endswith(".md"): continue
        tot += 1
        if f.endswith("-members.md") or f == "_core-objects-source.md":
            shell += 1; continue
        try:
            head = open(os.path.join(d, f), encoding="utf-8", errors="ignore").read(600)
        except OSError:
            continue
        if "<!-- path:" in head:
            have += 1
    w(f"{lay}: 总 {tot} 页，空壳 {shell} 页，实质页 {tot-shell} 页，有面包屑 {have} 页 -> 覆盖 {have/max(1,tot-shell)*100:.1f}%")
w()

# 3. 代码块多行验证（是否存在逐token断行）
w("--- 3. 代码块质量 ---")
src = os.path.join(REF, "fulltext", "sdk-guide", "_core-objects-source.md")
if os.path.exists(src):
    t = open(src, encoding="utf-8", errors="ignore").read()
    blocks = re.findall(r"```[a-z]*\n(.*?)```", t, re.S)
    if blocks:
        avg = sum(len(b.splitlines()) for b in blocks) / len(blocks)
        w(f"代码块数={len(blocks)}  平均行数={avg:.1f}  （远大于1说明未逐token断行 ✅）")
        # 检查是否有单token短行
        short = sum(1 for b in blocks for ln in b.splitlines() if 0 < len(ln.strip()) <= 2)
        w(f"极短行(<=2字符)数={short}  （占比 {short/max(1,sum(len(b.splitlines()) for b in blocks))*100:.1f}%）")
w()

# 4. 乱码检查
w("--- 4. 乱码检查 ---")
bad = 0; checked = 0
for root, _, files in os.walk(REF):
    for f in files:
        if not f.endswith(".md"): continue
        checked += 1
        p = os.path.join(root, f)
        try:
            t = open(p, encoding="utf-8", errors="ignore").read(4000)
        except OSError:
            continue
        if "\ufffd" in t:
            bad += 1
w(f"抽查 {checked} 个 md 文件，含替换字符(U+FFFD)的={bad}")
w()

# 5. 状态码覆盖
w("--- 5. 状态码库 ---")
sc = os.path.join(REF, "06-status-codes")
allc = 0
for f in os.listdir(sc):
    if not f.endswith(".md"): continue
    t = open(os.path.join(sc, f), encoding="utf-8", errors="ignore").read()
    c = len(re.findall(r"0x[0-9A-Fa-f]{4,8}", t))
    allc += c
    w(f"  {f:34s} 含码 {c:5d}")
w(f"  状态码值总出现次数 = {allc}")
w()

# 6. API 枚举带数值
w("--- 6. API 参考枚举带数值 ---")
ap = os.path.join(REF, "05-api")
tot_enum = 0
for f in sorted(os.listdir(ap)):
    if not f.endswith(".md"): continue
    t = open(os.path.join(ap, f), encoding="utf-8", errors="ignore").read()
    n = len(re.findall(r"=\s*0x[0-9A-Fa-f]+", t))
    tot_enum += n
    if n: w(f"  {f:20s} 枚举数值 {n:4d}")
w(f"  合计枚举带数值 = {tot_enum}")

sys.stdout.buffer.write("\n".join(out).encode("utf-8"))
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_verify_kb.txt", "w", encoding="utf-8").write("\n".join(out))
