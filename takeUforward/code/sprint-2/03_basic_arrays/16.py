# Check if the Array is Sorted
# Given an array `nums`, return True if the array is sorted in non-decreasing order, otherwise False.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: True
#
# Example 2:
# Input: nums = [1, 3, 2, 4, 5]
# Output: False
#
# Example 3 (Edge Case - Negative Numbers and Duplicates):
# Input: nums = [-10, -5, -5, 0, 3]
# Output: True  # Non-decreasing order maintained

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

