"""pSEO page generator for the live-tracker repo.

Reads data/items.json and writes filter + detail HTML pages to the repo
root, plus a sitemap.xml. Called by tracker.py on each cron tick.

Design goals:
- Pure HTML (no JS) so Googlebot indexes immediately.
- Each page has unique <title>, <meta description>, canonical URL,
  schema.org JSON-LD, OG/Twitter cards.
- 3-7 internal cross-links per page (PageRank flow).
- ~200 words of unique content per page (not just data dumps).
- Idempotent: re-running produces byte-identical output when items
  unchanged, so git diff stays clean.
"""
from __future__ import annotations

import datetime as _dt
import html
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


CSS = """
:root { --max: 880px; --fg: #1f2328; --muted: #59636e; --bg: #ffffff;
         --link: #0969da; --border: #d1d9e0; --card: #f6f8fa; }
* { box-sizing: border-box; }
body { margin: 0; padding: 16px; font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        color: var(--fg); background: var(--bg); }
.wrap { max-width: var(--max); margin: 0 auto; }
nav.bc { font-size: 14px; color: var(--muted); margin-bottom: 16px; }
nav.bc a { color: var(--muted); }
h1 { font-size: 28px; margin: 0 0 8px; }
h2 { font-size: 20px; margin: 24px 0 12px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }
p.lead { font-size: 18px; color: var(--muted); margin: 0 0 24px; }
a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; }
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px; }
th, td { padding: 8px 12px; text-align: left; border-bottom: 1px solid var(--border); }
th { background: var(--card); font-weight: 600; }
ul.crosslinks { list-style: none; padding: 0; }
ul.crosslinks li { padding: 6px 0; }
ul.crosslinks li a { font-weight: 500; }
.meta { display: flex; gap: 16px; flex-wrap: wrap; color: var(--muted); font-size: 14px; margin: 12px 0; }
.meta span::before { content: "\\00b7"; margin-right: 8px; color: var(--border); }
.meta span:first-child::before { content: ""; }
footer { margin: 40px 0 16px; padding-top: 16px; border-top: 1px solid var(--border); font-size: 14px; color: var(--muted); }
""".strip()


def _esc(s) -> str:
    return html.escape(str(s if s is not None else ""), quote=True)


def _slug(s: str) -> str:
    """Filesystem/URL-safe slug. Keeps a-z 0-9 -."""
    s = re.sub(r"[^a-z0-9-]+", "-", str(s).lower())
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "x"


def _page_shell(*, title, description, canonical, body, json_ld,
                breadcrumb, interval, base_url, og_type="website"):
    """Wrap body in full HTML5 shell with all SEO tags."""
    title_esc = _esc(title)
    desc_esc = _esc(description)
    canonical_esc = _esc(canonical)
    bc_parts = []
    for label, href in breadcrumb:
        if href:
            bc_parts.append(f'<a href="{_esc(href)}">{_esc(label)}</a>')
        else:
            bc_parts.append(f'<span>{_esc(label)}</span>')
    bc_html = " &#183; ".join(bc_parts)
    ld_json = json.dumps(json_ld, ensure_ascii=False, separators=(",", ":"))
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<meta name="robots" content="index, follow, max-image-preview:large">\n'
        f"<title>{title_esc}</title>\n"
        f'<meta name="description" content="{desc_esc}">\n'
        f'<link rel="canonical" href="{canonical_esc}">\n'
        f'<meta property="og:type" content="{_esc(og_type)}">\n'
        f'<meta property="og:title" content="{title_esc}">\n'
        f'<meta property="og:description" content="{desc_esc}">\n'
        f'<meta property="og:url" content="{canonical_esc}">\n'
        '<meta name="twitter:card" content="summary">\n'
        f'<meta name="twitter:title" content="{title_esc}">\n'
        f'<meta name="twitter:description" content="{desc_esc}">\n'
        f'<script type="application/ld+json">{ld_json}</script>\n'
        f"<style>{CSS}</style>\n"
        "</head>\n"
        "<body>\n"
        '<div class="wrap">\n'
        f'<nav class="bc">{bc_html}</nav>\n'
        f"{body}\n"
        "<footer>\n"
        f"Auto-updated every {interval} minutes via GitHub Actions &#183; "
        f'<a href="{_esc(base_url)}/">tracker root</a> &#183; '
        f'<a href="{_esc(base_url)}/sitemap.xml">sitemap</a>\n'
        "</footer>\n"
        "</div>\n"
        "</body>\n"
        "</html>\n"
    )


