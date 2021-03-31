n=int(input('entrer un nombre : '))
k=int(input('entrer un nombre : '))
while n!=k :
    if n>k :
        n=n-k
    else :
        k=k-n
print('le pgdc des deux nombres est : ',n)
p=input()