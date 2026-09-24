import argparse
from common import read_config,bind
p=argparse.ArgumentParser();p.add_argument('--task',required=True);p.add_argument('--kind',required=True);a=p.parse_args()
c=read_config('config.json');assert c['seed']==1 and a.task in c['tasks'];bind(c)
from control import evaluate
evaluate(c,a.task,a.kind)
