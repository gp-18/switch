# Select three unique random elements from a list using sample().

# Example 1:
# Input: items = [1, 2, 3, 4, 5, 6, 7]; random.sample(items, 3)
# Output: List of 3 unique elements, e.g. [2, 5, 1]

# Example 2:
# Input: items = ['a', 'b', 'c', 'd']; random.sample(items, 2)
# Output: List of 2 unique elements

import random

items = [1, 2, 3, 4, 5, 6, 7]
sample = random.sample(items, 3)
print(f"Random sample: {sample}")
