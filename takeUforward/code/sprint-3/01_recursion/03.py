# Print digits of a number from left to right
# Given a non-negative integer `n`, print its digits from left to right using recursion.
#
# Example 1:
# Input: n = 1234
# Output: 1 2 3 4
#
# Example 2:
# Input: n = 5
# Output: 5
#
# Example 3 (Edge Case):
# Input: n = 9070
# Output: 9 0 7 0
#

n = int(input("Enter the number : "))

print(f"n is : {n} and now doing the operations on it.")
def print_digits_left_to_right(n):
    if n < 10:
        print(n, end=" ")
        return
    print_digits_left_to_right(n // 10)
    print(n % 10, end=" ")

print_digits_left_to_right(n)
print()
