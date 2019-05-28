class Square:
    def __init__(self,x):
        self.x=x
    def area(self):
        print('area of square=',self.x*self.x)
        
class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def area(self):
        print('rectangle=',self.x*self.y)


r=Rectangle(12,56)
r.area()

s=Square(60)
s.area()
