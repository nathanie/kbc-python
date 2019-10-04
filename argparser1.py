import argparse

""" 
example arguments:
    --base=10 
    --exp=-3
"""

parser = argparse.ArgumentParser(description='get needed program parameters')
parser.add_argument('--base',default=2,type=float)
parser.add_argument('--exp',default=2,type=float)

args = parser.parse_args()
base = args.base
exp = args.exp

print('the result of {} to the power of {} is - {}'.format(base,exp,base**exp))

