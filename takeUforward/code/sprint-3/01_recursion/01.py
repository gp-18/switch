# Print 1 to N using recursion
# Given an integer `n`, print numbers from 1 to `n` in increasing order using recursion.
#
# Example 1:
# Input: n = 5
# Output: 1 2 3 4 5
#
# Example 2:
# Input: n = 1
# Output: 1
#
# Example 3 (Edge Case):
# Input: n = 3
# Output: 1 2 3
#

n = int(input("Enter the value of n : "))

print(f"n is : {n} and now doing the operations on it.")
def print_1_to_n(n):
    if n <= 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

print_1_to_n(n)
print()
