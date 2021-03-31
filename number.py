import random 


def numbergen(k):
    l=[]
    for i in range(0,k) :
        x='+336'
        n=0
        while n<=7 :
            y = random.randint(0,9)
            x=x+str(y)
            n+=1
        l.append(x)
    return l
        
        
k=int(input('entrer un nombre : '))
f=open("numbergen.vcf",'w')
l=numbergen(k)
for i in range(k) :
    f.write('BEGIN:VCARD'+'\n'+'VERSION:2.1'+'\n'+'N:;'+str(i)+';;;'+'\n'+'FN:'+str(i)+'\n'+'TEL;CELL:'+l[i]+'\n'+'END:VCARD'+'\n')
f.close()
    
    
