# A Python program to demonstrate working of string template
from string import Template

# List Student stores the name and marks of three students
Student = [('Ram', 90), ('Ankit', 78), ('Bob',89 )]
# We are creating a basic structure to print the name and
# marks of the students.
t = Template('Hi $name, you have got $marks marks')
for i in Student:
     print (t.safe_substitute(name=i[0], marks=i[1]))


def power(a, b):
    """Returns arg1 raised to power arg2."""

    return a ** b


print power.__doc__


tup = ('geek',)
n = 5  #Number of time loop runs
for i in range(int(n)):
    tup = (tup,)
    print(tup)