from abc import ABC , abstractmethod
class Pawan(ABC):
    def display(self):
        print('this is concrete method')
    @abstractmethod
    def cal(self,a):
        pass
class Suresh(Pawan):
    def cal(self,a):
        print('square=',a*a)

class Hari(Pawan):
    def cal(self,a):
        print('cube=',a*3)
h=Hari()
h.cal(8)
s=Suresh()
s.cal(8)
