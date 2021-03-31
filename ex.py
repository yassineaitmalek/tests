import scipy.optimize as so
import math as m


f=lambda x:(m.log(x))-x**(-1)
a=1
b=3
t=0.000001
n=100000
print(so.bisect(f,a,b,t,n))