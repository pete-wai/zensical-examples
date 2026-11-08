"""Verify observable native-plugin outcomes in the assembled Pages artifact.

Run after scripts/build.py. These checks inspect generated pages and files, including
features that can fail silently while the site build itself still succeeds.
"""
from pathlib import Path
import json
import re
import zipfile
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
VARIANTS = SITE / 'variants'
SOURCE = ROOT / 'variants/plugins'
errors = []
checked = set()


def require(slug, condition, message):
    checked.add(slug)
    if not condition:
        errors.append(f'{slug}: {message}')


def read(slug, path='index.html'):
    file = VARIANTS / slug / path
    if not file.is_file():
        require(slug, False, f'missing {path}')
        return ''
    return file.read_text(encoding='utf-8')


def soup(slug, path='index.html'):
    return BeautifulSoup(read(slug, path), 'html.parser')


def visible(slug, path='index.html'):
    return soup(slug, path).get_text(' ', strip=True)


def nav_links(slug):
    page = soup(slug)
    return [(a.get_text(' ', strip=True), a.get('href', ''))
            for a in page.select('nav a.md-nav__link')]


def has_text(slug, path, *needles):
    text = visible(slug, path)
    require(slug, all(n in text for n in needles), f'{path} missing rendered content {needles}')


# Generated Python API and docstring content.
has_text('api-autonav', 'reference/samplelib/index.html', 'greet', 'name')
has_text('autoapi', 'autoapi/samplelib/index.html', 'greet', 'name')
has_text('mkdocstrings', 'index.html', 'greet', 'name')

# Media must be converted to native players and point at real packaged files.
for slug, tag, filename in [('audio', 'audio', 'tone.wav'), ('video', 'video', 'clip.mp4')]:
    page = soup(slug)
    players = page.find_all(tag)
    require(slug, len(players) >= 2 and all(p.has_attr('controls') for p in players),
            f'expected two {tag} players with controls')
    require(slug, (VARIANTS / slug / filename).is_file(), f'missing playable {filename}')

refs = soup('autorefs', 'notes/index.html')
require('autorefs', any(a.get('href', '').endswith('#packing-checklist')
                        for a in refs.find_all('a')), 'cross-page heading reference did not resolve')
for slug in ('awesome-nav', 'literate-nav'):
    links = nav_links(slug)
    require(slug, any('Field notes' in title and 'notes/' in href for title, href in links),
            'curated Field notes navigation entry is missing')
    has_text(slug, 'notes/index.html', 'Bring a map')
has_text('blog', 'blog/2025/03/15/first-walk/index.html', 'First walk', 'morning light')
has_text('blog', 'blog/category/field-notes/index.html', 'First walk')
for slug, kinds in [('callouts', ('note', 'warning')), ('gh-admonitions', ('tip', 'warning'))]:
    page = soup(slug)
    for kind in kinds:
        require(slug, bool(page.select_one(f'.admonition.{kind}')), f'{kind} callout was not rendered')
require('exclude', (SOURCE / 'exclude/docs/drafts/private.md').is_file()
        and not (VARIANTS / 'exclude/drafts/private/index.html').exists()
        and (VARIANTS / 'exclude/public/index.html').is_file(), 'draft exclusion or public page failed')
require('glightbox', len(soup('glightbox').select('a.glightbox')) >= 2,
        'images were not linked to lightbox instances')
has_text('include-markdown', 'index.html', 'Shared prerequisite', 'Map', 'Water')

llms = read('llmstxt', 'llms.txt')
require('llmstxt', 'Field notes' in llms and 'notes/index.md' in llms,
        'llms.txt does not index the selected page')
require('llmstxt', 'weather' in read('llmstxt', 'llms-full.txt').lower(),
        'combined llms text lacks selected page content')
has_text('macros', 'index.html', 'Meadow walk', 'Welcome to the trail, Mira!')
exec_page = soup('markdown-exec')
require('markdown-exec', 'Trail distance: 6 km' in exec_page.get_text(' ', strip=True)
        and len(exec_page.select('li')) >= 2, 'executed arithmetic or generated checklist is missing')
has_text('markdownextradata', 'index.html', 'Trail Guide', '2.1')
for path in ('guide/index.html', 'guide/second/index.html'):
    meta = soup('meta', path).find('meta', attrs={'name': 'description'})
    require('meta', bool(meta and meta.get('content') == 'A field guide with inherited metadata.'),
            f'{path} did not inherit the shared description')

versions_file = VARIANTS / 'mike/versions.json'
try:
    versions = json.loads(versions_file.read_text())
    require('mike', {v['version'] for v in versions} >= {'1.0', '2.0'}
            and any(v['version'] == '2.0' and 'stable' in v.get('aliases', []) for v in versions),
            'version inventory or stable alias is missing')
except (OSError, ValueError, KeyError) as exc:
    require('mike', False, f'cannot read version inventory: {exc}')
has_text('mike', '1.0/index.html', 'hovering flight')
has_text('mike', '2.0/index.html', 'binoculars', 'checklist')
require('mike', '2.0/' in read('mike', 'stable/index.html'), 'stable alias does not redirect to 2.0')

css = read('minify', 'assets/custom.min.css')
source_css = (SOURCE / 'minify/docs/assets/custom.css').read_text()
require('minify', '.example' in css and len(css.encode()) < len(source_css.encode()),
        'minified CSS missing or not smaller than source')
