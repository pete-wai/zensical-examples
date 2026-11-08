"""Build every native site, then assemble a GitHub Pages artifact."""
from pathlib import Path
import json, re, shutil, subprocess, sys, zipfile
ROOT = Path(__file__).resolve().parents[1]
BIN = Path(sys.executable).parent / 'zensical'
LOGS = ROOT / '.build/logs'

def title(p):
    match = re.search(r'^# (.+)$',p.read_text(),re.M)
    return match.group(1) if match else p.stem.replace('-',' ').title()

def inline(v):
    if isinstance(v,dict): return '{' + ', '.join(json.dumps(k)+' = '+inline(x) for k,x in v.items())+'}'
    if isinstance(v,list): return '['+', '.join(inline(x) for x in v)+']'
    return json.dumps(v)

def main():
    LOGS.mkdir(parents=True,exist_ok=True)
    nav=[{'Start here':'index.md'}]
    for directory,label in [('authoring','Authoring'),('plugins','Plugins'),('ui','UI & configuration'),('changelog','Changelog')]:
        if directory == 'changelog':
            nav.append({label:'changelog/index.md'})
            continue
        paths=sorted((ROOT/'docs'/directory).rglob('*.md'),key=lambda p:(p.name!='index.md',str(p)))
        nav.append({label:[{title(p):str(p.relative_to(ROOT/'docs'))} for p in paths]})
    nav.append({'Coverage':'coverage.md'})
    config=(ROOT/'zensical.toml').read_text()
    config=re.sub(r'^nav = .*\n','',config,flags=re.M)
    config=config.replace('[project]\n','[project]\nnav = '+inline(nav)+'\n',1)
    (ROOT/'zensical.toml').write_text(config)
    configs=[ROOT/'zensical.toml',*sorted((ROOT/'variants').glob('**/zensical.toml'))]
    names=[c.parent.name for c in configs[1:]]
    if len(set(names)) != len(names): raise SystemExit('Variant slugs must be unique')
    for config in configs:
        slug='main' if config.parent==ROOT else config.parent.name
        result=subprocess.run([str(BIN),'build','--strict','-f',str(config)],cwd=config.parent,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (LOGS/f'{slug}.log').write_text(result.stdout)
        print(f'{slug}: '+('OK' if result.returncode==0 else 'FAILED'),flush=True)
        if result.returncode:
            print(re.sub(r'\x1b\[[0-9;]*m','',result.stdout)[-8000:])
            raise SystemExit(result.returncode)
        if slug!='main':
            dest=ROOT/'site/variants'/slug
            if dest.exists(): shutil.rmtree(dest)
            shutil.copytree(config.parent/'site',dest)
    from build_versions import build_versions
    build_versions()
    offline=ROOT/'site/variants/offline'
    downloads=ROOT/'site/downloads'; downloads.mkdir(exist_ok=True)
    if offline.exists():
        with zipfile.ZipFile(downloads/'offline-demo.zip','w',zipfile.ZIP_DEFLATED) as z:
            for path in offline.rglob('*'):
                if path.is_file(): z.write(path,Path('offline-demo')/path.relative_to(offline))
    (ROOT/'site/.nojekyll').touch()
    print(f'Built {len(configs)} native sites.')

if __name__=='__main__': main()
