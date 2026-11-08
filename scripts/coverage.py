#!/usr/bin/env python3
"""Validate the curated capability inventory and render its documentation."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "coverage.json"
OUTPUT = ROOT / "docs" / "coverage.md"
EXPECTED_PLUGINS = {
    "api-autonav", "audio", "autoapi", "autorefs", "awesome-nav", "blog",
    "callouts", "exclude", "gh-admonitions", "glightbox", "include-markdown",
    "literate-nav", "llmstxt", "macros", "markdown-exec", "markdownextradata",
    "meta", "mike", "minify", "mkdocstrings", "nav-weight", "offline",
    "optimize", "privacy", "redirects", "rss", "search", "section-index",
    "social", "table-reader", "tags", "video",
}


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    entries = data["entries"]
    seen: set[tuple[str, str]] = set()
    for entry in entries:
        key = entry["category"], entry["capability"]
        if key in seen:
            raise ValueError(f"Duplicate inventory entry: {key}")
        seen.add(key)
        if entry["status"] not in {"example", "gap", "unsupported"}:
            raise ValueError(f"Unknown status: {key}")
        if not entry["source_url"].startswith("https://"):
            raise ValueError(f"Missing source URL: {key}")
        path = entry["demo_path"]
        if path and not (ROOT / path).is_file():
            raise FileNotFoundError(f"Missing example for {key}: {path}")
        if entry["status"] == "example" and not path:
            raise ValueError(f"Example has no source path: {key}")
    actual = {e["capability"] for e in entries if e["category"] == "Plugin compatibility" and e["status"] != "unsupported"}
    if actual != EXPECTED_PLUGINS:
        raise ValueError(f"Supported plugin inventory differs: missing {sorted(EXPECTED_PLUGINS - actual)}; extra {sorted(actual - EXPECTED_PLUGINS)}")
    releases = json.loads((ROOT / "data/releases.json").read_text(encoding="utf-8"))
    expected_main = {f"0.0.{n}" for n in range(60, 75)} | {"0.1.0"}
    expected_ui = {f"0.0.{n}" for n in range(28, 42)}
    for key, expected in (("main", expected_main), ("ui", expected_ui)):
        found = {release["version"] for release in releases[key]}
        if found != expected or len(releases[key]) != len(expected):
            raise ValueError(f"Unexpected {key} release inventory")
        for release in releases[key]:
            if not (ROOT / release["page"]).is_file():
                raise FileNotFoundError(release["page"])
    for entry in releases["main"]:
        if entry["ui_version"] not in expected_ui:
            raise ValueError(f"Unknown UI release: {entry}")

    # Every UI release is explained once, alongside the first main release
    # that contains it; all former page URLs retain a destination anchor.
    changelog = (ROOT / "docs/changelog/index.md").read_text()
    included_ui = []
    positions = []
    for release in releases["main"]:
        marker = "{ #" + release["anchor"] + " }"
        if changelog.count(marker) != 1:
            raise ValueError(f"Missing or duplicate changelog section: {release['version']}")
        positions.append(changelog.index(marker))
        included_ui.extend(release["ui_changes"])
    if positions != sorted(positions, reverse=True):
        raise ValueError("Changelog must show newest main releases first")
    if len(included_ui) != len(expected_ui) or set(included_ui) != expected_ui:
        raise ValueError("Every UI release must be included exactly once")
    for kind in ("main", "ui"):
        for release in releases[kind]:
            if not (ROOT / release["evidence_path"]).is_file():
                raise FileNotFoundError(release["evidence_path"])
            if "{ #" + release["anchor"] + " }" not in changelog:
                raise ValueError(f"Missing destination for {release['legacy_path']}")
    if "/commit/" in changelog or "/issues/" in changelog:
        raise ValueError("Keep commit and issue references in the evidence archive")

    counts = Counter(e["status"] for e in entries)
    lines = [
        "# Capability inventory", "",
        "This inventory tracks the documentation families and plugin compatibility entries reviewed for this showcase. It does not claim exhaustive coverage of every option, combination, browser, or platform.", "",
        f"The local environment was checked with Zensical {data['observed_environment']['zensical']}, UI {data['observed_environment']['zensical_ui']}, Python {data['observed_environment']['python']}, and uv {data['observed_environment']['uv']}. These version checks do not verify the behavior of every example.", "",
        f"**{counts['example']} entries have example source; {counts['gap']} are gaps; {counts['unsupported']} are explicitly unsupported upstream.** An example status means only that its source path exists. A gap can include a source illustration that is not a working demonstration. Per-feature behavior is unverified unless an entry explicitly records a verified version.", "",
        "The official documentation changes over time. This snapshot was reviewed on 2026-11-08; compare its navigation and compatibility lists when updating it. A source path points to the repository, and may be a configuration file rather than a rendered page.", "",
    ]
    current = None
    for entry in entries:
        category = entry["category"]
        if category != current:
            current = category
            lines.extend([f"## {category}", "", "| Capability | Status | Example source | Details |", "| --- | --- | --- | --- |"])
        source = entry["demo_path"]
        if not source:
            path = "—"
        elif source.startswith("docs/"):
            path = f"[Open example]({source.removeprefix('docs/')})"
        elif source.startswith("variants/"):
            slug = Path(source).parent.name
            path = f"[Open demo](/zensical-examples/variants/{slug}/)"
        elif source.startswith("fixtures/"):
            path = "[Build workflow](ui/build-workflow.md)"
        else:
            path = "[Site behavior](ui/site-behavior.md)"
        version = entry.get("verified_version")
        note = entry["note"] + (f" Verified on Zensical {version}." if version else "")
        lines.append(f"| [{entry['capability']}]({entry['source_url']}) | {entry['status']} | {path} | {note} |")
    lines.append("")
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Validated {len(entries)} capability entries and {len(expected_main) + len(expected_ui)} releases; wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
