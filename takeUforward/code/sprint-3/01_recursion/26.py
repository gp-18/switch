# Check if the array is sorted using recursion
# Given an array `nums`, return True if the array is sorted in non-decreasing order, otherwise False, using recursion.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: True
#
# Example 2:
# Input: nums = [1, 3, 2, 4]
# Output: False
#
# Example 3 (Edge Case):
# Input: nums = [5]
# Output: True
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")
def is_sorted(arr, index=0):
    if index >= len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return is_sorted(arr, index + 1)

print(is_sorted(array, 0))
