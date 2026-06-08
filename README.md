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

> ⏰ Last updated: 2026-06-08 22:30 UTC
>
> Data source: `GitHub Search API`
>
> The table below is rewritten on every cron tick. Star the repo to bookmark.

<!-- TRACKER_TABLE_START -->
| # | Name | ⭐ | Lang | Updated | Install | Description |
|---|------|---|------|---------|---------|-------------|
| 1 | [cognis-digital/claimtrace](https://github.com/cognis-digital/claimtrace) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/claimtrace/) | Misinformation provenance tracer — earliest-known appearance graph |
| 2 | [cognis-digital/trialwatch](https://github.com/cognis-digital/trialwatch) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/trialwatch/) | Query, diff, and monitor ClinicalTrials.gov records, alerting on status, enrollment, or result changes. |
| 3 | [cognis-digital/synthcohort](https://github.com/cognis-digital/synthcohort) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/synthcohort/) | Generate statistically realistic synthetic patient cohorts (FHIR/CSV) from a schema spec for dev and testing. |
| 4 | [cognis-digital/phiscrub](https://github.com/cognis-digital/phiscrub) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/phiscrub/) | Stream-scan logs, CSVs, and free-text notes for PHI (names, MRNs, SSNs, dates, addresses) and redact or tokenize in plac |
| 5 | [cognis-digital/hl7tap](https://github.com/cognis-digital/hl7tap) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/hl7tap/) | Parse, pretty-print, diff, and replay HL7 v2 messages over MLLP from the terminal. |
| 6 | [cognis-digital/fhirlint](https://github.com/cognis-digital/fhirlint) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/fhirlint/) | Validate FHIR R4/R5 resources and bundles against profiles (US Core, etc.) with precise, line-level error reporting. |
| 7 | [cognis-digital/dicomsweep](https://github.com/cognis-digital/dicomsweep) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/dicomsweep/) | De-identify DICOM imaging studies per the DICOM PS3.15 Annex E profile, scrubbing tags and burned-in pixel text. |
| 8 | [cognis-digital/deidproof](https://github.com/cognis-digital/deidproof) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/deidproof/) | Re-identification risk assessment that computes k-anonymity, l-diversity, and HIPAA Safe Harbor compliance on a dataset. |
| 9 | [cognis-digital/consentledger](https://github.com/cognis-digital/consentledger) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/consentledger/) | Maintain a tamper-evident, hash-chained audit log of patient-data access and consent events. |
| 10 | [cognis-digital/codemap](https://github.com/cognis-digital/codemap) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/codemap/) | Translate and validate medical codes across ICD-10, SNOMED CT, LOINC, RxNorm, and CPT from the CLI. |
| 11 | [cognis-digital/baadiff](https://github.com/cognis-digital/baadiff) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/baadiff/) | Scan a repo or infra manifest for HIPAA Security Rule gaps and produce a Business Associate readiness scorecard. |
| 12 | [cognis-digital/webhookvty](https://github.com/cognis-digital/webhookvty) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/webhookvty/) | Verifies and replays signed payment webhooks (Stripe/Adyen/PayPal/Plaid) locally, catching signature, idempotency, and r |
| 13 | [mountainowl/bubo](https://github.com/mountainowl/bubo) | 0 | Python | 2026-06-08 | — | Bubo 🦉 — agentic AI code review for GitLab MRs and GitHub PRs, with the LLM of your choice. Posts only actionable findin |
| 14 | [cognis-digital/txgraph](https://github.com/cognis-digital/txgraph) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/txgraph/) | Builds a transaction graph from ledger/account data and surfaces structuring, layering, and mule-network patterns for AM |
| 15 | [cognis-digital/tokenvault](https://github.com/cognis-digital/tokenvault) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/tokenvault/) | Self-hostable PCI tokenization microservice and CLI that swaps PANs for format-preserving tokens and proves no raw card  |
| 16 | [cognis-digital/sanctscan](https://github.com/cognis-digital/sanctscan) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/sanctscan/) | Screens counterparties and transactions against OFAC/EU/UN sanctions lists with fuzzy name matching and explainable hit  |
| 17 | [cognis-digital/panhound](https://github.com/cognis-digital/panhound) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/panhound/) | Scans code, logs, fixtures, and S3 buckets for leaked PANs (Luhn-validated card numbers) and CVVs before they hit prod. |
| 18 | [cognis-digital/obscan](https://github.com/cognis-digital/obscan) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/obscan/) | Conformance and security linter for Open Banking / FAPI APIs: validates OAuth flows, consent scopes, and PSD2 endpoints  |
| 19 | [cognis-digital/ledgerproof](https://github.com/cognis-digital/ledgerproof) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/ledgerproof/) | Verifies double-entry ledger integrity and tamper-evidence by checking balance invariants and hash-chained journal entri |
| 20 | [cognis-digital/iso20022](https://github.com/cognis-digital/iso20022) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/iso20022/) | Validates, lints, and diffs ISO 20022 / pacs / camt payment messages and translates legacy MT into MX with schema-aware  |
| 21 | [cognis-digital/fraudlens](https://github.com/cognis-digital/fraudlens) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/fraudlens/) | Replays a stream of transactions against pluggable fraud rules and ML scorers, emitting precision/recall and alert volum |
| 22 | [cognis-digital/chargeguard](https://github.com/cognis-digital/chargeguard) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/chargeguard/) | Monitors dispute/chargeback feeds, flags fraud-rate threshold breaches (VAMP/Visa), and drafts representment evidence pa |
| 23 | [cognis-digital/sbirscout](https://github.com/cognis-digital/sbirscout) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/sbirscout/) | SBIR/STTR topic discovery — DSIP + SBIR.gov + NIH digest with bid scoring |
| 24 | [cognis-digital/gsafinder](https://github.com/cognis-digital/gsafinder) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/gsafinder/) | GSA Schedule opportunity surveyor — SAM.gov + eBuy + FedConnect |
| 25 | [COBACOBAINI/vibe](https://github.com/COBACOBAINI/vibe) | 8 | TypeScript | 2026-06-08 | — | Transcribe audio and video offline with OpenAI Whisper on your device, keeping data private. Supports many languages wit |
| 26 | [cognis-digital/fedramplens](https://github.com/cognis-digital/fedramplens) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/fedramplens/) | FedRAMP boundary visualizer & OSCAL-format SSP/POAM generator |
| 27 | [cognis-digital/cmmcmap](https://github.com/cognis-digital/cmmcmap) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/cmmcmap/) | CMMC Level 2 practice mapper — stack-aware SSP skeleton generator |
| 28 | [cognis-digital/clearancepath](https://github.com/cognis-digital/clearancepath) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/clearancepath/) | Personnel clearance hygiene tracker — SF-86, SEAD-3/4, training currency |
| 29 | [cognis-digital/checkpoint-ai](https://github.com/cognis-digital/checkpoint-ai) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/checkpoint-ai/) | NIST AI RMF / EU AI Act / ISO 42001 self-assessment & SSP generator |
| 30 | [cognis-digital/tokenmeter](https://github.com/cognis-digital/tokenmeter) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/tokenmeter/) | Token and cost counter / budgeter for LLM apps, CI-ready |
| 31 | [cognis-digital/shipcheck](https://github.com/cognis-digital/shipcheck) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/shipcheck/) | Dockerfile linter with image-size and CVE advisories |
| 32 | [cognis-digital/promptlint](https://github.com/cognis-digital/promptlint) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/promptlint/) | Lint, version, and test prompts as code with a CI gate |
| 33 | [cognis-digital/mcpforge](https://github.com/cognis-digital/mcpforge) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/mcpforge/) | Scaffold, test, and publish MCP servers in minutes |
| 34 | [cognis-digital/licenselens](https://github.com/cognis-digital/licenselens) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/licenselens/) | Dependency license + SBOM gate, developer-CLI first |
| 35 | [cognis-digital/gitstory](https://github.com/cognis-digital/gitstory) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/gitstory/) | Changelog and release notes from conventional commits |
| 36 | [cognis-digital/flakefinder](https://github.com/cognis-digital/flakefinder) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/flakefinder/) | Flaky-test detector from CI history with quarantine suggestions |
| 37 | [cognis-digital/envdoctor](https://github.com/cognis-digital/envdoctor) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/envdoctor/) | .env validator, secret-presence and config-drift checker |
| 38 | [cognis-digital/codeglance](https://github.com/cognis-digital/codeglance) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/codeglance/) | Repo onboarding map — architecture + hotspots for humans and agents |
| 39 | [cognis-digital/apidiff](https://github.com/cognis-digital/apidiff) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/apidiff/) | Breaking-change detector for OpenAPI / GraphQL across commits |
| 40 | [cognis-digital/pipewatch-pro](https://github.com/cognis-digital/pipewatch-pro) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/pipewatch-pro/) | CI/CD supply-chain auditor — GH Actions / GitLab CI / OWASP CI/CD Top 10 |
| 41 | [cognis-digital/ossaudit](https://github.com/cognis-digital/ossaudit) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/ossaudit/) | OSS license compliance auditor — AGPL contamination + NOTICE generation |
| 42 | [cognis-digital/depgraph](https://github.com/cognis-digital/depgraph) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/depgraph/) | Dependency risk visualizer — Scorecard + OSV + typosquat + maintainer signals |
| 43 | [cognis-digital/uaslog](https://github.com/cognis-digital/uaslog) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/uaslog/) | Counter-UAS telemetry/log analyzer that flags drone-detection events, RF bands, and track anomalies. |
| 44 | [cognis-digital/threatmodeler](https://github.com/cognis-digital/threatmodeler) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/threatmodeler/) | Generate STRIDE threat models and attack trees from a YAML system spec. |
| 45 | [salems-3Dpov/ai-agent-pipeline](https://github.com/salems-3Dpov/ai-agent-pipeline) | 1 | Python | 2026-06-08 | — | 🐙 AI Agent Pipeline routes queries by intent to docs, weather, or chat, with LangGraph, ChromaDB, and LangSmith for modu |
| 46 | [cognis-digital/sigmeta](https://github.com/cognis-digital/sigmeta) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/sigmeta/) | Parse and classify signal metadata (freq, modulation, bandwidth) into a normalized catalog. |
| 47 | [cognis-digital/rfsurvey](https://github.com/cognis-digital/rfsurvey) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/rfsurvey/) | Analyze RF spectrum-occupancy CSV/metadata for band usage, interference, and anomalies. |
| 48 | [cognis-digital/readiness](https://github.com/cognis-digital/readiness) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/readiness/) | Compute unit readiness (C-ratings style) from a personnel/equipment/training YAML and flag gaps. |
| 49 | [cognis-digital/opsecscan](https://github.com/cognis-digital/opsecscan) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/opsecscan/) | Scan documents and file metadata for OPSEC leaks: geotags, author, GPS EXIF, unit identifiers. |
| 50 | [cognis-digital/natosymbol](https://github.com/cognis-digital/natosymbol) | 0 | Python | 2026-06-08 | ✅ [pip install](https://linny006.github.io/mcp-servers-live/r/cognis-digital/natosymbol/) | Generate and validate APP-6/MIL-STD-2525 symbol identification codes (SIDC). |
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
