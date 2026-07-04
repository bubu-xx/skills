# skills

開発の各工程・各方法論を細かくスキル化したライブラリ。ウォーターフォールでもアジャイルでも、どの進め方を選んでも「その作業のスキルがある」状態を目指す。

A library of fine-grained development skills (requirements grilling, TDD, DDD, waterfall/agile/SDD orchestrators, and more) for Claude Code and other agents. Docs are in Japanese.

## インストール

```
npx skills add bubu-xx/skills -a claude-code
```

## 構成

```
skills/
  mode/          # 振る舞いモード（grill, tdd, ddd, spike, refactor, adversarial-review）
  generator/     # 成果物ジェネレータ（user-story, adr, api-first, runbook ...）
  orchestrator/  # 進め方の指揮者（waterfall, agile, sdd, lean-mvp）※明示起動のみ
```

- 全スキルの一覧・設計原理・使い分けは **[CATALOG.md](CATALOG.md)** を参照
- スキル同士は成果物（`docs/<機能名>/` の status ヘッダ付きドキュメント）で疎結合に連携する
- 検証: `python scripts/validate_skills.py`
