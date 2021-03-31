#programme pi
s=0
n=1
while n<(0.0000001)**(-1) :
    s=s+n**(-2)
    n=n+1
print('pi = ',(6*s)**(0.5))