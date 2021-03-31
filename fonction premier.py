def premier(p) :
    if p==0 or p==1 :
        return(False)
    elif p%2==0 :
        return(True)
    else :
        k=True
        d=int((p**0.5)+1)+1
        for i in range(3,d+1,2) :
            if p%i==0 :
                k=False
                break
                
                
                
p=int(input("donner un nombre : "))
if premier(p) :
    print("le nombre n'est pas premier")
else :
    print("le nombre est  premier ")

                
        
    