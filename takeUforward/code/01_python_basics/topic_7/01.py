# Read two numbers and print whether the first is greater, smaller, or equal.

# Example 1:
# Input: a = 10, b = 5
# Output: 10 is greater than 5

# Example 2:
# Input: a = 4, b = 4
# Output: 4 is equal to 4

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

# Convert to int if whole number for clean display
a_val = int(a) if a.is_integer() else a
b_val = int(b) if b.is_integer() else b

if a > b:
    print(f"{a_val} is greater than {b_val}")
elif a < b:
    print(f"{a_val} is smaller than {b_val}")
else:
    print(f"{a_val} is equal to {b_val}")
