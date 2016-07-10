# Car Salesman Program
# Write a Car Salesman program where the user enters the base price of a car. The program should add on a bunch of extra fees such as tax, license, dealer prep, and destination charge. Make tax and license a percent of the base price. The other fees should be set values. Display the actual price of the car once all the extras are applied.
# Jay 2016-07-07 21:48:12

#Program Welcome

print("Welcome to the Snakes Autodealer, where all car salesman are Snakes!")

print("\nThis program allows you to quickly work out the total price of your new victim's (customer's) brand new (Cat D write-off) car")

# Setting the base price of the car (what the user sees on the price sticker)

base_price = int(input("\nWhat is the base price of the car? £"))

# Setting the 'addons'

tax = base_price * 0.15
license = base_price * 0.1
dealer_prep = 200
delivery = 100

# Setting final prices and bonus

price = float(base_price + license + tax + dealer_prep + delivery)
bonus = price * 0.05
total_price = bonus + price

# Viewing the breakdown in price

print("\n\tTax = £", tax)
print("\n\tLicense = £", license)
print("\n\tDealer Preparation Fees = £", dealer_prep)
print("\n\tDelivery charges (mandatory) = £", tax)

print("\nThe price is £ ", price)
print("\nYour bonus is £", bonus)



print("\nThe total price for the customer to pay is £", total_price)

input("\nPress the enter key to exit")
