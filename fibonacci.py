n=int(input('entrer un rang : '))
a=1
b=1
for k in range(1,n,1) :   
    c=a+b
    a=b
    b=c
print(c)
p=input()
