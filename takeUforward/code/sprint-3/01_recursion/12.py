# Sum of digits of a number using recursion
# Given a non-negative integer `n`, return the sum of its digits using recursion.
#
# Example 1:
# Input: n = 1234
# Output: 10
#
# Example 2:
# Input: n = 99
# Output: 18
#
# Example 3 (Edge Case):
# Input: n = 5
# Output: 5
#

n = int(input("Enter the number : "))

print(f"n is : {n} and now doing the operations on it.")
def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(n))
