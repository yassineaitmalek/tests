n=int(input('entrer un nombre : '))
k=int(input('entrer la base cible : '))
while k<=0 :
    k=int(input('entrer la base cible : '))
while n!=0 :
    n=int(n/k)
    d=n%k
    print(d) 
print('lire du bas vers le haut ')
p=input()