import random as rd


n=int(input("entrer la longeur du code : "))
m=int(input("entrer le nombre de code : "))
a='aqwzsxedcrfvtgbyhnuj,ik;ol:pm!^ù$*1234567890./*-+²&é"(-è_çà)=<'
for j in range(m) :
    b=""
    for i in range (n) :
        y = rd.randint(0,61)
        b+=a[y]
    
    print('\n'+b+'\n')

