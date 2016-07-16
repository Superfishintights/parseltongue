# Coin Flipper
# Write a program that flips a coin 100 times and then tells you
# the number of heads and tails.
# Jay 2016-07-16 17:42

# Setting the variables
heads = 1
tales = 2
head_counter = 0
tales_counter = 0

flips = 0

import random

flip_count = input(int("How many times do you want to flip the coin?\n"))

while flips < flip_count:

    toss = random.randint(1, 2)

    if toss == heads:
        head_counter += 1

    elif toss == tales:
        tales_counter += 1

    else:
        print("Your coin landed on its side. The odds of this happening are " \
        "6000:1")

    flips += 1

print("The coin landed on heads,", head_counter, " times")
print("The coin landed on tales,", tales_counter, "times")

input("\n\nPress the enter key to exit..")
