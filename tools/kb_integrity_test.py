# -*- coding: utf-8 -*-
"""知识库完整性自检脚本。

本脚本对所有检查项做「按项 PASS/FAIL」判定：
  - T6 逐题校验「每道图形题(J列=是)都有对应图片文件」，而非只数图片张数；
  - T7 用「依赖表大点集合 ≡ 知识点md大点集合」做双向差集比较，不再重复计数前置/后继两列；
  - 总通过率 = 通过项数 / 总项数（每项 0/1），口径一致，结果必在 [0, 100%]。
输出：tools/test_report.txt。
"""
import openpyxl, os, re, json, time

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t0 = time.time()
report = []
def L(s=""): report.append(s)

CH = {
    "第1章-命题逻辑": 1, "第2章-谓词逻辑": 2, "第3章-集合论": 3,
    "第4章-二元关系": 4, "第5章-函数": 5, "第6章-代数系统基础": 6,
    "第7章-图论基础": 7,
}

checks = []  # (名称, 通过数, 总数, 详情)

# T1: 习题库完整性
L("=== T1 习题库完整性 ===")
for chname, chnum in CH.items():
    for suffix, tag in [("", "基础"), ("-综合提升", "综合")]:
        p = os.path.join(base, "习题库", chname + "-习题库" + suffix + ".xlsx")
        wb = openpyxl.load_workbook(p, data_only=True)
        ws = wb.worksheets[0]
        ok = 0; tot = 0
        for r in range(2, ws.max_row + 1):
            tot += 1
            # 10列必须非空（A~J），K列(知识大点)必须匹配
            vals = [ws.cell(r, c).value for c in range(1, 12)]
            if all(v is not None and str(v).strip() != "" for v in vals[:10]) and vals[10] is not None:
                ok += 1
        wb.close()
        checks.append((f"{chname}{tag} 全字段非空", ok, tot, ""))
        L(f"  {chname}{tag}: {ok}/{tot}")

# T2: 题目ID唯一性
L("\n=== T2 题目ID唯一性 ===")
all_ids = []
for chname in CH:
    for suffix in ["", "-综合提升"]:
        p = os.path.join(base, "习题库", chname + "-习题库" + suffix + ".xlsx")
        wb = openpyxl.load_workbook(p, data_only=True)
        ws = wb.worksheets[0]
        for r in range(2, ws.max_row + 1):
            all_ids.append(str(ws.cell(r, 8).value))
        wb.close()
uniq = len(set(all_ids))
checks.append(("题目ID唯一性", uniq, len(all_ids), ""))
L(f"  题目总数={len(all_ids)} 唯一={uniq} {'PASS' if uniq==len(all_ids) else 'FAIL'}")

# T3: topic_map 覆盖（题目→大点 映射）
L("\n=== T3 topic_map 映射覆盖 ===")
tm = open(os.path.join(base, "topic_map.md"), encoding="utf-8").read()
tmm = re.findall(r"^\|\s*(KP-CH\d+-[A\d]+)\s*\|\s*(CH\d+-\d\d)\s*\|$", tm, re.M)
tmap = {k: v for k, v in tmm}
missing = [i for i in all_ids if i not in tmap]
checks.append(("topic_map 题目→大点覆盖", len(all_ids) - len(missing), len(all_ids), ""))
L(f"  映射={len(tmap)} 缺失={missing if missing else '无'}")

# T4: error_points 关联完整性
L("\n=== T4 易错点库关联完整性 ===")
ep = open(os.path.join(base, "error_points_kb.md"), encoding="utf-8").read()
entries = re.findall(r"### 易错点(\d+)：", ep)
dad = re.findall(r"- \*\*关联知识大点ID\*\*：\[(CH\d+-\d\d)\]", ep)
qid = re.findall(r"- \*\*关联题目ID\*\*：\[(KP-CH\d+-[A\d]+)", ep)
checks.append(("易错点条目数", len(entries), 245, ""))
checks.append(("易错点关联题目ID", len(qid), 245, ""))
checks.append(("易错点关联知识大点ID", len(dad), 245, ""))
L(f"  条目={len(entries)} 关联题目ID={len(qid)} 关联大点ID={len(dad)}")

# T5: 知识点md 标题ID完整性
L("\n=== T5 知识点md 标题ID ===")
tot_h2 = tot_h3 = ok_h2 = ok_h3 = 0
for chname, chnum in CH.items():
    txt = open(os.path.join(base, "知识点", chname + "-知识点.md"), encoding="utf-8").read()
    h2 = re.findall(r"^## (.+)$", txt, re.M)
    h3 = re.findall(r"^### (.+)$", txt, re.M)
    tot_h2 += len(h2); tot_h3 += len(h3)
    ok_h2 += sum(1 for h in h2 if re.search(r"〔CH\d+-\d\d〕", h))
    ok_h3 += sum(1 for h in h3 if re.search(r"〔CH\d+-\d\d-\d\d〕", h))
