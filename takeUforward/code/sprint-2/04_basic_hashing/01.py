# Counting Frequencies of Array Elements
# Given an array `nums` of integers, count and return the frequency of each distinct element using a hash map or dictionary.
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 3, 3]
# Output: {1: 1, 2: 2, 3: 3}
#
# Example 2:
# Input: nums = [10, 5, 10, 15, 5]
# Output: {10: 2, 5: 2, 15: 1}
#
# Example 3 (Edge Case - Negative Numbers and Zero):
# Input: nums = [-1, 0, -1, -2]
# Output: {-1: 2, 0: 1, -2: 1}

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

freq  = {}

for value in array : 
  freq[value] = freq.get(value, 0) + 1

print(freq)  