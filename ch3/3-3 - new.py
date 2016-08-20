# Guess My Number - Modified
#
#Modify the Guess My Number game so that the player has a
# limited number of guesses. If the player fails to guess in time,
# the program should display an appropriately chastising
# message.
# Jay 2016-07-31 19:49

import random

print("\tWelcome To 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

turn_limit = int(input("What is the guess limit? "))


# Set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# Set the end game conditions
while tries <= turn_limit and guess != the_number:
    if guess > the_number:
        print("Lower..")
    elif guess < the_number:
        print("Higher..")

    else:
        guess = int(input("Take a guess: "))
        tries += 1

input("\n\nPress any key to exit")
