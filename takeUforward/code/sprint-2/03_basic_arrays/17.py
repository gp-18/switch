# Check if the Array is a Palindrome
# Given an array `nums`, return True if the array reads the same forward and backward, otherwise False.
#
# Example 1:
# Input: nums = [1, 2, 3, 2, 1]
# Output: True
#
# Example 2:
# Input: nums = [1, 2, 3, 4, 5]
# Output: False
#
# Example 3 (Edge Case - Negative Numbers / Single Element):
# Input: nums = [-1, 0, -1]
# Output: True

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


reverse_array = list(reversed(array))

if array == reverse_array : 
  print("The array is a palindrome")
else :
  print("The array is not a palindrome")