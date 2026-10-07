# Print N to 0 using recursion
# Given an integer `n`, print numbers from `n` down to `0` using tail recursion.
#
# Example 1:
# Input: n = 4
# Output: 4 3 2 1 0
#
# Example 2:
# Input: n = 0
# Output: 0
#
# Example 3 (Edge Case):
# Input: n = 2
# Output: 2 1 0
#

n = int(input("Enter the value of n : "))

print(f"n is : {n} and now doing the operations on it.")
def print_n_to_0(n):
    if n < 0:
        return
    print(n, end=" ")
    print_n_to_0(n - 1)

print_n_to_0(n)
print()
