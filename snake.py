import random 


convto20i=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
convto20j=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    


def border():
    b=[]
    for j in range(22):
        l=[]
        for i in range(22):
            l=l+['#']
        b=b+[l]
    
    for i in range(20) :
        for j in range(20):
            b[convto20i[i]][convto20j[j]]='-'
            
    return b
    
l=[]
 
def head(b,l):
    x=10
    y=10
    b[convto20i[x]][convto20j[y]]='O'
    
    
def fruit(b) :
    a=random.randint(0,19)
    b=random.randint(0,19)
    while a==l[
    b[convto20i[a]][convto20j[b]]='f'
    
    
    





    
    

def draw(b) :

    print("\n\t\tthis is a board\n")
    for i in range(22):
        for j in range(22):
            print(b[i][j], end='\t')
        print("\n")

headx=9
heady=9
fruitx=15
fruity=15


def play():
    placex=0
    placey=0
    m=0
    while m=0:
        for i in range (20):
            for j in range(20):
                if i=headx and j=heady :
                    b[convto20i[i]][convto20j[j]]='o'
                    placex=i
                    placey=j
                    
                if i=fruitx and j=fruity :
                    b[convto20i[i]][convto20j[j]]='f'
                    
                            
        k=str(int(input("avancer "))
        if k="z":
            headx+=1
                    
        if k="s" :
            headx-=1
                    
        if k="d":
            heady+=1
                    
        if k="q":
            heady-=1
        if fruitx==headx and fruity==heady:
            b[convto20i[headx]][convto20j[heady]]='o'
                        
                        
                        
            
    
    
    
draw(border())

            