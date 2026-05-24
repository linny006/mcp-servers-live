# mcp-servers-live

> 自动更新的 MCP 服务器索引，每 15 分钟从 GitHub 抓取最新数据

[English](./README.md) · **中文** · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md)

[![Stars](https://img.shields.io/github/stars/linny006/mcp-servers-live?style=for-the-badge&logo=github)](https://github.com/linny006/mcp-servers-live/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/mcp-servers-live?style=for-the-badge)](https://github.com/linny006/mcp-servers-live/commits)

---

一个实时追踪器，每 15 分钟调用 GitHub Search API，自动发现、归档并排名新的 Model Context Protocol (MCP) 服务器。不同于手动维护的 awesome 列表，本项目实时展示 star 数、提交记录和发布新鲜度，帮你找到真正在持续迭代的 MCP 集成项目。

列表由 GitHub Actions 定时任务**每 15 分钟自动更新**一次。每次提交都对应上游数据的真实变化——新增条目或移除过期条目——你看到的内容始终是最新的。

---

每 15 分钟，GitHub Action 会运行 `tracker.py`，脚本执行以下步骤：

1. 从 `GitHub Search API` 拉取最新数据。
2. 与 `data/items.json`（上次快照）做差异对比。
3. 在 `<!-- TRACKER_TABLE_* -->` 标记之间重写上方的表格。
4. 如有变化，提交 `feat: +N added, -M removed (timestamp)`。

无需外部服务，无需付费 API，只用公开数据源和免费的 GitHub Action。

---

## 📋 Live data

实时数据表格在英文版 README 中查看

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
