# Tipper
# Write a Tipper program where the user enters a restaurant bill total. The program should then display two amounts: a 15 percent tip and a 20 percent tip.
# Jay 2016-07-07 20:15:33

print("Welcome to the Snaketastic Tipper Calculator!")

party = int(input("\nFirst of all, how many people are sharing the bill? "))

bill = float(input("\nExcellent, now how much did your bill come to? £"))

tip15 = float(bill * 0.15)

tip20 = float(bill * 0.2)

print("\nAt 15% your tip is £", tip15, "and split between", party, "you would all pay £", tip15 / party)

print("\nAt 20% your tip is £", tip20, "and split between", party, "you would all pay £", tip20 / party)

input("\n\n Press the enter key to exit")
