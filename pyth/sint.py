from threading import *
from time import *
class MyThread:
    def Tea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print('boil milk and tea powder...')
        sleep(5)

    def task2(self):
         print('add sugar and boil for ...')
         sleep(3)

    def task3(self):
         print('filter it and serve for ...')

ob=MyThread()

t=Thread(target=ob.Tea)
t.start()
           
