# Majority Element-II
# Given an integer array nums of size n. Return all elements which appear strictly
# more than n // 3 times in the array. The output can be returned in any order.
#
# Example 1:
# Input:  nums = [1, 2, 1, 1, 3, 2]
# Output: [1]
# Explanation: n / 3 = 6 / 3 = 2. Element appearing >= 3 times is [1].
#
# Example 2:
# Input:  nums = [1, 2, 1, 1, 3, 2, 2]
# Output: [1, 2]
# Explanation: n / 3 = 7 / 3 = 2. Elements appearing >= 3 times are [1, 2].
#
# Example 3 (Edge Case):
# Input:  nums = [1, 2, 3]
# Output: []
# Explanation: No element appears > n/3 times.
#
# Think About:
# - Extended Boyer-Moore Voting Algorithm:
#   * At most 2 elements can appear > n/3 times.
#   * Maintain 2 candidates and 2 counters.
#   * Pass 1: Cancel triplets of 3 distinct elements.
#   * Pass 2: Verify candidate frequencies (mandatory!).
# - Time Complexity: O(N) linear time (two passes)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:

# Optimal Approach: Extended Boyer-Moore Voting Algorithm
# Time Complexity: O(N) | Space Complexity: O(1)

candidate1, candidate2 = None, None
count1, count2 = 0, 0

# 1st Pass: Voting / Candidate Selection
for num in array:
    if num == candidate1:
        count1 += 1
    elif num == candidate2:
        count2 += 1
    elif count1 == 0:
        candidate1 = num
        count1 = 1
    elif count2 == 0:
        candidate2 = num
        count2 = 1
    else:
        # Triplet cancellation
        count1 -= 1
        count2 -= 1

# 2nd Pass: Verification
actual_count1 = 0
actual_count2 = 0
for num in array:
    if num == candidate1:
        actual_count1 += 1
    elif num == candidate2:
        actual_count2 += 1

threshold = len(array) // 3
result = []

if actual_count1 > threshold:
    result.append(candidate1)
if actual_count2 > threshold:
    result.append(candidate2)

print(f"Elements appearing more than n/3 times are : {result}")