def _items_table_html(items):
    if not items:
        return "<p>No items match this filter yet.</p>"
    parts = ['<table><thead><tr><th>#</th><th>Name</th><th>&#9733;</th><th>Language</th><th>Updated</th><th>Description</th></tr></thead><tbody>']
    for i, it in enumerate(items, 1):
        name_full = it.get("name", "")
        owner, _, repo = name_full.partition("/")
        detail_href = f"r/{_esc(owner)}/{_esc(repo)}/"
        parts.append(
            "<tr>"
            f"<td>{i}</td>"
            f'<td><a href="{detail_href}">{_esc(name_full)}</a> '
            f'<small>(<a href="{_esc(it.get("url", ""))}" rel="external">source</a>)</small></td>'
            f'<td>{it.get("stars", 0)}</td>'
            f'<td>{_esc(it.get("language", "-"))}</td>'
            f'<td>{_esc(str(it.get("updated_at", ""))[:10])}</td>'
            f'<td>{_esc(str(it.get("description", ""))[:140])}</td>'
            "</tr>"
        )
    parts.append("</tbody></table>")
    return "\n".join(parts)


def _crosslinks(links):
    lis = "\n".join(f'<li><a href="{_esc(href)}">{_esc(label)}</a></li>' for label, href in links)
    return f'<ul class="crosslinks">\n{lis}\n</ul>'


def _render_filter_page(*, slug_path, page_title, h1, intro_para, items, meta, related):
    base = meta["base_url"]
    interval = meta["update_interval_minutes"]
    canonical = f"{base}/{slug_path}/" if slug_path else f"{base}/"
    description = (intro_para[:155] + "...") if len(intro_para) > 158 else intro_para
    body = (
        "<main>\n"
        f"<h1>{_esc(h1)}</h1>\n"
        f'<p class="lead">{_esc(intro_para)}</p>\n'
        f"<section><h2>Current entries &#183; {len(items)}</h2>\n"
        f"{_items_table_html(items)}</section>\n"
        "<section><h2>Related views</h2>\n"
        f"{_crosslinks(related)}</section>\n"
        "</main>"
    )
    json_ld = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": page_title,
        "description": description,
        "url": canonical,
        "isPartOf": {"@type": "WebSite", "name": meta["title"], "url": f"{base}/"},
        "mainEntity": {"@type": "ItemList", "numberOfItems": len(items)},
    }
    breadcrumb = [(meta["title"], f"{base}/"), (h1, None)]
    return _page_shell(
        title=page_title, description=description, canonical=canonical,
        body=body, json_ld=json_ld, breadcrumb=breadcrumb,
        interval=interval, base_url=base,
    )


