from threading import *
from time import *
class Produre:
    def __init__(self):
        self.lst=[]
        self.cv=Condition()
    def produre(self):
        self.cv.acquire()
        for i in range(1,11):
            self.lst.append(i)
            sleep(1)
            print('item produced')
        self.cv.notify()
        self.cv.release()

class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consumer(self):
        self.prod.cv.acquire()
        self.prod.cv.wait(timeout=0)
        self.prod.cv.release()
        print(self.prod.lst)

p=Produre()
c=Consumer(p)

t1= Thread(target=p.produre)
t2= Thread(target=c.consumer)

t1.start()
t2.start()
