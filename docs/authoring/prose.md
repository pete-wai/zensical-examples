---
title: Prose and structure
description: Practical, rendered examples of prose and structure.
---

# Prose and structure

Use ordinary Markdown for the narrative, then add extensions where they make a relationship easier to read.

## Formatting and keyboard input

Use emphasis sparingly, and reserve highlighting for text a reader should notice.

The **release owner** reviews the *draft* before publication. ==Confirm the version==, ~~remove the old link~~, and ^^add the migration note^^.

Water is H~2~O; the area is 12 m^2^. Press ++ctrl+shift+p++ to open the command palette.

??? abstract "Show Markdown source"

    ``````markdown
    The **release owner** reviews the *draft* before publication. ==Confirm the version==, ~~remove the old link~~, and ^^add the migration note^^.
    
    Water is H~2~O; the area is 12 m^2^. Press ++ctrl+shift+p++ to open the command palette.
    ``````

## Lists and definitions

Indent continuation paragraphs and nested blocks by four spaces.

1. Prepare the release notes.
2. Review the changes.

    Ask a second reviewer to check the migration steps.

3. Publish the documentation.

- [x] Verify the examples
- [x] Check internal links
- [ ] Announce the release

Artifact
:   A file produced by a build, such as a package or report.

Release candidate
:   A proposed release awaiting final checks.

??? abstract "Show Markdown source"

    ``````markdown
    1. Prepare the release notes.
    2. Review the changes.
    
        Ask a second reviewer to check the migration steps.
    
    3. Publish the documentation.
    
    - [x] Verify the examples
    - [x] Check internal links
    - [ ] Announce the release
    
    Artifact
    :   A file produced by a build, such as a package or report.
    
    Release candidate
    :   A proposed release awaiting final checks.
    ``````

## Tables and footnotes

Tables compare a few dimensions; a footnote keeps a qualification near the claim without interrupting it.

| Environment | Purpose | Retention |
| :--- | :--- | ---: |
| Development | Try changes | 7 days |
| Staging | Rehearse a release | 30 days |
| Production | Serve readers | 90 days |

The staging environment uses representative data.[^staging] The review window is two days.[^window]

[^staging]: Representative data is synthetic and contains no customer records.
[^window]: The window begins after the build passes.

??? abstract "Show Markdown source"

    ``````markdown
    | Environment | Purpose | Retention |
    | :--- | :--- | ---: |
    | Development | Try changes | 7 days |
    | Staging | Rehearse a release | 30 days |
    | Production | Serve readers | 90 days |
    
    The staging environment uses representative data.[^staging] The review window is two days.[^window]
    
    [^staging]: Representative data is synthetic and contains no customer records.
    [^window]: The window begins after the build passes.
    ``````

## Tooltips and links

Hover or focus a link for its title; abbreviations expand on hover.

The API returns a response after the request is validated. See the [authoring guide](https://zensical.org/docs/authoring/markdown/ "Read about Zensical Markdown") for the underlying syntax.

The SLA describes the service target; the API describes how clients interact with it.

*[API]: Application programming interface
*[SLA]: Service-level agreement

??? abstract "Show Markdown source"

    ``````markdown
    The API returns a response after the request is validated. See the [authoring guide](https://zensical.org/docs/authoring/markdown/ "Read about Zensical Markdown") for the underlying syntax.
    
    The SLA describes the service target; the API describes how clients interact with it.
    
    *[API]: Application programming interface
    *[SLA]: Service-level agreement
    ``````

## Buttons

Buttons are links styled for a clear next action. Their destinations here are real pages.

[Explore callouts](callouts.md){ .md-button .md-button--primary }
[See visual examples](visuals.md){ .md-button }

??? abstract "Show Markdown source"

    ``````markdown
    [Explore callouts](callouts.md){ .md-button .md-button--primary }
    [See visual examples](visuals.md){ .md-button }
    ``````

## References

- [Formatting](https://zensical.org/docs/authoring/formatting/)
- [Lists](https://zensical.org/docs/authoring/lists/)
- [Data tables](https://zensical.org/docs/authoring/data-tables/)
- [Footnotes](https://zensical.org/docs/authoring/footnotes/)
- [Tooltips](https://zensical.org/docs/authoring/tooltips/)
- [Buttons](https://zensical.org/docs/authoring/buttons/)
