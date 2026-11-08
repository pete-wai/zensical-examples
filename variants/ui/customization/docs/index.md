# CSS and template customization

The green header and narrower page width come from a local style sheet. The banner above is added by a custom template block override, so it appears throughout this variant. These are customizations layered on the built-in theme.

[Open the per-page template example](template.md) · [Return to the UI guide](/zensical-examples/ui/)

??? example "CSS and configuration source"

    ```toml
    [project]
    extra_css = ["assets/extra.css"]

    [project.theme]
    custom_dir = "overrides"
    ```

    ```css
    :root > * {
      --md-primary-fg-color: #315d51;
      --md-accent-fg-color: #a04f24;
    }
    .md-grid { max-width: 68rem; }
    ```

??? example "Template block override source"

    ```jinja
    {% extends "base.html" %}
    {% block content %}
      <div class="customization-banner">Custom block override: this banner is added to every page in this variant.</div>
      {{ super() }}
    {% endblock %}
    ```

The override calls `super()` to preserve the theme's original content. See [theme customization](https://zensical.org/docs/customization/).
