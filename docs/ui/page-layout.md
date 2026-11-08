# Page-level layout

Some changes belong to an individual page. Zensical's front matter can hide interface elements without affecting neighboring pages. It does not provide arbitrary per-page replacements for the global theme configuration.

## Give a landing page room

[Open a page with both sidebars hidden](wide-page.md). Compare its reading width with this page. This is useful for a landing page or a wide comparison table.

??? example "Source"

    ```yaml
    ---
    hide:
      - navigation
      - toc
    ---
    ```

## Remove distractions from a focused page

[Open a page without a contents list or footer navigation](focused-page.md). The main navigation remains available so a reader can leave the page.

??? example "Source"

    ```yaml
    ---
    hide:
      - toc
      - footer
      - path
    ---
    ```

The other supported hide values include `feedback` and `tags`. They matter only when those components are enabled. See the [tags demo](../plugins/tags.md) and [external service explanation](external-services.md).

## Give a page a distinct identity

The [front matter examples](../authoring/front-matter.md) demonstrate a navigation title, description, icon, and status. The [meta plugin](../plugins/meta.md) shares these settings across a directory.

[Official front matter guide](https://zensical.org/docs/authoring/frontmatter/)
