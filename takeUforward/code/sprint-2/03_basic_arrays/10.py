# Sum of Even Numbers in Array
# Given an array `nums` of integers, calculate and return the sum of all even numbers.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5, 6]
# Output: 12  # 2 + 4 + 6 = 12
#
# Example 2:
# Input: nums = [1, 3, 5, 7]
# Output: 0  # No even numbers present
#
# Example 3 (Edge Case - Negative Even Numbers):
# Input: nums = [-4, -2, 3, 5, -6]
# Output: -12  # (-4) + (-2) + (-6) = -12

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

sum = 0 

for value in array : 

  if value % 2 == 0 : 
    sum += value 

print(sum)

