import random

min=int(raw_input("Enter the minimum value"))
max=int(raw_input("Enter the maximum value"))

boo='True'
def diceValue():
    a = random.randrange ( min, max )
    return a

while (boo):
    dice_val=diceValue ()
    my_guess=raw_input("enter your guess")
    print "Value guessed is higher than original" if my_guess>dice_val else "value guessed is lower than the original one"
    print "original value", dice_val
    choice = raw_input ( "\tDo you want to roll the dice again?" )
    if choice=='Yes':
        boo=True
    else:
        boo=False

