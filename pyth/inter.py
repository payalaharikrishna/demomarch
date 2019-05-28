from abc import *
class Myinter(ABC):
    @abstractmethod
    def score(self,x):
        pass
class India(Myinter):
    def score(self,x):
        self.x=x
        if self.x>90:
            print('dhoni score is 180 ',self.x)
        elif self.x<80:
            print('kohli',self.x)
        elif self.x==60:
            print('sewag',self.x)

class Enga(Myinter):
    def score(self,x):
         self.x=x
         if self.x>100:
            print('cook score is 180 ')
         elif self.x>80:
            print('root')
         elif self.x>70:
            print('roy')
str=input('enter class name:')
classname=globals()[str]

c=classname()
x=int(input('enter score:'))
c.score(x)
