# What changed in Zensical

Everything from **0.0.60 to 0.1.0**, newest first. Each release includes the changes to the site interface that shipped with it, so you can catch up without reading a second changelog. Interface changes appear once, when they first reach a Zensical release.

The biggest additions in this period are blogs, subscription feeds, automatically generated API references, social preview images, Markdown exports, audio and video, and image optimization. Search, navigation, and local preview also received many fixes.

## 0.1.0 — A compatibility-focused milestone { #v0-1-0 }

November 5, 2026 · Includes UI 0.0.41, unchanged from 0.0.74.

This starts the beta release line. The work in this release mainly makes existing sites build more reliably, especially sites moving from MkDocs.

**Fixes and upgrade notes**

- Configuration mistakes are caught earlier. Incorrect setting types, missing watched paths, and overlapping source/output directories receive validation errors. In strict mode, configuration warnings stop the build before it clears existing output.
- Inherited configuration behaves more like MkDocs: a child configuration replaces list settings rather than unexpectedly combining them. Leaving navigation or the theme unset uses the defaults.
- Custom templates are retained correctly, including inherited static templates and extra template files. Projects that extend a theme are less likely to lose part of their output.
- Extra JavaScript files receive the appropriate script type using MkDocs-compatible rules. Site URLs, canonical page links, and repository defaults also receive compatibility fixes.
- Dependencies used for CSS processing and number parsing receive security updates.

## 0.0.74 — Smaller images and more reliable search filters { #v0-0-74 }

October 30, 2026 · Includes changes from UI 0.0.40–0.0.41.

**New features and improvements**

- **Optimize images during the build.** The `optimize` integration reduces the size of supported PNG and JPEG files while keeping their URLs the same. This is useful for image-heavy guides where readers would otherwise download unnecessarily large files. [See the image comparison](../plugins/optimize.md).
- The theme's templates, icons, and browser code now come from a separate `zensical-ui` package. This changes how Zensical is packaged; it does not require you to maintain a separate website. UI developers can work on that package independently.

**Fixes**

- Search tag filters return the correct subset of results. Selecting a topic should narrow the results to pages tagged with it. [Try filtered search](../plugins/search.md).
- An image gallery shows the image variants for the active light or dark theme, rather than mixing both versions into the slideshow.
- Redirects preserve query strings, so information after `?` in an old link is not lost when the reader reaches the replacement page.
- Blog dates follow the site's language and regional settings. Images referenced by URL remain present in exported Markdown.
- Page descriptions handle special HTML characters correctly. Older validation settings remain compatible, and the privacy integration respects custom certificate bundles when downloading assets.

## 0.0.73 — Better diagrams and fewer jumps when navigating { #v0-0-73 }

October 26, 2026 · Includes UI 0.0.39.

**New features and improvements**

- **Mermaid 12 is supported**, with updated diagram styling for light and dark themes. This keeps diagrams compatible with the newer renderer. The bundled icon collection also gains 16 icons. [Explore diagrams](../authoring/diagrams.md).

**Fixes**

- Reloading a page or using Back and Forward restores your reading position more reliably. Rapid navigation no longer applies an old scroll position to the wrong page, and clicking the same heading link repeatedly avoids unnecessary browser-history entries.
- The privacy integration fixes paths for assets loaded by JavaScript on nested pages and in local preview. A resource that works on the homepage should no longer break simply because the reader opens a page deeper in the site.
- The starter project's nested-list example has the indentation needed to render as a nested list.

## 0.0.72 — Serve external assets from your own site { #v0-0-72 }

October 23, 2026 · Includes UI 0.0.38.

**New features and improvements**

- **The privacy integration can download supported external assets and serve them locally.** Readers can receive those files from your site instead of requesting them directly from the original third-party host. [See a locally served asset](../plugins/privacy.md).
- The icon collection gains 26 Lucide icons.

**Fixes**

- Rapid template edits are detected even when several changes happen within the same second. Preview also handles replaced files on Linux more reliably and avoids unnecessary work when files are merely read.
- Markdown code fences work with the default settings. When you configure several Markdown extensions, code-block processing respects their configured order.
- Links ending in a slash resolve correctly. Rewriting asset and page URLs no longer alters the surrounding HTML, and URLs containing HTML character references are decoded correctly before rewriting.
- Files remain available when documentation and custom-theme directories overlap. Compatibility scripts for browsers are normalized correctly, the preview server lists all its listening addresses, and search indexing counts large fields correctly against its limits.
- Header controls have clearer labels for screen readers. Long words in the contents sidebar are shortened with an ellipsis instead of overflowing, while entries can still wrap. Notes in Mermaid state diagrams use readable theme text colors.
- Security maintenance updates the TLS library used for secure connections and removes a vulnerable CSS build dependency.

## 0.0.71 — Reuse Markdown across pages { #v0-0-71 }

