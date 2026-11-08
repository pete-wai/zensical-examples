---
title: Content tabs
---

# Content tabs


Tabs keep equivalent instructions together. Each selection shows one path.

=== "macOS"

    Open Terminal and check the active shell:

    ```sh
    echo "$SHELL"
    ```

=== "Linux"

    Open a terminal and check the active shell:

    ```sh
    echo "$SHELL"
    ```

=== "Windows"

    Open PowerShell and check its version:

    ```powershell
    $PSVersionTable.PSVersion
    ```

??? abstract "Show Markdown source"

    ``````markdown
    === "macOS"
    
        Open Terminal and check the active shell:
    
        ```sh
        echo "$SHELL"
        ```
    
    === "Linux"
    
        Open a terminal and check the active shell:
    
        ```sh
        echo "$SHELL"
        ```
    
    === "Windows"
    
        Open PowerShell and check its version:
    
        ```powershell
        $PSVersionTable.PSVersion
        ```
    ``````


## Nested alternatives

Tabs can contain other tabs and can be nested inside an admonition. Tab labels also have shareable anchors.

!!! example "Choose an environment"
    === "Local"
        === "Inspect"
            Run `git status` to inspect your working tree.
        === "Review"
            Run `git diff` to review uncommitted changes.
    === "Remote"
        Open the repository in your browser to review its history.

??? abstract "Show Markdown source"

    ``````markdown
    !!! example "Choose an environment"
        === "Local"
            === "Inspect"
                Run `git status` to inspect your working tree.
            === "Review"
                Run `git diff` to review uncommitted changes.
        === "Remote"
            Open the repository in your browser to review its history.
    ``````

## References

- [Admonitions](https://zensical.org/docs/authoring/admonitions/)
- [Content tabs](https://zensical.org/docs/authoring/content-tabs/)
- [Grids](https://zensical.org/docs/authoring/grids/)
