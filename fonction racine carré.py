def racinecarre(n) :
    b=1
    c=(1+a)/2
    k=0.0000001
    while c-b>k or b-c>k :
        b=c
        c=(b+(a/b))/2
    print('la racine carré est : ',c)
    
    
a=float(input('entrer un nombre positif : '))
while a<0 :
    a=float(input('entrer un nombre positif : '))
racinecarre(a)