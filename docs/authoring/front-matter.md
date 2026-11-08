---
title: Front matter
status: new
icon: lucide/book-open
description: Page metadata examples for Zensical.
---

# Front matter

This page sets a title, description, navigation icon, and the `new` status. The status label is configured by the site. Front matter sits between `---` lines at the start of a Markdown file and is consumed as metadata.

??? abstract "Show this page's front matter"

    ```yaml
    ---
    title: Front matter
    status: new
    description: Page metadata examples for Zensical.
    ---
    ```

## Page-level presentation

A page can hide individual interface elements. The following is a source example: applying it to this page would hide its own navigation and table of contents.

```yaml
---
hide:
  - navigation
  - toc
---
```

## References

- [Front matter](https://zensical.org/docs/authoring/frontmatter/)
