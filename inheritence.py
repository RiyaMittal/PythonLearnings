# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is employee
    def isEmployee(self):
        return False


# Inherited or Sub class (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())


class Base(object):
    pass  # Empty Class


class Derived(Base):
    pass  # Empty Class


# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))

# But d is an instance of Base
print(isinstance(d, Base))


# Python example to show working of multiple
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print "Base1"


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print "Base2"


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print "Derived"

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()


###################################

class Apple(object):

    # Constructor
    def __init__(self, sweetness):
        self.sweetness = sweetness


class AppleJuice(Apple):

    # Constructor
    def __init__(self, sweetness, sour):
        Apple.sweetness = sweetness
        self.sour = sour

    def printsweetnesssour(self):
        # print(self.x, self.y) will also work
        print(Apple.sweetness, self.sour)


# Driver Code
d = AppleJuice(100, 120)
d.printsweetnesssour()


######################33


class Orange(object):

    # Constructor
    def __init__(self, sweetness):
        self.sweetness = sweetness


class OrangeJuice(Apple):

    # Constructor
    def __init__(self, sweetness, sour):
        super(OrangeJuice,self).__init__(sweetness)
        self.sour = sour

    def printsweetnesssour(self):
        # print(self.x, self.y) will also work
        print(self.sweetness, self.sour)


# Driver Code
d = OrangeJuice(100, 120)
d.printsweetnesssour()


###########################


class X(object):
    def __init__(self, a):
        self.num = a

    def doubleup(self):
        self.num *= 2


class Y(X):
    def __init__(self, a):
        X.__init__(self, a)

    def tripleup(self):
        self.num *= 3


obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)

##############################

# Base or Super class
class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
    def __init__(self, name, eid):
        ''' In Python 3.0+, "super().__init__(name)"
            also works'''
        super(Employee, self).__init__(name)
        self.empID = eid

    def isEmployee(self):
        return True

    def getID(self):
        return self.empID


# Driver code
emp = Employee("Geek1", "E101")
print(emp.getName(), emp.isEmployee(), emp.getID())