checks.append(("知识大点标题带ID", ok_h2, tot_h2, ""))
checks.append(("知识小点标题带ID", ok_h3, tot_h3, ""))
L(f"  大点 {ok_h2}/{tot_h2}  小点 {ok_h3}/{tot_h3}")

# T6: 图形题接入（逐题校验：每道图形题 J列=是 必须有对应图片文件）
L("\n=== T6 图形题接入 ===")
fig_questions = 0          # J列=是 的图形题数
img_files = 0              # 实际存在的图片文件数
missing_img = []           # 标记为图形题却无对应图的题
for chname in CH:
    # 说明md：图片文件名 -> 对应习题库题号列表
    md = os.path.join(base, "图形题配套包", chname, chname + "-图形题说明.md")
    mdtxt = open(md, encoding="utf-8").read()
    img_map = {}   # 图片文件名 -> 题号集合
    for m in re.finditer(r"^\|\s*(题\d+)\s*\|\s*([^|]+?)\s*\|.*\|\s*([^|]*?)\s*\|\s*$", mdtxt, re.M):
        fig, img, lastcol = m.group(1), m.group(2).strip(), m.group(3)
        qnos = {int(x) for x in re.findall(r"第(\d+)题", lastcol)}
        if img:
            img_map[img] = qnos
    # 习题库 J列=是 的题号
    p = os.path.join(base, "习题库", chname + "-习题库.xlsx")
    wb = openpyxl.load_workbook(p, data_only=True)
    ws = wb.worksheets[0]
    yes = [r - 1 for r in range(2, ws.max_row + 1) if ws.cell(r, 10).value == "是"]
    wb.close()
    fig_questions += len(yes)
    # 该章图片文件实际存在数
    img_dir = os.path.join(base, "图形题配套包", chname)
    pngs = [f for f in os.listdir(img_dir) if f.endswith(".png")] if os.path.isdir(img_dir) else []
    img_files += len(pngs)
    # 每道 J列=是 的题，都要有一张存在的图片在其"对应题号"里
    covered = set()
    for img, qnos in img_map.items():
        if os.path.exists(os.path.join(img_dir, img)):
            covered |= qnos
    for q in yes:
        if q not in covered:
            missing_img.append(f"{chname}/第{q}题")
checks.append(("图形题标记(J列=是)", fig_questions, 53, ""))
checks.append(("图形题图片文件", img_files, 52, ""))
checks.append(("每道图形题均有对应图", fig_questions - len(missing_img), fig_questions,
               ("缺图:" + "、".join(missing_img)) if missing_img else ""))
L(f"  标记图形题={fig_questions} 图片文件={img_files} 缺图={missing_img if missing_img else '无'}")

# T7: 前置依赖完整性（依赖表大点 ≡ 知识点md大点，双向差集为空）
L("\n=== T7 前置依赖完整性（大点集合双向一致） ===")
kd = open(os.path.join(base, "knowledge_dependency.md"), encoding="utf-8").read()
# 依赖表「知识点ID」列（行首第一个单元格）的大点ID集合
dep_ids = set(re.findall(r"^\|\s*(CH\d+-\d\d)\s*\|", kd, re.M))
# 知识点md「## 大点标题」中的大点ID集合（仅大点，不含小点）
md_ids = set()
for chname, chnum in CH.items():
    txt = open(os.path.join(base, "知识点", chname + "-知识点.md"), encoding="utf-8").read()
    md_ids |= set(re.findall(r"〔(CH\d+-\d\d)〕", txt))
only_dep = sorted(dep_ids - md_ids)
only_md = sorted(md_ids - dep_ids)
consistent = (dep_ids == md_ids)
checks.append(("依赖表大点 ≡ 知识点大点（双向差集为空）", 1 if consistent else 0, 1,
               ("仅依赖表=" + str(only_dep) + " 仅知识点=" + str(only_md)) if not consistent else ""))
L(f"  依赖表大点={len(dep_ids)} 知识点大点={len(md_ids)} 双向差集={only_dep or only_md or '空'}")

# T8: 响应速度（本地检索基准）
elapsed = time.time() - t0
L(f"\n=== 全量校验耗时: {elapsed:.2f}s（本地检索基准） ===")

# 汇总（每项 PASS=1 / FAIL=0，口径一致）
L("\n===== 汇总 =====")
passed = sum(1 for name, ok, tot, _ in checks if ok == tot)
total = len(checks)
for name, ok, tot, detail in checks:
    verdict = "PASS" if ok == tot else "FAIL"
    L(f"  {verdict} {name}: {ok}/{tot}" + (f"  [{detail}]" if (ok != tot and detail) else ""))
L(f"  总通过率: {passed}/{total} 项校验通过 = {100.0*passed/total:.1f}%")

_outdir = os.path.join(base, "tools")
os.makedirs(_outdir, exist_ok=True)
open(os.path.join(_outdir, "test_report.txt"), "w", encoding="utf-8").write("\n".join(report))
print("test done, rate:", f"{100.0*passed/total:.1f}%")
print("report -> tools/test_report.txt")
