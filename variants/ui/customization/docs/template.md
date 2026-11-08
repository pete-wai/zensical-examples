---
template: example.html
---

# Per-page custom template

The orange note above appears only on this page. Its front matter selects a custom template, which extends the shared override; the green banner remains visible too.

??? example "Front matter and template source"

    ```yaml
    ---
    template: example.html
    ---
    ```

    ```jinja
    {% extends "main.html" %}
    {% block content %}
      <div class="custom-template-note">Custom per-page template: this note is added only to the template example.</div>
      {{ super() }}
    {% endblock %}
    ```

[Return to the UI guide](/zensical-examples/ui/)
