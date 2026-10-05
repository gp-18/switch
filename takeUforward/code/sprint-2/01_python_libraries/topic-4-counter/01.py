# Count the frequency of every number in a list using Counter.

# Example 1:
# Input: nums = [1, 2, 2, 3, 3, 3, 4]
# Output: Counter({3: 3, 2: 2, 1: 1, 4: 1})

# Example 2:
# Input: nums = [5, 5, 5, 5]
# Output: Counter({5: 4})

from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 4]
counts = Counter(nums)
print(counts)
