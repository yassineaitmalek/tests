n=int(input('entrer le nombre de lignes/colonnes : '))
u=[n*[0] for k in range (n)]
for i in range (n) :
    u[i][i]=1
print(u)
input()