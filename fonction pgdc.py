def pgdc(m,n) :
    while m!=n :
        if m<n :
            n=n-m
        else :
            m=m-n
    return(print("le pgdc des deux nombres est :",m))
    
    
m=int(input("entrer un nombre : "))
n=int(input("entrer un nombre : "))
pgdc(n,m)