October 16, 2026 · Includes UI 0.0.37, unchanged from 0.0.70.

**New features and improvements**

- **Include Markdown from another file.** Support for `include-markdown` lets you reuse a shared warning, procedure, or explanation without copying it into every page. Editing the shared file updates the places that include it. [See reusable content](../plugins/include-markdown.md).

**Fixes**

- Social preview cards keep their default colors when you have not explicitly chosen a palette.
- File discovery no longer causes unnecessary local-preview restarts.
- Search indexing reports when a field exceeds the supported size, making oversized content easier to diagnose.
- Linux ARM64 packages are built on native ARM hardware, improving the release packaging process for that platform.

## 0.0.70 — Keep drafts out of the published site { #v0-0-70 }

October 12, 2026 · Includes UI 0.0.37.

**New features and improvements**

- **Separate unfinished content from published content.** `draft_docs` keeps draft pages available in local preview but omits them from production. `exclude_docs` leaves files out altogether. `not_in_nav` hides pages from automatically generated navigation while leaving them accessible and searchable. The theme also gains styling for draft markers. [Compare the publishing options](../ui/build-workflow.md).
- Pages expose discovery links to their Markdown alternatives and `llms.txt` when those outputs are available, helping tools find a text version of the site.
- The bundled icon collection gains 17 icons.

**Fixes**

- Search is easier to use with a keyboard and assistive technology: focus handling, labels, and result announcements improve. Search startup, result rendering, and error handling also receive fixes.

## 0.0.69 — Control page order and reuse structured data { #v0-0-69 }

October 8, 2026 · Includes UI 0.0.36.

**New features and improvements**

- **Order navigation with page weights.** The `nav-weight` integration lets you give pages an explicit ordering value instead of relying on filenames. It is useful when an introduction should precede an advanced guide. [See ordered navigation](../plugins/nav-weight.md).
- **Use data files inside your Markdown.** The `markdownextradata` integration makes configured data available to page templates, so repeated facts can come from one source. [See data-driven content](../plugins/markdownextradata.md).

**Fixes**

- Emoji survive Markdown exports. HTML minification no longer crashes on multibyte characters, such as accented letters, in attribute values.
- Preview detects changes in watched files and directories reached through symbolic links.
- Code names have better spacing in navigation and breadcrumbs. Anchor elements without a destination no longer disrupt instant navigation.

## 0.0.68 — Embed audio and video { #v0-0-68 }

October 5, 2026 · Includes UI 0.0.35.

**New features and improvements**

- **Add playable media to a page.** Native implementations of the audio and video plugins turn their Markdown markers into media embeds. Use audio for a pronunciation example or video for a short procedure. [Try audio](../plugins/audio.md) or [video](../plugins/video.md).

**Fixes**

- Macros work more consistently in page titles as well as page bodies. Included templates refresh between builds, missing-variable behavior follows the configured policy, and rendering errors provide useful diagnostics instead of silently leaving misleading output.
- Opening a search result uses instant navigation when enabled, avoiding an unnecessary full-page reload.
- “Skip to content” links reliably reach the page content. Overlays and progress indicators have corrected names for assistive technology.

**Upgrade note:** Python 3.10 is no longer supported. Zensical now requires Python 3.11 or newer.

## 0.0.67 — Share pages as images or Markdown { #v0-0-67 }

September 30, 2026 · Includes UI 0.0.34.

**New features and improvements**

- **Generate social preview cards.** The `social` integration creates the image and metadata used when a page is shared, with bundled or custom layouts. [See a generated card](../plugins/social.md).
- **Publish text versions of your pages.** The `llmstxt` integration creates a Markdown index and page exports. The interface gains a “Copy as Markdown” action for pages with a Markdown equivalent, making content easier to reuse in another tool. [Try the Markdown outputs](../plugins/llmstxt.md).
- **Exclude selected files from the output** with the native `exclude` integration. This is useful when source material belongs in the project but should not be published. [See exclusions](../plugins/exclude.md).
- **Reuse GitHub-style alerts.** Familiar note, warning, and similar alert syntax can render as native callouts. The icon collection also gains 12 icons. [See the alert examples](../plugins/gh-admonitions.md).

**Fixes**

- Blog pages honor custom templates supplied by the project rather than ignoring those overrides.

## 0.0.66 — Generate an API reference from Python code { #v0-0-66 }

September 28, 2026 · Includes UI 0.0.33.

**New features and improvements**

- **Generate reference pages and their navigation automatically.** `autoapi` and `api-autonav` discover Python modules and use `mkdocstrings` to document them. You no longer need to hand-maintain a separate reference page and navigation entry for every module. [Compare the API generators](../plugins/autoapi.md).
- Links back from API objects to the pages that reference them gain styling in both themes. This makes the backlink support added in 0.0.65 easier to read.

**Fixes**

