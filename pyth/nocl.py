class Myclass:
    
    n=0
    
    #constructor
    def __init__(self):
        Myclass.n +=1
        

    @staticmethod
    def noObjects():
        print('noof objects:', Myclass.n)

obj1=Myclass()
obj2=Myclass()
obj3=Myclass()
Myclass.noObjects()

        
