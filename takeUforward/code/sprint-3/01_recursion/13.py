# Count digits of a number using recursion
# Given a non-negative integer `n`, count and return the total number of digits using recursion.
#
# Example 1:
# Input: n = 12345
# Output: 5
#
# Example 2:
# Input: n = 7
# Output: 1
#
# Example 3 (Edge Case):
# Input: n = 1000
# Output: 4
#

n = int(input("Enter the number : "))

print(f"n is : {n} and now doing the operations on it.")
def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(n))
