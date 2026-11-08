# autorefs

Resolve references to headings and API objects across pages. Native support was added in Zensical **0.0.22**.

Link to a glossary term from several guides; refer to an API object without hard-coding its URL.

## Try it

[Open the autorefs example](/zensical-examples/variants/autorefs/).

### Heading reference

Follow “packing checklist” to the heading on the same page.

### Cross-page reference

The [second reference](/zensical-examples/variants/autorefs/notes/) resolves the same heading from a different page.

??? example "Source and configuration"

    The [configuration](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/autorefs/zensical.toml) and [example Markdown](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/autorefs/docs/index.md) are available in the repository. Other files in that directory supply the example’s fixtures.

[Zensical compatibility and settings](https://zensical.org/docs/compatibility/mkdocs/plugins/#autorefs) · [Plugin documentation](https://mkdocstrings.github.io/autorefs/)
