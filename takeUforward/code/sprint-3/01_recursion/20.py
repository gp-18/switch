# Print array elements in order using recursion
# Given an array of integers, print all elements from index 0 to len-1 in order using recursion.
#
# Example 1:
# Input: nums = [10, 20, 30, 40]
# Output: 10 20 30 40
#
# Example 2:
# Input: nums = [5]
# Output: 5
#
# Example 3 (Edge Case):
# Input: nums = [1, 2, 3]
# Output: 1 2 3
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")
