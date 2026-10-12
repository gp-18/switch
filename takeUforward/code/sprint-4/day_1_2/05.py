# Two Sum in a Sorted Array (Two Sum II)
# Given an array of integers nums already sorted in ascending order, find two numbers
# such that they add up to a given target. Return their 1-based indices [index1, index2].
# Assume exactly one solution exists.
#
# Example 1:
# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [1, 2]  # nums[0] + nums[1] = 2 + 7 = 9 (1-based: indices 1 and 2)
#
# Example 2:
# Input:  nums = [2, 3, 4], target = 6
# Output: [1, 3]  # 2 + 4 = 6 (1-based: indices 1 and 3)
#
# Example 3 (Edge Case):
# Input:  nums = [-5, -2, 1, 4], target = -7
# Output: [1, 2]  # -5 + -2 = -7
#
# Think About:
# - Put left = 0 and right = len(nums) - 1.
# - Check current_sum = nums[left] + nums[right]:
#   * If current_sum == target: return [left + 1, right + 1].
#   * If current_sum < target: sum too small, left += 1.
#   * If current_sum > target: sum too big, right -= 1.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter the target sum : "))

print(f"Your array has become : {array}, target is : {target} and now doing the operations on it.")

# Write your solution below

