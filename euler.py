
import matplotlib.pyplot as plt
import math as m
import scipy.integrate as si


def euler(f,a,b,y0,n):
    h=(b-a)/n
    y=y0
    x=a
    X=[a]
    Y=[y0]
    for i in range(n):
        y=y+h*f(y,x)
        x=x+ih
        Y.append(y)
        X.append(x)
    return X,Y
    

r,c=1000,10**(-9)    
f=lambda y,x:-(r*c)**(-1)*y


a,b,n,y0=0,10**(-3),1000,1

X,Y=euler(f,a,b,y0,n)
