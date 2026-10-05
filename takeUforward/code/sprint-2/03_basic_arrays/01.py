# Sum of Array Elements
# Given an array `nums` of integers, calculate and return the sum of all elements.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 15
#
# Example 2:
# Input: nums = [10, 20, 30]
# Output: 60
#
# Example 3 (Edge Case - Negative Numbers):
# Input: nums = [-5, 10, -3, 8]
# Output: 10  # (-5) + 10 + (-3) + 8 = 10

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


sum = 0 

for value in array : 
  sum += value 

print(f"Sum = {sum}")

