# Contains Duplicate
# Given an array `nums`, return True if any value appears at least twice in the array, and False if every element is distinct.
#
# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: True
#
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: False
#
# Example 3 (Edge Case - Negative Numbers with Duplicates):
# Input: nums = [-1, -2, -3, -1]
# Output: True

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

