# Largest Element
# Given an array `nums` of integers, find and return the largest element.
#
# Example 1:
# Input: nums = [3, 7, 2, 9, 5]
# Output: 9
#
# Example 2:
# Input: nums = [10, 4, 15, 8]
# Output: 15
#
# Example 3 (Edge Case - All Negative Numbers):
# Input: nums = [-10, -3, -50, -1]
# Output: -1  # Largest element is -1

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

largest = float("-inf")

for value in array : 
  if value > largest : 
    largest = value

print(largest) 
    

