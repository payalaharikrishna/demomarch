a,b,c = [int(i) for i in input('enter three nos: '). split()]

if  a==b==c:
    print('both are same')

elif a > b :
    print(a ,'is big')
    

elif b>c :
    print(b , 'is big')

else :
    print(c,'is big')
