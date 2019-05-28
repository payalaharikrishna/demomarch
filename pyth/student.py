
from teacher import Teacher
class Student(Teacher):
    def setmarks(self,mark):
        self.marks=mark
    def getmarks(self):
        return self.marks

s=Student()
s.setid(89)
s.setName('harikrishna')
s.setaddr('tpp-98 gurramkonda chittoor')
s.setmarks(78)
print('id=',s.getid())
print('name=',s.getName())
print('address=',s.getaddr())
print('marks=',s.getmarks())
