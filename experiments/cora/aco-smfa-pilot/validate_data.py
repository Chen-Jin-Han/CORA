"""Check generated split integrity before interpreting adapter metrics."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

p = argparse.ArgumentParser()
p.add_argument('--root', type=Path, required=True)
p.add_argument('--tasks', nargs='+', default=['walker_walk','walker_run','finger_turn_hard'])
p.add_argument('--output', type=Path, required=True)
args = p.parse_args()
reports = []
for task in args.tasks:
    seeds, hashes, splits = {}, {}, {}
    for split, count in [('train',2000),('val',300),('test',500)]:
        with np.load(args.root/task/f'{split}.npz') as data:
            images, masks = data['image'], data['mask']
            assert images.shape == (count,64,64,3) and images.dtype == np.uint8
            assert masks.shape == (count,64,64) and np.isin(masks,[0,1]).all()
            assert all(len(data[k]) == count for k in ['episode_seed','frame','source'])
            keys = list(zip(data['episode_seed'].tolist(),data['frame'].tolist()))
            assert len(set(keys)) == count, (task,split,'duplicate state identifiers')
            seeds[split] = set(data['episode_seed'].tolist())
            hashes[split] = set(hashlib.sha256(x.tobytes()).hexdigest() for x in images)
            assert not seeds[split].intersection(range(40000,40010)), 'Control seed overlap'
            sources, counts = np.unique(data['source'], return_counts=True)
            splits[split] = dict(frames=count, episodes=len(seeds[split]),
                sources=dict(zip(sources.tolist(),counts.tolist())),
                empty_masks=int((masks.sum((1,2)) == 0).sum()))
    overlap = {}
    for a,b in [('train','val'),('train','test'),('val','test')]:
        assert not seeds[a] & seeds[b], (task,a,b,'trajectory overlap')
        overlap[a+'_'+b] = len(hashes[a] & hashes[b])
    # Identical RGB can occur at distinct simulation states; report separately.
    reports.append(dict(task=task,splits=splits,trajectory_overlap=False,
                        cross_split_identical_images=overlap))
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(reports,indent=2))
print(json.dumps(reports),flush=True)
