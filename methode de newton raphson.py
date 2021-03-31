
def df(f,x):
    h=0.0001
    return((f(x+h)-f(x-h))/(2*h))
    
def Newton(f,x,t,N):
    y=x
    n=0
    while abs(f(y))>t and n<=N :
        y=y-(f(y)/df(f,y))
        n+=1
    if n<=N:
        return print(y)
    else : 
        return(print("pas de racine"))
    
f=lambda x:m.acosh(x)-1
x=2
t=0.001
N=500
Newton(f,x,t,N)