# GCD of two numbers using recursion
# Given two integers `a` and `b`, compute their Greatest Common Divisor (GCD) using the Euclidean algorithm with recursion.
#
# Example 1:
# Input: a = 48, b = 18
# Output: 6
#
# Example 2:
# Input: a = 7, b = 5
# Output: 1
#
# Example 3 (Edge Case):
# Input: a = 20, b = 0
# Output: 20
#

a = int(input("Enter first number (a) : "))
b = int(input("Enter second number (b) : "))

print(f"Numbers are a = {a}, b = {b} and now doing the operations on them.")
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(a, b))