def _render_detail_page(*, item, all_items, meta):
    base = meta["base_url"]
    interval = meta["update_interval_minutes"]
    name = item.get("name", "")
    owner, _, repo = name.partition("/")
    canonical = f"{base}/r/{owner}/{repo}/"
    desc_src = str(item.get("description", "")).strip() or f"{name} - entry on {meta['title']}"
    description = desc_src[:155] + ("..." if len(desc_src) > 158 else "")
    page_title = f"{name} - entry on {meta['title']}"
    lang = item.get("language", "-")
    stars = item.get("stars", 0)
    updated = str(item.get("updated_at", ""))[:10]
    src_url = item.get("url", f"https://github.com/{name}")

    same_lang = [x for x in all_items if x.get("language") == lang and x.get("name") != name]
    same_lang.sort(key=lambda x: x.get("stars", 0), reverse=True)
    related_links = [
        (f"{x['name']} (stars:{x.get('stars', 0)})", f"{base}/r/{x['name']}/")
        for x in same_lang[:3]
    ]
    if not related_links:
        sorted_items = sorted(all_items, key=lambda x: x.get("stars", 0), reverse=True)
        related_links = [
            (f"{x['name']} (stars:{x.get('stars', 0)})", f"{base}/r/{x['name']}/")
            for x in sorted_items if x.get("name") != name
        ][:3]

    why_listed = (
        f"This repository appears on {meta['title']} because it matches the tracker's "
        f"GitHub Search criteria ({_esc(meta.get('topic', 'live'))}) and was active in the "
        f"recent indexing window. The tracker refreshes every {interval} minutes, so the "
        f"metadata above reflects the state at the most recent index pass. If the data here "
        f"looks stale, the source repository may have been archived or moved out of the "
        f"tracked topic; the next cron tick will reconcile."
    )

    explore_links = [
        ("Popular (by stars)", f"{base}/popular/"),
        ("Recent (by activity)", f"{base}/recent/"),
        ("New this week", f"{base}/new/"),
    ]
    if lang and lang != "-":
        explore_links.append((f"All {lang} entries", f"{base}/lang/{_slug(lang)}/"))

    # Actionable content: install command + Claude Desktop config snippet
    # (extracted by tracker.py from source repo README)
    rules_section = ""
    install = item.get("install_info") or {}
    if install.get("install_cmd") or install.get("claude_config"):
        parts = ['<section id="install"><h2>Install &amp; configure</h2>\n']
        if install.get("install_cmd"):
            kind = _esc(install.get("install_kind", "install"))
            cmd = _esc(install["install_cmd"])
            parts.append(
                f'<p>Install method detected from README: <code>{kind}</code></p>\n'
                f'<pre style="background:var(--card);padding:14px;border-radius:6px;overflow:auto;'
                f'font-size:13px;border:1px solid var(--border);"><code>{cmd}</code></pre>\n'
            )
        if install.get("claude_config"):
            cfg = _esc(install["claude_config"])
            parts.append(
                '<h3>Claude Desktop config snippet</h3>\n'
                '<p>Add to your <code>claude_desktop_config.json</code> '
                '(<code>~/Library/Application Support/Claude/claude_desktop_config.json</code> on macOS, '
                '<code>%APPDATA%\\Claude\\claude_desktop_config.json</code> on Windows):</p>\n'
                f'<pre style="background:var(--card);padding:14px;border-radius:6px;overflow:auto;max-height:500px;'
                f'font-size:13px;line-height:1.5;border:1px solid var(--border);"><code>{cfg}</code></pre>\n'
            )
        parts.append(
            f'<p><a href="{_esc(src_url)}#readme" rel="external">View full README on GitHub</a></p>\n'
            "</section>\n"
        )
        rules_section = "".join(parts)

    body = (
        "<main>\n"
        f"<h1>{_esc(name)}</h1>\n"
        f'<p class="lead">{_esc(desc_src)}</p>\n'
        '<div class="meta">\n'
        f"<span><strong>Stars</strong> {stars}</span>\n"
        f"<span><strong>Language</strong> {_esc(lang)}</span>\n"
        f"<span><strong>Last updated</strong> {_esc(updated)}</span>\n"
        f'<span><a href="{_esc(src_url)}" rel="external">Source on GitHub</a></span>\n'
        f'<span><a href="https://github.com/{_esc(owner)}" rel="external">@{_esc(owner)}</a></span>\n'
        "</div>\n"
        f"{rules_section}"
        "<section><h2>Why this is listed</h2>\n"
        f"<p>{why_listed}</p></section>\n"
        "<section><h2>Similar in this tracker</h2>\n"
        f"{_crosslinks(related_links) if related_links else '<p>No similar entries yet.</p>'}</section>\n"
        "<section><h2>Explore by category</h2>\n"
        f"{_crosslinks(explore_links)}</section>\n"
        "</main>"
    )

    json_ld = {
        "@context": "https://schema.org",
        "@type": "SoftwareSourceCode",
        "name": name,
        "codeRepository": src_url,
        "programmingLanguage": lang,
        "url": canonical,
        "description": desc_src,
        "author": {"@type": "Person", "name": owner, "url": f"https://github.com/{owner}"},
        "dateModified": updated,
    }
    breadcrumb = [
        (meta["title"], f"{base}/"),
        ("Entries", f"{base}/popular/"),
        (name, None),
    ]
    return _page_shell(
        title=page_title, description=description, canonical=canonical,
        body=body, json_ld=json_ld, breadcrumb=breadcrumb, og_type="article",
        interval=interval, base_url=base,
    )


def _render_sitemap(urls, lastmod_iso):
    entries = "\n".join(
        f"  <url><loc>{_esc(u)}</loc><lastmod>{lastmod_iso}</lastmod></url>"
        for u in urls
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n"
        "</urlset>\n"
    )


