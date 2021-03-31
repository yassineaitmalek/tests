class eleve :
    def __init__(self,m,n,p,s,t):
        self.matricule=m
        self.nom=n
        self.prenom=p
        self.sport_prefere=s
        self.note=t


f= open("eleve.txt","a+")
f.close()


def addeleve(m,n,p,s,t):
    f= open("eleve.txt","r")
    e=eleve(m,n,p,s,t)
    data = f.readlines()
    a=True 
    for d in data :
        
        d=d.split('\t')
        
        if e.matricule==d[0] :
             a=False
    f.close()
    f= open("eleve.txt","a+")
    if a==True  :
        f.write(e.matricule+"\t"+e.nom+"\t"+e.prenom+"\t"+e.sport_prefere+"\t"+str(e.note)+"\n")
        print("eleve ajoute")
    else :
        print("existe deja")
    f.close()

def moynote() :
    f=open("eleve.txt","r")
    s=0
    i=0
    data = f.readlines() 
    for d in data :
        d=d.split('\t')      
        s+=float(d[4])
        i+=1
    
    f.close()
    return(s/i)
    
def chg(mat,index,tobereplaced):
    
    f= open("eleve.txt","r")
    data=f.readlines()
    f.close()
    f=open("eleve.txt","w")
    for d in data :
        d=d.split('\t')
       
        if d[0]==mat :
            d[index]=str(tobereplaced)
            if index== 4: f.write(d[0]+"\t"+d[1]+"\t"+d[2]+"\t"+d[3]+"\t"+d[4]+'\n')
            else :f.write(d[0]+"\t"+d[1]+"\t"+d[2]+"\t"+d[3]+"\t"+d[4])
           
        if d[0]!=mat: f.write(d[0]+"\t"+d[1]+"\t"+d[2]+"\t"+d[3]+"\t"+d[4])
    
    f.close()
    print("change avec succes") 

def similar(index,sim):
    f=open("eleve.txt","r")
    data=f.readlines()
    f.close()
    i=0
    for d in data :
        d=d.split('\t')
        if d[index]==sim :
            print(d[1]+'\t'+d[2])
            i+=1


    return i

def max_min():
    f=open("eleve.txt","r")
    data=f.readlines()
    f.close()
   
    m=[]
    for d in data :
        d=d.split('\t')
        m+=[float(d[4])]
    i=m[0]
    j=m[0]
    for k in range(0,len(m)):
        if m[k]<i : i=m[k]
        if m[k]>j : j=m[k]
    print("min = "+str(i)+"  max = "+str(j))
    m=[i,j]
    return m 







addeleve("d125","ait malek","yassine","football",17)
addeleve("d1335","ali","mohammed","gaming",17)
chg("d125",4,18)
chg("d125",3,"gaming")
k=similar(3,"gaming")
m=max_min()


