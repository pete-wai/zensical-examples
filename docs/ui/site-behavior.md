# Site behavior beyond appearance

Some settings change generated files or build behavior rather than add a widget. The right demonstration is the resulting output.

## Site identity and repository links

The title in this site's header is `Zensical Examples`. Its description appears in generated page metadata, and the repository link opens the source. Each authoring page has a view-source action. These are useful both for an internal handbook whose owner should be clear and an open project accepting corrections.

The [page actions variant](/zensical-examples/variants/content-actions/) adds edit and view actions together. The [header variant](/zensical-examples/variants/header/) demonstrates hiding the header while scrolling. Logo and icon selection change the same native header; [icons](../authoring/icons.md) shows the available icon families in content.

[Basics](https://zensical.org/docs/setup/basics/) · [Repository](https://zensical.org/docs/setup/repository/) · [Logo and icons](https://zensical.org/docs/setup/logo-and-icons/)

## Search visibility is different from navigation visibility

A page may be absent from the navigation yet remain searchable and accessible by URL. Draft/excluded pages are a different choice: production output can omit them altogether. Use hidden navigation for a supporting reference; use a draft for unfinished content.

Try the [search plugin demo](../plugins/search.md) for indexed and excluded content, and [exclude](../plugins/exclude.md) for files omitted from output. A hidden page is not an access-control mechanism.

## Preserve links when content moves

Try the [redirect demo](../plugins/redirects.md): follow an old page address and arrive at its replacement. Another useful case is keeping a short campaign URL while a guide's canonical location changes.

## Make generated output useful elsewhere

The [RSS demo](../plugins/rss.md) produces a subscription feed. [Social cards](../plugins/social.md) give shared links a recognizable image. [llmstxt](../plugins/llmstxt.md) exposes a Markdown index and page copies. Each example links to the actual generated artifact.

## Reduce downloads and support offline reading

[Privacy](../plugins/privacy.md) demonstrates downloaded assets served locally. [Optimize](../plugins/optimize.md) compares image bytes; [minify](../plugins/minify.md) compares generated markup. [Offline](../plugins/offline.md) supplies a downloadable site whose search can work from the filesystem.

## Catch mistakes before publication

Strict builds turn reported warnings into a failed build. This project also checks local links and generated artifacts across the assembled sites, because a main-site build alone cannot validate links into independent variants.

A broken page link is one failure worth stopping for. A missing required snippet is another: publishing an empty example would be worse than a build failure. Configuration examples for validation live in the [official validation guide](https://zensical.org/docs/setup/validation/).
