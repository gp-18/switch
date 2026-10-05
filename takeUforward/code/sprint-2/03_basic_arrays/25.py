# Difference Between Largest and Smallest Element
# Given an array `nums` of integers, calculate and return the difference between the maximum and minimum elements (max - min).
#
# Example 1:
# Input: nums = [2, 10, 5, 1, 8]
# Output: 9  # 10 - 1 = 9
#
# Example 2:
# Input: nums = [7, 7, 7, 7]
# Output: 0  # 7 - 7 = 0
#
# Example 3 (Edge Case - Negative and Positive Numbers):
# Input: nums = [-10, 4, 2, -2]
# Output: 14  # 4 - (-10) = 14


length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

max_element = float("-inf")
min_element = float("inf")

for value in array : 

  if value > max_element :
    max_element = value 
  
  if value < min_element :
    min_element = value
    

print(max_element - min_element)