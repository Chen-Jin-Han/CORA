"""Resumable range download from the official PyTorch index, SHA256 verified."""
import concurrent.futures
import hashlib
import html
import re
import time
import urllib.request
from pathlib import Path

INDEX = 'https://download.pytorch.org/whl/cu121/torch/'
NAME = 'torch-2.5.1+cu121-cp310-cp310-win_amd64.whl'
ROOT = Path('../downloads')


def main():
    ROOT.mkdir(exist_ok=True)
    page = urllib.request.urlopen(INDEX, timeout=60).read().decode()
    urls = [html.unescape(u) for u in re.findall(r'href="([^"]+)"', page)
            if 'torch-2.5.1%2Bcu121-cp310-cp310-win_amd64.whl' in u]
    if len(urls) != 1:
        raise RuntimeError(f'Expected one official wheel, found {len(urls)}')
    url, expected = urls[0].split('#sha256=')
    # Some index mirrors advertise download-r2, which can reject this network.
    url = 'https://download.pytorch.org/whl/cu121/' + NAME.replace('+', '%2B')
    size = int(urllib.request.urlopen(urllib.request.Request(url, method='HEAD'), timeout=60).headers['Content-Length'])
    parts = ROOT / (NAME + '.parts')
    parts.mkdir(exist_ok=True)
    chunk = 8 * 1024 * 1024
    count = (size + chunk - 1) // chunk
    def fetch(i):
        start, end = i * chunk, min(size, (i+1)*chunk) - 1
        path = parts / f'{i:04d}'
        if path.exists() and path.stat().st_size == end - start + 1:
            return
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, headers={'Range': f'bytes={start}-{end}'})
                with urllib.request.urlopen(req, timeout=90) as response:
                    if response.status != 206 or response.headers.get('Content-Range') != f'bytes {start}-{end}/{size}':
                        raise RuntimeError('Server did not honor byte range')
                    data = response.read()
                if len(data) != end-start+1:
                    raise RuntimeError('Short range')
                path.write_bytes(data)
                return
            except Exception:
                if attempt == 4:
                    raise
                time.sleep(2)
    print(f'Downloading {size / 2**20:.1f} MiB in {count} verified ranges', flush=True)
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        futures = [pool.submit(fetch, i) for i in range(count)]
        for n, f in enumerate(concurrent.futures.as_completed(futures), 1):
            f.result()
            if n % 10 == 0 or n == count:
                print(f'{n}/{count} parts complete ({time.time()-start:.0f}s)', flush=True)
    digest = hashlib.sha256()
    dest = ROOT / NAME
    with dest.open('wb') as output:
        for i in range(count):
            data = (parts / f'{i:04d}').read_bytes()
            digest.update(data)
            output.write(data)
    if digest.hexdigest() != expected:
        raise RuntimeError('SHA256 mismatch; do not install this wheel')
    (ROOT / (NAME + '.sha256')).write_text(expected + '\n')
    print(f'VERIFIED {dest}: {expected}', flush=True)


if __name__ == '__main__':
    main()
