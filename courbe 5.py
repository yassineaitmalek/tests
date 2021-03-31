import numpy as np
import matplotlib.pyplot as plt
import math as m


n=10000
f=lambda x:m.log(m.atan(x)+x+1)+m.exp(m.tan(x)-x-1)
F=np.vectorize(f)
a=float(input('entrer la borne inf1: '))
b=float(input('entrer la borne sup1: '))
X=np.linspace(a,b,n)
Y=F(X)
plt.plot(X,Y,label='f(x)')
plt.title("courbe")
plt.xlabel('x')
plt.ylabel("y")
plt.grid()
plt.legend(loc=1)
plt.show()
plt.savefigure('courbe 5')


