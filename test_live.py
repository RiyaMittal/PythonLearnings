#!usr/bin/python

mystr='Riya Mittal'
orgstr=list(mystr)
revstr=[]
print(list(mystr))
#print(mystr[::-1])

for i in range(len(list(mystr))):
    index=len((list(mystr)))-i-1
    revstr[index]=orgstr[i]

