# Python code to demonstrate working of
# setitem(), delitem() and getitem()

# importing operator module
import operator

# Initializing list
li = [1, 5, 6, 7, 8]

# printing original list
print ("The original list is : ")
for i in range(0, len(li)):
    print (li[i])

print ("\r")

# using setitem() to assign 3 at 4th position
operator.setitem(li, 3, 3)

# printing modified list after setitem()
print ("The modified list after setitem() is : ")
for i in range(0, len(li)):
    print (li[i])

print ("\r")

# using delitem() to delete value at 2nd index
operator.delitem(li, 1)

# printing modified list after delitem()
print ("The modified list after delitem() is : ")
for i in range(0, len(li)):
    print (li[i])

print ("\r")

# using getitem() to access 4th element
print ("The 4th element of list is : ")
print (operator.getitem(li, 3))

# Python code to demonstrate working of
# setitem(), delitem() and getitem()


# Initializing list
li = [1, 5, 6, 7, 8]

# printing original list
print ("The original list is : ")
for i in range(0, len(li)):
    print (li[i])

print ("\r")

# using setitem() to assign 2,3,4 at 2nd,3rd and 4th index
operator.setitem(li, slice(1, 4), [2, 3, 4])

# printing modified list after setitem()
print ("The modified list after setitem() is : ")
for i in range(0, len(li)):
    print (li[i])

print ("\r")

# using delitem() to delete value at 3rd and 4th index
operator.delitem(li, slice(2, 4))

# printing modified list after delitem()
print ("The modified list after delitem() is : ")
for i in range(0, len(li)):
    print (li[i])

print ("\r")

# using getitem() to access 1st and 2nd element
print ("The 1st and 2nd element of list is : ")
print (operator.getitem(li, slice(0, 2)))

# Python code to demonstrate working of
# concat() and contains()


# Initializing string 1
s1 = "geeksfor"

# Initializing string 2
s2 = "geeks"

# using concat() to concatenate two strings
print ("The concatenated string is : ")
print (operator.concat(s1, s2))

# using contains() to check if s1 contains s2
if (operator.contains(s1, s2)):
    print ("geeksfor contains geeks")
else:
    print ("geeksfor does not contain geeks")