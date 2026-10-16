# Majority Element-I
# Given an integer array nums of size n, return the majority element of the array.
# The majority element of an array is an element that appears strictly more than n // 2 times.
# The array is guaranteed to always have a majority element.
#
# Example 1:
# Input:  nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
# Output: 7
#
# Example 2:
# Input:  nums = [1, 1, 1, 2, 1, 2]
# Output: 1
#
# Example 3 (Edge Case):
# Input:  nums = [-1, -1, -1, -1]
# Output: -1  # All elements are identical negative numbers
#
# Think About:
# - Boyer-Moore Voting Algorithm:
#   * Maintain a candidate and a count = 0.
#   * If count == 0: pick the current number as the new candidate.
#   * If num == candidate: count += 1.
#   * Else: count -= 1 (different elements cancel out).
#   * Since the majority element appears > n / 2 times, it cannot be completely
#     cancelled by all other elements combined.
# - Time Complexity: O(N) single pass
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

# Optimal Approach: Boyer-Moore Voting Algorithm
# Time Complexity: O(N) | Space Complexity: O(1)
candidate = None
count = 0

for num in array:
    # When count reaches 0, choose current element as the candidate
    if count == 0:
        candidate = num
        count = 1
    # If the same element appears, increment votes
    elif num == candidate:
        count += 1
    # Different element cancels out one vote of the candidate
    else:
        count -= 1

print(f"Majority Element is : {candidate}")
