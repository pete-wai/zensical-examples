"""Regenerate the authored UI fixtures and their native configuration matrix."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://pete-wai.github.io/zensical-examples/'
# slug, label, flags, explanation, theme additions
variants = [
('baseline','Plain navigation',[], 'The sidebar uses collapsible groups. Open Guides, then return here to compare the expanded version.', ''),
('classic','Classic theme',[], 'Compare the header, typography, spacing, and code blocks with the modern baseline. The content is identical.', 'variant = "classic"'),
('tabs','Navigation tabs',['navigation.tabs','navigation.tabs.sticky'], 'Top-level sections become tabs. Scroll down: the tab bar stays visible. On a narrow screen, use the menu instead.', ''),
('sections','Navigation sections',['navigation.sections'], 'Top-level groups are visible section labels instead of collapsed containers. Compare this with Plain navigation.', ''),
('expanded','Expanded navigation',['navigation.expand'], 'All navigation groups start expanded. This suits short manuals but gets noisy on large sites.', ''),
('pruned','Pruned navigation',['navigation.prune','navigation.indexes'], 'Only the current branch is expanded in the generated navigation. Enter Guides to see its children. This reduces large navigation trees.', ''),
('breadcrumbs','Breadcrumbs and section indexes',['navigation.path','navigation.indexes','navigation.footer'], 'Open Guides → Field notes. Breadcrumbs expose the hierarchy and the footer moves through the reading sequence.', ''),
('integrated-toc','Table of contents in navigation',['toc.integrate','toc.follow'], 'The current page headings appear in the left navigation. Scroll through the page to follow the active section.', ''),
('instant','Instant navigation and previews',['navigation.instant','navigation.instant.prefetch','navigation.instant.progress','navigation.instant.preview','navigation.tracking','navigation.top'], 'Follow an internal link without a full page reload. Hover the preview link for a page preview; scroll upward near the bottom for the back-to-top control.', ''),
('dark','Dark color scheme',[], 'A fixed dark palette changes surfaces and code colors. Compare the same callout and code block in the light baseline.', 'palette = { scheme = "slate", primary = "teal", accent = "amber" }'),
('colors','Primary and accent colors',[], 'A teal primary color and orange accent change navigation and interactive emphasis. Hover a link to see the accent.', 'palette = { scheme = "default", primary = "teal", accent = "orange" }'),
('fonts','Alternative typography',[], 'Serif body text gives long prose a different texture; monospace source uses Fira Code. Font loading requires a network connection.', 'font = { text = "Lora", code = "Fira Code" }'),
('system-fonts','System fonts',[], 'The theme uses locally available system fonts without fetching Google Fonts. Compare text width and code with the typography variant.', 'font = false'),
('rtl','Arabic and right-to-left layout',[], 'The navigation and interface run right to left. The Arabic sample shows text direction; English examples remain intentionally visible for comparison.', 'language = "ar"\ndirection = "rtl"'),
('header','Autohiding header',['header.autohide','navigation.tabs'], 'Scroll down until the header leaves view, then scroll upward to reveal it. This creates more reading space.', ''),
('content-actions','Page and code actions',['content.action.edit','content.action.view','content.code.copy','content.code.select','content.code.annotate'], 'Use the source/view links near the title and the copy/select controls in the code block. The repository links point to the shared fixture generator.', ''),
('search-ui','Search suggestions and highlighting',['search.suggest','search.highlight','search.share'], 'Search for kestrel. Follow a result to see matching text highlighted. Use the share control to preserve a search query in a URL.', ''),
]
nav='[{"Overview"="index.md"}, {"Guides"=[{"Start here"="guides/index.md"},{"Field notes"="guides/notes.md"},{"Equipment"="guides/equipment.md"}]}, {"Reference"=[{"Species"="reference/species.md"}]}]'
fixture='''# Field guide\n\n[← Back to UI comparisons](/zensical-examples/ui/)\n\n!!! info "What to notice"\n\n    {explanation}\n\n## Read a field note\n\nA kestrel can hover over a field while scanning for prey. Record the place, time, and weather before counting observations.\n\n[Open the field notes](guides/notes.md){{ .md-button }}\n[Preview the field notes](guides/notes.md){{ data-preview }}\n\n## Bring the right equipment\n\n| Item | Purpose |\n| --- | --- |\n| Binoculars | Observe without approaching |\n| Notebook | Keep a timestamped record |\n| Field guide | Compare similar species |\n\n## Save an observation\n\n```python title="observation.py" linenums="1"\nobservation = {{"species": "kestrel", "count": 2}}\nprint(observation["species"])\n```\n\n## A second reading path\n\nUse the navigation to move between Guides and Reference. The same information architecture appears in every variant, so differences come from the native settings.\n\n## Reading in Arabic\n\nدليل مراقبة الطيور: سجل المكان والوقت وعدد الطيور التي شاهدتها.\n\n## Before leaving\n\nLeave nesting areas undisturbed. A note about uncertainty is more useful than a confident but incorrect identification.\n\n## Compare the interface\n\nReturn to the [UI gallery](/zensical-examples/ui/) and open another variant at the same screen width. Compare the position of the navigation, the contents list, and the header.\n'''
for slug,label,flags,explanation,extra in variants:
    root=ROOT/'variants/ui'/slug
    (root/'docs/guides').mkdir(parents=True,exist_ok=True)
    (root/'docs/reference').mkdir(parents=True,exist_ok=True)
    config=f'''[project]\nsite_name = "{label}"\nsite_url = "{BASE}variants/{slug}/"\nsite_description = "Native Zensical UI comparison"\nnav = {nav}\nrepo_url = "https://github.com/pete-wai/zensical-examples"\nedit_uri = "edit/main/variants/ui/{slug}/docs/"\n[project.theme]\nfeatures = {json.dumps(flags)}\n{extra}\n[project.markdown_extensions]\nadmonition = {{}}\nattr_list = {{}}\ntables = {{}}\n"pymdownx.superfences" = {{}}\n"pymdownx.highlight" = {{}}\n'''
    (root/'zensical.toml').write_text(config)
    (root/'docs/index.md').write_text(fixture.format(explanation=explanation))
    for path,title,body in [('guides/index.md','Guides','Choose field notes or equipment from the navigation.'),('guides/notes.md','Field notes','## Morning survey\n\nTwo kestrels hovered over the meadow at 08:10.\n\n## Afternoon survey\n\nOne kestrel perched on a fence at 15:30.\n\n## Compare conditions\n\nThe morning was calm; the afternoon was windy.'),('guides/equipment.md','Equipment','## Travel light\n\nBinoculars and a notebook are enough for a first survey.\n\n## Longer surveys\n\nAdd water, a map, and weather protection.'),('reference/species.md','Species','## Kestrel\n\nLook for hovering flight and a long tail.\n\n## Buzzard\n\nLook for broad wings when soaring.')]:
        (root/'docs'/path).write_text(f'# {title}\n\n[← Back to UI comparisons](/zensical-examples/ui/)\n\n{body}\n')
(ROOT/'data/ui-variants.json').write_text(json.dumps([{'id':s,'title':l,'features':f,'description':e,'config':f'variants/ui/{s}/zensical.toml'} for s,l,f,e,x in variants],indent=2)+'\n')
