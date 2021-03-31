n=int(input('entrer le nombre de lignes : '))
m=int(input('entrer le nombre de colonnes : '))
T=[m*[0] for k in range (n)]
L=[n*[0] for k in range (m)]
R=[n*[0] for k in range (n)]
for i in range (n) :
    for j in range (m) :
        T[i][j]=int(input('T[%d][%d]='%(i+1,j+1)))
        L[j][i]=int(input('L[%d][%d]='%(j+1,i+1)))
for i in range (n) :
    for j in range (m) :
        for k in range (n) :
            R[i][j]=T[i][k]*L[k][j]
            
print(R)
input()