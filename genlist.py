def genlist(n) :
    s=n*[0]
    for i in range(0,n):
        s[i]=(2*i)+1
    return(print(s))
    
def genlist2(n) :
    s=n*[0]
    for i in range(0,n):
        s[i]=i
    return(s)
    
    
p=int(input())
genlist(p)
genlist2