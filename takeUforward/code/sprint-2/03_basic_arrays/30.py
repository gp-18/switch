# Sum of Largest and Smallest Element
# Given an array `nums` of integers, find the sum of the maximum and minimum elements in the array.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 6  # min = 1, max = 5 -> 1 + 5 = 6
#
# Example 2:
# Input: nums = [10, 20, 30]
# Output: 40  # min = 10, max = 30 -> 10 + 30 = 40
#
# Example 3 (Edge Case - Negative Numbers):
# Input: nums = [-15, 2, 8, -3]
# Output: -7  # min = -15, max = 8 -> -15 + 8 = -7

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

if len(array) == 0 : 
  print("Array is empty")
else : 
  max_element = float("-inf")
  min_element = float("inf")

  for value in array : 
    if value > max_element : 
      max_element = value 
    if value < min_element : 
      min_element = value 

  print(f"The sum of largest and smallest element is : {max_element + min_element}")
