def inc() :
    global x
    global y
    x=x+1
    y=y+1
    
    
x=float(input("donner x : "))
y=float(input("donner y : "))
print("x = ",x," y = ",y)
inc()
print("x = ",x," y = ",y)
