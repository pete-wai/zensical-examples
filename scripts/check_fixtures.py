"""Check intentional validation failures and equivalent config formats."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
BIN = Path(sys.executable).parent / 'zensical'


def run(directory: Path, config: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([str(BIN), 'build', '--strict', '-f', config], cwd=directory,
                          text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def main() -> None:
    validation = run(ROOT / 'fixtures/validation', 'invalid.toml')
    if validation.returncode == 0 or 'page does not exist' not in validation.stdout.lower():
        raise SystemExit('Expected missing-page validation failure; got:\n' + validation.stdout)
    for config, output in [('mkdocs.yml', 'site-yaml'), ('equivalent.toml', 'site-toml')]:
        result = run(ROOT / 'fixtures/mkdocs-config', config)
        if result.returncode:
            raise SystemExit(f'{config} failed:\n{result.stdout}')
        site = ROOT / 'fixtures/mkdocs-config' / output
        index = (site / 'index.html').read_text()
        guide = (site / 'guide.html').read_text()
        if 'Configuration equivalence' not in index or 'guide.html' not in index or 'Both configuration formats' not in guide:
            raise SystemExit(f'{config}: expected content or navigation is missing')
    # These sites are built by scripts/build.py. Check the public artifacts,
    # including absence, rather than treating configuration as proof.
    from bs4 import BeautifulSoup
    for name, hidden, visible in [
        ('build-workflow', 'hidden.html', 'visible.html'),
        ('build-workflow-explicit', 'hidden/index.html', 'visible/index.html'),
    ]:
        site = ROOT / 'variants/ui' / name / 'site'
        if not (site / hidden).is_file() or not (site / visible).is_file():
            raise SystemExit(f'{name}: expected pages are missing; run scripts/build.py first')
        if any((site / path).exists() for path in ('draft.html', 'draft', 'excluded.html', 'excluded')):
            raise SystemExit(f'{name}: draft or excluded page was published')
        nav = BeautifulSoup((site / 'index.html').read_text(), 'html.parser').select('nav a')
        labels = [a.get_text(' ', strip=True) for a in nav]
        if ('Hidden, explicitly listed' in labels) != (name == 'build-workflow-explicit'):
            raise SystemExit(f'{name}: unexpected hidden page in navigation')
    print('Validated strict missing-link failure, TOML/YAML examples, and workflow output.')


if __name__ == '__main__':
    main()
