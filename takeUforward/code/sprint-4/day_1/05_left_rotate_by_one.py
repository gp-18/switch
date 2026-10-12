# Left Rotate Array by One
# Given an array nums of N integers, rotate the array to the left by one position in-place.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5]
# Output: [2, 3, 4, 5, 1]
#
# Example 2:
# Input:  nums = [3]
# Output: [3]
#
# Think About:
# - Store the first element temp = nums[0].
# - Shift elements from index 1 to N - 1 one place to the left: nums[i - 1] = nums[i].
# - Place temp at the last index: nums[N - 1] = temp.
# - Time Complexity: O(N)
# - Space Complexity: O(1) extra space.
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

