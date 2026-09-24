import argparse,os
from common import read_config,bind
p=argparse.ArgumentParser();p.add_argument('stage',choices=['audit','train','images']);p.add_argument('--model',choices=['safmn','shufflemixer']);a=p.parse_args()
c=read_config(os.environ['EXPERIMENT_CONFIG']);assert a.model is None or a.model==c['model'];bind(c)
if a.stage=='audit':
 from data import audit
 audit(c)
elif a.stage=='train':
 from engine import train
 train(c,a.model,'cuda')
else:
 from engine import image_eval
 image_eval(c,a.model,'cuda')
