# Shuffle a list and verify that the original list has been modified.

# Example 1:
# Input: items = [1, 2, 3, 4, 5]; random.shuffle(items)
# Output: items order is permuted in-place

# Example 2:
# Input: items = ['x', 'y', 'z']
# Output: items shuffled in-place

import random

items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f"Shuffled list: {items}")
