# Maximum Product Subarray in an Array
# Given an integer array nums. Find the contiguous subarray (containing at least one number)
# with the largest product, and return the product of the elements present in that subarray.
#
# Example 1:
# Input:  nums = [4, 5, 3, 7, 1, 2]
# Output: 840
# Explanation: Entire array product is 4 * 5 * 3 * 7 * 1 * 2 = 840.
#
# Example 2:
# Input:  nums = [-5, 0, -2]
# Output: 0
# Explanation: Maximum product is 0.
#
# Example 3:
# Input:  nums = [1, -2, 3, 4, -4, -3]
# Output: 144
# Explanation: Subarray [3, 4, -4, -3] has product 3 * 4 * (-4) * (-3) = 144.
#
# Think About:
# - Two-Way Prefix and Suffix Traversal:
#   * If even negatives: product of entire array is positive.
#   * If odd negatives: exclude either the first negative (leaving suffix)
#     or the last negative (leaving prefix).
#   * If zero: reset prefix or suffix to 1.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:

# Optimal Approach: Prefix & Suffix Products
# Time Complexity: O(N) | Space Complexity: O(1)

ans = float('-inf')
prefix = 1
suffix = 1

for i in range(length):
    # Reset prefix or suffix to 1 if it encountered a 0
    if prefix == 0:
        prefix = 1
    if suffix == 0:
        suffix = 1

    # Accumulate products from left (prefix) and right (suffix)
    prefix *= array[i]
    suffix *= array[length - i - 1]

    # Track maximum product encountered so far
    ans = max(ans, prefix, suffix)

print(f"The maximum product of a subarray is : {ans}")
