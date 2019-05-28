from threading import *

def display(x):
    print('hello iam running',x)

t=Thread(target=display,args=(120,))
t.start()
