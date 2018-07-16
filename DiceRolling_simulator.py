import random

min=int(raw_input("Enter the minimum value"))
max=int(raw_input("Enter the maximum value"))

boo='True'
def diceValue():
    a = random.randrange ( min, max )
    print a

while (boo):
    diceValue ()
    choice = raw_input ( "\tDo you want to roll the dice again?" )
    if choice=='Yes':
        boo=True
    else:
        boo=False

