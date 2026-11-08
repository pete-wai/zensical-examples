# social

Generate social preview cards and Open Graph metadata. Native support was added in Zensical **0.0.67**.

Give shared documentation pages a consistent preview; customize cards for a release announcement.

## Try it

[Open the social example](/zensical-examples/variants/social/).

### Preview card

Open the generated image to see the page’s social card.

### Open Graph metadata

Inspect the page source for the `og:image` link to that card.

## Generated card

![Generated social card](/zensical-examples/variants/social/assets/images/social/index.png)

[Open the PNG](/zensical-examples/variants/social/assets/images/social/index.png). Its URL also appears in the example page's Open Graph metadata.

??? example "Source and configuration"

    The [configuration](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/social/zensical.toml) and [example Markdown](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/social/docs/index.md) are available in the repository. Other files in that directory supply the example’s fixtures.

[Zensical compatibility and settings](https://zensical.org/docs/compatibility/mkdocs/plugins/#social) · [Plugin documentation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/)
