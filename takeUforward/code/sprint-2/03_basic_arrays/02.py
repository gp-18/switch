# Count of Odd Numbers in Array
# Given an array `nums` of integers, count and return how many numbers are odd.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5, 6]
# Output: 3  # Odd elements: 1, 3, 5
#
# Example 2:
# Input: nums = [2, 4, 6, 8]
# Output: 0
#
# Example 3 (Edge Case - Negative Numbers):
# Input: nums = [-1, -2, -3, -4, -5]
# Output: 3  # Odd elements: -1, -3, -5

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


odd_element = []

for value in array : 
  if value % 2 != 0 : 
    odd_element.append(value)

print(f"The count of odd elements is : {len(odd_element)}")
