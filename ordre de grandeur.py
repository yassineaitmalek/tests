x=float(input('entrer un nombre : '))
if x<=0 :
    y=-x
else :
    y=x
if y>1 :
    s=1
    n=0
    while s<=y :
        s=s*10
        n=n+1
    print("l'ordre de grandeur du nombre entrer est : ",n-1)
else :
    s=1
    n=0
    while y<=s :
        s=s/10
        n=n+1
    print("l'ordre de grandeur du nombre entrer est : ",-n)