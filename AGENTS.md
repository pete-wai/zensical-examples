# Maintaining this showcase

Keep the project on its explicitly pinned versions unless an upgrade is requested: Zensical 0.1.0, zensical-ui 0.0.41, Python 3.13.15, and uv 0.12.19. Use the project-local uv environment and lockfile; do not use the system Python. Install the pinned uv with mise and check version resolution before running work.

From the repository root:

```sh
uv run --locked python scripts/coverage.py
uv run --locked python scripts/build.py
uv run --locked python scripts/check.py
```

`coverage.py` validates the declared example paths and release counts and renders `docs/coverage.md` from `data/coverage.json`. Keep that data honest: `example` indicates source exists, not that all options work. Record a verified version only after checking the relevant behavior, and document partial coverage and gaps. The inventory is a snapshot of upstream documentation; review the authoring, setup, Markdown compatibility, and plugin compatibility navigation for changes.

The build discovers `variants/**/zensical.toml`, executes each build from its own directory, and combines the output under `site/variants/<slug>`. Preserve distinct configs and keep examples independent. For UI variants with shared content, update the generation inputs and regenerate the variants instead of hand-editing generated copies. Do not claim that a plugin or configuration setting is supported solely because a build completes: check the output or observable behavior relevant to the example.

## Release updates

When an update is requested, inspect the official [Zensical releases](https://github.com/zensical/zensical/releases) and [UI releases](https://github.com/zensical/ui/releases), including every release since the recorded versions. Read individual notes and, when needed, linked commits, issues, tests, and package metadata. Identify which UI release each main release uses; carry forward a prior version only with that inference labeled, and include UI-only releases. Update `data/releases.json` and the corresponding human-readable pages in `docs/changelog/`, with direct evidence links, impact, fixes, compatibility changes, and any uncertainty. Avoid copying upstream release text wholesale. Update pins only as part of an authorized upgrade, resolve the lockfile, regenerate the inventory, build and check, and inspect behavior affected by the upgrade. This is a manual process; no schedule is configured.

## Screenshots and visual verification

Run the local preview bound to `127.0.0.1` and use the available native browser/computer-use integration to inspect representative pages and capture screenshots when needed. Compare light/dark, narrow/wide, and affected interactive states as relevant; check examples after they finish rendering. Save approved reference images in the project only when the task calls for them, and describe the viewport and state. Do not automate screenshot updates by silently replacing baselines or publishing artifacts. No screenshot-refresh schedule is configured.

## Build fixtures and packaged output

`uv run --locked python scripts/check_fixtures.py` checks the expected strict-validation failure and compares the TOML and MkDocs YAML fixture output. It also inspects the previously built workflow variants, including omitted drafts and excluded pages. Run the main build first. The main build invokes the local `scripts/build_versions.py` workflow to deploy the mike example into a disposable local Git repository; it creates two sample editions and a `stable` alias without pushing a remote. The offline example is packaged as a ZIP in the assembled output. Check those generated artifacts after relevant changes.

## Verified initial release

- Zensical 0.1.0 and UI 0.0.41; 55 strict site builds (main plus 54 variants), plus two sample editions assembled by the actual mike fork.
- `scripts/check_plugins.py` verifies observable output for all 32 native plugin demos. `scripts/check_fixtures.py` verifies deliberate strict failure, equivalent YAML/TOML configuration, and draft/exclusion/navigation output. Run both in addition to the general link checker.
- Browser QA exercised content tabs/source disclosures, diagrams, math, annotations, lightbox, search and Botany filtering, media loading/playback, mobile navigation without horizontal overflow, and mike switching while preserving the current page.
- Offline ZIP contents and embedded search index are checked. The browser tool blocks `file://`, so actual filesystem search remains a manual verification step; do not claim it has been browser-tested.
- `data/screenshots.json` records capture URLs, dimensions, versions, and state. Images are real native browser screenshots. Refresh affected captures with the supported browser tool when configurations change.
- Plugin and UI variant slugs must be globally unique. The UI search variant is `search-ui`; `search` belongs to the plugin demonstration.
- The privacy fixture downloads a commit-pinned Simple Icons SVG. It requires network on its first build. The mike fork is pinned to a Git commit in pyproject.toml and uv.lock. Do not replace it with the unrelated PyPI mike package.
