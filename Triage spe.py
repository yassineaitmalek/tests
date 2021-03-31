#methodes de tri

def tribulles(T):
    echange=True
    n=len(T)
    while echange==True :
        echange=False
        for i in range(n):
            if T[i]>T[i+1]:
                T[i],T[i+1]=T[i+1],T[i]
                echange=True
        n=n-1
        
def triselection(T):
    for i in range(len(T)):
        p=i
        for j in range (i+1,len(T)):
            if T[j]<T[i]:
                p=j
        T[i],T[j]=T[j],T[i]
        
def triinsertion(T]:
    for i in range(len(T)):
        x=T[i]
        j=i
        while j>0 and T[j]>T[j-1]:
            T[j]=T[j-1]
            j=j-1
        T[j]=x
        
def trirapide(T):
    x=T[0]
    l1=|]
    l2=[]
    for i in range(len(T)):
        if T[i]<x:
            l1.append(T[i])
        else:
            l2.append(T[i])
    return trirapide(l1)+[x]+trirapide(l2)
    
def fusion(a,b):
    l=[]
    i,j=0,0
    while i<len(a) and b<len(b):
        if a[i]<b[j]:
            l.append(a[i])
            i=i+1
        else:
             l.append(b[j])
             j=j+1

    return l+a[i:]+b[j:]
    
    
def trifus(a):
    if len(a)<=1 :
        return a
    x=len(a)//2
    return fusion(trifus(a[x:]),trifus(a[:x])
    
    