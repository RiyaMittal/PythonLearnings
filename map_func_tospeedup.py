# Python program to illustrate library functions
# save time while coding with the example of map()
import time

# slower (Without map())
start = time.clock()
s = 'geeks'
U = []
for c in s:
    U.append(c.upper())
print U
elapsed = time.clock()
e1 = elapsed - start
print "Time spent in function is: ", e1

# Faster (Uses builtin function map())
s = 'geeks'
start = time.clock()
U = map(str.upper, s)
print U
elapsed = time.clock()
e2 = elapsed - start
print "Time spent in builtin function is: ", e2

# Python program to illustrate
# importing list-like container with
# fast appends and pops on either end
from collections import deque

s1 = 'geek'

# make a new deque
d = deque(s1)

# add a new entry to the right side
d.append('y')

# add a new entry to the left side
d.appendleft('h')
print d

d.pop()  # return and remove the rightmost item

d.popleft()  # return and remove the lefttmost item

# print list deque in reverse
print list(reversed(d))

# Python program to illustrate
# using keys for sorting
somelist = [1, -3, 6, 11, 5]
somelist.sort()
print somelist

s = 'geeks'
# use sorted() if you don't want to sort in-place:
s = sorted(s)
print s
