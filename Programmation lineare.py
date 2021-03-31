def colone_pivot(l):
    max=l[0]
    j=0
    for i in range(len(l)):
        if l[i]>0 and l[i]>max:
        
            max=l[i]
            j=i
        else : max=0
    a=[j,max]
    return a
    
def lingne_pivot(A,b,a):
    min=b[0]/A[j][a[0]]
    i=0
    for j in range(len(b)):
        if min>(b[j]/A[j][a[0]]) and A[j][a[0]]>0 :
            min=(b[j]/a[1])
            i=j
def pivot(colone_pivot(l),lingne_pivot(A,b,a)):
    pivot=A[lingne_pivot(A,b,a)][colone_pivot(l)[0]]
    return pivot

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

gama=[]
c1=[]

if nature == 'max':
    w=0
    t=0
    base=[]
    cbase
    for i in range(1,m+1):
        if b1[i]=='<':
            l0+=["t"+str(i)]
            for j in range(1,m+1):
                A[j]+=[0]
            A[i]+=[1]  
            t+=1  
            base+=["t"+str(i)]
            cbase+=[0]
        elif b1[i]=='>':
            l0+=["t"+str(i)]+["v"+str(w+1)]
            for j in range(1,m+1):
                A[j]+=[0]+[0]
            A[i]+=[-1]+[1]
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
    
    