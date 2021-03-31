#integrate

def integrate(f,a,b,n):
    s=0
    h=(b-a)/float(n)
    for i in range(1,n):
        c=a+i*h
        s+=f(c)
    return h*((f(a)+f(b))/2+s)
    
    


def df(f,x):
    h=0.0000001
    return (f(x+h)-f(x-h))/(2*h)
    
    
def newton(f,a,b,t,n):
    y=x
    s=0
    while abs(f(y))>t and s<n :
        y=y-(f(y)/df(f,y))
        s+=1
    return y



def dichotomie(f,a,b,t,n):
    m=(b-a)/2
    s=0
    while abs(f(m))>t and s<n :
        if f(a)*f(b)<0 :
            b=m
        else :
            a=m
        m=(b-a)/2
        s+=1
    return  m
    
