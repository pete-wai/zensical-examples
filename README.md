# Zensical Examples

A showcase for Zensical 0.1.0 and its UI 0.0.41, with authoring examples, isolated plugin and UI variants, and release notes. The [capability inventory](docs/coverage.md) records examples and known gaps; a source file's presence alone does not prove that every feature works.

The project pins Python 3.13.15 with uv and uv 0.12.19 with mise. Install the pinned uv version with `mise install` and ensure `uv --version` reports 0.12.19. From the repository root, run:

```sh
uv run --locked python scripts/build.py
uv run --locked python scripts/check.py
uv run --locked python scripts/check_fixtures.py
uv run --locked python scripts/coverage.py
```

The build discovers each `variants/**/zensical.toml`, runs it from that variant's directory, and combines the outputs under `site/variants/<slug>`. The coverage command validates its source paths and release inventory, then regenerates `docs/coverage.md` from `data/coverage.json`. Run it before the build when the inventory changes so the generated page is included in the output. See [AGENTS.md](AGENTS.md) for maintenance and verification guidance.
