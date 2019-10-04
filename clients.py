import argparse
import os
import logging
import time
from joblib import Parallel,delayed

comm_fee = 1.25

class person(object):
    """
    this class implements a data structure for a person details

    a person details includes the person id, age and gender
    """

    def __init__(self,p_id,age,gender):
        self.id = p_id
        self.age = age
        self.gender = gender
    def print_details(self):
        print('id={}, age={}, and gender={}.'.format(self.id,self.age,self.gender))


class client(person):
    """
    this class implements a data structure for a client details

    a client details includes all the person details (id, age and gender) and also client id and balance
    """
    def __init__(self,path):
        stem = path.split('.')[0]
        p_id = int(stem)
        age = int(stem[1:3])
        gender = 'male' if int(stem[-1])%2==1 else 'female'
        super().__init__(p_id,age,gender)
        self.client_id = self.id
        self.__balance = 0
        self.__commission = 0
        self.calc_transaction_data(path)

    def transaction(self,amount):
        self.__balance += amount

    def get_balance_without_comm_fee(self):
        return self.__balance

    def get_balance_after_comm_fee(self):
        return self.__balance - self.__commission

    def calc_transaction_data(self,filename):
        f = open('practice1/'+filename,'rt')
        for i, l in enumerate(f):
            if i > 0:
                self.__balance += (int(l.split(',')[1].split('\n')[0]))
                self.__commission += comm_fee


if __name__=='__main__':
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
    parser.add_argument('--path',default='',type=str)

    args = parser.parse_args()
    path = args.path
    filelist = os.listdir(os.path.join(path, 'practice1'))

    logger.debug('start comparison between serial and parallel processing of clients')
    filelist = [x for x in filelist if '.csv' in x]
    # this is just a way to simulate a large number of clients
    # remember that parallel processing has some overheads
    # so using it for small size data may be even slower than serial processing
    filelist = filelist*100

    # create clients object-list in a sequential way
    start = time.time()
    logger.debug('creating clients serially')
    clients = [client(f) for f in filelist]
    print({c.client_id:(c.get_balance_without_comm_fee(),c.get_balance_after_comm_fee()) for c in clients})
    print('processing time running serially is: {0:.2f}'.format(time.time()-start))
    logger.debug('done serial processing of clients')

    # delete the existing clients object-list and recreate it in a parallel way
    del clients
    start = time.time()
    logger.debug('creating clients in parallel')
    clients = Parallel(n_jobs=12)(delayed(client)(f) for f in filelist)
    print({c.client_id: (c.get_balance_without_comm_fee(), c.get_balance_after_comm_fee()) for c in clients})
    print('processing time running parallel is: {0:.2f} seconds'.format(time.time()-start))
    logger.debug('done parallel processing of clients')

    logger.debug('done!')
    # c1 = client(filelist[0])
    # c1.print_details()

