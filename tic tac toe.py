

convto25=[6,7,8,11,12,13,16,17,18]


def border(b):

    for i in range(25):
        b[i]='#'
    
    for i in range(9) :
        b[convto25[i]]='-'


def draw(b) :

    print("\nthis is a board\n")
    for i in range(25):
        if i%5==0 :
            print("\n")
        
        print(b[i], end='\t')
    print("\n")



def entrval():
        c=str(input("player please enter X or O : \n"))
        if c=="x" or c=="X":
            c="X"
        if c=="o" or c=="O":
            c="O"
        while c!="x" and c!="X" and c!="o" and c!="O":
            c=str(input("please retry with  X or O : "))
        return c


def entrpos():
        
        d=int(input("player please enter the position form 1 to 9  : \n"))
        while d<1 or d>9 :
            d=int(input("please enter a valid number between 1 and 9 \n"))
        return d

def win(b):
    gameover=0
    if (b[convto25[0]]==b[convto25[1]] and b[convto25[1]]==b[convto25[2]] and b[convto25[0]]!="-") or (b[convto25[3]]==b[convto25[4]] and b[convto25[4]]==b[convto25[5]] and b[convto25[3]]!="-")or(b[convto25[6]]==b[convto25[7]] and b[convto25[7]]==b[convto25[8]] and b[convto25[6]]!="-")or (b[convto25[0]]==b[convto25[4]] and b[convto25[4]]==b[convto25[8]] and b[convto25[0]]!="-")or(b[convto25[2]]==b[convto25[4]] and b[convto25[4]]==b[convto25[6]] and b[convto25[2]]!="-")or (b[convto25[0]]==b[convto25[3]] and b[convto25[3]]==b[convto25[6]] and b[convto25[0]]!="-")or(b[convto25[1]]==b[convto25[4]] and b[convto25[4]]==b[convto25[7]] and b[convto25[1]]!="-")or (b[convto25[2]]==b[convto25[5]] and b[convto25[5]]==b[convto25[8]] and b[convto25[2]]!="-"): gameover=1
    return gameover

def play(b):
    i=0
    v=[]
    p=[]
    for j in range(9):
        v=v+[0]
        p=p+[0]
    gameover=0
    while gameover!=1 and i<9 :
        v[i]=entrval()
        lastplayer=v[i]
        if i!=0 :
            while lastplayer==v[i-1]:
                print("its not your turn ")
                v[i]=entrval()
            
        p[i]=entrpos()
        if (b[convto25[p[i]-1]]=='-'):
           b[convto25[p[i]-1]]=v[i]
        else :
            while (b[convto25[p[i]-1]]!='-'):
                print("valeur incorrect \n")
                p[i]=entrpos()
        draw(b)
        gameover=win(b)
        if gameover==1:
            print("the winner is : ",lastplayer)
        i=i+1
        if i==8:
            print("it's a draw")
            




b=[]
for i in range(25):
    b=b+[0]
    
border(b)
play(b)

