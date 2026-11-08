---
title: Admonitions
---

# Admonitions


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


## Types and title choices

Admonitions can communicate distinct levels of urgency and use a custom title.

!!! success "Checks passed"
    The documentation build is ready for review.

!!! danger "Destructive operation"
    Check the target before deleting a directory.

!!! quote "From the review"
    A short example made the change easier to understand.

??? abstract "Show Markdown source"

    ``````markdown
    !!! success "Checks passed"
        The documentation build is ready for review.
    
    !!! danger "Destructive operation"
        Check the target before deleting a directory.
    
    !!! quote "From the review"
        A short example made the change easier to understand.
    ``````

## References

- [Admonitions](https://zensical.org/docs/authoring/admonitions/)
- [Content tabs](https://zensical.org/docs/authoring/content-tabs/)
- [Grids](https://zensical.org/docs/authoring/grids/)
