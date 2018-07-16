# A Python program that uses Bitwise Not or ~ on boolean
a = True
b = False
print a,b
print ~a
print ~b


# A Python program that uses Logical Not or ! on boolean
a = not True
b = not False
print a
print b

#ternary Operator
# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)

# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
print((b, a)[a < b])

# Use Dictionary for selecting an item
print({True: a, False: b}[a < b])

# Python program to demonstrate nested ternary operator
a, b = 55, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
if a > b else "b is greater than a")

# Python program to demonstrate nested ternary operator using if else
a, b = 10, 20

if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")


#'/' and '//' operators

print(3.54/2)# it will divide and give result in floating decimal
fl=3.54//2
print(fl)# it will return the floor value for the floating and integer type and returns the result