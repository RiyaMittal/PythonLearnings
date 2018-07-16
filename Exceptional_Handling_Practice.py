#!/usr/bin/Python
"""

def IntInput():
    p=raw_input("Enter an integer number")
    p=int(p)
    print p

try:
    IntInput()
except(ValueError):
    print("Caught the exception:ValueError",ValueError)


try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
finally:
    print("There may or may not have been an exception.")
print("The inverse: ", inverse)

"""

import sys

file_name=raw_input("enter the filename")
text=[]

try:
    fh=open(file_name,'r')
    text=fh.readlines()
    fh.close()
except IOError:
    print("error opening file",file_name)

if text:
    print( text[12])

