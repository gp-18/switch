# Second Smallest Element
# Given an array `nums` of integers, find and return the second smallest distinct element. If no second smallest exists, return -1.
#
# Example 1:
# Input: nums = [12, 35, 1, 10, 34, 1]
# Output: 10
#
# Example 2:
# Input: nums = [7, 7, 2, 9, 3]
# Output: 3
#
# Example 3 (Edge Case - All Negative Numbers):
# Input: nums = [-10, -5, -20, -1]
# Output: -10  # Smallest is -20, second smallest is -10

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

