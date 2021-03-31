import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,2*np.pi,1000000)
for i in range(2,50) :
    r=1/(i-np.cos(t))
    x=r*np.cos(t)
    y=r*np.sin(t)
    plt.plot(x,y)
    plt.axis('equal')
    plt.grid()
    plt.show()
plt.savefig("courbe 3")
