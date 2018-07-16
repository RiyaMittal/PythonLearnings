#!/usr/bin/python

class MyClass:
   __hiddenVariable=0 # hidden variable created using double underscore '__'

   def add(self,increment):
       self.__hiddenVariable+=increment
       print("value of hidden attribute: ",self.__hiddenVariable)


myObject=MyClass()
myObject.add(21)
myObject.add(1)
#print(myObject.__hiddenVariable) # to check the visibility of hidden variable outside the class : it will throw exception

print(myObject._MyClass__hiddenVariable) # to check the visibility of hidden variable outside the class : it will work out ( thats the trick to use different syntax and access it outside the class also


# PRinting objects

class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __repr__(self):
        print "a= %s and b=%s "%(self.a,self.b)

    def __str__(self):
        print "inside str function: a= %s and b=%s " %(self.a, self.b)


#driver code:

t=Test(100,200)
print(str(t))
print([t])
