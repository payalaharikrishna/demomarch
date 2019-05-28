class Father:
    def height(self):
        print('height is 6.6')

class Mother:
    def color(self):
        print('color white')

class Son(Father,Mother):
    pass

s=Son()
print('execute propertys')
s.height()
s.color()
