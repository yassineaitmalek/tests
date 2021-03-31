import numpy as np
import matplotlib.pyplot as plt
import math as m
import scipy as si


T=np.linspace(0,2*np.pi,1000000)
plt.title("mangekyo")
plt.axis("equal")
for i in range(2,10) :
    plt.subplot(8,7,i)
    f=lambda t:m.cos((i+1)*t)
    g=lambda t:m.sin(i*t)
    F=np.vectorize(f)
    G=np.vectorize(g)
    X=F(T)
    Y=G(T)
    plt.plot(X,Y)
    plt.show()
plt.savefig('courbe 4')