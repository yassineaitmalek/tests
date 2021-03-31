def trisel(s) :
    n=len(s)
    for i in range (0,n-1):
        p=i
        for j in range (i,n-1) :
            if s[j]<s[p] :
                p=j
                s[p],s[i]=s[i],s[p]
    print(s) 
    
    
def triins(s) :
    n=len(s)
    for i in range (0,n-1) :
        e=s[i]
        j=i
        while j>0 and s[j-1]>e :
            s[j]=s[j-1]
            j-=1
            e=s[j]
    print(s)        
       
              
def tribul(s) :
    n=len(s)
    change=True
    while  change :
        change=False
        for i in range (n-1) :
            if s[i]>s[i+1] :
                s[i],s[i+1]=s[i+1],s[i]
                change=True
    print(s)
    
def reclin(s,x) :
    for i in s :
        if x==i :
            return(True)
    return(False)
    
                
s=[0,7,4,9,78]
l=[0,55,9458,-89415,26554,5648,897415]
tribul(l)
triins(l)
trisel(l)  