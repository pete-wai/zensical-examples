"""Exercise the official compatible mike fork in a disposable local Git repository.

No remote is configured or pushed. Its gh-pages artifact is merged into the main
Pages artifact, so this remains a real mike deployment without a second host.
"""
from pathlib import Path
import os, shutil, subprocess, sys, tarfile, io
ROOT=Path(__file__).resolve().parents[1]

def build_versions():
    target=ROOT/'.build/mike'
    if target.exists(): shutil.rmtree(target)
    shutil.copytree(ROOT/'variants/plugins/mike',target,ignore=shutil.ignore_patterns('site','.cache'))
    env={**os.environ,'PATH':str(Path(sys.executable).parent)+os.pathsep+os.environ['PATH']}
    def run(*args):
        p=subprocess.run(args,cwd=target,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        if p.returncode: raise RuntimeError(p.stdout)
        return p.stdout
    run('git','init','-b','main')
    run('git','config','user.name','Zensical Examples build')
    run('git','config','user.email','build@example.invalid')
    run('git','add','.')
    run('git','commit','-m','Local versioning fixture')
    for version,title,body,alias in [
        ('1.0','Field guide 1.0','This sample edition describes identifying a kestrel by its hovering flight. It deliberately lacks the newer equipment advice.',[]),
        ('2.0','Field guide 2.0','This sample edition adds a field checklist: binoculars, notebook, and a timestamp for each observation. Switch to 1.0 to compare the older edition.',['stable'])]:
        (target/'docs/index.md').write_text(f'# {title}\n\n{body}\n\nThese are fictional guide editions, both built with Zensical 0.1.0. They demonstrate documentation versioning, not historical Zensical runtimes.\n\n[Read the field notes](notes.md)\n\n[← Return to the mike explainer](/zensical-examples/plugins/mike/)\n')
        (target/'docs/notes.md').write_text(f'# Field notes — edition {version}\n\n{body}\n\nSwitch editions while on this page: the selector preserves the matching page path.\n\n[Return to overview](index.md)\n')
        run('mike','deploy','-F','zensical.toml','--ignore-remote-status','--alias-type','redirect','-t',title,version,*alias)
    run('mike','set-default','-F','zensical.toml','--ignore-remote-status','stable')
    dest=ROOT/'site/variants/mike'
    if dest.exists(): shutil.rmtree(dest)
    dest.mkdir(parents=True)
    data=subprocess.check_output(['git','archive','gh-pages'],cwd=target)
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        tar.extractall(dest,filter='data')
    print('mike: built two real versioned editions and stable alias')

if __name__=='__main__': build_versions()