links = nav_links('nav-weight')
ordered = [title for title, href in links if 'zebra/' in href or 'apple/' in href]
require('nav-weight', len(ordered) >= 2 and 'Zebra' in ordered[0] and 'Apple' in ordered[1],
        'weighted navigation did not place Zebra before Apple')

offline_index = read('offline', 'search.json')
require('offline', 'kestrel' in offline_index and 'binoculars' in offline_index,
        'offline search index lacks the example terms')
try:
    with zipfile.ZipFile(SITE / 'downloads/offline-demo.zip') as archive:
        names = set(archive.namelist())
        require('offline', {'offline-demo/index.html', 'offline-demo/search.js',
                            'offline-demo/search.json'} <= names, 'offline ZIP lacks search files')
        require('offline', b'kestrel' in archive.read('offline-demo/search.json'),
                'offline ZIP index lacks searchable content')
except (OSError, zipfile.BadZipFile, KeyError) as exc:
    require('offline', False, f'cannot inspect offline ZIP: {exc}')

original = SOURCE / 'optimize/docs/photo.jpg'
optimized = VARIANTS / 'optimize/photo.jpg'
require('optimize', original.is_file() and optimized.is_file()
        and 0 < optimized.stat().st_size < original.stat().st_size, 'JPEG was not reduced')
privacy = soup('privacy')
local_images = [img.get('src', '') for img in privacy.find_all('img')
                if 'assets/external/' in img.get('src', '') and 'python.svg' in img.get('src', '')]
require('privacy', bool(local_images) and (VARIANTS / 'privacy' / local_images[0]).is_file(),
        'external SVG was not downloaded and rewritten to a local URL')
require('privacy', any(a.get('target') == '_blank' and 'noopener' in a.get('rel', [])
                       for a in privacy.find_all('a') if a.get('href', '').startswith('https://')),
        'external link is missing target or noopener')
for old, new in [('old-guide', 'new-guide/'), ('old-kit', 'kit/')]:
    redirect = soup('redirects', f'{old}/index.html')
    refresh = redirect.find('meta', attrs={'http-equiv': re.compile('refresh', re.I)})
    require('redirects', bool(refresh and new in refresh.get('content', '')),
            f'{old} does not redirect to {new}')
try:
    rss = ET.fromstring(read('rss', 'feed_rss_created.xml'))
    titles = [node.text or '' for node in rss.findall('./channel/item/title')]
    require('rss', any('Spring update' in t for t in titles), 'created feed lacks Spring update')
except ET.ParseError as exc:
    require('rss', False, f'invalid created RSS: {exc}')
try:
    search = json.loads(read('search', 'search.json'))
    items = search['items']
    require('search', any('moonflower' in json.dumps(item).lower() for item in items),
            'search index lacks moonflower')
    for location, tag in [('plants/', 'Botany'), ('equipment/', 'Equipment')]:
        require('search', any(item.get('location') == location and tag in item.get('tags', [])
                              and 'field guide' in item.get('text', '').lower() for item in items),
                f'{location} is missing indexed text or {tag} filter tag')
    require('search', not any('quartzbeacon' in json.dumps(item).lower()
                              or item.get('location', '').startswith('unindexed/') for item in items),
            'excluded page appears in the search index')
    has_text('search', 'unindexed/index.html', 'quartzbeacon')
except (ValueError, KeyError) as exc:
    require('search', False, f'invalid search index: {exc}')
links = nav_links('section-index')
require('section-index', any('guide/' in href for _, href in links)
        and (VARIANTS / 'section-index/guide/index.html').is_file(),
        'section landing page is not linked in navigation')
social = soup('social').find('meta', property='og:image')
card = VARIANTS / 'social/assets/images/social/index.png'
require('social', bool(social and 'assets/images/social/index.png' in social.get('content', ''))
        and card.is_file() and card.stat().st_size > 0, 'social card or Open Graph reference is missing')
tables = soup('table-reader').find_all('table')
require('table-reader', len(tables) >= 2 and 'Water bottles' in tables[0].get_text(' ', strip=True)
        and 'Tuesday' in tables[1].get_text(' ', strip=True), 'CSV tables did not render')
tag_page = visible('tags')
require('tags', all(x in tag_page for x in ('Fieldwork', 'Preparation', 'Equipment', 'Field notes')),
        'tag listings are incomplete')

# Each landing page must provide a way back to its explainer. The mike root is a
# redirect, so inspect its current edition; the offline copy uses an absolute URL.
for slug in sorted(p.name for p in SOURCE.iterdir() if (p / 'zensical.toml').is_file()):
    path = '2.0/index.html' if slug == 'mike' else 'index.html'
    page = soup(slug, path)
    target = f'/plugins/{slug}/'
    require(slug, any(target in a.get('href', '') and 'return' in a.get_text(' ', strip=True).lower()
                      for a in page.find_all('a')), 'landing page lacks a return link')

expected = {p.name for p in SOURCE.iterdir() if (p / 'zensical.toml').is_file()}
if len(expected) != 32:
    errors.append(f'expected 32 plugin variants, found {len(expected)}')
if expected != checked:
    errors.append(f'coverage mismatch: missing {sorted(expected - checked)}, extra {sorted(checked - expected)}')
if errors:
    print('\n'.join(errors))
    raise SystemExit(f'{len(errors)} plugin outcome checks failed')
print(f'Checked rendered outcomes, artifacts, and return links for {len(checked)} plugin variants.')
