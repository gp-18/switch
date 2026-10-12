# Second Largest Element
# Given an array nums of N integers, find and return the second largest distinct element without sorting.
# If no second largest distinct element exists, return -1.
#
# Example 1:
# Input:  nums = [1, 2, 4, 7, 7, 5]
# Output: 5
#
# Example 2:
# Input:  nums = [10, 10, 10]
# Output: -1
#
# Think About:
# - Single pass approach with two variables: largest = -float('inf') and second_largest = -float('inf').
# - For each num in nums:
#   * If num > largest: update second_largest = largest, then largest = num.
#   * Else if num < largest and num > second_largest: update second_largest = num.
# - Check if second_largest was updated; if not, return -1.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

