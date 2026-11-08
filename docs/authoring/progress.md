---
title: Progress indicators
---

# Progress indicators

HTML progress elements provide a native way to show the completion of a known task. These values are examples, not live build data.

## Review progress

<label for="review-progress">Review checklist: 3 of 5 complete</label>
<progress id="review-progress" value="3" max="5">3 of 5</progress>

??? abstract "Show Markdown source"

    ```html
    <label for="review-progress">Review checklist: 3 of 5 complete</label>
    <progress id="review-progress" value="3" max="5">3 of 5</progress>
    ```

## Import progress

<label for="import-progress">Imported: 75 of 100 records</label>
<progress id="import-progress" value="75" max="100">75 of 100</progress>

??? abstract "Show Markdown source"

    ```html
    <label for="import-progress">Imported: 75 of 100 records</label>
    <progress id="import-progress" value="75" max="100">75 of 100</progress>
    ```

These use standard HTML rather than an extension-specific progress-bar syntax. See [Zensical's Markdown guide](https://zensical.org/docs/authoring/markdown/) and the [HTML progress element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress).
