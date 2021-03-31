def tri(A,B):
    a=len(A)
    b=len(B)
    FUS=(a+b)*[0.]
    IA=0
    IB=0
    for IFUS in range(a+b):
        if IA<a and IB<b :
            if A[IA]<B[IB]:
                FUS[IFUS]=A[IA]
                IA+=1
            else: 
                FUS[IFUS]=B[IB]
                IB+=1
        elif IA==a:
            FUS[IFUS]=B[IB]
            IB+=1
        else :
            FUS[IFUS]=A[IA]
            IA+=1
    print(FUS)        

l=[5, 6, 45, 87, 545, 547]
s=[0, 1, 2, 56, 232, 5348, 5698, 6546, 23548641]
tri(l,s)