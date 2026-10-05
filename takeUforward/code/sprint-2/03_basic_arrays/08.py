# Linear Search
# Given an array `nums` and a target value `target`, return the index of the first occurrence of `target`, or -1 if it is not present in `nums`.
#
# Example 1:
# Input: nums = [10, 25, 30, 45, 50], target = 30
# Output: 2
#
# Example 2:
# Input: nums = [4, 2, 7, 1, 9], target = 5
# Output: -1  # Element not found
#
# Example 3 (Edge Case - Searching Negative Number):
# Input: nums = [-5, -2, 0, 3], target = -5
# Output: 0

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


target = int(input("Enter the element to search : "))

found = False 

for i in range(0 , len(array)) :
  if array[i] == target : 
    print(f"Element found at index {i}")
    found = True 
    break

if not found : 
  print("-1")

