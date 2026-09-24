import tarfile,hashlib,json
from pathlib import Path
p=Path(__file__).resolve().parent
out=p.parent/'aco-smfa-full13-source.tar.gz'
with tarfile.open(out,'w:gz') as tar:
    for f in p.rglob('*'):
        if f.is_file() and '__pycache__' not in f.parts and '.git' not in f.parts:tar.add(f,arcname=str(f.relative_to(p)))
print(json.dumps(dict(path=str(out),bytes=out.stat().st_size,sha256=hashlib.sha256(out.read_bytes()).hexdigest())))
