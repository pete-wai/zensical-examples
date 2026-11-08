---
title: Code annotations
---

# Code annotations


Select the numbered marker for an explanation alongside the code.

```toml title="settings.toml"
[build]
target = "site" # (1)!
```

1. The target names the output directory for this illustrative configuration.

??? abstract "Show Markdown source"

    ``````markdown
    ```toml title="settings.toml"
    [build]
    target = "site" # (1)!
    ```
    
    1. The target names the output directory for this illustrative configuration.
    ``````


## Multiple markers

Each marker corresponds to a list item immediately after the code fence.

```yaml
name: docs # (1)!
steps:
  - build # (2)!
```

1. Give the workflow a descriptive name.
2. Run the documentation build as a step.

??? abstract "Show Markdown source"

    ``````markdown
    ```yaml
    name: docs # (1)!
    steps:
      - build # (2)!
    ```
    
    1. Give the workflow a descriptive name.
    2. Run the documentation build as a step.
    ``````

## References

- [Code blocks](https://zensical.org/docs/authoring/code-blocks/)
- [Directives](https://zensical.org/docs/authoring/directives/)
- [Markdown extension compatibility](https://zensical.org/docs/compatibility/markdown/python-markdown-extensions/)
