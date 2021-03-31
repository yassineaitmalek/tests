def listsuite(n) :
    s=n*[0.]
    s[0]=2
    for i in range (1,n):
        s[i]=1+s[i]+((s[i-1])**0.5)
    return(print(s))
    
n=int(input("entrer un rang : "))
listsuite(n)