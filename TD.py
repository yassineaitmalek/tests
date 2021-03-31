import math

def generateList(n):
    list=n*[0]
    for i in range(0,n):
        list[i]=2*i+1
    return list

def generateList2(n):
    list=n*[0]
    for i in range(0,n):
        list[i]=i
    return list
    
def listSuite(n):
    list=n*[0.]
    list[0]=2
    for i in range(1,n):
        list[i]=1+list[i-1]+math.sqrt(list[i-1])
    return list
    
def number(list):
    length=len(list)
    number=0
    for i in range(0,length):
        number+=list[i]**(length-1-i)
    
def words(string):
    word=1
    for i in range(0,len(string)):
        if string[i]==" " or string[i]=="'":
            word+=1
    return word
    
def listDh(price):
    list=[]
    while price!=0:
        if price-20>=0:
            price=price-20
            list.append(20)
        elif price-2>=0:
            price=price-2
            list.append(2)
        else :
            price=price-1
            list.append(1)
    return list
            
dh=[200,100,50,20,10,5,2,1,0.5,0.2,0.1]
list=[]
def listDh2(price,i=0):
    global list
    if price!=0 and i<=10:
        print(price)
        if price-dh[i]+0.000001<0 :
            i=i+1
            listDh2(price,i)
        else :
            list.append(dh[i])
            listDh2((price-dh[i]),i)
        
    return list
    
