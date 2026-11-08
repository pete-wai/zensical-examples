---
title: Code highlighting
---

# Code highlighting


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


## Shell example

A second language demonstrates that the highlighter follows the selected lexer.

```sh title="inspect.sh" linenums="1"
printf 'Current directory: '
pwd
```

??? abstract "Show Markdown source"

    ``````markdown
    ```sh title="inspect.sh" linenums="1"
    printf 'Current directory: '
    pwd
    ```
    ``````

## References

- [Code blocks](https://zensical.org/docs/authoring/code-blocks/)
- [Directives](https://zensical.org/docs/authoring/directives/)
- [Markdown extension compatibility](https://zensical.org/docs/compatibility/markdown/python-markdown-extensions/)
