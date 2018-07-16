#!/usr/bin/python

# -*- coding: utf-8 -*-

"""

import os

def rm(filename):
    os.remove(filename)



with open() as x:
    count=0
    for i in x.read():
        if x.isupper():
            count=count+1
    print count



x=raw_input().split(',')
print x

print '/'.join(x)


"""

foo = 100


def hello():
    print("i am from my_module.py")


if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    hello ()