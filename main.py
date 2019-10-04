from clients import *
import argparse
import os
import logging
import time
import pickle
from joblib import Parallel,delayed

comm_fee = 1.25

# this program will compare the runtime for processing ~280k clients data using sequential process
# relatively to using parallel processing

# here we define our logger and make it save the logs to a file
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('debug.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# we also use an argument parser so that we can use the same code for clients data in different directories
parser = argparse.ArgumentParser(description='get needed program parameters')
parser.add_argument('--path', default='', type=str)

args = parser.parse_args()
path = args.path
filelist = os.listdir(os.path.join(path, 'practice1'))

logger.debug('start comparison between serial and parallel processing of clients')
filelist = [x for x in filelist if '.csv' in x]
# this is just a way to simulate a large number of clients
# remember that parallel processing has some overheads
# so using it for small size data may be even slower than serial processing
filelist = filelist  # *100

# create clients object-list in a sequential way
start = time.time()
logger.debug('creating clients serially')
clients = [client(f) for f in filelist]
# print({c.client_id: (c.get_balance_without_comm_fee(), c.get_balance_after_comm_fee()) for c in clients})
print('processing time running serially is: {0:.2f}'.format(time.time() - start))
logger.debug('done serial processing of clients')

# delete the existing clients object-list and recreate it in a parallel way
del clients
start = time.time()
logger.debug('creating clients in parallel')
clients = Parallel(n_jobs=12)(delayed(client)(f) for f in filelist)
# print({c.client_id: (c.get_balance_without_comm_fee(), c.get_balance_after_comm_fee()) for c in clients})
print('processing time running parallel is: {0:.2f} seconds'.format(time.time() - start))
logger.debug('done parallel processing of clients')
f = open('client_list.pickle', 'wb')
pickle.dump(clients, f)
f.close()

logger.debug('done!')
