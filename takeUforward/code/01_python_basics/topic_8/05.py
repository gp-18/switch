# Calculate a ticket price based on age bands, with a separate rule for children and senior citizens; test each boundary.

# Example 1:
# Input: age = 8 (Child < 12: $5)
# Output: Ticket price: $5

# Example 2:
# Input: age = 65 (Senior >= 65: $7, Standard: $10)
# Output: Ticket price: $7

# Age rules:
# Child (< 12): $5
# Standard (12 to 64): $10
# Senior (>= 65): $7

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age!")
elif age < 12:
    print("Ticket price: $5")
elif age < 65:
    print("Ticket price: $10")
else:
    print("Ticket price: $7")
