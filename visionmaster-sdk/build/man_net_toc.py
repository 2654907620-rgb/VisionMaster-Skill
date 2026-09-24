"""从 CHM 目录树提取算子开发包 .NET 指南结构"""
import os, re, io, sys, json

BASE = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\man_net"
hhc = os.path.join(BASE, "index.hhc")
raw = open(hhc, "rb").read().decode("gb18030", errors="ignore")

# UL 嵌套 + LI>OBJECT>param(Name/Local)
pat = re.compile(r"(<UL>)|(</UL>)|(<LI><OBJECT type=\"text/sitemap\">(.*?)</OBJECT>)", re.S | re.I)
depth = 0
entries = []
for m in pat.finditer(raw):
    if m.group(1):
        depth += 1
    elif m.group(2):
        depth -= 1
    else:
        payload = m.group(4)
        nm = re.search(r'name="Name"\s+value="(.*?)"', payload, re.I)
        lo = re.search(r'name="Local"\s+value="(.*?)"', payload, re.I)
        if nm:
            entries.append({
                "depth": depth,
                "name": nm.group(1).strip(),
                "local": (lo.group(1).split("#")[0].strip() if lo else ""),
            })

out = []
out.append(f"=== 算子开发包(.NET) 目录项 {len(entries)} 条 ===\n")
for e in entries:
    out.append(f"{'  '*(e['depth']-1)}{e['name']}   [{e['local']}]")

open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_man_net_toc.txt", "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out[:100]))
print(f"\n... 共 {len(entries)} 条，完整写入 _man_net_toc.txt")
