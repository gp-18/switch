# Average of Array Elements
# Given an array `nums` of integers, calculate and return the average (arithmetic mean) of its elements.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 3.0
#
# Example 2:
# Input: nums = [10, 20, 30, 40]
# Output: 25.0
#
# Example 3 (Edge Case - Negative Numbers with Non-Integer Average):
# Input: nums = [-10, 5, 2, -1]
# Output: -1.0

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


sum = 0 

for value in array : 
  sum += value 

average = sum / len(array)

print(average)