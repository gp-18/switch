# Count occurrences of a number in an array using recursion
# Given an array `nums` and a `target` integer, count how many times `target` appears in the array using recursion.
#
# Example 1:
# Input: nums = [1, 2, 3, 2, 4, 2], target = 2
# Output: 3
#
# Example 2:
# Input: nums = [5, 5, 5], target = 5
# Output: 3
#
# Example 3 (Edge Case):
# Input: nums = [1, 2, 3], target = 9
# Output: 0
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter the target element to count : "))

print(f"Your array has become : {array}, target is : {target} and now doing the operations on it.")
