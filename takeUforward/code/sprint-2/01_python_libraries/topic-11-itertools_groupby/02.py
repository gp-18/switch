# Explain what happens when equal values are separated, such as [1, 2, 1, 1].

# Example 1:
# Input: data = [1, 2, 1, 1]
# Output: Groups: 1 -> [1], 2 -> [2], 1 -> [1, 1] (groupby only groups consecutive identical keys)

# Example 2:
# Input: data = ['A', 'B', 'A']
# Output: Groups: 'A' -> ['A'], 'B' -> ['B'], 'A' -> ['A']

import itertools

data = [1, 2, 1, 1]
grouped = [(k, list(g)) for k, g in itertools.groupby(data)]
print(f"Groups: {grouped}")
