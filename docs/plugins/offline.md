# Offline: read and search without a web server

A static site can be copied to a laptop, but browser restrictions make ordinary search indexes difficult to load from `file://` URLs. The offline implementation, supported since **0.0.3**, packages search for that setting.

## Read a field guide without a connection

[Download the offline demo](/zensical-examples/downloads/offline-demo.zip){ .md-button }

Unzip the archive and open `offline-demo/index.html` in your browser. Follow the local page links. The example uses local theme assets and system fonts, so reading does not depend on a font service.

This is useful for a field handbook in a place without connectivity or a documentation bundle supplied with a software release.

## Search the downloaded pages

Search for **kestrel** and follow the field-notes result. Then try **binoculars** for the equipment page. These queries distinguish working offline search from merely being able to open an HTML file.

[Open the same demo online](/zensical-examples/variants/offline/) for comparison. An online visit alone does not prove filesystem search works; use the downloaded copy for that test.

## What offline mode does not provide

It does not turn a remote video embed, analytics service, or external link into an offline resource. This fixture uses local content. Its return link to the main showcase needs a connection.

??? example "Source"

    ```toml
    [project.theme]
    font = false

    [project.plugins.offline]
    ```

    [All fixture pages](https://github.com/pete-wai/zensical-examples/tree/main/variants/plugins/offline/docs)

[Official offline guide](https://zensical.org/docs/setup/offline/)

!!! note "Verification note"

    The download and embedded index are checked by this project. Filesystem search still needs a manual browser check: the automated browser used for this showcase cannot open `file://` URLs.
