# exclude

Omit matching source files from the built site. Native support was added in Zensical **0.0.67**.

Keep working drafts out of a published guide; leave source-only notes beside public pages.

## Try it

[Open the exclude example](/zensical-examples/variants/exclude/).

### Excluded draft

The source contains `drafts/private.md`, but the built site does not publish it.

### Public page

Open Public notes to confirm that unmatched files remain available.

??? example "Source and configuration"

    The [configuration](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/exclude/zensical.toml) and [example Markdown](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/exclude/docs/index.md) are available in the repository. Other files in that directory supply the example’s fixtures.

[Zensical compatibility and settings](https://zensical.org/docs/compatibility/mkdocs/plugins/#exclude) · [Plugin documentation](https://github.com/apenwarr/mkdocs-exclude)
