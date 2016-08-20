# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
# Jay 2016-07-12 22:48

import random
import sys

print("\tWelcome To 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# Set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop

while tries < 5:
    if guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")
    else:
        print("You guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!\n")
        input("\n\nPress the enter key to exit.")
        sys.exit()



    guess = int(input("Take a guess: "))
    tries  += 1

# guessing the right number
print("You dumbfuck who can't even guess a number in 5 tries, the number was", the_number)
input("\n\nPress the enter key to exit.")








# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
# Jay 2016-07-12 22:48

import random
import sys

print("\tWelcome To 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# Set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop

while tries < 5:
    if guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")
    else:
        print("You guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!\n")
        input("\n\nPress the enter key to exit.")
        sys.exit()



    guess = int(input("Take a guess: "))
    tries  += 1

# guessing the right number
print("You dumbfuck who can't even guess a number in 5 tries, the number was", the_number)
input("\n\nPress the enter key to exit.")
