# Build workflow: what gets published

Compare [automatic navigation](/zensical-examples/variants/build-workflow/) with [explicit navigation](/zensical-examples/variants/build-workflow-explicit/). Both sites use the same four kinds of source page, but the second explicitly lists the otherwise hidden page.

| Source | Production output | Preview | Automatic navigation |
| --- | --- | --- | --- |
| `visible.md` | Included | Included | Included |
| `hidden.md` matched by `not_in_nav` | Included and searchable | Included | Omitted |
| `draft.md` matched by `draft_docs` | Omitted | Included | Omitted by default |
| `excluded.md` matched by `exclude_docs` | Omitted | Omitted | Omitted |

These are publishing controls, not access controls: the hidden page is still public. In the [explicit example](/zensical-examples/variants/build-workflow-explicit/), it appears in navigation because `nav` lists it explicitly.

The automatic site sets `use_directory_urls = false` and builds `hidden.html`. The explicit site sets it to `true` and builds `hidden/index.html`, linked as `hidden/`. Both enable link and anchor validation. In a local build of Zensical 0.1.0, both omitted `draft` and `excluded` from their production output; the hidden and visible pages were present, and only the explicit site's navigation listed the hidden page. Preview behavior follows the [upstream settings](https://zensical.org/docs/setup/basics/#draft_docs); the production build alone does not verify it.

## Validation failure

A separate broken-link fixture deliberately fails a strict build. It lives outside the discovered variants, so normal builds can succeed. Run `uv run --locked python scripts/check_fixtures.py` from the repository root to check that it fails for the expected missing-page warning. The same command builds a small project using both `mkdocs.yml` and `zensical.toml`, and checks its example content and navigation. This is a comparison of those settings, not a blanket claim about all MkDocs plugins.

[File selection and URL settings](https://zensical.org/docs/setup/basics/) · [Navigation](https://zensical.org/docs/setup/navigation/) · [Validation](https://zensical.org/docs/setup/validation/) · [MkDocs migration](https://zensical.org/docs/compatibility/mkdocs/migration/)
