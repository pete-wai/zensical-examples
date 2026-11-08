# mike: keep several editions online

A version selector lets readers use documentation that matches the software they actually have. Zensical's integration was added in **0.0.30** and uses the official compatible fork of mike.

## Compare two editions

[Open the versioned field guide](/zensical-examples/variants/mike/){ .md-button }

The selector offers **Field guide 1.0** and **Field guide 2.0**. Edition 2.0 adds equipment advice; switch to 1.0 to see the older text. These are fictional guide editions built with the same Zensical 0.1.0 runtime, not claims about historical Zensical behavior.

Keeping the older text accessible is useful when a product's newest instructions no longer apply to an earlier release.

## Keep the current page when switching

[Open field notes in edition 2.0](/zensical-examples/variants/mike/2.0/notes/), then switch to 1.0. The selector takes you to the matching field-notes page in the other edition. This is useful when comparing an API reference or migration procedure across versions.

## Give stable documentation a durable address

[The stable alias](/zensical-examples/variants/mike/stable/) redirects to edition 2.0. A product homepage can link to `stable` while archived release notes link to a numbered edition. [Version metadata](/zensical-examples/variants/mike/versions.json) lists the actual deployed editions and alias.

??? example "How this demo is built"

    The build runs the compatible mike fork in a temporary local Git repository. It creates two editions and a redirect alias, then assembles its actual deployment output into this site's Pages artifact. No second remote repository or hosting service is involved.

    ```sh
    mike deploy -F zensical.toml --alias-type redirect 1.0
    mike deploy -F zensical.toml --alias-type redirect 2.0 stable
    mike set-default -F zensical.toml stable
    ```

    [Exact build script](https://github.com/pete-wai/zensical-examples/blob/main/scripts/build_versions.py)

[Official versioning guide](https://zensical.org/docs/compatibility/mkdocs/mike/)
