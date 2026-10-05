# Count Distinct Elements in Array
# Given an array `nums`, count and return the total number of unique (distinct) elements using a hash set or hash map.
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

length = int(input("Enter the length of the array : "))
array = []

for i in range(0, length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

array_set = set()

for value in array:
    array_set.add(value)

print(f"The number of distinct elements is : {len(array_set)}")

