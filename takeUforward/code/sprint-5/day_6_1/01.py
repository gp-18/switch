# Longest Subarray with Sum K
# Given an array nums of size n and an integer k, find the length of the longest
# sub-array that sums to k. If no such sub-array exists, return 0.
#
# Example 1:
# Input:  nums = [10, 5, 2, 7, 1, 9], k = 15
# Output: 4
# Explanation: Subarray [5, 2, 7, 1] sums to 15, length = 4.
#
# Example 2:
# Input:  nums = [-3, 2, 1], k = 6
# Output: 0
# Explanation: No subarray sums to 6.
#
# Example 3:
# Input:  nums = [-1, 1, 1], k = 1
# Output: 3
# Explanation: Entire array [-1, 1, 1] sums to 1, length = 3.
#
# Think About:
# - Maintain running prefix sum and a hash map {prefix_sum: earliest_index}.
# - If running sum == k: max_len = i + 1.
# - If (running sum - k) in map: max_len = max(max_len, i - map[running sum - k]).
# - CRITICAL: Only store prefix sum if it is NOT already in map to preserve earliest index
#   for maximum length (handles repeated sums due to zeros or canceling negatives).
# - Time Complexity: O(N)
# - Space Complexity: O(N) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

k = int(input("Enter target sum k : "))

print(f"Your array has become : {array} with target k = {k} and now doing the operations on it.")

# Write your solution below:
# Optimal Approach: Prefix Sum + Hash Map
# Time Complexity: O(N) | Space Complexity: O(N)

pre_sum_map = {}
running_sum = 0
max_len = 0

for i in range(length):
    running_sum += array[i]

    # Case 1: Subarray starting from index 0 directly sums to k
    if running_sum == k:
        max_len = max(max_len, i + 1)

    # Case 2: Subarray between an earlier prefix sum and current index sums to k
    rem = running_sum - k
    if rem in pre_sum_map:
        sub_len = i - pre_sum_map[rem]
        max_len = max(max_len, sub_len)

    # Case 3: Only store the first occurrence of running_sum
    if running_sum not in pre_sum_map:
        pre_sum_map[running_sum] = i

print(f"The length of the longest subarray with sum {k} is : {max_len}")
