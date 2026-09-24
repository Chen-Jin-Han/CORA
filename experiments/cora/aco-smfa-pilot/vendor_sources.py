"""Reproduce lightweight local vendor snapshots with provenance hashes."""
from pathlib import Path
import hashlib
import json
root = Path(__file__).resolve().parent
dest = root / 'vendor/aco'
dest.mkdir(exist_ok=True)
sources = {}
for relative in ['aco_moe/moe_unet.py', 'envs/visual_degradations.py']:
    src = root.parent / 'aco-moe-code' / relative
    data = src.read_bytes()
    (dest / src.name).write_bytes(data)
    sources[relative] = hashlib.sha256(data).hexdigest()
source = root.parent / 'aco-moe-code/envs/visual_degraded_control.py'
text = source.read_text(encoding='utf-8')
body = text[text.index('class MarkovTemporalDegradation:'):text.index('class VisualDegradedControl:')]
(dest / 'markov.py').write_text('from typing import List, Dict, Any, Optional\nimport numpy as np\nfrom visual_degradations import get_degradation\n\n' + body, encoding='utf-8')
sources['envs/visual_degraded_control.py'] = hashlib.sha256(source.read_bytes()).hexdigest()
source = root / 'vendor/SMFANet/basicsr/archs/SMFANet_arch.py'
text = source.read_text().replace('from torchvision import ops\n', '').replace('from basicsr.utils.registry import ARCH_REGISTRY\n', '').replace('@ARCH_REGISTRY.register()\n', '')
(root / 'smfa_blocks.py').write_text('# Derived from official SMFANet, see vendor/SMFANet/LICENSE.txt.\n' + text)
sources['SMFANet_arch.py'] = hashlib.sha256(source.read_bytes()).hexdigest()
(root / 'source_manifest.json').write_text(json.dumps(dict(
    dreamerv3_commit='e3f02248693a79dc8b0ebd62c93683888ddaccfe',
    smfanet_commit='a05e0bb554bbbb80cd27d8fd2b78d4228c657170',
    aco='Local modified reproduction, not author checkpoint', sources=sources), indent=2))
