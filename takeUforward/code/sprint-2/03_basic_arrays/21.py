# Counting Frequencies of Array Elements
# Given an array `nums`, count and return the frequency of each distinct element (e.g. as a dictionary or map).
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 3, 3]
# Output: {1: 1, 2: 2, 3: 3}
#
# Example 2:
# Input: nums = [10, 20, 20, 10, 10]
# Output: {10: 3, 20: 2}
#
# Example 3 (Edge Case - Negative Numbers and Zero):
# Input: nums = [-1, -1, 0, -2]
# Output: {-1: 2, 0: 1, -2: 1}

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

