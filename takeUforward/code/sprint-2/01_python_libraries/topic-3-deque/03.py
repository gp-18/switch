# Given a list of integers, use a deque to simulate a sliding window of fixed size.

# Example 1:
# Input: nums = [1, 3, -1, -3, 5, 3], k = 3
# Output: Windows: [1, 3, -1] -> [3, -1, -3] -> [-1, -3, 5] -> [-3, 5, 3]

# Example 2:
# Input: nums = [10, 20, 30, 40], k = 2
# Output: Windows: [10, 20] -> [20, 30] -> [30, 40]

from collections import deque

nums = [1, 3, -1, -3, 5, 3]
k = 3

window = deque()
windows = []

for num in nums:
    window.append(num)
    if len(window) > k:
        window.popleft()
    if len(window) == k:
        windows.append(list(window))

print(" -> ".join(str(w) for w in windows))
