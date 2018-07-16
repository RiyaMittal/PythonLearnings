# A Python program to show different ways to create
# Counter
from collections import Counter

# With sequence of items
print Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C'])

# with dictionary
print Counter({'A': 3, 'B': 5, 'C': 2})

# with keyword arguments
print Counter(A=3, B=5, C=2)

#how to update the counter

import collections

coun=collections.Counter()
#before updating
print "just created a counter",coun

coun.update([1,2,3])
#after updating

print "counter updated", coun

c1 = Counter(A=4, B=3, C=10)
print c1
c2 = Counter(A=10, B=3, C=4)
print c2

c1.subtract(c2)
print(c1)

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

# Count distinct elements and print Counter aboject
print(Counter(z))

# Python program to demonstrate accessing of
# Counter elements
from collections import Counter

# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
col_count = Counter(z)
print(col_count)

col = ['blue', 'red', 'yellow', 'green']

# Here green is not in col_count
# so count of green will be zero
for color in col:
    print (color, col_count[color])

cc=Counter(A=1,B=2,C=3,D=0)
print list(cc.elements())

for letter, count in cc.most_common(1):
    print('%s: %d' % (letter, count))
