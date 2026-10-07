# Sum of first N natural numbers
# Given an integer `n`, calculate and return the sum of the first `n` natural numbers (1 to n) using recursion.
#
# Example 1:
# Input: n = 5
# Output: 15
#
# Example 2:
# Input: n = 3
# Output: 6
#
# Example 3 (Edge Case):
# Input: n = 1
# Output: 1
#

n = int(input("Enter the value of n : "))

print(f"n is : {n} and now doing the operations on it.")
def sum_1_to_n(n):
    if n <= 0:
        return 0
    return n + sum_1_to_n(n - 1)

print(sum_1_to_n(n))
