import argparse
import json
import time
from pathlib import Path
import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from adapters import build, forward
from dreamer_bridge import DEGRADATIONS
from visual_degradations import get_degradation


class Pairs(Dataset):
    def __init__(self, root, split, augment=False):
        self.augment = augment
        files = sorted(Path(root).glob(f'*/{split}.npz'))
        assert len(files) == 3, files
        data = [np.load(f) for f in files]
        self.images = np.concatenate([d['image'] for d in data])
        self.masks = np.concatenate([d['mask'] for d in data])
        self.split_seed = dict(train=700000, val=800000, test=900000)[split]

    def __len__(self):
        return len(self.images) * len(DEGRADATIONS)

    def __getitem__(self, idx):
        frame, deg = divmod(int(idx), len(DEGRADATIONS))
        seed = int(np.random.randint(2**31 - 1)) if self.augment else self.split_seed + idx
        rng = np.random.RandomState(seed)
        name, intensity = DEGRADATIONS[deg]
        transform = get_degradation(name, intensity=intensity * rng.uniform(.9, 1.1), seed=seed)
        clean = self.images[frame]
        corrupted = transform(clean)
        convert = lambda x: torch.from_numpy(np.ascontiguousarray(x)).permute(2, 0, 1).float() / 127.5 - 1
        x, gt, mask = convert(corrupted), convert(clean), torch.from_numpy(self.masks[frame].astype(np.int64))
        if self.augment and rng.uniform() < .5:
            x, gt, mask = x.flip(-1), gt.flip(-1), mask.flip(-1)
        return x, gt, mask


def losses(pred, clean, mask):
    target_fg = (clean + 1) * mask[:, None] - 1
    rgb = F.l1_loss(pred['restored_rgb'], clean)
    seg = F.cross_entropy(pred['mask_logits'], mask)
    fg = F.l1_loss(pred['agent_only_rgb'], target_fg)
    return rgb + seg + fg, dict(rgb=float(rgb.detach()), seg=float(seg.detach()), fg=float(fg.detach()))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--data', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--model', choices=['aco', 'smfa'], required=True)
    p.add_argument('--steps', type=int, default=10000)
    p.add_argument('--batch', type=int, default=8)
    p.add_argument('--accum', type=int, default=8)
    p.add_argument('--device', default='cuda')
    p.add_argument('--workers', type=int, default=4)
    args = p.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(4)
    torch.manual_seed(0)
    np.random.seed(0)
    model = build(args.model).to(args.device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4, weight_decay=1e-4)
    scaler = torch.amp.GradScaler('cuda', enabled=args.device.startswith('cuda'))
    generator = torch.Generator().manual_seed(0)
    loader = DataLoader(Pairs(args.data, 'train', True), batch_size=args.batch, shuffle=True,
                        num_workers=args.workers, generator=generator, drop_last=True)
    iterator = iter(loader)
    start_step = 0
    path = args.output / 'last.pt'
    if path.exists():
        state = torch.load(path, map_location='cpu', weights_only=False)
        assert state['name'] == args.model
        model.load_state_dict(state['model'])
        optimizer.load_state_dict(state['optimizer'])
        scaler.load_state_dict(state['scaler'])
        start_step = state['step']
        # Resume is step-safe but not bitwise exact with prefetched augmented batches.
    begin = time.perf_counter()
    model.train()
    for step in range(start_step + 1, args.steps + 1):
        optimizer.zero_grad(set_to_none=True)
        total = 0.
        for _ in range(args.accum):
            try:
                batch = next(iterator)
            except StopIteration:
                iterator = iter(loader)
                batch = next(iterator)
            x, gt, mask = [v.to(args.device) for v in batch]
            with torch.autocast(device_type='cuda', enabled=args.device.startswith('cuda')):
                pred = forward(model, x, args.model, training=True)
                loss, values = losses(pred, gt, mask)
            assert torch.isfinite(loss), (step, values)
            scaler.scale(loss / args.accum).backward()
            total += float(loss.detach()) / args.accum
        scaler.step(optimizer)
        scaler.update()
        if step % 50 == 0 or step == 1:
            row = dict(step=step, loss=total, **values, elapsed=time.perf_counter()-begin)
            print(json.dumps(row), flush=True)
            with (args.output / 'train.jsonl').open('a') as f:
                f.write(json.dumps(row) + '\n')
        if step % 500 == 0 or step == args.steps:
            state = dict(name=args.model, model=model.state_dict(), optimizer=optimizer.state_dict(),
                         scaler=scaler.state_dict(), step=step, config=vars(args),
                         params=sum(p.numel() for p in model.parameters()))
            temp = path.with_suffix('.tmp')
            torch.save(state, temp)
            temp.replace(path)
    print('TRAIN_COMPLETE', args.model, args.steps, flush=True)


if __name__ == '__main__':
    main()
