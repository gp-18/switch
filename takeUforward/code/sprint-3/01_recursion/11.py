# Nth Fibonacci number
# Given an integer `n`, return the nth Fibonacci number using recursion (F(0)=0, F(1)=1).
#
# Example 1:
# Input: n = 4
# Output: 3
#
# Example 2:
# Input: n = 0
# Output: 0
#
# Example 3 (Edge Case):
# Input: n = 6
# Output: 8
#

n = int(input("Enter the value of n : "))

print(f"n is : {n} and now doing the operations on it.")
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(n))
