# Reverse an Array
# Given an array `nums`, reverse the order of its elements.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
#
# Example 2:
# Input: nums = [10, 20]
# Output: [20, 10]
#
# Example 3 (Edge Case - Negative Numbers / Single Element):
# Input: nums = [-1, -2, -3]
# Output: [-3, -2, -1]

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

