# minify

Reduce generated HTML, CSS, and JavaScript size. Native support was added in Zensical **0.0.58**.

Reduce transfer size for a large documentation site; minify selected custom styles.

## Try it

[Open the minify example](/zensical-examples/variants/minify/).

### HTML

View the generated page source to inspect minified HTML.

### CSS

Open the linked CSS file to see the minified version of the spaced source fixture.

## CSS result

The 88-byte source fixture:

```css
/* A deliberately spaced fixture. */
.example {
    color: #336699;
    margin:  0px;
}
```

The [29-byte generated file](/zensical-examples/variants/minify/assets/custom.min.css):

```css
.example{color:#369;margin:0}
```

??? example "Source and configuration"

    The [configuration](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/minify/zensical.toml) and [example Markdown](https://github.com/pete-wai/zensical-examples/blob/main/variants/plugins/minify/docs/index.md) are available in the repository. Other files in that directory supply the example’s fixtures.

[Zensical compatibility and settings](https://zensical.org/docs/compatibility/mkdocs/plugins/#minify) · [Plugin documentation](https://github.com/byrnereese/mkdocs-minify-plugin)
