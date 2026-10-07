# Linear search using recursion
# Given an array `nums` and a `target` element, return the index of the first occurrence of `target` using recursion, or -1 if not found.
#
# Example 1:
# Input: nums = [10, 20, 30, 40], target = 30
# Output: 2
#
# Example 2:
# Input: nums = [1, 2, 3], target = 5
# Output: -1
#
# Example 3 (Edge Case):
# Input: nums = [4, 4, 4], target = 4
# Output: 0
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter the target element to search : "))

print(f"Your array has become : {array}, target is : {target} and now doing the operations on it.")
def linear_search(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search(arr, target, index + 1)

print(linear_search(array, target, 0))
