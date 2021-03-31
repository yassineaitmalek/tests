a=float(input("entrer l'année : "))
n=int(input('entrer le numero du mois : '))
while n<1 or n>12 :
    n=int(input('entrer le numero du mois : '))
if n==1 :
    print('le nombre de jours de janvier est 31')
elif n==2 :
    if a%4==0 :
        print('le nombre de jours de février est 29')
    else :
        print('le nombre de jours de février est 28')
elif n==3 :
    print('le nombre de jours de mars est 31')
elif n==4 :
    print('le nombre de jours de avril est 30')
elif n==5 :
    print('le nombre de jours de mai est 31')
elif n==6 :
    print('le nombre de jours de juin est 30')
elif n==7 :
    print('le nombre de jours de juillet est 31')
elif n==8 :
    print('le nombre de jours de aout est 31')
elif n==9 :
    print('le nombre de jours de septembre est 30')
elif n==10 :
    print('le nombre de jours de octobre est 31')
elif n==11 :
    print('le nombre de jours de novembre est 30')
else :
    print('le nombre de jours de décembre est 31')