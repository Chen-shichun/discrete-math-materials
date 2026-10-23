# -*- coding: utf-8 -*-
"""固化脚本：向 student_progress.json 追加一条诊断记录（按 user_id 分桶，append-only）。

用法：
  python record_diagnosis.py --user <user_id> [--name <姓名>] --kp CH1-03 \
         [--question KP-CH1-07] --result wrong --error-type 符号形式

字段说明：
  --user       用户唯一标识（学号/姓名拼音/平台注入的ID），必填
  --name       用户显示名（可选，首次可填）
  --kp         知识大点ID（如 CH1-03），必填
  --question   题目ID（如 KP-CH1-07；未匹配时省略或填 "未匹配"），可选
  --result     判定结果：wrong / correct，必填
  --error-type 错误大类（见 SKILL.md 步骤3）：概念性/方法性/符号形式/计算粗心/其他。
               答错时建议显式指定；缺省时记为「其他」（不参与错误聚类）并打印警告；答对时留空。

作用：正确率不在本文件维护，读取时按 history 现算。
"""
import json, os, argparse, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, "student_progress.json")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True)
    ap.add_argument("--name", default=None)
    ap.add_argument("--kp", required=True)
    ap.add_argument("--question", default=None)
    ap.add_argument("--result", required=True, choices=["wrong", "correct"])
    ap.add_argument("--error-type", default=None,
                    choices=["概念性", "方法性", "符号形式", "计算粗心", "其他"])
    args = ap.parse_args()

    if args.result not in ("wrong", "correct"):
        print("error: result 必须是 wrong 或 correct")
        return 1

    # 错误大类：答错时显式指定；缺省记为「其他」并警告；答对时置空
    et = args.error_type
    if args.result == "wrong" and et is None:
        print("warning: --result wrong 但未指定 --error-type，已记为「其他」（不参与错误聚类），建议显式指定")
        et = "其他"
    elif args.result == "correct":
        et = None

    data = {}
    if os.path.exists(PATH) and os.path.getsize(PATH) > 0:
        data = json.load(open(PATH, encoding="utf-8-sig"))
    data.setdefault("schema_version", "2.0")
    users = data.setdefault("users", {})
    u = users.setdefault(args.user, {"name": args.name or args.user, "history": []})
    if args.name:
        u["name"] = args.name
    u["history"].append({
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "question_id": args.question or "未匹配",
        "kp": args.kp,
        "result": args.result,
        "error_type": et,
    })
    json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"已记录: user={args.user} kp={args.kp} result={args.result} 大类={et}  (共 {len(u['history'])} 条)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
