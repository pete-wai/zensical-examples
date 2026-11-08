# MkDocs configuration fixture

This small site has equivalent `mkdocs.yml` and `equivalent.toml` configurations. `uv run --locked python scripts/check_fixtures.py` builds both with Zensical, verifies the expected content and navigation, and leaves their output under `fixtures/mkdocs-config/site-yaml/` and `fixtures/mkdocs-config/site-toml/`. It demonstrates these settings only; it is not proof that every MkDocs plugin or setting migrates unchanged.
