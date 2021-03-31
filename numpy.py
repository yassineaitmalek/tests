import numpy as np
import numpy.linalg as nl
A=[[2,0,0,6,0],[1,-1,0,-1,0],[0,3,0,-6,7],[0,1,-1,0,-1],[0,0,4,0,-7]]
D=[3,0,0,0,6]
if nl.det(A)==0:
    print('Hors programme')
else:
    X=nl.solve(A,D)
    print(X)
