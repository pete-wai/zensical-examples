# nav-weight

Order and hide navigation entries using page metadata. Native support was added in Zensical **0.0.69**.

Place an introduction before alphabetically earlier pages; hide a supporting page from navigation.

## Try it

[Open the nav-weight example](/zensical-examples/variants/nav-weight/).

### Weighted order

Zebra appears before Apple despite its alphabetical position.

### Different weights

Inspect their front matter: Zebra has weight −10 and Apple has weight 10.

??? example "Source and configuration"

    The [configuration](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/nav-weight/zensical.toml) and [example Markdown](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/nav-weight/docs/index.md) are available in the repository. Other files in that directory supply the example’s fixtures.

[Zensical compatibility and settings](https://zensical.org/docs/compatibility/mkdocs/plugins/#nav-weight) · [Plugin documentation](https://github.com/shu307/mkdocs-nav-weight)
