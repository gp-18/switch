# Remove Duplicates from a Sorted Array
# Given an array nums sorted in ascending order, remove duplicates in-place
# so that each unique element appears only once. Return the number of unique elements k.
#
# Example 1:
# Input:  nums = [1, 1, 2]
# Output: k = 2, nums starts with [1, 2]
#
# Example 2:
# Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: k = 5, nums starts with [0, 1, 2, 3, 4]
#
# Example 3 (Edge Case):
# Input:  nums = [5]
# Output: k = 1, nums = [5]  # Single element has no duplicates
#
# Think About:
# - If array is empty, return 0.
# - First element is always kept: slow = 0.
# - Loop fast from index 1 to N - 1:
#   * If nums[fast] != nums[slow]:
#     slow += 1
#     nums[slow] = nums[fast]
# - Return slow + 1.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

