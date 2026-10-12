# Find Missing Number
# Given an array nums containing N distinct numbers taken from the range [0, N] (or [1, N]),
# find the single number missing from the range.
#
# Example 1:
# Input:  nums = [3, 0, 1]
# Output: 2  # Range [0, 3], missing number is 2
#
# Example 2:
# Input:  nums = [1, 2, 4, 5], N = 5
# Output: 3  # Range [1, 5], missing number is 3
#
# Think About:
# - Approach 1 (Sum formula):
#   * Expected sum = N * (N + 1) // 2.
#   * Missing = Expected Sum - sum(nums).
# - Approach 2 (XOR property):
#   * XOR all numbers in the full range and XOR all numbers present in nums.
#   * Duplicates cancel out (a ^ a = 0), leaving only the missing number.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

