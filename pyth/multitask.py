from threading import *
from time import *

class Railway:
    def __init__(self,available):
        self.available=available
        self.l=Semaphore(4)

    def reserve(self,wanted):
        self.l.acquire()
        print('available no.of berths',self.available)
        if(self.available>=wanted):
            name=current_thread().getName()
            print('%d berths allocated for %s' %(wanted,name))
            sleep(1)
            self.available-=wanted

        else:
            print('sorry no berths to allot')
        self.l.release()

obj=Railway(15)

t1=Thread(target=obj.reserve, args=(15,))
t2=Thread(target=obj.reserve, args=(15,))

t1.setName('First Person')
t2.setName('Second person')


t1.start()
t2.start()
