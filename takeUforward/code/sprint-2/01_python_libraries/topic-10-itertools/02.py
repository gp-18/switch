# Generate all 2-element permutations of a list and explain why the result differs from combinations.

# Example 1:
# Input: lst = [1, 2, 3]
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)] (order matters in permutations)

# Example 2:
# Input: lst = ['A', 'B']
# Output: [('A', 'B'), ('B', 'A')]

import itertools

lst = [1, 2, 3]
perms = list(itertools.permutations(lst, 2))
print(f"Permutations: {perms}")
