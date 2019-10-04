import argparse

"""
example arguments:
    --num_iterations=3 
    --names="jhon,sara,jeremy" 
    --pred_text="my name is "
"""

parser = argparse.ArgumentParser(description='get needed program parameters')
parser.add_argument('--num_iterations',default=2,type=int)
parser.add_argument('--names',default=2,type=str)
parser.add_argument('--pred_text',default=2,type=str)

args = parser.parse_args()
n_iter = args.num_iterations
name_list = args.names.split(',')
pred_text = args.pred_text

for i in range(n_iter):
    for j in name_list:
        print(pred_text+j)
