class Father:
    def __init__(self):
        self.property=400000

    def display(self):
        print('father property=',self.property)

class Son(Father):
    def __init__(self):
        self.property=30000
    def display(self):
        print('son property=',self.property)
s=Son()
s.display()
