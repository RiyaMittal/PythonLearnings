a="GeeksforGeeks"
c=b"GeeksforGeeks"
print a,c

d=a.encode('ASCII')
if(d==c):
  print ("encoding successfull")
else: print ("encoding unsuccessfull")

# Python code to demonstate Byte Decoding

# initialising a String
a = 'GeeksforGeeks'

# initialising a byte object
c = b'GeeksforGeeks'

# using decode() to decode the Byte object
# decoded version of c is stored in d
# using ASCII mapping
d = c.decode('ASCII')

# checking if c is converted to String or not
if (d == a):
    print ("Decoding successful")
else:
    print ("Decoding Unsuccessful")