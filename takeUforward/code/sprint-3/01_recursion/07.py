# Print array elements in reverse order using recursion
# Given an array of integers, print all elements from last to first using recursion.
#
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 5 4 3 2 1
#
# Example 2:
# Input: nums = [10, 20]
# Output: 20 10
#
# Example 3 (Edge Case):
# Input: nums = [7]
# Output: 7
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")
def print_reverse(arr, index):
    if index >= len(arr):
        return
    print_reverse(arr, index + 1)
    print(arr[index], end=" ")

print_reverse(array, 0)
print()
