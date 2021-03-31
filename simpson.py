#integration

def simpson(f,a,b,n):
    p=(b-a)/n
    m=a+p/2
    sm=f(m)
    sx=0
    for k in range(1,n):
        sm+=f(m+k*p)
        sx+=f(a+kp)
    return (p/6)*(f(a)+f(b)+4*sm+2*sx)
    
