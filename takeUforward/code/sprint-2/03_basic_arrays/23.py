# Missing Number
# Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.
#
# Example 1:
# Input: nums = [3, 0, 1]
# Output: 2  # n = 3, range [0, 3], missing is 2
#
# Example 2:
# Input: nums = [0, 1]
# Output: 2  # n = 2, range [0, 2], missing is 2
#
# Example 3 (Edge Case - Missing Zero):
# Input: nums = [1, 2, 3]
# Output: 0  # n = 3, range [0, 3], missing is 0

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

