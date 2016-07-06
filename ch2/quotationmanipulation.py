# Quotation Manipulation
# Demonstrates string methods
# Jay 2016-07-06 19:45:58

# Quote from IBM Chairman, Thomas Watson, in 1943
quote = "I think there is a world market for maybe five computers."


print("Original Quote")
print(quote)

print("\nIn uppercase:")
print(quote.upper())

print("\nIn lowercase:")
print(quote.lower())

print("\nAs a Title:")
print(quote.title())

print("\nWith a minor replacement:")
print(quote.replace("five", "millions of"))

print("\nOriginal quote is still:")
print(quote)

print("\nStripped Text")
print(quote.strip())


input("\n\nPress the enter key to exit.")
