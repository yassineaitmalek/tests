a=float(input("entrer la borne inf : "))
b=float(input("entrer la borne sup : "))
e=float(input("entrer la precision : "))

A=a
B=b
f=lambda x: x**(2)+5*x+8
m=1
while abs(B-A)>e :
    
    h=(B-A)/10
    i=1
    x1=A
    c=f(x1)
    x2=x1+h
    d=f(x2)
    while d*c>0 or i<10 :
        c=d
        x1+=h
        x2+=h
        c=f(x1)
        d=f(x2)
        i+=1
    if (i==10):
        m=0
        break
    else :
            B=x2
            A=x1

if m==0 :
    print("pas de racines")
else :
    print("l racine est dans l'intervalle [ %f ; %f ]",A,B)