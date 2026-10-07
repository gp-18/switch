# Sum of first N numbers using an accumulator
# Given an integer `n`, compute the sum of the first `n` numbers using tail recursion with an accumulator parameter.
#
# Example 1:
# Input: n = 5
# Output: 15
#
# Example 2:
# Input: n = 1
# Output: 1
#
# Example 3 (Edge Case):
# Input: n = 4
# Output: 10
#

n = int(input("Enter the value of n : "))

print(f"n is : {n} and now doing the operations on it.")
def sum_first_n(n, acc=0):
    if n <= 0:
        return acc
    return sum_first_n(n - 1, acc + n)

print(sum_first_n(n, 0))
