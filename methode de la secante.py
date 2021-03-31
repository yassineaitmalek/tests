f=lambda x: x**(3)+4*x**(2)+10


a=float(input("entrer la 1er estimation : "))
b=float(input("entrer la 2eme estimation : "))
e=float(input("entrer la precision : "))
nmax=int(input("entrer le nombre d'iterations : "))

q0=f(a)
q1=f(b)
i=0
while i<nmax :
    y=b-q1*((b-a)/(q1-q0))
    if abs(y-b)<e:
        print("la racine est %f : ",y)
        break
    else :
        a=b
        q0=q1
        b=y
        q1=f(y)
    i+=1
if(i==nmax):
    print("la pas de racine ")    