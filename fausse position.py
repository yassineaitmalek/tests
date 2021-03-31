import math as m



def fausseposition(f,a,b,tol) :
    m=(-f(a)*(b-a))/(f(b)-f(a))+a
    if f(a)*f(m)<0 :
        c=(a+m)/2
        while abs(f(c))>=tol  :
                if f(a)*f(m)<0 :
                    m=c
                else :
                    a=c
                c=(a+m)/2                            
                    
    elif f(m)*f(b)<0 :
        c=(b+m)/2
        while abs(f(c))>=tol  :
                if f(m)*f(b)<0 :
                    b=c
                else :
                    m=c
                c=(m+b)/2
                
    return c        
    
    

a=1
b=2
tol=10**(-3)
print(fausseposition(f,a,b,tol))
f=lambda x:m.log(x)-x**3+4
X=np.linspace(1/10,4,1000000)
F=np.vectorize(f)
Y=F(X)
plt.plot(X,Y)
plt.grid()
plt.title("courbe ")
plt.legend()
plt.show()


