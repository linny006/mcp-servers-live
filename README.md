<!--
SEO: mcp servers live index
-->

<div align="center">

# MCP Servers Live Index

Auto-updated index of MCP servers shipping on GitHub, refreshed every 15 minutes

[![Stars](https://img.shields.io/github/stars/linny006/mcp-servers-live?style=for-the-badge&logo=github)](https://github.com/linny006/mcp-servers-live/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/mcp-servers-live?style=for-the-badge)](https://github.com/linny006/mcp-servers-live/commits)
[![Items](https://img.shields.io/badge/Tracked_Items-50-brightgreen?style=for-the-badge)](#)
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

> ⏰ Last updated: 2026-06-02 14:30 UTC
>
> Data source: `GitHub Search API`
>
> The table below is rewritten on every cron tick. Star the repo to bookmark.

<!-- TRACKER_TABLE_START -->
| # | Name | ⭐ | Lang | Updated | Install | Description |
|---|------|---|------|---------|---------|-------------|
| 1 | [cyanheads/noaa-cdo-mcp-server](https://github.com/cyanheads/noaa-cdo-mcp-server) | 1 | TypeScript | 2026-06-02 | — | Search NOAA CDO stations and datasets, fetch historical weather observations via MCP. STDIO or Streamable HTTP. |
| 2 | [cyanheads/onebusaway-mcp-server](https://github.com/cyanheads/onebusaway-mcp-server) | 1 | TypeScript | 2026-06-02 | ✅ [docker run](https://linny006.github.io/mcp-servers-live/r/cyanheads/onebusaway-mcp-server/) | Query stops, routes, real-time arrivals, vehicle positions, and schedules from OneBusAway transit APIs via MCP. STDIO or |
| 3 | [cyanheads/nhtsa-vehicle-safety-mcp-server](https://github.com/cyanheads/nhtsa-vehicle-safety-mcp-server) | 1 | TypeScript | 2026-06-02 | ✅ [docker run](https://linny006.github.io/mcp-servers-live/r/cyanheads/nhtsa-vehicle-safety-mcp-server/) | Vehicle safety data from NHTSA — recalls, complaints, crash ratings, investigations, VIN decoding. |
| 4 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 190740 | TypeScript | 2026-06-02 | ✅ [docker run](https://linny006.github.io/mcp-servers-live/r/n8n-io/n8n/) | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host  |
| 5 | [cyanheads/nist-nvd-mcp-server](https://github.com/cyanheads/nist-nvd-mcp-server) | 1 | TypeScript | 2026-06-02 | ✅ [docker run](https://linny006.github.io/mcp-servers-live/r/cyanheads/nist-nvd-mcp-server/) | Search and audit CVEs by keyword, severity, CWE, CISA KEV status, and CPE via the NIST National Vulnerability Database.  |
| 6 | [cyanheads/hn-mcp-server](https://github.com/cyanheads/hn-mcp-server) | 2 | TypeScript | 2026-06-02 | ✅ [docker run](https://linny006.github.io/mcp-servers-live/r/cyanheads/hn-mcp-server/) | MCP server for Hacker News. Feeds, threaded discussions, user profiles, and full-text search via the HN Firebase and Alg |
| 7 | [cyanheads/gbif-biodiversity-mcp-server](https://github.com/cyanheads/gbif-biodiversity-mcp-server) | 1 | TypeScript | 2026-06-02 | — | Search GBIF species taxonomy, occurrence records, datasets, and publishers via MCP. STDIO or Streamable HTTP. |
| 8 | [proompteng/bilig](https://github.com/proompteng/bilig) | 30 | TypeScript | 2026-06-02 | ✅ [npm install](https://linny006.github.io/mcp-servers-live/r/proompteng/bilig/) | Headless spreadsheet workbooks for Node services and agents, no need for excel or browser |
| 9 | [cyanheads/gdelt-mcp-server](https://github.com/cyanheads/gdelt-mcp-server) | 1 | TypeScript | 2026-06-02 | ✅ [docker run](https://linny006.github.io/mcp-servers-live/r/cyanheads/gdelt-mcp-server/) | Search and analyze global news coverage and US television transcripts via the GDELT Project's real-time APIs via MCP. ST |
| 10 | [griddynamics/rosetta](https://github.com/griddynamics/rosetta) | 224 | Python | 2026-06-02 | ✅ [claude mcp add](https://linny006.github.io/mcp-servers-live/r/griddynamics/rosetta/) | Meta-prompting, context engineering, and centralized instructions management for AI coding agents |
| 11 | [oomkapwn/enquire-mcp](https://github.com/oomkapwn/enquire-mcp) | 9 | TypeScript | 2026-06-02 | ✅ [claude mcp add](https://linny006.github.io/mcp-servers-live/r/oomkapwn/enquire-mcp/) | The most advanced Obsidian MCP — long-term memory for AI agents. Hybrid retrieval (BM25 + ML + BGE rerank, RRF-fused), H |
| 12 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | 16253 | TypeScript | 2026-06-02 | ✅ [claude mcp add](https://linny006.github.io/mcp-servers-live/r/mksglu/context-mode/) | Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 15 platforms |
| 13 | [systempromptio/systemprompt-template](https://github.com/systempromptio/systemprompt-template) | 14 | Rust | 2026-06-02 | — | AI Governance Infrastructure — local evaluation. The governance layer for AI agents: a single compiled Rust binary that  |
| 14 | [eslaim/AI-Diagram-Prototype-Generator-MCP-Server-](https://github.com/eslaim/AI-Diagram-Prototype-Generator-MCP-Server-) | 0 | Python | 2026-06-02 | — | 🤖 Generate AI-driven diagrams and prototypes in draw.io and HTML formats, tailored to your requirements with advanced la |
| 15 | [Bruno1702vm/AI-Infra](https://github.com/Bruno1702vm/AI-Infra) | 0 | — | 2026-06-02 | — | 🌐 Explore AI-Infra to visualize the AI infrastructure landscape and discover a structured learning path for building in  |
| 16 | [Hyperkorn/qdrant-neo4j-crawl4ai-mcp](https://github.com/Hyperkorn/qdrant-neo4j-crawl4ai-mcp) | 3 | Python | 2026-06-02 | — | 🧠 Enhance AI coordination with the Qdrant Neo4j Crawl4AI MCP server, combining vector search, knowledge graphs, and web  |
| 17 | [Jimartskenya/ai-code-context](https://github.com/Jimartskenya/ai-code-context) | 2 | TypeScript | 2026-06-02 | — | 🤖 Automate code documentation with AI to enhance understanding and streamline your workflow, saving time on unfamiliar c |
| 18 | [speakeasy-api/gram](https://github.com/speakeasy-api/gram) | 244 | TypeScript | 2026-06-02 | — | Securely scale AI usage across your organization.  Control plane for building, securing and monitoring your agents, mcp  |
| 19 | [OneGoodArea/OneGoodArea](https://github.com/OneGoodArea/OneGoodArea) | 0 | TypeScript | 2026-06-02 | ✅ [npm install](https://linny006.github.io/mcp-servers-live/r/OneGoodArea/OneGoodArea/) | The deterministic UK location intelligence layer. Intent-driven scoring for regulated B2B (mortgage lenders, insurers, P |
| 20 | [gambletan/cortex](https://github.com/gambletan/cortex) | 15 | Rust | 2026-06-02 | ✅ [claude mcp add](https://linny006.github.io/mcp-servers-live/r/gambletan/cortex/) | Private. Free. Local. — Memory engine for personal AI agents. AES-256-GCM encrypted, 73.7% on LoCoMo (beats Mem0), 156µs |
| 21 | [asciimoo/hister](https://github.com/asciimoo/hister) | 1115 | Go | 2026-06-02 | — | Your own search engine |
| 22 | [JasonFinestone/runspec](https://github.com/JasonFinestone/runspec) | 0 | Python | 2026-06-02 | ✅ [npm install](https://linny006.github.io/mcp-servers-live/r/JasonFinestone/runspec/) | A language-agnostic, TOML-based interface specification for anything runnable — scripts, applications, and MCP tools — r |
| 23 | [Brahhime/yokai-mcp-template](https://github.com/Brahhime/yokai-mcp-template) | 0 | Go | 2026-06-02 | — |  |
| 24 | [FezAreCool/mcp-claude-hackernews](https://github.com/FezAreCool/mcp-claude-hackernews) | 0 | — | 2026-06-02 | — | 🚀 Connect Claude Desktop with Hacker News through the Model Context Protocol (MCP) for seamless interactions and enhance |
| 25 | [ImpactMojo/ImpactMojo](https://github.com/ImpactMojo/ImpactMojo) | 1 | HTML | 2026-06-02 | — | Free development education platform for South Asia — 48 courses, 16 games, 11 labs, 400+ handouts, 200 case studies, MCP |
| 26 | [maximhq/bifrost](https://github.com/maximhq/bifrost) | 5424 | Go | 2026-06-02 | ✅ [npx](https://linny006.github.io/mcp-servers-live/r/maximhq/bifrost/) | Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ mod |
| 27 | [pedrohenrique316/Cursor-history-MCP](https://github.com/pedrohenrique316/Cursor-history-MCP) | 2 | Python | 2026-06-02 | — | 🚀 Extract and vectorize your Cursor chat history, enabling efficient search through a Dockerized FastAPI API with LanceD |
| 28 | [Omkarjamadar/MCP-server-client-computer-use-ai-sdk](https://github.com/Omkarjamadar/MCP-server-client-computer-use-ai-sdk) | 2 | Rust | 2026-06-02 | — | 🖥️ Control your computer effortlessly with our AI SDK, enabling seamless interaction with apps and websites without virt |
| 29 | [Johnza06/advance-fraud-analyst](https://github.com/Johnza06/advance-fraud-analyst) | 1 | Python | 2026-06-02 | — | 🛡️ Analyze transactions for fraud using advanced models and tools, providing insights and risk scores to enhance investi |
| 30 | [cyanheads/fcc-broadband-mcp-server](https://github.com/cyanheads/fcc-broadband-mcp-server) | 1 | TypeScript | 2026-06-02 | ✅ [docker run](https://linny006.github.io/mcp-servers-live/r/cyanheads/fcc-broadband-mcp-server/) | Access FCC broadband availability, coverage analysis, and digital divide data for US geographies and census blocks via M |
| 31 | [sailorpepe/undesirables-mcp-server](https://github.com/sailorpepe/undesirables-mcp-server) | 0 | Python | 2026-06-02 | ✅ [npm install](https://linny006.github.io/mcp-servers-live/r/sailorpepe/undesirables-mcp-server/) | Zero-trust Python FastMCP intelligence core for The Undesirables Ecosystem. Enables 100% local, offline AI agent tool-ca |
| 32 | [WP2-Danikusuma/AgentX](https://github.com/WP2-Danikusuma/AgentX) | 1 | HTML | 2026-06-02 | — | 🤖 Build personalized intelligent agents easily with AgentX, a platform that simplifies creation using natural language a |
| 33 | [sohail123op/markitdown-mcp](https://github.com/sohail123op/markitdown-mcp) | 3 | Python | 2026-06-02 | — | 📄 Convert 29+ file formats to clean Markdown using the Model Context Protocol for seamless integration with AI workflows |
| 34 | [RavenQueen03/btp-sap-odata-to-mcp-server](https://github.com/RavenQueen03/btp-sap-odata-to-mcp-server) | 2 | — | 2026-06-02 | — | 🌐 Expose SAP OData services as dynamic MCP tools, enabling natural language interactions with your ERP data for enhanced |
| 35 | [antonbabenko/deliberation](https://github.com/antonbabenko/deliberation) | 41 | JavaScript | 2026-06-02 | — | Ask Codex, Gemini/Antigravity, Grok (xAI), and 400+ more models through OpenRouter including Qwen, Kimi, DeepSeek for se |
| 36 | [memtomem/memtomem-stm](https://github.com/memtomem/memtomem-stm) | 2 | Python | 2026-06-02 | ✅ [claude mcp add](https://linny006.github.io/mcp-servers-live/r/memtomem/memtomem-stm/) | Short-term memory proxy gateway with proactive memory surfacing for AI agents |
| 37 | [cyanheads/eia-energy-mcp-server](https://github.com/cyanheads/eia-energy-mcp-server) | 1 | TypeScript | 2026-06-02 | — | Browse and query the U.S. Energy Information Administration API v2 — electricity, petroleum, natural gas, coal, forecast |
| 38 | [sumithr/sumo-qa](https://github.com/sumithr/sumo-qa) | 4 | Python | 2026-06-02 | ✅ [uvx](https://linny006.github.io/mcp-servers-live/r/sumithr/sumo-qa/) | MCP server that brings senior-QA discipline to AI coding assistants — test planning, TDD, mutation testing, code review. |
| 39 | [cyanheads/eurostat-mcp-server](https://github.com/cyanheads/eurostat-mcp-server) | 1 | TypeScript | 2026-06-02 | — | Search and query 8,933 Eurostat datasets — EU economy, demography, trade, health, and NUTS regional data via MCP. STDIO  |
| 40 | [linny006/mcp-servers-live](https://github.com/linny006/mcp-servers-live) | 0 | HTML | 2026-06-02 | — | Auto-updated index of MCP servers shipping on GitHub, refreshed every 15 minutes |
| 41 | [Yapade0708/catalyst_builder](https://github.com/Yapade0708/catalyst_builder) | 0 | Python | 2026-06-02 | — | 🔧 Build and validate Catalyst Knowledge Packs to integrate seamlessly with external systems through simple YAML configur |
| 42 | [linny006/trending-claude-skills](https://github.com/linny006/trending-claude-skills) | 1 | Python | 2026-06-02 | — | Auto-updated leaderboard of trending claude-skills and AI agent repos, refreshed every 15 minutes |
| 43 | [26zl/cybersec-toolkit](https://github.com/26zl/cybersec-toolkit) | 7 | Python | 2026-06-02 | ✅ [docker run](https://linny006.github.io/mcp-servers-live/r/26zl/cybersec-toolkit/) | 580+ cybersecurity tools, one command. Modular bash installer for Linux & Termux with 14 profiles, 18 modules, and an MC |
| 44 | [ermermermermidk/mcp-ai-memory](https://github.com/ermermermermidk/mcp-ai-memory) | 1 | TypeScript | 2026-06-02 | — | 🧠 Manage AI context seamlessly with the MCP server for storing and retrieving semantic memory across sessions. Enhance y |
| 45 | [lemonade-sdk/lemonade](https://github.com/lemonade-sdk/lemonade) | 4194 | C++ | 2026-06-02 | — | Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join o |
| 46 | [nram-ai/nram](https://github.com/nram-ai/nram) | 4 | Go | 2026-06-02 | ✅ [claude mcp add](https://linny006.github.io/mcp-servers-live/r/nram-ai/nram/) | Self-hosted long-term memory substrate for any LLM-using tool. Hybrid vector + lexical recall with MMR reranking, auto-e |
| 47 | [giancarloerra/JanuScope](https://github.com/giancarloerra/JanuScope) | 18 | TypeScript | 2026-06-02 | — | Local-first MCP policy proxy. Tool-block, SQL-mutation gate, PII redact, audit, rate-limit, OpenTelemetry, vault secrets |
| 48 | [docsector/docsector-reader](https://github.com/docsector/docsector-reader) | 21 | JavaScript | 2026-06-02 | ✅ [npm install](https://linny006.github.io/mcp-servers-live/r/docsector/docsector-reader/) | A documentation rendering engine built with Vue 3, Quasar v2 and Vite with AI features. |
| 49 | [xcodethink/pixelcheck](https://github.com/xcodethink/pixelcheck) | 4 | TypeScript | 2026-06-02 | ✅ [npm install -g](https://linny006.github.io/mcp-servers-live/r/xcodethink/pixelcheck/) | MCP-first browser primitives for AI agents — real eyes and hands on the web. Local-first. Vendor-agnostic. |
| 50 | [SidCorp-co/forge](https://github.com/SidCorp-co/forge) | 4 | TypeScript | 2026-06-02 | — | Self-hosted lifecycle platform for software powered by Claude Code. Configurable pipelines, devices you control, no cred |
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
