# Given three numbers, print the largest without using max().

# Example 1:
# Input: 12, 45, 32
# Output: Largest: 45

# Example 2:
# Input: -5, -2, -10
# Output: Largest: -2

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

largest_val = int(largest) if largest.is_integer() else largest
print(f"Largest: {largest_val}")
