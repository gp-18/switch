# Single Number
# Given a non-empty array of integers `nums`, every element appears twice except for one. Find and return that single element.
#
# Example 1:
# Input: nums = [2, 2, 1]
# Output: 1
#
# Example 2:
# Input: nums = [4, 1, 2, 1, 2]
# Output: 4
#
# Example 3 (Edge Case - Single Element is Negative):
# Input: nums = [-1, 2, 2]
# Output: -1

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

freq = {} 

for value in array : 
  freq[value] = freq.get(value, 0) + 1 

for key , value in freq.items() :
  if value == 1 :
    print(f"The single number is : {key}")

#  optimize code 

single_number = 0

for value in array:
    single_number = single_number ^ value

print(f"The single number is : {single_number}")
