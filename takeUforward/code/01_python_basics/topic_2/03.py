# Read a price as input and convert it to float; print the price plus 18% tax.

# Example 1:
# Input: Enter the price: 100
# Output: The price after adding 18% tax is: 118.0

# Example 2:
# Input: Enter the price: 250
# Output: The price after adding 18% tax is: 295.0

price = float(input("Enter the price: "))
tax = price * 0.18
print(f"The price after adding 18% tax is: {price + tax}")
