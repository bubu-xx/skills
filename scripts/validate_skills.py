#!/usr/bin/env python3
"""SKILL.md の最低限の品質チェック。量産時の事故（frontmatter 欠落、名前不一致、
契約ブロック抜け、階層の混在）を機械で拾う。"""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent / "skills"
errors = []

# 階層の混在チェック（浅い SKILL.md が深い方の発見を壊す）
for p in list(root.glob("SKILL.md")) + list(root.glob("*/SKILL.md")):
    errors.append(f"{p}: カタログ配置(skills/<種類>/<名前>/SKILL.md)と混在している")

skills = sorted(root.glob("*/*/SKILL.md"))
if not skills:
    errors.append("skills/<種類>/<名前>/SKILL.md が1つも見つからない")

for p in skills:
    text = p.read_text(encoding="utf-8")
    rel = p.relative_to(root.parent)
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        errors.append(f"{rel}: frontmatter が無い")
        continue
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)", fm, re.MULTILINE)
    if not name:
        errors.append(f"{rel}: name が無い")
    elif name.group(1) != p.parent.name:
        errors.append(f"{rel}: name '{name.group(1)}' がディレクトリ名 '{p.parent.name}' と不一致")
    if not re.search(r"^description:\s*\S", fm, re.MULTILINE):
        errors.append(f"{rel}: description が無い")
    if "種類:" not in text:
        errors.append(f"{rel}: 契約ブロック（種類:）が無い")
    if "## 防ぐ失敗" not in text:
        errors.append(f"{rel}: 「防ぐ失敗」節が無い")
    # 契約の種類とディレクトリの一致
    kind = re.search(r"種類:\s*(Mode|Generator|Orchestrator)", text)
    kind_dir = {"Mode": "mode", "Generator": "generator", "Orchestrator": "orchestrator"}
    if kind and kind_dir[kind.group(1)] != p.parent.parent.name:
        errors.append(f"{rel}: 契約の種類 '{kind.group(1)}' が配置 '{p.parent.parent.name}/' と不一致")
    # Orchestrator は明示起動のみ
    if p.parent.parent.name == "orchestrator" and "disable-model-invocation: true" not in fm:
        errors.append(f"{rel}: Orchestrator に disable-model-invocation: true が無い")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(skills)} skills validated")
