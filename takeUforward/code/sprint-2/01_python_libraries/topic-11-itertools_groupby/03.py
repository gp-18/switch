# Sort a list before using groupby() and compare the result.

# Example 1:
# Input: data = [1, 2, 1, 1]; sorted_data = sorted(data)
# Output: sorted_data = [1, 1, 1, 2] -> Groups: 1 -> [1, 1, 1], 2 -> [2]

# Example 2:
# Input: data = ['b', 'a', 'b']; sorted_data = ['a', 'b', 'b']
# Output: Groups: 'a' -> ['a'], 'b' -> ['b', 'b']

import itertools

data = [1, 2, 1, 1]
sorted_data = sorted(data)
grouped = [(k, list(g)) for k, g in itertools.groupby(sorted_data)]
print(f"Sorted: {sorted_data}")
print(f"Grouped: {grouped}")
