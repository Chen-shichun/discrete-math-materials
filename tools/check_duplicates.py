# -*- coding: utf-8 -*-
"""维护脚本：扫描重复文件（内容哈希 / 同名）"""
import os, hashlib
from collections import defaultdict

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

by_hash = defaultdict(list)
by_name = defaultdict(list)
sizes = {}

for dirpath, dirnames, filenames in os.walk(base):
    for fn in filenames:
        full = os.path.join(dirpath, fn)
        rel = os.path.relpath(full, base)
        try:
            sz = os.path.getsize(full)
        except Exception:
            continue
        sizes[rel] = sz
        by_name[fn].append(rel)
        if sz < 5 * 1024 * 1024:
            try:
                by_hash[hashlib.md5(open(full, "rb").read()).hexdigest()].append(rel)
            except Exception:
                pass

print("=== 内容完全相同的文件 ===")
dups = {h: v for h, v in by_hash.items() if len(v) > 1}
if not dups:
    print("  无")
for h, files in dups.items():
    print(f"  [{sizes.get(files[0],0)} 字节] " + " == ".join(files))

print("\n=== 同名但内容不同的文件 ===")
found = False
for name, files in sorted(by_name.items()):
    if len(files) > 1 and not any(files[0] in v for v in dups.values()):
        print(f"  {name}: " + " | ".join(files))
        found = True
if not found:
    print("  无")
