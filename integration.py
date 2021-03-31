import numpy as np
import math as m
import scipy.integrate as si
import matplotlib.pyplot as plt



def integr(f,a,b,n):
    s=0
    h=(b-a)/float(n)
    for k in range (1,n):
        c=a+h*k
        s+=f(c)
    return(h*(((f(a)+f(b))/2)+s))
    
    
    
f=lambda x:-39 -43*x +39*x**2 -5*x**3
g=lambda x:-4*x-8.95+x**3
F=np.vectorize(f)
G=np.vectorize(g)
a=float(input('entrer la borne inf1: '))
b=float(input('entrer la borne sup1: '))
c=float(input('entrer la borne inf2: '))
d=float(input('entrer la borne sup2: '))
n=1000000
h=(b-a)/n




X1=np.linspace(a,b,n)
X2=np.linspace(c,d,n)
Y=F(X1)
Z=G(X2)


print(integr(f,a,b,n))
print(si.trapz(Y,dx=h))
print(si.quad(f,a,b))

plt.subplot(2,1,1)
plt.plot(X1,Y,color=(1,5,8,10),label='f(x)',linewidth=10)
plt.title('fonction')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=2)
plt.grid()
plt.subplot(2,1,2)
plt.plot(X2,Z,'y',label='g(x)',linewidth=10)
plt.title('fonction')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend(loc=2)
plt.show()


