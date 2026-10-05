# Count Elements That Appear Exactly Once
# Given an array `nums`, count and return how many elements have a frequency of exactly 1.
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 4, 4, 5]
# Output: 3  # Elements appearing once: 1, 3, 5
#
# Example 2:
# Input: nums = [1, 1, 2, 2, 3, 3]
# Output: 0  # Every element repeats
#
# Example 3 (Edge Case - Negative Numbers):
# Input: nums = [-5, -2, -2, 0, 7, 7]
# Output: 2  # Elements appearing once: -5, 0

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

freq = {} 

for value in array : 
  freq[value] = freq.get(value, 0) + 1

count = 0

for key , value in freq.items() : 
  if value == 1 : 
    count += 1

print(f"The number of elements that appear exactly once is : {count}")