"""Freeze existing checkpoints and reuse the completed NAFNet image assessment."""
import hashlib
import json
from pathlib import Path

import torch
from common import bind, fingerprint, read_config, root, save_json

BASE = Path('/data1/CST/CORA/promptir-nafnet-frozen6500')
EXPECTED_SHA256 = {
    'promptir': '60b755df954caea9ff5dab2c83e7c584c100c807b22ac1e6954a41ef89e4c645',
    'nafnet': 'afcdcda39783b45c0f0a7386670984600310d5746357fdaf57cf5be6f61a1d21',
}


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024),b''):h.update(block)
    return h.hexdigest()


def main():
    manifest={}
    for model in ['promptir','nafnet']:
        c=read_config('config_'+model+'.json')
        r=bind(c)
        src=Path(c['checkpoint_source'])
        ck=src/'checkpoints'/model/'last.pt'
        assert sha(ck)==EXPECTED_SHA256[model],f'{model}: checkpoint changed after freezing'
        state=torch.load(ck,map_location='cpu',weights_only=False)
        protocol=json.loads((src/'protocol.json').read_text())
        assert state['name']==model and state['step']==c['frozen_checkpoint_step']
        assert state['config_hash']==fingerprint(protocol)
        manifest[model]=dict(checkpoint=str(ck),sha256=EXPECTED_SHA256[model],step=state['step'],source_protocol=str(src/'protocol.json'))
        if model=='nafnet':
            image_src=src/'images'/model
            assert json.loads((image_src/'summary.json').read_text())['all']['n']==130000
            image_dest=r/'images'/model
            image_dest.parent.mkdir(parents=True,exist_ok=True)
            if image_dest.exists():assert image_dest.resolve()==image_src.resolve()
            else:image_dest.symlink_to(image_src,target_is_directory=True)
    out=BASE/'frozen_manifest.json'
    if out.exists():assert json.loads(out.read_text())==manifest
    else:save_json(out,manifest)
    print(json.dumps(manifest),flush=True)


if __name__=='__main__':main()
