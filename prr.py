def lisnbrzero(l) :
    n=len(l)
    k=n*[0]
    c=1
    for i in range (n) :
            if l[i]==1 :
                k[i]=0
            
            else:
                for j in range (i,n) :
                    while l[j]==0 and l[j+1]!=1  :
                        c+=1
                k[i]=c 
                c=1
                        
               
    return(print(k))    

    
    
l=[0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1]
lisnbrzero(l)    
