# Branding in the header

Look at the custom triangular logo in the header, the favicon in the browser tab, and the named repository link. The search and menu icons are configured from the bundled icon sets. On a narrow screen, open the menu to see its icon; scroll down to see the back-to-top control.

[Return to the UI guide](/zensical-examples/ui/)

??? example "Configuration source"

    ```toml
    [project]
    site_name = "Field guide branding"
    repo_url = "https://github.com/pete-wai/zensical-examples"
    repo_name = "Example repository"

    [project.theme]
    logo = "assets/mark.svg"
    favicon = "assets/mark.svg"
    features = ["navigation.top"]

    [project.theme.icon]
    repo = "fontawesome/brands/github"
    search = "lucide/search"
    menu = "lucide/menu"
    top = "lucide/arrow-up"
    ```

The logo and favicon both come from the local `docs/assets/mark.svg`. The logo links to the site homepage by default. [Official logo and icon guide](https://zensical.org/docs/setup/logo-and-icons/).
