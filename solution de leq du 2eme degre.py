a=float(input('entrer le coef de x^2 : '))
d=float(input('entrer le coef de x : '))
c=float(input('entrer la cte : '))

if a!=0 :
    k=(d*d)-(4*a*c)
    x=(-d+k**0.5)/(2*a)
    y=(-d-k**0.5)/(2*a)
    if k>0 :
        print('les solution de l équation ',x,' et ',y)
    elif k==0 :
        print('les solution de l équation ',x)
    else :
        print('l équation n a pas de solution')
else :
    g=-c/d
    print('la solution de l equation est : ',g)
p=input()


