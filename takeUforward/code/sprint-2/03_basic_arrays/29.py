# Count Distinct Elements in Array
# Given an array `nums` of integers, count and return the number of distinct (unique) elements present.
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 4, 4, 5]
# Output: 5  # Distinct: 1, 2, 3, 4, 5
#
# Example 2:
# Input: nums = [10, 10, 10, 10]
# Output: 1
#
# Example 3 (Edge Case - Negative Numbers and Zero):
# Input: nums = [-1, -2, -1, 0, 0]
# Output: 3  # Distinct: -1, -2, 0


length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


unique_array = set()

for value in array : 
  unique_array.add(value)

print(f"The number of unique elements in the array is : {len(unique_array)}")
