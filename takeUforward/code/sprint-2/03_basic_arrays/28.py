# Third Largest Element
# Given an array `nums` of integers, find and return the third largest distinct element. If it does not exist, return -1.
#
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 3
#
# Example 2:
# Input: nums = [10, 20, 30, 40, 50]
# Output: 30
#
# Example 3 (Edge Case - All Negatives / Insufficient Distinct Elements):
# Input: nums = [-10, -5, -2, -1]
# Output: -5  # Third largest is -5 (after -1 and -2)

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

third_largest = second_largest = largest = float("-inf") 

for value in array : 
  if value > largest : 
    third_largest = second_largest 
    second_largest = largest 
    largest = value 
  
  elif value > second_largest and value != largest : 
    third_largest = second_largest 
    second_largest = value  

  elif value > third_largest and value < second_largest and value < largest: 
    third_largest = value 

if third_largest == float("-inf") : 
  print("No third largest element exists") 
else : 
  print(f"The third largest element is : {third_largest}") 

