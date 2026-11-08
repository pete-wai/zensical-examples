---
title: Formatting
---

# Formatting


Use emphasis sparingly, and reserve highlighting for text a reader should notice.

The **release owner** reviews the *draft* before publication. ==Confirm the version==, ~~remove the old link~~, and ^^add the migration note^^.

Water is H~2~O; the area is 12 m^2^. Press ++ctrl+shift+p++ to open the command palette.

??? abstract "Show Markdown source"

    ``````markdown
    The **release owner** reviews the *draft* before publication. ==Confirm the version==, ~~remove the old link~~, and ^^add the migration note^^.
    
    Water is H~2~O; the area is 12 m^2^. Press ++ctrl+shift+p++ to open the command palette.
    ``````


## Inline edits and scientific notation

Subscripts, superscripts, and inserted text can make small changes legible.

The revised threshold is ^^25 ms^^; the old value was ~~50 ms~~.

Carbon dioxide is CO~2~. A square has area A = s^2^.

??? abstract "Show Markdown source"

    ``````markdown
    The revised threshold is ^^25 ms^^; the old value was ~~50 ms~~.
    
    Carbon dioxide is CO~2~. A square has area A = s^2^.
    ``````

## References

- [Formatting](https://zensical.org/docs/authoring/formatting/)
- [Lists](https://zensical.org/docs/authoring/lists/)
- [Data tables](https://zensical.org/docs/authoring/data-tables/)
- [Footnotes](https://zensical.org/docs/authoring/footnotes/)
- [Tooltips](https://zensical.org/docs/authoring/tooltips/)
- [Buttons](https://zensical.org/docs/authoring/buttons/)

## Smart symbols

SmartSymbols converts familiar character sequences to typographic symbols in prose. For example, (c) Example Documentation and (tm) Example Guide render copyright and trademark symbols; 1/2 and 3/4 become fractions.

??? abstract "Show Markdown source"

    ```markdown
    (c) Example Documentation and (tm) Example Guide
    1/2 and 3/4
    ```

The [SmartSymbols guide](https://facelessuser.github.io/pymdown-extensions/extensions/smartsymbols/) lists the supported substitutions.
