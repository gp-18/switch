# Highest Occurring Element in an Array
# Given an array `nums` of integers, find and return the element that appears the most number of times (has the maximum frequency). If there is a tie, return the smaller element.
#
# Example 1:
# Input: nums = [1, 3, 2, 1, 4, 1]
# Output: 1  # Frequency is 3
#
# Example 2:
# Input: nums = [10, 20, 20, 30]
# Output: 20  # Frequency is 2
#
# Example 3 (Edge Case - All Negative Numbers with Tie):
# Input: nums = [-2, -2, -5, -5]
# Output: -5  # Both appear twice; -5 is smaller than -2

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

