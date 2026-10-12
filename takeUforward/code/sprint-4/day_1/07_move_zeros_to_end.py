# Move Zeros to End
# Given an integer array nums, move all 0s to the end of the array while maintaining the relative order of non-zero elements in-place.
#
# Example 1:
# Input:  nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Example 2:
# Input:  nums = [0, 0, 1]
# Output: [1, 0, 0]
#
# Think About:
# - Find the index j of the first zero in the array. If no zero exists, return.
# - Loop pointer i from j + 1 to N - 1:
#   * Whenever nums[i] != 0: swap nums[i] with nums[j], then increment j += 1.
# - All non-zeros stay in relative order, and zeros naturally slide to the back.
# - Time Complexity: O(N)
# - Space Complexity: O(1) in-place.
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

