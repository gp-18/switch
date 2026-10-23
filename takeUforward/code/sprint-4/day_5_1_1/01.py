# Minimum Subarray Sum (Inverted Kadane)
# Given an integer array nums, find the contiguous non-empty subarray with the smallest sum
# and return that sum.
#
# Example 1:
# Input:  nums = [3, -4, 2, -3, -1, 7, -5]
# Output: -6
# Explanation: The subarray [-4, 2, -3, -1] has the smallest sum = -6.
#
# Example 2:
# Input:  nums = [2, 6, 8, 1, 4]
# Output: 1
# Explanation: The single element [1] has the minimum sum.
#
# Example 3 (Edge Case):
# Input:  nums = [-1, -2, -3]
# Output: -6
# Explanation: The entire array has minimum sum = -6.
#
# Think About:
# - Inverted Kadane:
#   * min_sum = float('inf')
#   * current_sum = 0
#   * For each element in nums:
#       - Add element to current_sum
#       - Update min_sum = min(min_sum, current_sum)
#       - If current_sum > 0: reset current_sum = 0 (positive prefix increases minimum sum)
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

print(f"Your array has become: {array} and now doing the operations on it.")

# Write your solution below
min_sum = float("inf")
current_sum = 0 

for i in range(len(array)) :
    current_sum += array[i]

    min_sum = min(current_sum , min_sum)
    
    if current_sum > 0 : 
        current_sum = 0