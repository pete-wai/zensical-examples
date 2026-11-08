---
title: Authoring field guide
description: Practical, rendered examples of authoring field guide.
---

# Authoring field guide

Explore the rendered examples first, then open **Show Markdown source** to copy the exact input. Examples use four spaces for nested blocks, as required by Python Markdown.

## Choose a pattern

Start with the content you need to explain.

<div class="grid cards" markdown>

- **[Prose and structure](prose.md)**

    Headings, lists, formatting, footnotes, tables, tooltips, and buttons.

- **[Callouts and tabs](callouts.md)**

    Notes, collapsible details, alternative paths, and cards.

- **[Code and reuse](code.md)**

    Highlighting, annotations, snippets, and the limits of directives.

- **[Visual explanations](visuals.md)**

    Diagrams, equations, images, icons, and emoji.

</div>

??? abstract "Show Markdown source"

    ``````markdown
    <div class="grid cards" markdown>
    
    - **[Prose and structure](prose.md)**
    
        Headings, lists, formatting, footnotes, tables, tooltips, and buttons.
    
    - **[Callouts and tabs](callouts.md)**
    
        Notes, collapsible details, alternative paths, and cards.
    
    - **[Code and reuse](code.md)**
    
        Highlighting, annotations, snippets, and the limits of directives.
    
    - **[Visual explanations](visuals.md)**
    
        Diagrams, equations, images, icons, and emoji.
    
    </div>
    ``````

## Focused examples

- [Front matter](front-matter.md), [formatting](formatting.md), [lists](lists.md), [tables](tables.md), [footnotes](footnotes.md), [tooltips](tooltips.md), and [buttons](buttons.md)
- [Admonitions](admonitions.md), [tabs](tabs.md), and [grids](grids.md)
- [Code highlighting](highlighting.md), [annotations](annotations.md), [snippets](snippets.md), and [directives](directives.md)
- [Diagrams](diagrams.md), [diagram models](models.md), [math](math.md), [images](images.md), and [icons](icons.md), and [progress indicators](progress.md)

## Page metadata

This page supplies a title and description in YAML front matter. The title appears in the page metadata and navigation context; the description is available to the site as page metadata.

??? abstract "Show Markdown source"

    ```yaml
    ---
    title: Authoring field guide
    description: Practical, rendered examples of authoring field guide.
    ---
    ```

## References

- [Front matter](https://zensical.org/docs/authoring/frontmatter/)

- [Authoring in Zensical](https://zensical.org/docs/authoring/markdown/)
- [Extension compatibility](https://zensical.org/docs/compatibility/markdown/python-markdown-extensions/)
