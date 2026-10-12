# Squares of a Sorted Array
# Given an array of integers nums sorted in non-decreasing order (which may include negative numbers),
# return an array of the squares of each number, also sorted in non-decreasing order.
#
# Example 1:
# Input:  nums = [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
#
# Example 2:
# Input:  nums = [-7, -3, 2, 3, 11]
# Output: [4, 9, 9, 49, 121]
#
# Example 3 (Edge Case):
# Input:  nums = [-5, -4, -3, -2, -1]
# Output: [1, 4, 9, 16, 25]  # All negatives reversed when squared
#
# Think About:
# - Negatives produce large squares. Largest squares are at the extreme left or extreme right.
# - Fill result array from the very back (pos = N - 1 down to 0).
# - Compare nums[left] ** 2 and nums[right] ** 2:
#   * Place larger square at result[pos] and move that pointer inward.
#   * Decrement pos -= 1.
# - Time Complexity: O(N)
# - Space Complexity: O(N) for result array, O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

