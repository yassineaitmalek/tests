def lisnbrzero(l,m) :
    n=len(l)
    k=n*[0]
    c=1
    for i in range (n) :
            if l[i]==1 :
                k[i]=0
            elif l[i]==0 and l[i+1]==1 :
                k[i]=1
            
            
            else:
                for j in range (i,n) :
                    if l[j]==0 and l[j+1]==0:
                        c=c+1
                k[i]=c 
                c=1
                        
               
    return(print(k,k[m]))    

    
    
l=[0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]
lisnbrzero(l,5)    
