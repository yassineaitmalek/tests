a=float(input('entrer Ux : '))
b=float(input('entrer Uy : '))
x=float(input('entrer Vx : '))
y=float(input('entrer Vy : '))
det=(a*y)-(b*x)
if det==0 :
    print('les deux vecteurs sont colineaires ')
else :
    print('les deux vecteurs ne sont pas colineaires ')
p=input()    