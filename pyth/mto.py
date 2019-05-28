class Myclass:
    def method(self,*a):
        s=0
        for i in range(len(a)):
            s+=a[i]
            print('sum=', s)


m=Myclass()
m.method(3,2)
m.method(7,9,90)
        
