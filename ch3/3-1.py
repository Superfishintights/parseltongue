# Fortune Cookie
# Write a program that simulates a fortune cookie. The program
# should display one of five unique fortunes, at random, each
# time it’s run.
# Jay 2016-07-16 16:26

# Setting up the random modules

import random

print("I can sense your future. I can read your fate.")
print("It becomes ever clearer with each passing moment..")

name = input("What is your name? ")

cookie = random.randint(1,5)

if cookie == 1:
    print(name, "You're going to die in a car crash in the next 24 hours.")
elif cookie == 2:
    print(name ,"You will find a winning lottery ticket on the floor outside " \
    "your house, however when you take it to be cashed, it was for the wrong " \
    "week.")
elif cookie == 3:
    print(name, "A child will sneeze on you as you sit on the bus. " \
    "You catch flu.")
elif cookie == 4:
    print(name, "You get laid off after having your name drawn out of a hat " \
    "at work")
elif cookie == 5:
    print("You happen to save a random person's life, and it turns out " \
    "to be the billionaire heiress who falls in love with you. " \
    "You live happily ever after.  The end.")
else:
    print("Illegal cookie value ", name, " you really are unlucky..")

input("\n\nPress the enter key to exit")
