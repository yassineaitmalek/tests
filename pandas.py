import pandas as p
import random as r
import numpy as np

head=["name",'age','score']
dt=[["yassine",20,1],["jamal",27,2]]
#dt=["yassine",20,1]
#s=p.Series(data=dt,index=head)

d=p.DataFrame(np.random.randn(3,3),index=head,columns=['c1','c2','c3'])
# print(d)
# print(d[['c1','c3']])
# print(d.loc[['age','score']])
# print(d.loc[['age','score'],['c1']])
#
# p=d.drop('c1',axis=1)
# print (p)
# print(d)
#
# d.drop('c3',axis=1,inplace=True)
# print (d)

# print(d.head(2))

# print(d<0)

d2=d[(d['c2']<0) & (d['c3']>0) ]
print(d2)
