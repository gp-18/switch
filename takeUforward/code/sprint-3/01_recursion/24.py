# Maximum element in an array using recursion
# Given an array `nums` of integers, find and return the maximum element using recursion.
#
# Example 1:
# Input: nums = [1, 5, 3, 9, 2]
# Output: 9
#
# Example 2:
# Input: nums = [-10, -3, -20]
# Output: -3
#
# Example 3 (Edge Case):
# Input: nums = [42]
# Output: 42
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")
