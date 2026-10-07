# Sum of array elements using recursion
# Given an array `nums` of integers, calculate and return the sum of all elements using recursion.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 15
#
# Example 2:
# Input: nums = [10, -5, 20]
# Output: 25
#
# Example 3 (Edge Case):
# Input: nums = [42]
# Output: 42
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")
def sum_of_array(arr, index):
    if index >= len(arr):
        return 0
    return arr[index] + sum_of_array(arr, index + 1)

print(sum_of_array(array, 0))
