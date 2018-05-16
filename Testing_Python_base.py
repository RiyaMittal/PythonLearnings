import numpy as np

# Q1:
"""
list_dp=[]

for i in range(2000,3201):
    if (i%7==0)&(i%5<>0):
        list_dp.append(i)

print list_dp

#Q2:

_number=input("Enter the number you wish to calculate factorial of")

facto=1
for i in range(1,_number+1):
    facto=facto*i

print "factorial of %d is %d "%(_number,facto)

#Q3:

dict=dict()
for i in range(1,input("enter the limit")+1):
    dict[i]=i*i
print dict


#Q4:

inputs=[]
inputs=raw_input().split(',')
print inputs

list_v=list(inputs)
tuple_v=tuple(inputs)

print list_v
print tuple_v

x= int(raw_input('enter the number of rows'))
y= int(raw_input('enter the number of columns'))
lists=[]
listt=[]
Matrix = [[0 for y1 in xrange(y)] for x1 in xrange(x)]
for i in range(0,x):
    for j in range(0,y):
        lists.append(i*j)
    Matrix[i].append(lists)

print Matrix


words=raw_input("enter the words").split(',')
print words
new=sorted(words)
print new



class Pizza(object):
    def __init__(self, size):
        self.size = size
    def get_size(self):
        return self.size

p=Pizza(2)
print p.get_size()



class A():
    def __init__(self,name):
        self.name=name

a = A('mary')
b=a
del a
print b.name



class A():
    def __setattribute__(self,name,value):
        if name =='gender':
            self.name = name
            if value in ('male' ,'female'):
                self.value = value


a = A('A','B')
print (a.value)


class A():
    pass

class B():
    pass

a=A()
b=B()
a == b

class A ():
    a = 6


class C ():
    a = 7


class B( A, C ):
    pass
b = B()
print b.a

var1 = lambda var: var * 2
ret = lambda var: var * 3
result = 2
result = var1(result)
result = ret(result)
result = var1(result)
print(result)

print __doc__


foo = [1, 2]
bar = {foo: 3}
foo.append(4)


class Plist(list):

    def __init__(self, l):
        list.__init__(self, l)

    def push(self, item):
        self.append(item)


if __name__ == "__main__":
    x = Plist([3,4])
    x.push(47)
    print(x)
"""



list=[1,1,1,1,1,1,4,1,1,1,3,1,1,1,4,1,1,3,4,4,3]
flag_firsT_ele=False
sum=0

for i in list:
    if(i==3 and flag_firsT_ele==True ):
        flag_firsT_ele=False

    elif( i==4 or flag_firsT_ele==True):
        flag_firsT_ele=True
    else:
        sum=sum+i

print sum
