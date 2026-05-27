"""Update script for mcp-servers-live.

Runs on a cron via .github/workflows/update.yml every 15 minutes.
Fetches upstream MCP server repos, ALSO extracts install command +
Claude Desktop config snippet from each repo's README (the value-add —
readers can copy-paste). Diffs, rewrites README between sentinel
markers, writes new JSON snapshot, regenerates pSEO pages.
"""
from __future__ import annotations

import base64
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx


DATA_FILE = Path("data/items.json")
README_FILE = Path("README.md")
TABLE_START = "<!-- TRACKER_TABLE_START -->"
TABLE_END = "<!-- TRACKER_TABLE_END -->"
LAST_UPDATED_RE = re.compile(r"^> ⏰ Last updated: .+$", re.MULTILINE)
ITEMS_BADGE_RE = re.compile(r"badge/Tracked_Items-\d+-brightgreen")


GITHUB_QUERY = 'topic:mcp-server sort:updated-desc'
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
MAX_ITEMS = 50

REPO_OWNER = "linny006"
REPO_SLUG = "mcp-servers-live"
REPO_TITLE = "MCP Servers Live"
REPO_BASE_URL = f"https://{REPO_OWNER}.github.io/{REPO_SLUG}"
REPO_TOPIC = "mcp-server"
REPO_NICHE = "mcp"


# Patterns to extract from a source repo's README, ranked by signal strength.
# Each tuple = (label, compiled regex). First match wins per category.

# Install commands — any line within a code block that starts with one of these.
INSTALL_PATTERNS = [
    ("claude mcp add",       re.compile(r"^(claude\s+mcp\s+add\s+[^\n]+)", re.MULTILINE)),
    ("npm install -g",       re.compile(r"^(npm\s+install\s+-g\s+@?[\w./@-]+)", re.MULTILINE)),
    ("npm install",          re.compile(r"^(npm\s+install\s+@?[\w./@-]+)", re.MULTILINE)),
    ("npx",                  re.compile(r"^(npx\s+-y\s+@?[\w./@-]+(?:\s+[\w./@-]+)*)", re.MULTILINE)),
    ("uvx",                  re.compile(r"^(uvx\s+[\w./@-]+(?:\s+[\w./@-]+)*)", re.MULTILINE)),
    ("uv pip install",       re.compile(r"^(uv\s+pip\s+install\s+[\w./@-]+)", re.MULTILINE)),
    ("pip install",          re.compile(r"^(pip\s+install\s+[\w./@-]+)", re.MULTILINE)),
    ("pipx install",         re.compile(r"^(pipx\s+install\s+[\w./@-]+)", re.MULTILINE)),
    ("cargo install",        re.compile(r"^(cargo\s+install\s+[\w./@-]+)", re.MULTILINE)),
    ("docker run",           re.compile(r"^(docker\s+run\s+[^\n]+)", re.MULTILINE)),
    ("docker pull",          re.compile(r"^(docker\s+pull\s+[^\n]+)", re.MULTILINE)),
]

# Match a fenced JSON code block that contains "mcpServers" — likely a
# claude_desktop_config.json snippet ready to copy.
MCP_CONFIG_RE = re.compile(
    r"```(?:json|jsonc)?\s*\n(\{[^`]*?\"mcpServers\"[^`]*?\})\s*\n```",
    re.DOTALL,
)


def _auth_headers() -> dict:
    h = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"token {GITHUB_TOKEN}"
    return h


def _fetch_readme(full_name: str) -> str:
    """Return the source repo's README text, or empty string."""
    try:
        r = httpx.get(
            f"https://api.github.com/repos/{full_name}/readme",
            headers=_auth_headers(), timeout=15,
        )
        if r.status_code != 200:
            return ""
        data = r.json()
        if data.get("encoding") == "base64":
            return base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    except Exception:
        pass
    return ""


def fetch_install_info(full_name: str) -> dict:
    """Extract install command + (optional) Claude Desktop config from a
    source repo's README.

    Returns {"install_cmd": "...", "install_kind": "...",
             "claude_config": "..." (optional)} or {} if nothing usable found.
    """
    readme = _fetch_readme(full_name)
    if not readme:
        return {}

    out = {}

    for kind, pat in INSTALL_PATTERNS:
        m = pat.search(readme)
        if m:
            cmd = m.group(1).strip()
            # Reject lines that look like comments / fragments
            if len(cmd) < 200 and len(cmd) > 5:
                out["install_cmd"] = cmd
                out["install_kind"] = kind
                break

    cfg = MCP_CONFIG_RE.search(readme)
    if cfg:
        snippet = cfg.group(1).strip()
        if len(snippet) < 4000:
            out["claude_config"] = snippet

    return out


