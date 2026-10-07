# Print first N even numbers in increasing order
# Given an integer `n`, print the first `n` even natural numbers (2, 4, 6, ..., 2*n) in increasing order using recursion.
#
# Example 1:
# Input: n = 4
# Output: 2 4 6 8
#
# Example 2:
# Input: n = 1
# Output: 2
#
# Example 3 (Edge Case):
# Input: n = 5
# Output: 2 4 6 8 10
#

n = int(input("Enter the value of n : "))

print(f"n is : {n} and now doing the operations on it.")
def print_first_n_even(n):
    if n <= 0:
        return
    print_first_n_even(n - 1)
    print(2 * n, end=" ")

print_first_n_even(n)
print()
