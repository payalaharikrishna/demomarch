class Duck:
    def talk(self):
        print('quack quack!')

class Dog:
    def talk(self):
        print('bow wow!')


class Human:
    def talk(self):
        print('hello iam')

def call_talk(obj):
    obj.talk()

a=Human()
call_talk(a)
d=Duck()
call_talk(d)
s=Dog()
call_talk(s)
