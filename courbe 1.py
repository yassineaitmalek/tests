import numpy as np
import matplotlib.pyplot as plt
import scipy as si
import math as m






f=lambda 
X=np.linspace(1/10,4,1000000)
F=np.vectorize(f)

Y=F(X)

plt.plot(X,Y)
plt.grid()
plt.title("courbe ")
plt.legend()
plt.show()
plt.savefig("courbe 1")
