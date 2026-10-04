# Second Largest Element
# Given an array `nums` of integers, find and return the second largest distinct element. If no second largest exists, return -1.
#
# Example 1:
# Input: nums = [12, 35, 1, 10, 34, 1]
# Output: 34
#
# Example 2:
# Input: nums = [10, 5, 10]
# Output: 5
#
# Example 3 (Edge Case - All Negatives / All Identical):
# Input: nums = [-10, -5, -2, -20]
# Output: -5  # Largest is -2, second largest is -5

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

