# Check if Two Arrays are Equal
# Given two arrays `a` and `b`, determine if they contain the exact same elements with the same frequencies (irrespective of order).
#
# Example 1:
# Input: a = [1, 2, 5, 4, 0], b = [2, 4, 5, 0, 1]
# Output: True
#
# Example 2:
# Input: a = [1, 2, 3], b = [1, 2, 4]
# Output: False
#
# Example 3 (Edge Case - Negative Elements & Different Counts):
# Input: a = [-1, -2, -2], b = [-1, -1, -2]
# Output: False

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

