# Factorial of N
# Given a non-negative integer `n`, compute and return `n!` using recursion.
#
# Example 1:
# Input: n = 5
# Output: 120
#
# Example 2:
# Input: n = 0
# Output: 1
#
# Example 3 (Edge Case):
# Input: n = 1
# Output: 1
#

n = int(input("Enter the value of n : "))

print(f"n is : {n} and now doing the operations on it.")
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(n))
