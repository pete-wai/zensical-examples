---
title: Snippets
---

# Snippets


The following source file is included at build time using the Snippets extension.

```text title="release-note.txt"
--8<-- "assets/authoring/release-note.txt"
```

??? abstract "Show Markdown source"

    ``````markdown
    ```text title="release-note.txt"
    ;--8<-- "assets/authoring/release-note.txt"
    ```
    ``````


## Source regions

Snippets may also select portions of a file; see the [Snippets extension documentation](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/) for line and named-section syntax. The example below shows a second fixed inclusion.

```text title="Release note, reused"
--8<-- "assets/authoring/release-note.txt"
```

??? abstract "Show Markdown source"

    ``````markdown
    ```text title="Release note, reused"
    ;--8<-- "assets/authoring/release-note.txt"
    ```
    ``````

## References

- [Code blocks](https://zensical.org/docs/authoring/code-blocks/)
- [Directives](https://zensical.org/docs/authoring/directives/)
- [Markdown extension compatibility](https://zensical.org/docs/compatibility/markdown/python-markdown-extensions/)
