from threading import *
from time import *
from queue import *
class Produre:
    def __init__(self):
        self.q=Queue()
    def produre(self):
        for i in range(1,11):
            print('item produced',i)
        self.q.put(i)
        sleep(1)

class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consumer(self):
        for i in range(1,11):
            print('receiving item',self.prod.q.get(i))

p=Produre()
c=Consumer(p)

t1= Thread(target=p.produre)
t2= Thread(target=c.consumer)

t1.start()
t2.start()
