import numpy as np
import matplotlib.pyplot as plt

T=np.linspace(0,2*np.pi,1000000)
R=(1+np.sin(T)+np.cos(T))**(-1)
X=R*np.cos(T)
Y=R*np.sin(T)
plt.plot(X,Y)
plt.axis('equal')
plt.polar(T,R)
plt.show()
plt.savefig('courbe 2')