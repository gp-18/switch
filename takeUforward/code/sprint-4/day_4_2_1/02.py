# Move All Negative Numbers to Beginning and Positive to End
# Given an unsorted integer array nums containing both positive and negative values,
# rearrange the elements in-place such that all negative numbers appear at the beginning
# and all positive numbers (including zero) appear at the end.
#
# Example 1:
# Input:  nums = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# Output: [-12, -6, -13, -5, -3, -7, 5, 6, 11]  # Any valid negative-first segregation
#
# Example 2:
# Input:  nums = [1, -2, 3, -4, 5]
# Output: [-2, -4, 3, 1, 5]
#
# Example 3 (Edge Case):
# Input:  nums = [-1, -2, -3]
# Output: [-1, -2, -3]  # All elements negative
#
# Think About:
# - Two-Pointer Partition:
#   * left = 0, right = n - 1
#   * While left <= right:
#       - If nums[left] < 0: left += 1
#       - Else if nums[right] >= 0: right -= 1
#       - Else: swap nums[left] and nums[right], left += 1, right -= 1
# - Time Complexity: O(N)
# - Space Complexity: O(1) in-place
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

print(f"Your array has become: {array} and now doing the operations on it.")

# Write your solution below
