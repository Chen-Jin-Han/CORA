from pathlib import Path
import tarfile
root = Path(__file__).resolve().parent
with tarfile.open(root / 'source.tar.gz', 'w:gz') as tar:
    for path in root.iterdir():
        if path.suffix in ['.py', '.txt', '.json', '.sh', '.md'] and path.name != 'remote_session.py':
            tar.add(path, arcname=path.name)
    for folder in ['vendor/dreamerv3', 'vendor/aco']:
        for path in (root / folder).rglob('*'):
            if path.is_file() and '.git' not in path.parts and '__pycache__' not in path.parts:
                tar.add(path, arcname=path.relative_to(root))
    tar.add(root / 'vendor/SMFANet/LICENSE.txt', arcname='vendor/SMFANet/LICENSE.txt')
print(root / 'source.tar.gz')
