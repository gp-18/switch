# Group consecutive equal values in [1, 1, 2, 2, 3].

# Example 1:
# Input: data = [1, 1, 2, 2, 3]
# Output: [(1, [1, 1]), (2, [2, 2]), (3, [3])]

# Example 2:
# Input: data = ['a', 'a', 'b']
# Output: [('a', ['a', 'a']), ('b', ['b'])]

import itertools

data = [1, 1, 2, 2, 3]
grouped = [(k, list(g)) for k, g in itertools.groupby(data)]
print(grouped)
