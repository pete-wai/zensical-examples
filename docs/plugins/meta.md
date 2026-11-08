# meta

Apply shared front matter to a directory and its descendants. Native support was added in Zensical **0.0.58**.

Share a tag across a group of guides; provide a default description for related pages.

## Try it

[Open the meta example](/zensical-examples/variants/meta/).

### Inherited description

Inspect the guide page’s HTML meta description; it comes from `.meta.yml`.

### Nested page

A second page in the same directory inherits the same description.

??? example "Source and configuration"

    The [configuration](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/meta/zensical.toml) and [example Markdown](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/meta/docs/index.md) are available in the repository. Other files in that directory supply the example’s fixtures.

[Zensical compatibility and settings](https://zensical.org/docs/compatibility/mkdocs/plugins/#meta) · [Plugin documentation](https://squidfunk.github.io/mkdocs-material/plugins/meta/)
