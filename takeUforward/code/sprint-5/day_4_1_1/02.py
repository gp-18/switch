# Maximum Product of Three Numbers
# Given an integer array nums, find three numbers whose product is maximum
# and return the maximum product.
#
# Example 1:
# Input:  nums = [1, 2, 3]
# Output: 6
#
# Example 2:
# Input:  nums = [1, 2, 3, 4]
# Output: 24
#
# Example 3:
# Input:  nums = [-10, -10, 5, 2]
# Output: 500
# Explanation: (-10) * (-10) * 5 = 500.
#
# Think About:
# - Two negative numbers multiplied together become positive!
# - The maximum product of 3 numbers can only come from:
#   1. Product of the 3 largest numbers: max1 * max2 * max3
#   2. Product of the 2 smallest numbers (most negative) and the largest number: min1 * min2 * max1
# - Compare both possibilities: ans = max(max1 * max2 * max3, min1 * min2 * max1).
# - Time Complexity: O(N) single scan (or O(N log N) by sorting)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array (at least 3) : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:

