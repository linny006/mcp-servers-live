# mcp-servers-live

> GitHub 上の MCP サーバーを 15 分ごとに自動更新するインデックス

[English](./README.md) · [中文](./README_CN.md) · **日本語** · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md)

[![Stars](https://img.shields.io/github/stars/linny006/mcp-servers-live?style=for-the-badge&logo=github)](https://github.com/linny006/mcp-servers-live/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/mcp-servers-live?style=for-the-badge)](https://github.com/linny006/mcp-servers-live/commits)

---

GitHub Search API を 15 分ごとに叩いて、新しい Model Context Protocol (MCP) サーバーを自動で発見・整理・ランキングするライブトラッカーです。手動メンテの awesome リストとは違い、スター数・コミット履歴・リリースの鮮度といったリアルタイムの活動状況を反映しているので、実際に開発が続いている MCP インテグレーションをすぐに見つけられます。

このリストは GitHub Actions の cron によって**15 分ごとに自動更新**されます。各コミットはアップストリームデータの実際の変化（新規追加・期限切れ削除）を反映しているので、表示内容は常に最新です。

---

15 分ごとに GitHub Action が `tracker.py` を実行します。スクリプトの処理内容：

1. `GitHub Search API` から最新の状態を取得。
2. `data/items.json`（前回のスナップショット）と差分を比較。
3. `<!-- TRACKER_TABLE_* -->` マーカー間のテーブルを書き換え。
4. 変更があれば `feat: +N added, -M removed (timestamp)` をコミット。

外部サービス不要。有料 API 不要。公開データソースと無料の GitHub Action だけで動きます。

---

## 📋 Live data

ライブデータのテーブルは英語版 README で確認できます

---

## 🔗 Related live trackers

- [trending-claude-skills](https://github.com/linny006/trending-claude-skills) — What's shipping in Claude Skills this week (`topic:claude-skills`)
- [cursor-rules-live](https://github.com/linny006/cursor-rules-live) — Newest Cursor rules and .cursorrules patterns (`topic:cursor-rules`)
- [claude-code-plugin-tracker](https://github.com/linny006/claude-code-plugin-tracker) — Claude Code plugins and hook configs (`topic:claude-code`)
- [llm-agents-radar](https://github.com/linny006/llm-agents-radar) — Newest LLM agent frameworks (`topic:llm-agent`)
- [rag-radar](https://github.com/linny006/rag-radar) — Newest RAG implementations and tools (`topic:rag`)
- [llm-eval-tracker](https://github.com/linny006/llm-eval-tracker) — Newest LLM evaluation tools and benchmarks (`topic:llm-eval`)
- [agent-framework-radar](https://github.com/linny006/agent-framework-radar) — Newest agent frameworks shipping on GitHub (`topic:agent-framework`)
- [vector-db-live](https://github.com/linny006/vector-db-live) — Newest vector DB projects and integrations (`topic:vector-database`)
- [llmops-radar](https://github.com/linny006/llmops-radar) — Newest LLMOps tooling (observability, deployment) (`topic:llmops`)
- [prompt-tools-live](https://github.com/linny006/prompt-tools-live) — Newest prompt-engineering tools and prompt repos (`topic:prompt-engineering`)
- [agent-eval-harness](https://github.com/linny006/agent-eval-harness) — Live benchmark of AI coding agents (`topic:llm-eval`)
- [skills-tracker](https://github.com/linny006/skills-tracker) — Tracking new GitHub 'skills' repos (`topic:agent-skills`)
- [awesome-agent-skills](https://github.com/linny006/awesome-agent-skills) — Curated auto-updated awesome-list of AI agent skills (`topic:agent-skills`)

---

## 📜 License

MIT — see `LICENSE`.
