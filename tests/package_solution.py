"""Portable source archive; excludes runtimes, credentials, Git and recursive zips."""
from pathlib import Path
import shutil
import zipfile

root=Path(__file__).resolve().parents[1]
output=root/'output'
output.mkdir(exist_ok=True)
files=[]
for folder in ['src','web','examples','tests','docs','.github']:
    for p in (root/folder).rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts or p.suffix in ['.zip','.log']:
            continue
        files.append(p)
for name in ['README.md','README-EXPERT.md','.gitignore','start.ps1','start.sh','start-local.cmd','Dockerfile','compose.yaml']:
    files.append(root/name)
files.append(output/'pdf/Java-Blueprints-solution.pdf')
target=output/'Java-Blueprints-complete.zip'
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for p in sorted(files):archive.write(p,'java-blueprints/'+p.relative_to(root).as_posix())
with zipfile.ZipFile(target) as archive:
    assert archive.testzip() is None
    assert 'java-blueprints/src/BlueprintServer.java' in archive.namelist()
    assert not any('.runtime/' in n or '/.git/' in n for n in archive.namelist())
    assert archive.read('java-blueprints/output/pdf/Java-Blueprints-solution.pdf') == (output/'pdf/Java-Blueprints-solution.pdf').read_bytes()
    assert 'java-blueprints/.github/workflows/verify.yml' in archive.namelist()
    assert 'java-blueprints/docs/verification-summary.json' in archive.namelist()
shutil.copyfile(target,root/'web/java-blueprints-source.zip')
print(target, target.stat().st_size,'bytes;',len(files),'files; ZIP verified')
