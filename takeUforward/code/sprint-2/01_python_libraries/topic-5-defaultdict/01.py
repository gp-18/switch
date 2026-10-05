# Count the frequency of numbers using defaultdict(int).

# Example 1:
# Input: nums = [1, 2, 2, 3, 1, 1]
# Output: defaultdict(<class 'int'>, {1: 3, 2: 2, 3: 1})

# Example 2:
# Input: nums = [4, 5, 4]
# Output: defaultdict(<class 'int'>, {4: 2, 5: 1})

from collections import defaultdict

nums = [1, 2, 2, 3, 1, 1]
counts = defaultdict(int)
for x in nums:
    counts[x] += 1
print(counts)
