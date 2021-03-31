import numpy as np
import matplotlib.pyplot as plt
import math as m


n=10000
O=np.linspace(0,2*np.pi,n)
e=float(input("entrer e : "))
p=float(input("entrer p : "))
l=float(input('entrer la phase : '))
r=lambda x:p/(1+e*(m.cos(x+l)))
f=np.vectorize(r)
R=f(O)
X=R*np.cos(O)
Y=R*np.sin(O)
plt.plot(X,Y)
plt.axis("equal")
plt.grid()
plt.polar(R,O)
plt.show()
plt.savefig("courbe 6")