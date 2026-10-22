# Generalized K-Sum: Two-Pointer Reduction (Google, Meta, Apple)
# Implement the universal K-Sum algorithm to find all unique combinations of k integers
# in nums that sum to target. Return all unique k-tuples in any order.
#
# Example 1:
# Input:  nums = [1, 0, -1, 0, -2, 2], target = 0, k = 4
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
#
# Example 2:
# Input:  nums = [2, 2, 2, 2, 2], target = 8, k = 4
# Output: [[2, 2, 2, 2]]
#
# Example 3 (Edge Case):
# Input:  nums = [1, 2, 3], target = 6, k = 4
# Output: []  # n < k
#
# Think About:
# - Sort nums in ascending order.
# - Break down k-Sum recursively into (k-1)-Sum until k == 2.
# - Base Case (k == 2):
#   * Two pointers low and high from left and right.
#   * If nums[low] + nums[high] == target: record pair, skip duplicates, move both inward.
#   * If sum < target: low += 1
#   * If sum > target: high -= 1
# - Recursive Step (k > 2):
#   * Loop i from start to n - k:
#       * Skip duplicates: if i > start and nums[i] == nums[i - 1]: continue
#       * Pruning: if nums[i] * k > target or nums[-1] * k < target: break / continue
#       * Recursively call kSum(i + 1, target - nums[i], k - 1)
#       * Prepend nums[i] to each returned sub-tuple.
# - Time Complexity: O(N^(k-1)) -> O(N^3) for k = 4
# - Space Complexity: O(k) recursion stack space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter the target sum : "))
k = int(input("Enter the value of k (e.g. 4 for 4-Sum) : "))

print(f"Your array has become : {array}, target is : {target}, k is : {k} and now doing the operations on it.")

# Write your solution below
