"""Generate matched four-condition restoration figures from existing checkpoints."""
from __future__ import annotations
import argparse, gc, importlib.util, json, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

DATA = Path('/data1/CST/CORA/aco-smfa-full13/datasets/full13_v1')
OUT = Path('/data1/CST/CORA/Latex/效果图')
FULL = Path('/home/gpuadmin/CST/CORA/aco-smfa-full13')
BASE = Path('/home/gpuadmin/CST/CORA/promptir-nafnet-baselines')
TASK = 'walker_walk'
KINDS = ['rain','fog','snow','motion_blur','gaussian_noise','low_light','jpeg','defocus_blur','frost','occlusion_patch','saturation','shadow','shot_noise']
CHECKPOINTS = {
    'ACO': Path('/data1/CST/CORA/aco-smfa-full13/rgb10_seed6_fft_b128_s15000_full13_v1/checkpoints/aco/last.pt'),
    'CORA': Path('/data1/CST/CORA/aco-smfa-full13/rgb10_seed6_fft_b128_s15000_full13_v1/checkpoints/smfa/last.pt'),
    'PromptIR': Path('/data1/CST/CORA/promptir-nafnet-baselines/promptir_seed6_b128_s15000_full13_v1/checkpoints/promptir/last.pt'),
    'NAFNet': Path('/data1/CST/CORA/promptir-nafnet-baselines/nafnet_seed6_b128_s15000_full13_v1/checkpoints/nafnet/last.pt'),
}

def font(n):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'):
        if Path(p).exists(): return ImageFont.truetype(p,n)
    return ImageFont.load_default()

def module(path,name):
    sys.path.insert(0,str(path.parent)); s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def pair(task, kind, idx=42):
    d=DATA/task/'test'; clean=np.load(d/'clean.npy',mmap_mode='r'); inp=np.load(d/'input.npy',mmap_mode='r')
    k=KINDS.index(kind); return np.array(clean[idx]), np.array(inp[idx*13+k])

def infer(method, frames):
    import torch
    if method in ('ACO','CORA'):
        builder=module(FULL/'models.py','cora_models'); model=builder.build('aco' if method=='ACO' else 'smfa')
    else: builder=module(BASE/'models.py','base_models'); model=builder.build(method.lower())
    state=torch.load(CHECKPOINTS[method],map_location='cpu',weights_only=False); model.load_state_dict(state['model'],strict=True); step=int(state['step']); model.eval()
    out=[]
    with torch.inference_mode():
        for f in frames:
            x=torch.from_numpy(f.copy()).permute(2,0,1)[None].float()/127.5-1
            y=model(x).clamp(-1,1)[0].permute(1,2,0).numpy(); out.append(np.uint8(np.clip((y+1)*127.5,0,255).round()))
    del model; gc.collect(); return out,step

def render(task,kind,idx):
    clean,raw=pair(task,kind,idx); outputs={'Clean':[clean],'Raw':[raw]}; steps={}
    for m in ('ACO','CORA','PromptIR','NAFNet'): outputs[m],steps[m]=infer(m,[raw])
    side,gap=170,10; labels=['Clean','Raw','ACO','CORA','PromptIR','NAFNet']; W=24+6*side+5*gap; H=side+100
    c=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(c); f,b=font(16),font(12)
    d.text((W//2,10),f'{task} / {kind} / test frame {idx}',fill='#172033',font=f,anchor='ma')
    for j,label in enumerate(labels):
        x=12+j*(side+gap); c.paste(Image.fromarray(outputs[label][0]).resize((side,side),Image.Resampling.NEAREST),(x,34)); d.text((x+side//2,34+side+10),label,fill='#25344d',font=b,anchor='ma')
    return c

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,default=42); ap.add_argument('--task',default=TASK); ap.add_argument('--kind',choices=KINDS); a=ap.parse_args(); OUT.mkdir(parents=True,exist_ok=True)
    kinds=[a.kind] if a.kind else KINDS; meta={'task':a.task,'index':a.index,'models':{}}
    for kind in kinds:
        c=render(a.task,kind,a.index); p=OUT/f'ACO_CORA_PromptIR_NAFNet_Raw_{a.task}_{kind}.png'; c.save(p); meta['models'][kind]=str(p)
    (OUT/'metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf8')

if __name__=='__main__': main()
