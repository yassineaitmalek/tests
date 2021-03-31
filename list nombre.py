def nbr(s) :
    n=0
    for i in range(0,len(s)) :
        n+=s[i]*(10**(len(s)-1-i)
    return(n)
    

n=int(input('entrer la longueur de la liste : '))
s=n*[0]
for i in range(0,n) :
    s[i]=int(input('donner un entier compris entre 0-9 :'))
print(nbr(n))