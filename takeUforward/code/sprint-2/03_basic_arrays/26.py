# Count Occurrences of a Given Number
# Given an array `nums` and a target integer `target`, count how many times `target` appears in `nums`.
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 2, 4, 2], target = 2
# Output: 4
#
# Example 2:
# Input: nums = [1, 2, 3, 4, 5], target = 6
# Output: 0
#
# Example 3 (Edge Case - Target is Negative):
# Input: nums = [-5, -2, -5, -5, 1], target = -5
# Output: 3

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

target = int(input("Enter the target value : "))

 
freq = {} 
for value in array : 
  freq[value] = freq.get(value, 0) + 1 
 

print(f"The frequency of the target value {target} is : {freq.get(target, 0)}")