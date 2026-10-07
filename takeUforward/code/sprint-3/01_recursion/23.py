# Factorial of N using an accumulator
# Given an integer `n`, compute n! using tail recursion with an accumulator parameter.
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
# Input: n = 4
# Output: 24
#

n = int(input("Enter the value of n : "))

print(f"n is : {n} and now doing the operations on it.")
def factorial_n(n, acc=1):
    if n <= 1:
        return acc
    return factorial_n(n - 1, acc * n)

print(factorial_n(n, 1))
