# Kadane's Algorithm (Maximum Subarray Sum)
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# Example 1:
# Input:  nums = [2, 3, 5, -2, 7, -4]
# Output: 15
# Explanation: The subarray [2, 3, 5, -2, 7] from index 0 to 4 has the largest sum = 15.
#
# Example 2:
# Input:  nums = [-1, 2, 3, -1, 2, -6, 5]
# Output: 6
# Explanation: The subarray [2, 3, -1, 2] from index 1 to 4 has the largest sum = 6.
#
# Example 3 (Edge Case):
# Input:  nums = [-2, -3, -7, -2, -10, -4]
# Output: -2
# Explanation: All numbers are negative; the maximum single element is -2.
#
# Think About:
# - Optimal Approach (Kadane's Algorithm):
#   * max_sum = float('-inf')
#   * current_sum = 0
#   * Iterate through array:
#       - Add current element to current_sum
#       - Update max_sum = max(max_sum, current_sum)
#       - If current_sum < 0: reset current_sum = 0
# - Why reset to 0? A negative running sum will only reduce any future contiguous sum.
# - Time Complexity: O(N) single pass
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

print(f"Your array has become: {array} and now doing the operations on it.")

# Write your solution below

current = 0 
maximum = float("-inf")

for i in range(len(array)) :
    current += array[i] 
    maximum = max(current , maximum) 
    
    if current < 0 :
        current = 0 
        
print(f"maximum subarray sum is: {maximum}")