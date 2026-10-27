<!--
SEO: mcp servers live index
-->

<div align="center">

# MCP Servers Live Index

Auto-updated index of MCP servers shipping on GitHub, refreshed every 15 minutes

[![Stars](https://img.shields.io/github/stars/linny006/mcp-servers-live?style=for-the-badge&logo=github)](https://github.com/linny006/mcp-servers-live/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/mcp-servers-live?style=for-the-badge)](https://github.com/linny006/mcp-servers-live/commits)
[![Items](https://img.shields.io/badge/Tracked_Items-7-brightgreen?style=for-the-badge)](#)
[![Updated](https://img.shields.io/badge/Updates-every_15min-blue?style=for-the-badge)](#)

**⭐ Star this repo to bookmark — fresh data every 15 minutes**

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md)

</div>

## 🩺 Diagnose your installed MCP servers

```bash
npx github:linny006/mcp-doctor check
```

Health-checks every MCP server in your Claude Desktop config — finds stale packages, broken endpoints, renamed packages. [See mcp-doctor →](https://github.com/linny006/mcp-doctor)

---


---

## 💡 What is this?

A live tracker that queries the GitHub Search API every 15 minutes to discover, catalog, and rank new Model Context Protocol (MCP) servers. Unlike manually curated awesome-lists, this project surfaces real-time activity including stars, commits, and release freshness so developers can find actually-shipping MCP integrations.

This list is **auto-updated every 15 minutes** by a GitHub Actions cron.
Each commit reflects a real change in the upstream data source — new items added,
expired items removed — so you can rely on what you see being current.

---

## 📋 Current Items

> ⏰ Last updated: 2026-10-27 20:30 UTC
>
> Data source: `GitHub Search API`
>
> The table below is rewritten on every cron tick. Star the repo to bookmark.

<!-- TRACKER_TABLE_START -->
| # | Name | ⭐ | Lang | Updated | Install | Description |
|---|------|---|------|---------|---------|-------------|
| 1 | [SenjuWoo/Ultimate-AI-Starter-Bundle](https://github.com/SenjuWoo/Ultimate-AI-Starter-Bundle) | 6 | JavaScript | 2026-10-27 | — | Ultimate AI Starter Bundle multi-provider skills/MCP/plugins (Claude, Codex, Grok, Kimi, Hermes) + optional full Skyrim  |
| 2 | [aashishmahajan/kube-noob](https://github.com/aashishmahajan/kube-noob) | 0 | Python | 2026-10-27 | — | public agent for training everything kubernetes, helm, openshift rosa and stackrox |
| 3 | [ashlrai/ashlr-plugin](https://github.com/ashlrai/ashlr-plugin) | 3 | TypeScript | 2026-10-27 | — | Token-efficiency plugin for Claude Code and Codex: MCP tools and hooks that replace high-volume Read/Grep/Edit/Bash call |
| 4 | [cordanaLLM/praetor](https://github.com/cordanaLLM/praetor) | 0 | Go | 2026-10-27 | — | Enterprise Fleet Governance, Repository-as-Code & Universal AI Agent Engineering Engine |
| 5 | [tikoci/rosetta](https://github.com/tikoci/rosetta) | 51 | TypeScript | 2026-10-27 | ✅ [claude mcp add](https://linny006.github.io/mcp-servers-live/r/tikoci/rosetta/) | MCP Server with RouterOS docs + commands + products + changelogs, using SQLite-as-RAG, sourced from MikroTik |
| 6 | [heymrun/heym](https://github.com/heymrun/heym) | 1261 | Python | 2026-10-27 | ✅ [docker run](https://linny006.github.io/mcp-servers-live/r/heymrun/heym/) | Build agentic systems. Run them with confidence. Orchestrate agents, automate business processes, inspect every executio |
| 7 | [shashwatgtm/impact-mcp](https://github.com/shashwatgtm/impact-mcp) | 1 | TypeScript | 2026-10-27 | ✅ [npx](https://linny006.github.io/mcp-servers-live/r/shashwatgtm/impact-mcp/) | Hypothesis-Driven B2B Positioning Engine - 8 strategic positioning tools |
<!-- TRACKER_TABLE_END -->

---

## 🔍 How it works

Every 15 minutes, a GitHub Action runs `tracker.py`. That script:

1. Fetches the latest state from `GitHub Search API`.
2. Diffs against `data/items.json` (the previous snapshot).
3. Rewrites the table above between the `<!-- TRACKER_TABLE_* -->` markers.
4. Commits `feat: +N added, -M removed (timestamp)` if anything changed.

No external services. No paid APIs. Just a public data source and a free GitHub Action.

---

## 🤝 Contributing

See `CONTRIBUTING.md` — usually you don't need to: the tracker keeps itself current.
If you spot a data-source bug or want to suggest a new column for the table, open
an issue.

---

## 🔗 Related live trackers

If you find this useful, you might also like these other auto-updated
trackers from the same maintainer — same mechanism, different upstream:

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
