# Count Triplets with Sum Less Than Target (3 Sum Smaller)
# Given an integer array nums of length n and an integer target,
# return the number of triplets (i, j, k) with 0 <= i < j < k < n
# such that: nums[i] + nums[j] + nums[k] < target.
#
# Example 1:
# Input:  nums = [-2, 0, 1, 3], target = 2
# Output: 2  # Triplets: (-2, 0, 1) and (-2, 0, 3)
#
# Example 2:
# Input:  nums = [5, 1, 3, 4, 7], target = 12
# Output: 4  # Triplets: (1, 3, 4), (1, 3, 5), (1, 3, 7), (1, 4, 5)
#
# Example 3 (Edge Case):
# Input:  nums = [1, 2, 3], target = 5
# Output: 0  # Smallest sum is 6 (>= 5)
#
# Think About:
# - Sort nums in ascending order.
# - Initialize count = 0.
# - Loop i from 0 to n - 3.
# - Set low = i + 1, high = n - 1.
# - While low < high:
#   * If nums[i] + nums[low] + nums[high] < target:
#       All elements between low and high will also produce a sum < target!
#       Add (high - low) to count all at once: count += (high - low)
#       Advance low += 1.
#   * Else:
#       high -= 1 (sum too large).
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

# Optimal Approach: Sort + Two Pointers with (high - low) interval shortcut
# Time Complexity: O(N^2) | Space Complexity: O(1) auxiliary space
array.sort()
n = len(array)
count = 0

for i in range(n - 2):
    low = i + 1
    high = n - 1

    while low < high:
        current_sum = array[i] + array[low] + array[high]

        if current_sum < target:
            # Key Insight:
            # Since the array is sorted, pairing array[i] and array[low] with
            # ANY element from low + 1 up to high will ALSO give sum < target!
            # So add all (high - low) valid pairs at once.
            count += (high - low)
            # Advance low to try a larger middle number
            low += 1
        else:
            # Sum is too large or equal, decrement high
            high -= 1

print(f"Total triplets with sum less than {target} : {count}")

