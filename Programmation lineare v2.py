##construction d tableau simplex


nature=str(input('entre la nature du probleme : '))
n=int(input('enter le nombre de variables : '))
m=int(input('entrer le nombre de contraintes : '))

l0=[]
for i in range (1,n+1):
    l0+=['x'+str(i)]
c=[]
for i in range (1,n+1):
    k=float(input('entrer la valeur de x'+str(i)+' dans la fonction objective : '))
    c+=[k]
    
b=[]
for i in range (1,m+1):
    k=float(input('entrer la valeur de la '+str(i)+' valeur du second membre : '))
    b+=[k]

b1=[]
for i in range (1,m+1):
    k=str(input('entrer le signe de la '+str(i)+' valeur du second membre : '))
    b1+=[k] 
    
    
A=[]
for i in range(1;m+1):
    l=[]
    for j in range(1,n+1):
        k=float(input('entrer la valeur de la '+str(j)+' coef de la '+str(i)+'contrainte : '))
        l+=[k]
    A+=[l]



if nature == 'max':
    c1=[]
    gama=[]
    w=0
    t=0
    base=[]
    cbase
    for i in range(1,m+1):
        if b1[i]=='<':
            l0+=["t"+str(i)]
            for j in range(1,m+1):
                if j=i :A[i]+=[1]
                
                else : A[j]+=[0]
              
            t+=1  
            base+=["t"+str(i)]
            cbase+=[0]
        elif b1[i]=='>':
            l0+=["t"+str(i)]+["v"+str(w+1)]
            for j in range(1,m+1):
               if j=i :A[i]+=[-1]+[1]
               else : A[j]+=[0]+[0]
            
            base+=["v"+str(w+1)]
            cbase+=[-1]
            
            t+=1
            w+=1
                    
    for i in l0:
        if i[0]==x or i[0]==t:
            c1+=[0]
        else:
            c1+=[-1]
    for j in range (1,n+t+w+1):
        s=0
        for i in range (1,m+1):
            s=s+A[j][i]*cbase[i]
        gama[j]=c1[j]-s