# Print Subarray with Maximum Sum (Kadane's Algorithm Follow-up)
# Given an integer array nums, find the contiguous subarray that yields the largest sum.
# Print or return the actual subarray elements (along with their starting and ending indices)
# as well as the maximum sum.
#
# Example 1:
# Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: Subarray: [4, -1, 2, 1], Maximum Sum: 6
# Explanation: The subarray from index 3 to 6 has the largest sum = 4 + (-1) + 2 + 1 = 6.
#
# Example 2:
# Input:  nums = [2, 3, 5, -2, 7, -4]
# Output: Subarray: [2, 3, 5, -2, 7], Maximum Sum: 15
# Explanation: The subarray from index 0 to 4 has the largest sum = 15.
#
# Example 3 (Edge Case):
# Input:  nums = [-2, -3, -7, -2, -10, -4]
# Output: Subarray: [-2], Maximum Sum: -2
# Explanation: All numbers are negative; the maximum single element is -2.
#
# Think About:
# - Track subarray boundary indices:
#   * start = 0 (marks start of candidate subarray)
#   * ans_start = -1, ans_end = -1 (boundaries of best subarray so far)
#   * max_sum = float('-inf'), current_sum = 0
# - In each iteration i:
#   * If current_sum == 0: start = i
#   * current_sum += nums[i]
#   * If current_sum > max_sum:
#       max_sum = current_sum
#       ans_start = start
#       ans_end = i
#   * If current_sum < 0:
#       current_sum = 0
# - Result subarray: nums[ans_start : ans_end + 1]
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

maximum = float("-inf")
current = 0 
start = 0 
ans_start , ans_end = 0 , 0 

for i in range(len(array)) : 
    
    if current == 0 :
        start = i 
    
    current += array[i] 
    
    if current > maximum :
        maximum = current 
        ans_start = start 
        ans_end = i 
    
    if current < 0 :
        current = 0 

print(f"maximum sum is {maximum} and subarray is {array[ans_start : ans_end+1]} ") 