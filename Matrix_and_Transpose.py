#!/usr/bin/python

m=[[2,0],[9,8],[3,5]]

#print the matrix
for row in m:
    print row

#print the transpose
for i in m:
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    print rez
