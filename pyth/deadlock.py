from threading import *
from time import *

l1=Lock()
l2=Lock()

def bookticket():
    l1.acquire()
    print('bookticket locked train')
    sleep(1)
    print('bookticket wants to lock on components')
    l2.acquire()
    print('bookticket locked compartment')
    l2.release()
    l1.release()
    print('booking ticket is done...')

def cancelticket():
    l1.acquire()
    print('cancelticket locked compartment....')
    sleep(1.5)
    print('cancelticket wants to lock on train')
    l2.acquire()
    print('cancel ticket locked train')
    l1.release()
    l2.release()
    print('cancelticket of ticket is done....')

t1 = Thread(target=bookticket)
t2 = Thread(target=cancelticket)

t1.start()
t2.start()
