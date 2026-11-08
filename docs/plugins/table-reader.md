# table-reader

Read data files and render them as Markdown tables. Native support was added in Zensical **0.0.41**.

Publish a CSV inventory; keep a comparison table in a data file maintained by another process.

## Try it

[Open the table-reader example](/zensical-examples/variants/table-reader/).

### CSV table

The table is rendered from `gear.csv`, rather than typed into Markdown.

### Multiple rows

The second table reads a separate weather CSV, with Monday and Tuesday rows.

??? example "Source and configuration"

    The [configuration](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/table-reader/zensical.toml) and [example Markdown](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/table-reader/docs/index.md) are available in the repository. Other files in that directory supply the example’s fixtures.

[Zensical compatibility and settings](https://zensical.org/docs/compatibility/mkdocs/plugins/#table-reader) · [Plugin documentation](https://timvink.github.io/mkdocs-table-reader-plugin/)
