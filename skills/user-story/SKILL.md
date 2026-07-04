---
name: user-story
description: 要件をユーザーストーリー（〈誰〉として〈何〉がしたい、なぜなら〈理由〉）と受入基準(Given-When-Then)の形に整理する。Use when the user says "user-story", "/user-story", "ユーザーストーリーにして", "ストーリーで整理して", or requirements need to be organized by user value for agile development.
---

# User Story

```
種類: Generator
入力: 会話、または 要件 型の成果物
出力: 要件 型の変種（docs/<機能名>/requirements.md にストーリー形式で、status ヘッダ付き）
完成基準: 下記
```

## 出力の型

requirements.md（frontmatter: `type: 要件` / `feature:` / `status:`）に:

```markdown
## ストーリー: <短いタイトル>
<役割> として、<やりたいこと>。なぜなら <価値・理由>。

### 受入基準
- Given <前提の状態> When <操作> Then <期待する結果>
- Given ... When ... Then ...

### 優先度: 高 | 中 | 低
```

## ルール

- **「なぜなら」が書けないストーリーは要件にしない。** 価値の説明がつかない機能は、grill で詰め直すか捨てる
- **役割は具体的に。** 「ユーザーとして」で全部書けてしまうなら役割の解像度が足りない（例: 「初回訪問者として」「管理者として」）
- **1ストーリーは1回のリリースに収まる粒度。** 大きすぎたら分割する
- **受入基準は最低1つ、テスト可能な形で。** Then が観測できない基準は書き直す
- 受入基準はそのまま `tdd` のテストリストや `bdd` の入力になる形を保つ

## 完成基準

- [ ] すべてのストーリーに「なぜなら」がある
- [ ] すべてのストーリーに受入基準が1つ以上ある
- [ ] 優先度が付いている
- [ ] status ヘッダを付けた（目標 status は Orchestrator またはユーザー指定に従う）
