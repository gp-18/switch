# Majority Element-II (> n/3)
# Given an integer array nums of size n, find all elements that appear strictly
# more than n // 3 times. Return the answer in any order.
#
# Example 1:
# Input:  nums = [3, 2, 3]
# Output: [3]
#
# Example 2:
# Input:  nums = [1, 2]
# Output: [1, 2]
#
# Think About:
# - Maintain two candidates and two counters.
# - Triplet cancellation: decrement both counters when a number differs from both candidates.
# - Run a second verification pass.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:

# Optimal Approach: Extended Boyer-Moore Voting Algorithm (2 Candidates, 2 Counters)
# Time Complexity: O(N) | Space Complexity: O(1)

cand1, cand2 = None, None
cnt1, cnt2 = 0, 0

# 1st Pass: Voting / Candidate Selection
for num in array:
    if num == cand1:
        cnt1 += 1
    elif num == cand2:
        cnt2 += 1
    elif cnt1 == 0:
        cand1 = num
        cnt1 = 1
    elif cnt2 == 0:
        cand2 = num
        cnt2 = 1
    else:
        # Triplet cancellation: cancel 3 mutually distinct elements
        cnt1 -= 1
        cnt2 -= 1

# 2nd Pass: Manual Verification Pass
actual_cnt1 = 0
actual_cnt2 = 0

for num in array:
    if num == cand1:
        actual_cnt1 += 1
    elif num == cand2:
        actual_cnt2 += 1

threshold = length // 3
result = []

if actual_cnt1 > threshold:
    result.append(cand1)
if actual_cnt2 > threshold:
    result.append(cand2)

print(f"Elements appearing strictly more than n/3 times are: {result}")

