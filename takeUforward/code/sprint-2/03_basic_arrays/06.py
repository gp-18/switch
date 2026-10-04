# Smallest Element
# Given an array `nums` of integers, find and return the smallest element.
#
# Example 1:
# Input: nums = [4, 7, 1, 9, 3]
# Output: 1
#
# Example 2:
# Input: nums = [15, 22, 8, 30]
# Output: 8
#
# Example 3 (Edge Case - All Negative Numbers):
# Input: nums = [-5, -2, -100, -1]
# Output: -100  # Smallest element is -100

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

