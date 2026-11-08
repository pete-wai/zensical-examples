# Footer controls

Scroll to the footer to see the next-page link, custom copyright text, and two named links. Follow **Next page** to see the previous-page link as well.

[Return to the UI guide](/zensical-examples/ui/)

??? example "Configuration source"

    ```toml
    [project]
    copyright = "Example field guide · Documentation demo"
    nav = [{"Overview"="index.md"}, {"Next page"="next.md"}]

    [project.theme]
    features = ["navigation.footer"]

    [project.theme.icon]
    previous = "fontawesome/solid/angle-left"
    next = "fontawesome/solid/angle-right"

    [[project.extra.social]]
    icon = "fontawesome/brands/github"
    link = "https://github.com/pete-wai/zensical-examples"
    name = "Example repository on GitHub"

    [[project.extra.social]]
    icon = "fontawesome/solid/book-open"
    link = "https://zensical.org/docs/"
    name = "Zensical documentation"
    ```

The `name` values give the icon links discernible labels. See the [footer guide](https://zensical.org/docs/setup/footer/).
