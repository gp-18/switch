# 3 Sum Closest
# Given an integer array nums of length n and an integer target,
# find three integers in nums such that their sum is closest to target.
# Return the sum of the three integers.
#
# Example 1:
# Input:  nums = [-1, 2, 1, -4], target = 1
# Output: 2  # Triplet (-1, 1, 2) has sum = 2, distance from 1 is |2 - 1| = 1
#
# Example 2:
# Input:  nums = [0, 0, 0], target = 1
# Output: 0  # Triplet (0, 0, 0) has sum = 0, distance is 1
#
# Example 3 (Edge Case):
# Input:  nums = [1, 1, 1], target = -100
# Output: 3  # Sum far from negative target
#
# Think About:
# - Sort nums in ascending order.
# - Initialize closest_sum = nums[0] + nums[1] + nums[2].
# - Loop i from 0 to n - 3.
# - Set low = i + 1, high = n - 1.
# - While low < high:
#   * current_sum = nums[i] + nums[low] + nums[high]
#   * If abs(current_sum - target) < abs(closest_sum - target):
#       closest_sum = current_sum
#   * If current_sum == target: return target immediately!
#   * If current_sum < target: low += 1 (need bigger sum).
#   * If current_sum > target: high -= 1 (need smaller sum).
# - Return closest_sum.
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

# Optimal Approach: Sort + Two Pointers
# Time Complexity: O(N^2) | Space Complexity: O(1) auxiliary space
array.sort()
n = len(array)

# Initialize with the sum of the first three elements
closest_sum = array[0] + array[1] + array[2]

for i in range(n - 2):
    low = i + 1
    high = n - 1

    while low < high:
        current_sum = array[i] + array[low] + array[high]

        # Check if current_sum is closer to target than our previous best
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum

        if current_sum == target:
            # Distance is 0, cannot get closer than exact match
            break
        elif current_sum < target:
            # Sum is too small, advance low pointer
            low += 1
        else:
            # Sum is too large, decrement high pointer
            high -= 1

    if closest_sum == target:
        break

print(f"Closest triplet sum to {target} : {closest_sum}")

