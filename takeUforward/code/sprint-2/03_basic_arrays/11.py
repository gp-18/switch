# Sum of Odd Numbers in Array
# Given an array `nums` of integers, calculate and return the sum of all odd numbers.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5, 6]
# Output: 9  # 1 + 3 + 5 = 9
#
# Example 2:
# Input: nums = [2, 4, 6, 8]
# Output: 0  # No odd numbers present
#
# Example 3 (Edge Case - Negative Odd Numbers):
# Input: nums = [-1, -3, 2, 4, -5]
# Output: -9  # (-1) + (-3) + (-5) = -9

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