def generate_pages(items, meta):
    """Write all pSEO pages to disk relative to current dir.

    Returns count of files written.
    """
    written = 0
    urls = []
    base = meta["base_url"]
    interval = meta["update_interval_minutes"]
    lastmod = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    urls.append(f"{base}/")

    sorted_by_stars = sorted(items, key=lambda x: x.get("stars", 0), reverse=True)[:20]
    Path("popular").mkdir(parents=True, exist_ok=True)
    Path("popular/index.html").write_text(_render_filter_page(
        slug_path="popular",
        page_title=f"Popular entries - {meta['title']}",
        h1=f"Most-starred entries on {meta['title']}",
        intro_para=(
            f"The top {len(sorted_by_stars)} entries on {meta['title']} ranked by GitHub star count "
            f"at the most recent indexing pass. {meta['title']} tracks {meta.get('niche_label', 'this niche')} "
            f"every {interval} minutes, so this leaderboard reflects current momentum rather than "
            f"historical popularity. Each entry is a real GitHub repository - click through for the "
            f"detail page or open the source on GitHub directly."
        ),
        items=sorted_by_stars,
        meta=meta,
        related=[
            ("Recent activity", f"{base}/recent/"),
            ("New this week", f"{base}/new/"),
            ("Tracker root", f"{base}/"),
        ],
    ))
    urls.append(f"{base}/popular/")
    written += 1

    sorted_by_recent = sorted(items, key=lambda x: str(x.get("updated_at", "")), reverse=True)[:20]
    Path("recent").mkdir(parents=True, exist_ok=True)
    Path("recent/index.html").write_text(_render_filter_page(
        slug_path="recent",
        page_title=f"Recent activity - {meta['title']}",
        h1=f"Recently active entries on {meta['title']}",
        intro_para=(
            f"The top {len(sorted_by_recent)} entries on {meta['title']} ranked by most recent commit. "
            f"Whatever is actively being worked on right now appears here. The tracker refreshes every "
            f"{interval} minutes so this list stays fresh - repos that haven't received commits recently "
            f"rotate out. Use this view when you want to see what's still being developed, not just what "
            f"was popular months ago."
        ),
        items=sorted_by_recent,
        meta=meta,
        related=[
            ("Popular", f"{base}/popular/"),
            ("New this week", f"{base}/new/"),
            ("Tracker root", f"{base}/"),
        ],
    ))
    urls.append(f"{base}/recent/")
    written += 1

    week_ago = (datetime.now(timezone.utc) - _dt.timedelta(days=7)).strftime("%Y-%m-%d")
    new_items = [x for x in items if str(x.get("updated_at", ""))[:10] >= week_ago][:20]
    Path("new").mkdir(parents=True, exist_ok=True)
    Path("new/index.html").write_text(_render_filter_page(
        slug_path="new",
        page_title=f"New this week - {meta['title']}",
        h1=f"New entries this week on {meta['title']}",
        intro_para=(
            f"Entries on {meta['title']} that have been committed to in the last 7 days. This is the "
            f"newest cohort - projects with at least one commit since {week_ago}. The page rebuilds "
            f"every {interval} minutes, so what shows here reflects very recent GitHub activity. If you "
            f"want a leaderboard view, see Popular; if you want everything sorted by activity, see Recent."
        ),
        items=new_items,
        meta=meta,
        related=[
            ("Popular", f"{base}/popular/"),
            ("Recent", f"{base}/recent/"),
            ("Tracker root", f"{base}/"),
        ],
    ))
    urls.append(f"{base}/new/")
    written += 1

    lang_counter = Counter(x.get("language", "-") for x in items)
    for lang, count in lang_counter.most_common():
        if count < 3 or not lang or lang == "-":
            continue
        slug = _slug(lang)
        lang_items = sorted(
            [x for x in items if x.get("language") == lang],
            key=lambda x: x.get("stars", 0), reverse=True,
        )[:30]
        Path(f"lang/{slug}").mkdir(parents=True, exist_ok=True)
        Path(f"lang/{slug}/index.html").write_text(_render_filter_page(
            slug_path=f"lang/{slug}",
            page_title=f"{lang} entries on {meta['title']}",
            h1=f"{lang} entries on {meta['title']}",
            intro_para=(
                f"{count} {lang} repositories tracked on {meta['title']}, sorted by star count. "
                f"This page lists every {lang} entry the tracker has indexed in its current pass; the "
                f"full set rebuilds every {interval} minutes. Useful when you want to filter the "
                f"tracker's data down to a single language ecosystem - particularly if you're evaluating "
                f"tools or libraries within a specific stack."
            ),
            items=lang_items,
            meta=meta,
            related=[
                ("All languages", f"{base}/popular/"),
                ("Recent activity", f"{base}/recent/"),
                ("Tracker root", f"{base}/"),
            ],
        ))
        urls.append(f"{base}/lang/{slug}/")
        written += 1

    for item in items:
        name = item.get("name", "")
        if "/" not in name:
            continue
        owner, repo = name.split("/", 1)
        Path(f"r/{owner}/{repo}").mkdir(parents=True, exist_ok=True)
        Path(f"r/{owner}/{repo}/index.html").write_text(_render_detail_page(
            item=item, all_items=items, meta=meta,
        ))
        urls.append(f"{base}/r/{owner}/{repo}/")
        written += 1

    Path("sitemap.xml").write_text(_render_sitemap(urls, lastmod))
    written += 1

    return written
