# Rearrange Array Elements by Sign
# Given an integer array nums of even length consisting of an equal number of positive and negative integers,
# rearrange the array such that:
# 1. Every consecutive pair of integers have opposite signs.
# 2. For all integers with the same sign, the relative order from nums is preserved.
# 3. The rearranged array begins with a positive integer.
#
# Example 1:
# Input:  nums = [2, 4, 5, -1, -3, -4]
# Output: [2, -1, 4, -3, 5, -4]
#
# Example 2:
# Input:  nums = [1, -1, -3, -4, 2, 3]
# Output: [1, -1, 2, -3, 3, -4]
#
# Example 3 (Edge Case):
# Input:  nums = [3, -2]
# Output: [3, -2]  # Smallest even length array (n = 2)
#
# Think About:
# - Positive numbers go to even indices (0, 2, 4, ...).
# - Negative numbers go to odd indices (1, 3, 5, ...).
# - Single pass approach: initialize ans array of size n, pos_idx = 0, neg_idx = 1.
# - If num > 0: place at ans[pos_idx] and pos_idx += 2.
# - If num < 0: place at ans[neg_idx] and neg_idx += 2.
# - Time Complexity: O(N) single pass
# - Space Complexity: O(N) for output array
#

length = int(input("Enter the length of the array (must be an even number) : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

# Optimal Approach: Single Pass Direct Index Placement
# Time Complexity: O(N) | Space Complexity: O(N) for answer array
n = len(array)
ans = [0] * n

pos_idx = 0  # Even index pointer for positives: 0, 2, 4, ...
neg_idx = 1  # Odd index pointer for negatives:  1, 3, 5, ...

for num in array:
    # If the number is positive, place at current even slot
    if num > 0:
        ans[pos_idx] = num
        pos_idx += 2
    # If the number is negative, place at current odd slot
    else:
        ans[neg_idx] = num
        neg_idx += 2

print(f"Rearranged array : {ans}")
