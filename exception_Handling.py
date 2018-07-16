#!/usr/bin/python

#Assertion
#def KelvinToFahrenheit(Temperature):
 #   assert (Temperature >= 0),"Colder than absolute zero!"
  #  return ((Temperature-273)*1.8)+32

#print KelvinToFahrenheit(273)
#print int(KelvinToFahrenheit(505.78))
#print KelvinToFahrenheit(-5)

#Exception
try:
 fh = open("testfile1", "w")
 fh.write("This is my test file for exception handling!!")
 print(fh.read()) # it is expected to throw exception
except IOError:
 print "Error: can\'t find file or read data"
else:
 print "Written content in the file successfully"

fh.close()

