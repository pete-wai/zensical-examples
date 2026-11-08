"""Check the assembled artifact, including links between independent builds."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json, sys
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
PREFIX='/zensical-examples/'
errors=[]
cache={}
def read_html(path):
    key=str(path.resolve())
    if key not in cache: cache[key]=BeautifulSoup(path.read_text(),'html.parser')
    return cache[key]
html=list(SITE.rglob('*.html'))
if not html: raise SystemExit('No site output. Run scripts/build.py first.')
for p in html:
    soup=read_html(p)
    for tag,attr in [('a','href'),('img','src'),('script','src'),('link','href'),('source','src'),('video','src'),('audio','src')]:
        for node in soup.find_all(tag):
            url=node.get(attr,'')
            parsed=urlsplit(url)
            if not url: continue
            if parsed.netloc == 'pete-wai.github.io' and parsed.path.startswith(PREFIX): pass
            elif parsed.scheme or parsed.netloc: continue
            path=unquote(parsed.path)
            if not path: target=p
            elif path.startswith(PREFIX): target=SITE/path[len(PREFIX):]
            elif path.startswith('/'):
                errors.append(f'{p.relative_to(SITE)}: invalid root URL {url}'); continue
            else: target=p.parent/path
            target=target.resolve()
            if target.is_dir(): target=target/'index.html'
            if not target.exists(): errors.append(f'{p.relative_to(SITE)}: missing {url}')
            elif parsed.fragment and target.suffix=='.html' and not parsed.fragment.startswith('__'):
                ts=soup if target==p.resolve() else read_html(target)
                frag=unquote(parsed.fragment)
                if not ts.find(id=frag) and not ts.find('a',attrs={'name':frag}):
                    errors.append(f'{p.relative_to(SITE)}: missing anchor {url}')
# Assert visible outcomes, not just successful builds.
checks={
 'variants/markdown-exec/index.html':['<h1'],
 'variants/audio/index.html':['<audio'],
 'variants/video/index.html':['<video'],
 'variants/table-reader/index.html':['<table'],
 'variants/callouts/index.html':['admonition'],
 'variants/gh-admonitions/index.html':['admonition'],
 'authoring/math/index.html':['arithmatex'],
 'authoring/diagrams/index.html':['mermaid'],
}
for path,needles in checks.items():
    p=SITE/path
    if not p.exists(): errors.append(f'Missing required demonstration {path}'); continue
    for needle in needles:
        if needle not in p.read_text(): errors.append(f'{path}: expected {needle}')
for slug in ['optimize','social','rss','llmstxt','redirects','offline','mike']:
    if not (SITE/'variants'/slug/'index.html').exists(): errors.append(f'Missing {slug} output')
if errors:
    print('\n'.join(sorted(set(errors))))
    raise SystemExit(f'{len(set(errors))} checks failed across {len(html)} HTML files')
print(f'Checked links, anchors, assets, and demo markers across {len(html)} HTML files.')
