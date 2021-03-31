import scipy.optimize as so
import math as m

def df(f,x):
    h=0.0001
    return((f(x+h)-f(x-h))/(2*h))
    
    
def Newton(f,g,x,t,N):
    y=x
    n=0
    while abs(f(y))>t and n<=N :
        y=y-(f(y)/g(y))
        n+=1
    return print(y)
    
    
def secante(f,x,b,t,n):
    y=x
    s=0
    while abs(f(y))>t and s<n :
        y=y-((y-b)/(f(y)-f(b)))*f(y)
        s+=1
    return print(y)
    
    
def dicho(f,a,b,t,N) :
    m=(a+b)/2
    n=0
    while abs(f(m))<=t and n<=N :
        if f(a)*f(m)<0 :
            b=m
        else :
            a=m
        m=(a+b)/2
        n+=1
    return print(m)
    

f=lambda x,y=0:m.log(x)-(x**3)+4
x=1
a=1
b=2.5
t=10**(-10)
N=80000000000
b=2
dicho(f,a,b,t,N)
g=lambda x,y=0:(x**(-1))-3*(x**(2))
print(so.bisect(f,a,b,t,N))
print(so.newton(f,x,g))
Newton(f,g,x,t,N)
secante(f,x,b,t,N)
