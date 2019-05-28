class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def talk(self):
        print('hello iam:',self.name)
        print('my age is:',self.age)

p=Person('hari',23)
p.talk()
