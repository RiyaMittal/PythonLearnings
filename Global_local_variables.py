#!usr/bin/python

# 1) Basic use of global and local variable
print "basic usage of global and local var"
def f():

  s = "this is local variable"
  print "value of s",s

s="this is global variable"
f()
print s

# 2) scope of global and local variable when doing assignments
print "usage of global and local variable in dffrnt ways"

def f11():
  global s # to use a global variable inside a function where you are doing assignments to it, you need to declare it global first
  print "first print inside func",s
  s="local variable"
  print "secont print inside func",s
  s="local var changes"
  print "third print inside func",s

s="global var"
f11()
print "global var print",s


#3) another example

a = 1

# Uses global because there is no local 'a'
def fi():
  print 'Inside f() : ', a


# Variable 'a' is redefined as a local
def gi():
  a = 2
  print 'Inside g() : ', a


# Uses global keyword to modify global 'a'
def hi():
  global a
  a = 3
  print 'Inside h() : ', a


# Global scope
print 'global : ', a
fi()
print 'global : ', a
gi()
print 'global : ', a
hi()
print 'global : ', a