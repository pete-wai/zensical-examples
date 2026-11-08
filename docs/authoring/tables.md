---
title: Tables and footnotes
---

# Tables and footnotes


Tables compare a few dimensions; a footnote keeps a qualification near the claim without interrupting it.

| Environment | Purpose | Retention |
| :--- | :--- | ---: |
| Development | Try changes | 7 days |
| Staging | Rehearse a release | 30 days |
| Production | Serve readers | 90 days |

The staging environment uses representative data.[^staging] The review window is two days.[^window]

[^staging]: Representative data is synthetic and contains no customer records.
[^window]: The window begins after the build passes.

??? abstract "Show Markdown source"

    ``````markdown
    | Environment | Purpose | Retention |
    | :--- | :--- | ---: |
    | Development | Try changes | 7 days |
    | Staging | Rehearse a release | 30 days |
    | Production | Serve readers | 90 days |
    
    The staging environment uses representative data.[^staging] The review window is two days.[^window]
    
    [^staging]: Representative data is synthetic and contains no customer records.
    [^window]: The window begins after the build passes.
    ``````


## Alignment and compact comparisons

Use centered and right-aligned columns where they help readers scan values. Sorting requires an additional JavaScript library; this table is static.

| Check | Status | Minutes |
| :--- | :---: | ---: |
| Links | Pass | 2 |
| Examples | Review | 15 |
| Layout | Pass | 5 |

??? abstract "Show Markdown source"

    ``````markdown
    | Check | Status | Minutes |
    | :--- | :---: | ---: |
    | Links | Pass | 2 |
    | Examples | Review | 15 |
    | Layout | Pass | 5 |
    ``````

## Longer footnote

Footnotes can contain multiple paragraphs and are collected at the bottom of the page.

The estimate excludes review time.[^estimate]

[^estimate]: The estimate covers the build itself.

    Review time depends on the number of changes and the availability of reviewers.

??? abstract "Show Markdown source"

    ``````markdown
    The estimate excludes review time.[^estimate]
    
    [^estimate]: The estimate covers the build itself.
    
        Review time depends on the number of changes and the availability of reviewers.
    ``````

## References

- [Formatting](https://zensical.org/docs/authoring/formatting/)
- [Lists](https://zensical.org/docs/authoring/lists/)
- [Data tables](https://zensical.org/docs/authoring/data-tables/)
- [Footnotes](https://zensical.org/docs/authoring/footnotes/)
- [Tooltips](https://zensical.org/docs/authoring/tooltips/)
- [Buttons](https://zensical.org/docs/authoring/buttons/)

## Caption a table

The Caption extension can describe a table as well as an image.

| Stage | Owner |
| --- | --- |
| Draft | Author |
| Review | Reviewer |

/// caption
A small review handoff.
///

??? abstract "Show Markdown source"

    ```markdown
    | Stage | Owner |
    | --- | --- |
    | Draft | Author |
    | Review | Reviewer |

    /// caption
    A small review handoff.
    ///
    ```
