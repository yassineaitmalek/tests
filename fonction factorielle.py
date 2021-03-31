def fact(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return(print(s))
    
    
n=int(input("entrer un nombre : "))
fact(n)