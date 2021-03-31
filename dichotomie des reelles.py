 #import scipy.optimize as so
import math as m
def dicho(f,a,b,tol,n) :
    m=(a+b)/2
    j=0
    while abs(f(m))>=tol and j<=n :
        if f(a)*f(b)<0 :
            b=m
        else :
            a=m
        m=(a+b)/2
        j+=1
    return print(m)
    
    
def df(x):
    h=0.01
    return((f(x+h)-f(x-h))/(2*h))
    
def newton(f,df,x,tol,n):
    X=x
    j=0
    while abs(f(X))>=tol and j<=n :
        X=X-((f(X))/(df(X)))
        j+=1
    return print(X)    
    
    
    
f=lambda x:m.log(x)-1
h=0.0001
a=1
b=4
tol=0.00001
n=400
dicho(f,a,b,tol,n)
df(0)
newton(f,df(0),0,tol,n)
#y=so.bisect(f,a,b,tol,n)
#print(y)
