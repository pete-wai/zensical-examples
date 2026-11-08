# privacy

Self-host external assets and annotate external links. Native support was added in Zensical **0.0.72**.

Reduce third-party requests for fonts or images; add attributes to outbound links.

## Try it

[Open the privacy example](/zensical-examples/variants/privacy/).

### External link

Inspect the external link’s HTML: the configured target opens a new tab.

### Safe relationship

A second outbound link receives the same target and `rel="noopener"` attributes.

## Self-hosted asset

The source page references a Python logo at a commit-pinned GitHub URL. The plugin downloads it and rewrites the image to a local URL during the build:

![Downloaded Python logo](/zensical-examples/variants/privacy/assets/external/raw.githubusercontent.com/simple-icons/simple-icons/1bb2f6e6ea50f920de8d2f3d273ae48564a5eaee/icons/python.svg)

[Open the self-hosted SVG](/zensical-examples/variants/privacy/assets/external/raw.githubusercontent.com/simple-icons/simple-icons/1bb2f6e6ea50f920de8d2f3d273ae48564a5eaee/icons/python.svg). The build needs network access on the first fetch; `assets_include` limits this example to that source.

??? example "Source and configuration"

    The [configuration](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/privacy/zensical.toml) and [example Markdown](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/privacy/docs/index.md) are available in the repository. Other files in that directory supply the example’s fixtures.

[Zensical compatibility and settings](https://zensical.org/docs/compatibility/mkdocs/plugins/#privacy) · [Plugin documentation](https://squidfunk.github.io/mkdocs-material/plugins/privacy/)
