x=float(input('entrer un nombre positif : '))
while x<0 :
    x=float(input('entrer un nombre positif : '))
a=1
b=x
c=(a+b)/2
d=(2*a*b)/(a+b)
while c-a>0.00001 and a-c<-0.00001 and d-b>0.00001 and b-d<-0.00001:
    c=(a+b)/2
    d=(2*a*b)/(a+b)
    a=c
    b=d
print(a)