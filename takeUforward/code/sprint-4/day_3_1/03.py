# Count Triplets with Given Sum
# Given an array of distinct integers nums and an integer target, count the total
# number of unique triplets (i, j, k) with i < j < k such that:
# nums[i] + nums[j] + nums[k] == target.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5], target = 9
# Output: 2  # Triplets: (1, 3, 5) and (2, 3, 4)
#
# Example 2:
# Input:  nums = [0, -1, 2, -3, 1], target = -2
# Output: 2  # Triplets: (-3, 0, 1) and (-3, -1, 2)
#
# Example 3 (Edge Case):
# Input:  nums = [1, 2, 3], target = 10
# Output: 0  # No triplet reaches target
#
# Think About:
# - Sort nums in ascending order.
# - Initialize count = 0.
# - Loop i from 0 to n - 3.
# - Set low = i + 1, high = n - 1.
# - While low < high:
#   * current_sum = nums[i] + nums[low] + nums[high]
#   * If current_sum == target:
#       count += 1, low += 1, high -= 1
#   * Else if current_sum < target:
#       low += 1
#   * Else:
#       high -= 1
# - Time Complexity: O(N^2)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter the target sum : "))

print(f"Your array has become : {array}, target is : {target} and now doing the operations on it.")

# Write your solution below
