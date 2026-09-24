import argparse
from common import read_config,bind

def main():
    p=argparse.ArgumentParser();p.add_argument('stage',choices=['benchmark','generate','audit','baseline','train','images','control','report'])
    p.add_argument('--model',choices=['aco','smfa']);p.add_argument('--task');p.add_argument('--mode',choices=['markov','single','clean']);p.add_argument('--kind');p.add_argument('--condition',choices=['aco','smfa','raw','clean'])
    a=p.parse_args();c=read_config(__import__('os').environ.get('EXPERIMENT_CONFIG','config_seed7.json'));bind(c)
    if a.stage=='audit':
        from data import audit
        audit(c)
    elif a.stage=='baseline':
        from reuse_baseline import reuse
        reuse(c)
    elif a.stage=='benchmark':
        from data import benchmark
        benchmark(c)
    elif a.stage=='generate':
        from data import generate
        generate(c)
    elif a.stage=='train':
        from engine import train
        train(c,a.model,'cuda')
    elif a.stage=='images':
        from engine import image_eval
        image_eval(c,a.model,'cuda')
    elif a.stage=='control':
        from control import evaluate
        assert a.task in c['tasks']
        assert (a.mode=='clean')==(a.condition=='clean')
        assert (a.mode=='single')==(a.kind is not None)
        evaluate(c,a.task,a.condition,a.mode,a.kind)
    else:
        from summarize import summarize
        summarize(c)
if __name__=='__main__':main()
