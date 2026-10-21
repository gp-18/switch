# Wiggle Sort: Peak and Valley In-Place Traversal (Google, Meta, Amazon)
# Given an unsorted integer array nums, reorder it in-place such that:
#   nums[0] <= nums[1] >= nums[2] <= nums[3]...
# For even index i: nums[i] <= nums[i + 1]
# For odd index i:  nums[i] >= nums[i + 1]
# Solve this in O(N) time and O(1) auxiliary space without fully sorting the array.
#
# Example 1:
# Input:  nums = [3, 5, 2, 1, 6, 4]
# Output: [3, 5, 1, 6, 2, 4]  # 3 <= 5 >= 1 <= 6 >= 2 <= 4
#
# Example 2:
# Input:  nums = [6, 6, 5, 6, 3, 8]
# Output: [6, 6, 5, 6, 3, 8]
#
# Example 3 (Edge Case):
# Input:  nums = [1]
# Output: [1]  # Single element
#
# Think About:
# - Single-Pass Greedy Inversion:
#   * Loop i from 0 to n - 2:
#       - If i is even: we need nums[i] <= nums[i + 1]. If nums[i] > nums[i + 1], swap them.
#       - If i is odd:  we need nums[i] >= nums[i + 1]. If nums[i] < nums[i + 1], swap them.
# - Invariant: A local swap at an odd index never breaks the previous condition because
#   the element swapped in is even larger than the one that was there!
# - Time Complexity: O(N) single pass
# - Space Complexity: O(1) in-place
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

print(f"Your array has become: {array} and now doing the operations on it.")

# Write your solution below
