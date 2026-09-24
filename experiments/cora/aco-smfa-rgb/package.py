"""Create a source-only bundle; excludes checkpoints, datasets, PDFs and model assets."""
import hashlib
import json
from pathlib import Path
import tarfile

src=Path(__file__).resolve().parent
dest=src.parent/'aco-smfa-rgb-source.tar.gz'
files=[]
for p in src.rglob('*'):
    if not p.is_file() or '__pycache__' in p.parts or '.git' in p.parts: continue
    if any(x in p.parts for x in ['outputs','datasets','pretrain','figs','assets','.eggs','basicsr.egg-info']): continue
    if p.suffix.lower() in ['.py','.json','.md','.sh','.txt','.yaml','.yml','.toml','.cfg'] or p.name.startswith('LICENSE'):
        files.append(p)
# Hash runtime Python independently of optional vendor data/docs; installed copy is self contained.
with tarfile.open(dest,'w:gz') as tar:
    for p in sorted(files): tar.add(p,arcname=str(Path(src.name)/p.relative_to(src)),recursive=False)
sha=hashlib.sha256(dest.read_bytes()).hexdigest()
print(json.dumps(dict(archive=str(dest),files=len(files),bytes=dest.stat().st_size,sha256=sha),indent=2))
dest.with_suffix(dest.suffix+'.sha256').write_text(sha+'  '+dest.name+'\n')
