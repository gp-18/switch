# 3 Sum
# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
# such that:
#   - i != j, i != k, and j != k
#   - nums[i] + nums[j] + nums[k] == 0
# The solution set must not contain duplicate triplets.
#
# Example 1:
# Input:  nums = [2, -2, 0, 3, -3, 5]
# Output: [[-3, -2, 5], [-3, 0, 3], [-2, 0, 2]]
#
# Example 2:
# Input:  nums = [2, -1, -1, 3, -1]
# Output: [[-1, -1, 2]]
#
# Example 3 (Edge Case):
# Input:  nums = [8, -6, 5, 4]
# Output: []  # No triplet sums to 0
#
# Think About:
# - Sort the array first so identical elements cluster together.
# - Fix the first element nums[i] with a loop up to n - 3.
#   * If nums[i] > 0: stop early (no three positive numbers can sum to 0).
#   * If i > 0 and nums[i] == nums[i - 1]: skip duplicate first element.
# - Use two pointers low = i + 1 and high = n - 1 for the remaining pair:
#   * If nums[i] + nums[low] + nums[high] == 0:
#       record triplet, skip duplicate low and high values, move both inward.
#   * If sum < 0: low += 1 (need a larger sum).
#   * If sum > 0: high -= 1 (need a smaller sum).
# - Time Complexity: O(N^2)
# - Space Complexity: O(1) auxiliary space (excluding result list)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

