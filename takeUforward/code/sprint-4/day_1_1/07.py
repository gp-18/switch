# Count Pairs Whose Sum is Less than Target (Sorted Array)
# Given an array nums of integers sorted in ascending order and an integer target,
# count how many pairs (i, j) with i < j have a sum strictly less than target (nums[i] + nums[j] < target).
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5], target = 6
# Output: 4  # Pairs: (1, 2), (1, 3), (1, 4), (2, 3)
#
# Example 2:
# Input:  nums = [-1, 1, 2, 3], target = 2
# Output: 2  # Pairs: (-1, 1), (-1, 2)
#
# Example 3 (Edge Case):
# Input:  nums = [4, 5, 6], target = 5
# Output: 0  # Smallest sum is 4 + 5 = 9, none < 5
#
# Think About:
# - Put left = 0 and right = len(nums) - 1.
# - If nums[left] + nums[right] < target:
#   * Since array is sorted, pairing nums[left] with any element between left + 1 and right also < target.
#   * Add (right - left) to count at once!
#   * Move left += 1.
# - If nums[left] + nums[right] >= target:
#   * Sum is too large, move right -= 1.
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


low_index = 0
high_index = len(array) - 1
count = 0

while low_index < high_index:
    current_sum = array[low_index] + array[high_index]

    if current_sum < target:
        count += high_index - low_index
        low_index += 1
    else:
        high_index -= 1

print(f"Count of pairs: {count}")