- Published pages are no longer missing from the sitemap, which helps search engines discover them.
- Responsive-image URLs in raw HTML resolve relative to the source page. Custom inline-code highlighting formatters load correctly from TOML configuration.
- Lightbox galleries keep their styling after instant navigation. Mermaid diagrams respect custom node-label colors, and the `/` keyboard shortcut opens search reliably.

## 0.0.65 — Let readers subscribe to updates { #v0-0-65 }

September 24, 2026 · Includes UI 0.0.32, unchanged from 0.0.64.

**New features and improvements**

- **Publish feeds for new and updated pages.** The native RSS integration generates RSS and JSON feeds that readers can subscribe to in a feed reader. They can follow changes without repeatedly checking the site. [Open the sample feeds](../plugins/rss.md).
- **Show where an API object is used in the documentation.** API pages can link back to the pages that reference an object, including when rebuilding from cached content. The `enable_inventory` setting also controls the object index used for cross-project references.
- Automatic cross-references gain options for choosing the closest matching target when a name is ambiguous and for controlling link tooltips and their formatting.
- Macros gain more control over which pages are processed and how much diagnostic output is printed. Versioned sites can honor mike's setting to show or hide the version selector.

**Fixes**

- Links written to a blog post's Markdown source now lead to the correct published post address.

## 0.0.64 — Publish a blog alongside your documentation { #v0-0-64 }

September 22, 2026 · Includes UI 0.0.32.

**New features and improvements**

- **Native blog support arrives.** Posts can have authors and categories, with archive pages and pagination for browsing older entries. This suits release announcements, project updates, or articles that belong beside the reference documentation. [Explore the sample blog](../plugins/blog.md).
- The modern theme's blog sidebar gets a revised layout for author information and post metadata, with configurable icons. The classic theme keeps its existing presentation.

**Fixes**

- Search highlighting stops when there are no search terms left to highlight, avoiding inappropriate highlighting after a query is cleared or reduced to nothing.

## 0.0.63 — Shared snippets update properly in preview { #v0-0-63 }

September 19, 2026 · Includes UI 0.0.31.

**New features and improvements**

- Task-list checkboxes have better sizing and alignment in the modern theme. The bundled icon collection gains 60 icons.

**Fixes**

- Editing an included snippet triggers a rebuild of the page that uses it. You can change a shared instruction and see the updated result in preview without having to touch the containing page. [See snippets](../authoring/snippets.md).
- Hidden files and directories are kept out of the generated site.
- The preview server redirects its root address to the expected trailing-slash URL.
- Navigation sections that contain only an index page no longer display an empty submenu.

## 0.0.62 — Reuse Obsidian-style callouts { #v0-0-62 }

September 13, 2026 · Includes UI 0.0.30.

**New features and improvements**

- **Obsidian-style callouts render as native admonitions.** Notes written with that syntax can keep their warning or information-box presentation when moved into a Zensical site. [Compare the callouts](../plugins/callouts.md).

**Fixes**

- A link to content inside a collapsed detail, a tab, or a code annotation opens the enclosing components before scrolling to the target. This also works when those components are nested, so a deep link can reveal the passage it points to.
- Listing the configuration file among watched files no longer breaks the build. Plugin validation is less restrictive for existing configurations, including mike's versioning settings.

## 0.0.61 — Keep old links working when headings move { #v0-0-61 }

September 11, 2026 · Includes UI 0.0.29.

**New features and improvements**

- **Redirect individual sections, not just whole pages.** If `#installation` becomes `#getting-started`, the old link can still take readers to the right place. A page redirect can also land on a particular heading. Chains of redirects resolve to their final destination, while loops are rejected. [Try redirects](../plugins/redirects.md).

**Fixes**

- Existing automatic-reference and search configurations are accepted more flexibly when migrating a project.
- Lightbox galleries load their styles correctly when those styles are hosted locally.
- A pruned navigation section with only an index page no longer shows an expand control with nothing to expand.

**Maintenance:** Redirect processing was reorganized internally, and preview-server tests no longer compete for the same network port. These changes mainly help maintain the project rather than add a visible feature.

## 0.0.60 — Turn data files into tables directly { #v0-0-60 }

September 8, 2026 · Includes UI 0.0.28.

**New features and improvements**

- **Render supported data files, including CSV, as tables without a macros wrapper.** The direct `table-reader` integration is useful for publishing a dataset or comparison table that is maintained outside the Markdown page. [See data tables](../plugins/table-reader.md).
- The bundled icon collection gains 51 icons.

**Fixes**

- Pruned navigation retains section names and links to the section's index page, so shortening a large navigation tree does not make its groups hard to identify.
- Alternate-page links are treated as language alternatives only when they declare a language. Other kinds of alternate links are no longer mistaken for translations.
- Macro template includes work with Windows extended-length paths.

**Maintenance:** The UI build toolchain and development dependencies were updated, including fixes for reported dependency vulnerabilities.
