# Remove Element In-Place
# Given an array nums and a value val, remove all instances of val in-place.
# Return the number of elements left that are not equal to val (k).
# The first k elements of nums should hold the answer.
#
# Example 1:
# Input:  nums = [3, 2, 2, 3], val = 3
# Output: k = 2, nums starts with [2, 2]
#
# Example 2:
# Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# Output: k = 5, nums starts with [0, 1, 3, 0, 4]
#
# Example 3 (Edge Case):
# Input:  nums = [7, 7, 7], val = 7
# Output: k = 0, nums is empty of valid elements
#
# Think About:
# - Writer pointer slow = 0.
# - Reader pointer fast scans from index 0 to N - 1:
#   * If nums[fast] != val: copy nums[slow] = nums[fast], advance slow += 1.
# - Return slow.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

val = int(input("Enter the value val to remove : "))

print(f"Your array has become : {array}, val to remove is : {val} and now doing the operations on it.")

# Write your solution below

