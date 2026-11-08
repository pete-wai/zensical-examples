---
title: Code, snippets, and directives
description: Practical, rendered examples of code, snippets, and directives.
---

# Code, snippets, and directives

Examples should be small enough to understand and complete enough to try.

## Highlighted code

A title identifies the file, line numbers support discussion, and a highlight directs attention.

```python title="greeting.py" linenums="1" hl_lines="2"
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("reader"))
```

Inline highlighting works too: `#!python greet("reader")`.

??? abstract "Show Markdown source"

    ``````markdown
    ```python title="greeting.py" linenums="1" hl_lines="2"
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    
    print(greet("reader"))
    ```
    
    Inline highlighting works too: `#!python greet("reader")`.
    ``````

## Annotations

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

## Reusable fixed text

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

## References

- [Code blocks](https://zensical.org/docs/authoring/code-blocks/)
- [Directives](https://zensical.org/docs/authoring/directives/)
- [Markdown extension compatibility](https://zensical.org/docs/compatibility/markdown/python-markdown-extensions/)

## Conditional directives

The official directives extension is distributed separately through Zensical Spark. It uses a catalog and a selected variant; it is not enabled in this example site. The following is illustrative source, not a live demo.

```text
@if deployment = cloud

    Open the cloud console.

@else

    Configure the local service.

This guide covers @var{deployment}.

@use shared/security-notice.md
```

See the [directives guide](https://zensical.org/docs/authoring/directives/) for installation, catalog configuration, conditions, variables, and source reuse.
