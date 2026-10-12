# Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove duplicates in-place
# such that each unique element appears only once. Return the number of unique elements k.
#
# Example 1:
# Input:  nums = [1, 1, 2]
# Output: k = 2, nums = [1, 2, _]
#
# Example 2:
# Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: k = 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
#
# Think About:
# - Use two pointers: i = 0 tracks the index of the last placed unique element.
# - Pointer j iterates from 1 to N - 1:
#   * If nums[j] != nums[i]: increment i += 1 and set nums[i] = nums[j].
# - The number of unique elements is i + 1.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space.
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

