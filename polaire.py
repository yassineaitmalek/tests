import numpy as np
import matplotlib.pyplot as plt



theta=np.linspace(0,2*np.pi,100)
R=1+np.cos(theta)
X=R*np.cos(theta)
Y=R*np.sin(theta)
plt.axis("equal")
plt.plot(X,Y)
plt.polar(theta,R)
plt.show()
