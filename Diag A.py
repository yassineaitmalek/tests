import numpy as np

def diag(A):
    Z=np.matrix(A)
    if len(Z)==1:
        B=np.eye(len(A))
        for i in range(len(A)):
            B[i,i]=A[i]
    else :
        B=[]
        for i in range(len(Z)):
            B+=[A[i,i]]
    return print(B)