def fetch_items() -> list[dict]:
    if not GITHUB_TOKEN:
        print("WARN: GITHUB_TOKEN not set; running with anonymous quota")

    url = "https://api.github.com/search/repositories"
    params = {"q": GITHUB_QUERY, "sort": "updated", "order": "desc", "per_page": MAX_ITEMS}
    resp = httpx.get(url, headers=_auth_headers(), params=params, timeout=30)
    resp.raise_for_status()

    # Cache install_info from prev run when source repo unchanged.
    cache: dict[str, tuple[str, dict]] = {}
    if DATA_FILE.exists():
        try:
            prev_items = json.loads(DATA_FILE.read_text())
            for p in prev_items:
                if p.get("install_info") and p.get("id"):
                    cache[p["id"]] = (p.get("updated_at", ""), p["install_info"])
        except Exception:
            pass

    out: list[dict] = []
    n_fetched = 0
    n_cached = 0
    for r in resp.json().get("items", [])[:MAX_ITEMS]:
        item = {
            "id": r["full_name"],
            "name": r["full_name"],
            "url": r["html_url"],
            "stars": r["stargazers_count"],
            "language": r.get("language") or "—",
            "description": (r.get("description") or "")[:120],
            "updated_at": r["pushed_at"],
        }
        prev_updated, prev_info = cache.get(item["id"], ("", None))
        if prev_info and prev_updated == item["updated_at"]:
            item["install_info"] = prev_info
            n_cached += 1
        else:
            info = fetch_install_info(item["id"])
            if info:
                item["install_info"] = info
                n_fetched += 1
        out.append(item)

    n_with = sum(1 for x in out if x.get("install_info"))
    print(f"items={len(out)} with_install={n_with} (fetched={n_fetched}, cached={n_cached})")
    return out


def load_previous() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text())
    except json.JSONDecodeError:
        return []


def diff_counts(old: list[dict], new: list[dict]) -> tuple[int, int]:
    old_ids = {i["id"] for i in old}
    new_ids = {i["id"] for i in new}
    return len(new_ids - old_ids), len(old_ids - new_ids)


def render_table(items: list[dict]) -> str:
    if not items:
        return "_No items in the upstream feed right now. Next check in 15 minutes._"
    rows = ["| # | Name | ⭐ | Lang | Updated | Install | Description |",
            "|---|------|---|------|---------|---------|-------------|"]
    for i, it in enumerate(items, 1):
        name = f"[{it['name']}]({it['url']})"
        desc = (it.get("description") or "").replace("|", "\\|")
        updated = it.get("updated_at", "")[:10]
        owner, _, repo = it["name"].partition("/")
        install = it.get("install_info") or {}
        install_link = (
            f"✅ [{install.get('install_kind', 'view')}](https://linny006.github.io/mcp-servers-live/r/{owner}/{repo}/)"
            if install.get("install_cmd") else "—"
        )
        rows.append(
            f"| {i} | {name} | {it.get('stars', 0)} | {it.get('language', '—')} | "
            f"{updated} | {install_link} | {desc} |"
        )
    return "\n".join(rows)


def rewrite_readme(items: list[dict]) -> None:
    txt = README_FILE.read_text()

    table = render_table(items)
    section = f"{TABLE_START}\n{table}\n{TABLE_END}"
    pattern = re.compile(re.escape(TABLE_START) + r".*?" + re.escape(TABLE_END), re.DOTALL)
    txt = pattern.sub(section, txt)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    txt = LAST_UPDATED_RE.sub(f"> ⏰ Last updated: {now}", txt)

    txt = ITEMS_BADGE_RE.sub(f"badge/Tracked_Items-{len(items)}-brightgreen", txt)

    README_FILE.write_text(txt)


def main() -> int:
    items = fetch_items()
    previous = load_previous()
    added, removed = diff_counts(previous, items)

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(items, indent=2, sort_keys=True))
    rewrite_readme(items)

    try:
        import pseo
        meta = {
            "title": REPO_TITLE,
            "base_url": REPO_BASE_URL,
            "topic": REPO_TOPIC,
            "niche_label": REPO_NICHE,
            "update_interval_minutes": 15,
        }
        n_pages = pseo.generate_pages(items, meta)
        print(f"pseo: {n_pages} pages written")
    except Exception as exc:
        print(f"pseo: skipped (error: {exc})")

    now_short = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    msg = f"feat: +{added} added, -{removed} removed ({now_short})"
    print(msg)

    gho = os.environ.get("GITHUB_OUTPUT")
    if gho:
        with open(gho, "a") as f:
            f.write(f"message={msg}\n")
            f.write(f"changed={'true' if (added or removed) else 'false'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
