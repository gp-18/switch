# GCD / HCF
# Find the Greatest Common Divisor of two numbers a and b.
#
# Example 1:
# Input: a = 12, b = 18
# Output: 6
#
# Example 2:
# Input: a = 20, b = 28
# Output: 4
#
# Example 3 (Edge Case - One Number is Zero):
# Input: a = 0, b = 15
# Output: 15  # gcd(0, b) = b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

while b != 0:
    a, b = b, a % b

print(a)