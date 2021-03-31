f=lambda x: x**(3)+4*x**(2)+10


a=float(input("entrer la borne inf : "))
b=float(input("entrer la borne sup : "))
e=float(input("entrer la precision : "))
nmax=int(input("entrer le nombre d'iterations : "))
N=0
while N <= nmax :
    c = (a + b)/2 
    if f(c) == 0 or ((b-a)/2 < e) :
        print("%f est la racine",c)
        break
    
    N = N + 1 
    if f(a)*f(c) < 0 :
       a = c 
    else :
       b = c
