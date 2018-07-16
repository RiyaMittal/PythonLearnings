# Python code to demonstrate difference between
# Inplace and Normal operators in Immutable Targets

# importing operator to handle operator operations
import operator

# Initializing values
x = 5
y = 6
a = 5
b = 6

# using add() to add the arguments passed
z = operator.add(a, b)

# using iadd() to add the arguments passed
p = operator.iadd(x, y)

# printing the modified value
print ("Value after adding using normal operator : ",z)


# printing the modified value
print ("Value after adding using Inplace operator : ",p)


# printing value of first argument
# value is unchanged
print ("Value of first argument using normal operator : ",a)

# printing value of first argument
# value is unchanged
print ("Value of first argument using Inplace operator : ",x)

# Python code to demonstrate difference between
# Inplace and Normal operators in mutable Targets

# importing operator to handle operator operations
import operator

# Initializing list
a = [1, 2, 4, 5]

# using add() to add the arguments passed
z = operator.add(a, [1, 2, 3])

# printing the modified value
print ("Value after adding using normal operator : ", z)

# printing value of first argument
# value is unchanged
print ("Value of first argument using normal operator : ", a)

# using iadd() to add the arguments passed
# performs a+=[1, 2, 3]
p = operator.iadd(a, [1, 2, 3])

# printing the modified value
print ("Value after adding using Inplace operator : ",p)

# printing value of first argument
# value is changed
print ("Value of first argument using Inplace operator : ",a)

# initializing values
y = "geeks"

z = "forgeeks"

# using iconcat() to concat the sequences
y = operator.iconcat(y, z)

# using iconcat() to concat sequences
print ("The string after concatenation is : ")
print(y)

r = operator.imul(2, 3);
print r

# Python code to demonstrate the working of
# itruediv() and imod()

# using itruediv() to divide and assign value
x = operator.itruediv(10, 5);

# printing the modified value
print ("The value after dividing and assigning : ")
print (x)

# using imod() to modulus and assign value
x = operator.imod(10, 6);

# printing the modified value
print ("The value after modulus and assigning : ")
print (x)

# Python code to demonstrate the working of
# ilshift() and irshift()

# importing operator to handle operator operations
import operator

# using ilshift() to bitwise left shift and assign value
x = operator.ilshift(8, 2);

# printing the modified value
print ("The value after bitwise left shift and assigning : ")
print (x)

# using irshift() to bitwise right shift and assign value
x = operator.irshift(8, 2);

# printing the modified value
print ("The value after bitwise right shift and assigning : ")
print (x)

# Python code to demonstrate the working of
# ilshift() and irshift()

# importing operator to handle operator operations
import operator

# using ilshift() to bitwise left shift and assign value
x = operator.ilshift(8, 2);

# printing the modified value
print ("The value after bitwise left shift and assigning : ")
print (x)

# using irshift() to bitwise right shift and assign value
x = operator.irshift(8, 2);

# printing the modified value
print ("The value after bitwise right shift and assigning : ")
print (x)

# Python code to demonstrate working of
# lt(), le() and eq()

# importing operator module
import operator

# Initializing variables
a = 3

b = 3

# using lt() to check if a is less than b
if (operator.lt(a, b)):
    print ("3 is less than 3")
else:
    print ("3 is not less than 3")

# using le() to check if a is less than or equal to b
if (operator.le(a, b)):
    print ("3 is less than or equal to 3")
else:
    print ("3 is not less than or equal to 3")

# using eq() to check if a is equal to b
if (operator.eq(a, b)):
    print ("3 is equal to 3")
else:
    print ("3 is not equal to 3")