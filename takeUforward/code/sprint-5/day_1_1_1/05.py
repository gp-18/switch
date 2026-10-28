# Generalized Heavy Hitters (> n/k) — Misra-Gries Algorithm
# Given an array nums of size n and an integer k, find all distinct elements
# that appear strictly more than n // k times. Implement the generalized
# Misra-Gries algorithm using O(k) auxiliary memory.
#
# Example 1:
# Input:  nums = [3, 1, 2, 2, 1, 2, 3, 3], k = 4
# Output: [2, 3]
# Explanation: n = 8, threshold = 8 // 4 = 2. Elements appearing >= 3 times: 2 and 3.
#
# Example 2:
# Input:  nums = [1, 2, 3, 4, 5], k = 2
# Output: []
# Explanation: Threshold = 5 // 2 = 2. No element appears >= 3 times.
#
# Think About:
# - Maintain a dictionary of at most k - 1 candidates.
# - If num in candidates: candidates[num] += 1.
# - Else if len(candidates) < k - 1: candidates[num] = 1.
# - Else: decrement all values in candidates, delete keys with count == 0.
# - Second pass: verify frequencies in nums > n // k.
# - Time Complexity: O(N * k)
# - Space Complexity: O(k) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

k = int(input("Enter threshold divisor k: "))

print(f"Your array has become : {array} with k = {k}.")

# Write your solution below:

# Optimal Approach: Misra-Gries Heavy Hitters Algorithm
# Time Complexity: O(N * k) | Space Complexity: O(k)

if k <= 1 or length == 0:
    print(f"Elements appearing strictly more than n/{k} times are: []")
else:
    # 1. Candidate Selection (at most k - 1 candidates)
    candidates = {}

    for num in array:
        if num in candidates:
            candidates[num] += 1
        elif len(candidates) < k - 1:
            candidates[num] = 1
        else:
            # Decrement all candidate counts by 1 (cancelling k distinct elements)
            to_delete = []
            for cand in candidates:
                candidates[cand] -= 1
                if candidates[cand] == 0:
                    to_delete.append(cand)
            for cand in to_delete:
                del candidates[cand]

    # 2. Verification Pass
    threshold = length // k
    result = []

    for cand in candidates:
        actual_count = array.count(cand)
        if actual_count > threshold:
            result.append(cand)

    print(f"Elements appearing strictly more than n/{k} times are: {sorted(result)}")

