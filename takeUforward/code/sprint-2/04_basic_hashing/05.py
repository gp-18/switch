# Lowest Occurring Element in an Array
# Given an array `nums`, find and return the element that appears the least number of times (lowest frequency). If multiple elements have the lowest frequency, return the smallest element.
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 3, 3]
# Output: 1  # Frequency is 1
#
# Example 2:
# Input: nums = [4, 4, 5, 5, 6, 6, 7]
# Output: 7  # Frequency is 1
#
# Example 3 (Edge Case - Negative Elements with Tie):
# Input: nums = [-10, -5, -5, 2, 2]
# Output: -10  # Frequency is 1 (smallest among ties)

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

freq = {} 

for value in array : 
  freq[value] = freq.get(value, 0) + 1


lowest_frequency = float("inf")
lowest_element = float("inf")

for key , value in freq.items() : 
  if value < lowest_frequency : 
    lowest_frequency = value 
    lowest_element = key 
  elif value == lowest_frequency and key < lowest_element : 
    lowest_element = key 

print(f"The lowest occurring element is : {lowest_element}")
