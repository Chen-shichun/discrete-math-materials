# -*- coding: utf-8 -*-
"""只读分析 student_progress.json，现算学习画像（不落地任何计数器）。

输出（供智能体在「成长反馈 / 薄弱点复盘 / 错误聚类 / 遗忘提醒」时引用）：
  1) 薄弱知识大点 Top5（正确率升序，作答 >= 1）
  2) 错误聚类（按 error_type 计数，>= 3 次标为高频雷区）
  3) 成长里程碑（连续答对、薄弱点进步、反复出错）
  4) 遗忘提醒（距上次作答 >= N 天的大点）

用法：
  python analyze_progress.py --user <user_id> [--days 7] [--file <path>] [--json]
  --file 缺省读 student_progress.json；也可指向参赛材料/student_progress_demo.json 做演示。
"""
import json, os, argparse, datetime, re
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, "student_progress.json")

MEANINGFUL_TYPES = {"概念性", "方法性", "符号形式", "计算粗心"}

# 大点ID -> 名称（来自 knowledge_dependency.md 知识点ID/名称列）
def load_kp_names():
    kd = open(os.path.join(BASE, "knowledge_dependency.md"), encoding="utf-8").read()
    names = {}
    for m in re.finditer(r"^\|\s*(CH\d+-\d\d)\s*\|\s*([^|]+?)\s*\|", kd, re.M):
        names[m.group(1)] = m.group(2).strip()
    return names

KP_NAMES = load_kp_names()

def _rate(seg):
    return sum(1 for r in seg if r == "correct") / len(seg)

def _parse_time(s):
    """兼容带秒/不带秒/仅日期三种时间格式；均无法解析返回 None。"""
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None

def analyze(user_id, days=7, path=None):
    fpath = path or PATH
    data = json.load(open(fpath, encoding="utf-8-sig"))
    u = data.get("users", {}).get(user_id)
    if not u or not u.get("history"):
        return {"user": user_id, "name": (u or {}).get("name", user_id),
                "empty": True, "history_count": 0}
    hist = u.get("history", [])
    now = datetime.datetime.now()

    # 大点统计
    kp = {}
    for h in hist:
        k = h.get("kp", "未标记")
        s = kp.setdefault(k, {"total": 0, "correct": 0, "wrong": 0,
                              "last_time": "", "timeline": []})
        s["total"] += 1
        s["correct"] += (1 if h.get("result") == "correct" else 0)
        s["wrong"] += (1 if h.get("result") == "wrong" else 0)
        s["last_time"] = h.get("time", "")
        s["timeline"].append(h.get("result"))

    # 1) 薄弱大点 Top5（正确率升序，同率时作答多者靠前）
    weak = []
    for k, s in kp.items():
        if s["total"] >= 1:
            weak.append((k, s["correct"] / s["total"], s["correct"], s["total"]))
    weak.sort(key=lambda x: (x[1], -x[3]))
    top5 = weak[:5]

    # 2) 错误聚类（仅统计有明确大类且为 wrong 的记录）
    type_counter = Counter()
    for h in hist:
        et = h.get("error_type")
        if h.get("result") == "wrong" and et in MEANINGFUL_TYPES:
            type_counter[et] += 1
    clusters = [(t, c) for t, c in type_counter.most_common() if c >= 3]

    # 3) 成长里程碑
    milestones = []
    # 连续答对（最近作答起连续 correct）
    streak = 0
    for h in reversed(hist):
        if h.get("result") == "correct":
            streak += 1
        else:
            break
    if streak >= 3:
        milestones.append(f"已连续答对 {streak} 题，状态正佳")
    # 进步 / 反复出错 / 已掌握
    for k, s in kp.items():
        if s["total"] < 3:
            continue
        pct = int(100 * s["correct"] / s["total"])
        tl = s["timeline"]
        # 进步：前段正确率低、后段显著提升
        if len(tl) >= 4:
            mid = len(tl) // 2
            r1, r2 = _rate(tl[:mid]), _rate(tl[mid:])
            if r1 < 0.5 and r2 >= 0.6:
                milestones.append(f"进步显著：{k} {KP_NAMES.get(k, '')}（正确率 {int(100*r1)}% → {int(100*r2)}%）")
                continue
        rate = s["correct"] / s["total"]
        if rate >= 0.6 and tl[-1] == "correct":
            milestones.append(f"已掌握：{k} {KP_NAMES.get(k, '')}（正确率 {pct}%，最近一次做对）")
        elif rate < 0.4:
            milestones.append(f"反复出错：{k} {KP_NAMES.get(k, '')}（正确率 {pct}%），建议按前置依赖优先攻克")

    # 4) 遗忘提醒（兼容带秒/不带秒/仅日期三种时间格式）
    forget = []
    for k, s in kp.items():
        if s["last_time"]:
            t = _parse_time(s["last_time"])
            if t is not None:
                gap = (now - t).days
                if gap >= days:
                    forget.append((k, gap))
    forget.sort(key=lambda x: -x[1])

    return {
        "user": user_id,
        "name": u.get("name", user_id),
        "empty": False,
        "history_count": len(hist),
        "last_time": hist[-1].get("time", ""),
        "weak_top5": top5,
        "clusters": clusters,
        "milestones": milestones,
        "forget": forget,
        "streak": streak,
    }

def render_text(r):
    if r["empty"]:
        print(f"=== 学习画像（user={r['user']}）===\n暂无作答记录，尚未形成画像。")
        return
    print(f"=== 学习画像（user={r['user']} / {r['name']}）===")
    print(f"作答记录 {r['history_count']} 条，最近一次 {r['last_time']}")
    print()
    print("【薄弱知识大点 Top5】")
    if not r["weak_top5"]:
        print("  （暂无）")
    for k, rate, c, t in r["weak_top5"]:
        print(f"  {k} {KP_NAMES.get(k, '')} —— 正确率 {int(100*c/t)}%（{c}/{t}）")
    print()
    print("【错误聚类（高频雷区，≥3 次）】")
    if not r["clusters"]:
        print("  （暂无高频雷区）")
    for t, c in r["clusters"]:
        print(f"  {t}：{c} 次 —— 反复出现，建议专项练习")
    print()
    print("【成长里程碑】")
    if not r["milestones"]:
        print("  （暂无可庆祝 / 需警惕的里程碑）")
    for m in r["milestones"]:
        print(f"  - {m}")
    print()
    print("【遗忘提醒（距上次作答 ≥ 天数）】")
    if not r["forget"]:
        print("  （无）")
    for k, gap in r["forget"]:
        print(f"  {k} {KP_NAMES.get(k, '')}：距上次作答 {gap} 天，建议复习")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True)
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--file", default=None, help="进度文件路径，缺省读 student_progress.json")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    r = analyze(args.user, args.days, args.file)
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        render_text(r)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
