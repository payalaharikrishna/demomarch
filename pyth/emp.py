class Employe:
    
    def __init__(self ,i,n,s,g,add):
        self.idno=i
        self.name=n
        self.salary=s
        self.gen=g
        self.address=add
    #instance metod
    def display(self):
        print('idno= ', self. idno)
        print('name= ', self.name)
        print('salary=', self.salary)
        print('gender= ', self.gen)
        print('adress=', self.address)

e= Employe(112,'hari',50000,'m','gurr' )
e.display()
