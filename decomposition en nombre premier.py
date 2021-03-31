n=int(input("entrer un nombre : "))
x=int(n**(1/2))
l=[]
for i in range(2,x+1) :
    j=0
    while n%i==0:
        j+=1
        n=n/i
    if j==0 :
        l+=[]
    else :
        l=l+[(i,j)]
print(l)
    