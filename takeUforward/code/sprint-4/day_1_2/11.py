# Move All Zeros to the End
# Given an array of integers nums, move all 0s to the end of the array in-place
# while maintaining the relative order of the non-zero elements.
#
# Example 1:
# Input:  nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Example 2:
# Input:  nums = [0, 0, 1]
# Output: [1, 0, 0]
#
# Example 3 (Edge Case):
# Input:  nums = [4, 5, 6]
# Output: [4, 5, 6]  # No zeros to move
#
# Think About:
# - Use Reader and Writer pattern: slow = 0.
# - Loop fast from 0 to len(nums) - 1:
#   * If nums[fast] != 0: swap nums[slow] and nums[fast], slow += 1.
# - Every non-zero gets placed in front, naturally sliding zeros to back.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

