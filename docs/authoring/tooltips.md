---
title: Tooltips and abbreviations
---

# Tooltips and abbreviations


Hover or focus a link for its title; abbreviations expand on hover.

The API returns a response after the request is validated. See the [authoring guide](https://zensical.org/docs/authoring/markdown/ "Read about Zensical Markdown") for the underlying syntax.

The SLA describes the service target; the API describes how clients interact with it.

*[API]: Application programming interface
*[SLA]: Service-level agreement

??? abstract "Show Markdown source"

    ``````markdown
    The API returns a response after the request is validated. See the [authoring guide](https://zensical.org/docs/authoring/markdown/ "Read about Zensical Markdown") for the underlying syntax.
    
    The SLA describes the service target; the API describes how clients interact with it.
    
    *[API]: Application programming interface
    *[SLA]: Service-level agreement
    ``````


## Reference links

A title on a reference-style link supplies a tooltip while keeping prose compact.

Read the [Markdown guide][markdown-guide] before choosing an extension.

[markdown-guide]: https://zensical.org/docs/authoring/markdown/ "Python Markdown in Zensical"

??? abstract "Show Markdown source"

    ``````markdown
    Read the [Markdown guide][markdown-guide] before choosing an extension.
    
    [markdown-guide]: https://zensical.org/docs/authoring/markdown/ "Python Markdown in Zensical"
    ``````

## Shared glossary

The CI pipeline builds the documentation, and CD delivers a reviewed build. These definitions come from one local file through the Snippets extension, so authors can reuse the same terms across pages.

--8<-- "assets/authoring/glossary.txt"

??? abstract "Show Markdown source"

    ```markdown
    The CI pipeline builds the documentation, and CD delivers a reviewed build.

    ;--8<-- "assets/authoring/glossary.txt"
    ```

    The included file contains:

    ```text
    *[CI]: Continuous integration
    *[CD]: Continuous delivery
    ```

## References

- [Formatting](https://zensical.org/docs/authoring/formatting/)
- [Lists](https://zensical.org/docs/authoring/lists/)
- [Data tables](https://zensical.org/docs/authoring/data-tables/)
- [Footnotes](https://zensical.org/docs/authoring/footnotes/)
- [Tooltips](https://zensical.org/docs/authoring/tooltips/)
- [Buttons](https://zensical.org/docs/authoring/buttons/)
