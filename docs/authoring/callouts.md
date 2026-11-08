---
title: Callouts, tabs, and grids
description: Practical, rendered examples of callouts, tabs, and grids.
---

# Callouts, tabs, and grids

Use structure to separate a caveat, present alternatives, or give readers a choice of starting points.

## Callouts and details

A note is always visible. A details block can start closed or open.

!!! note "Before you begin"
    Create a clean working directory and record the version you are using.

!!! warning "Review the target"
    Confirm the destination before running a command that changes data.

??? tip "Why use a staging environment?"
    It gives reviewers a place to exercise the release before readers see it.

???+ example "An open detail"
    This detail starts expanded, but can be collapsed by the reader.

??? abstract "Show Markdown source"

    ``````markdown
    !!! note "Before you begin"
        Create a clean working directory and record the version you are using.
    
    !!! warning "Review the target"
        Confirm the destination before running a command that changes data.
    
    ??? tip "Why use a staging environment?"
        It gives reviewers a place to exercise the release before readers see it.
    
    ???+ example "An open detail"
        This detail starts expanded, but can be collapsed by the reader.
    ``````

## Alternative paths

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

## Cards and mixed content

Cards are useful for a small collection of equally important options.

<div class="grid cards" markdown>

- **Plan**

    ---

    Identify the audience and define the outcome.

- **Draft**

    ---

    Write a short example and explain its result.

- **Review**

    ---

    Test the example and check the links.

</div>

??? abstract "Show Markdown source"

    ``````markdown
    <div class="grid cards" markdown>
    
    - **Plan**
    
        ---
    
        Identify the audience and define the outcome.
    
    - **Draft**
    
        ---
    
        Write a short example and explain its result.
    
    - **Review**
    
        ---
    
        Test the example and check the links.
    
    </div>
    ``````

## References

- [Admonitions](https://zensical.org/docs/authoring/admonitions/)
- [Content tabs](https://zensical.org/docs/authoring/content-tabs/)
- [Grids](https://zensical.org/docs/authoring/grids/)
