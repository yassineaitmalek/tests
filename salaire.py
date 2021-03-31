z=1
while z==1 :
    a=input('Nom  : ')
    b=float(input('Indice : '))
    while b<80 or b>450 :
        b=float(input("l'indice doit étre compris entre 80 et 450 : "))
    c=float(input('Ancienneté : '))
    d=float(input("Chiffres d'affaires : "))
    k=b*79.6
    if c<3 :
        s=0
    elif 3<c<10 :
        s=k*0.1
    else :
        s=k*0.15
    if d<10000 :
        h=0
    elif 10000<d<20000 :
        h=400
    else :
        h=700
    x=k+s+h
    print('Fixe mensuel : ',k,' DH ','\n')
    print("Prime d'ancienneté : ",s,' DH ','\n')
    print('Prime sur objectif :',h,' DH ','\n')
    print('Salaire global : ',x,' DH ','\n')
    z=float(input('Entrer 1 pour continuer ou 0 pour arréter : '))
    while z!=1 and z!=0 :
        z=float(input('Préciser votre répanse 1 ou 0: '))
p=input()


