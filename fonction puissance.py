def puissance(n,x) :
    s=1
    for i in range(1,n+1) :
        s=s*x
    return(print(s))
    
    
x=float(input("entrer un nombre : "))
n=int(input("entrer la puissance : "))
puissance(n,x)