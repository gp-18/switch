# Count of Even Numbers in Array
# Given an array `nums` of integers, count and return how many numbers are even.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5, 6]
# Output: 3  # Even elements: 2, 4, 6
#
# Example 2:
# Input: nums = [1, 3, 5, 7]
# Output: 0
#
# Example 3 (Edge Case - Negative Numbers and Zero):
# Input: nums = [-2, 0, -4, 3, 5]
# Output: 3  # Even elements: -2, 0, -4

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

