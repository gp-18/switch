# Product of Array Elements
# Given an array `nums` of integers, find and return the product of all elements.
#
# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: 24  # 1 * 2 * 3 * 4 = 24
#
# Example 2:
# Input: nums = [2, 5, 10]
# Output: 100
#
# Example 3 (Edge Case - Array with Zero and Negatives):
# Input: nums = [-2, 3, 0, 4]
# Output: 0  # Multiplying by zero gives 0

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

