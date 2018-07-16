# Python program to illustrate the use of args which
# multiplies all the values given to the function as parameter

def multiplyAll(*val):
    mul = 1

    # values(args) will be in the form of tuple
    print val
    print "Type = ", type(val)

    # Multiplying the all the parameters and return the result
    for i in val:
        mul = mul * i

    return mul


ans = multiplyAll(1, 2)
print "The multiplication of 1 and 2 is ", ans

# Multiply 5 numbers using above function
ans = multiplyAll(3, 4, 5, 6, 7)
print "The multiplication of 3 to 7 is ", ans


# Program to illustrate the use of kwargs in Python

# Function that print the details of a student
# The number of details per student may vary
def printDetails(**details):
    # Variable 'details' contains the details in the
    # form of dictionary
    print "Parameter details contains"
    print details
    print "Type = ", type(details)

    # Print first name
    print "First Name = ", details['firstName']

    # Print the department of student
    print "Department = ", details['department']
    print ""  # Extra line break


# Driver program to test above function

# Calling the function with three arguments
printDetails(firstName="Nikhil",
             rollNumber="007",
             department="CSE")

# Calling the function with two arguments
printDetails(firstName="Abhay",
             department="ECE")


# Function containing both args and kwargs
def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]


# Driver program to test above function
cheeseshop("Burger", "It's very funny, sir.",
           "It's really very, VERY funny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")