import pandas as pd
import numpy as np
import os

ar=np.arange(1,9)
print ar

row=int(input("enter row number"))
col=int(input("enter column number"))
mat=np.random.normal(1,9,(row,col))
print mat
print np.size(mat)

print mat[0][0]

leng= np.size(mat)
row1,col1= np.shape(mat)  # if row and column are not taken as input then we can extract their values using shape function
print leng, row1,col1

output_ls=[]
for i in range(0,row):
    if (i%2==0):
        mat_l=list(mat[i])
        output_ls.append(mat_l)
    else:
        mat_l_rev = list ( mat[i][::-1] )
        output_ls.append(mat_l_rev)

print output_ls

