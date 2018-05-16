def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        print "inside function call value of a",a
        a, b = b, a + b

x=fib(8)

print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
#print(x.next())


#using for loop
print("\nUsing for in loop")
for i in fib(5):
    print(i)

