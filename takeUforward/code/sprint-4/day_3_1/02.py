# Triplet Sum Equal to Target
# Given an integer array nums and an integer target, find any one triplet
# [nums[i], nums[j], nums[k]] such that i != j != k and their sum equals target.
# Return the triplet in a list. If no such triplet exists, return an empty list [].
#
# Example 1:
# Input:  nums = [12, 3, 4, 1, 6, 9], target = 24
# Output: [3, 9, 12]  # 3 + 9 + 12 = 24
#
# Example 2:
# Input:  nums = [1, 2, 3, 4, 5], target = 50
# Output: []
#
# Example 3 (Edge Case):
# Input:  nums = [-5, 2, 3], target = 0  # Exact size 3 array
# Output: [-5, 2, 3]
#
# Think About:
# - Sort nums in ascending order.
# - Loop i from 0 to n - 3.
# - Set low = i + 1, high = n - 1.
# - While low < high:
#   * total = nums[i] + nums[low] + nums[high]
#   * If total == target: return [nums[i], nums[low], nums[high]].
#   * If total < target: low += 1 (need bigger sum).
#   * If total > target: high -= 1 (need smaller sum).
# - Return [] if no triplet matches target.
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
