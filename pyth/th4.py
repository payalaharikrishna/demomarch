from threading import *
class MyThread:
    def display(self,x,y):
        print('hello i am running',x,y)

ob=MyThread()
t=Thread(target=ob.display,args=(10,11.8,))
t.start()
