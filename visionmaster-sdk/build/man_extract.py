"""提取 用户手册 PDF (1219页) + 两个小工具说明 PDF"""
import pymupdf, os, re, json

OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\man_pdf"
TOOLS = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\tools_pdf"
os.makedirs(OUT, exist_ok=True)
os.makedirs(TOOLS, exist_ok=True)

DOCS = [
    (r"D:\VisionMaster4.4.0\Applications\Help\CH\Vision Master算法开发平台_用户手册_4.4.3_20251108.pdf", OUT, "manual"),
    (r"D:\VisionMaster4.4.0\Applications\Tools\LogLevelAdjustmentTool\日志等级切换工具使用说明.pdf", TOOLS, "loglevel"),
    (r"D:\VisionMaster4.4.0\Applications\Tools\VersionSwitchAssistant\版本切换工具使用说明.pdf", TOOLS, "versionswitch"),
]

report = []
for src, outdir, tag in DOCS:
    if not os.path.exists(src):
        report.append(f"MISSING {src}"); continue
    doc = pymupdf.open(src)
    n = doc.page_count
    pages = []
    for i in range(n):
        t = doc[i].get_text("text")
        pages.append(t)
    # 逐页写文件，便于按需检索
    for i, t in enumerate(pages, 1):
        open(os.path.join(outdir, f"{tag}_p{i:04d}.txt"), "w", encoding="utf-8").write(t)
    # 合并全文
    full = "\n\n".join(f"\n===== PAGE {i} =====\n{t}" for i, t in enumerate(pages, 1))
    open(os.path.join(outdir, f"_{tag}_FULL.txt"), "w", encoding="utf-8").write(full)
    short = sum(1 for t in pages if len(t.strip()) < 30)
    report.append(f"{tag}: {n} 页, 全文 {len(full)} 字符, 近空页(截图页) {short}")
    doc.close()

open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_log_man.txt", "w", encoding="utf-8").write("\n".join(report))
print("\n".join(report))
