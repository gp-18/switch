# Maximum Consecutive Ones
# Given a binary array `nums` containing only 0s and 1s, return the maximum number of consecutive 1s in the array.
#
# Example 1:
# Input: nums = [1, 1, 0, 1, 1, 1]
# Output: 3
#
# Example 2:
# Input: nums = [1, 0, 1, 1, 0, 1]
# Output: 2
#
# Example 3 (Edge Case - No Ones in Array):
# Input: nums = [0, 0, 0, 0]
# Output: 0

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

current_count = 0 
max_count = 0 

for value in array : 
  if value == 1 : 
    current_count += 1 
  else : 
    max_count = max(max_count, current_count) 
    current_count = 0 

max_count = max(max_count, current_count) 

print(f"The maximum number of consecutive ones is : {max_count}")