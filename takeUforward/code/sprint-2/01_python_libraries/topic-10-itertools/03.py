# Generate the Cartesian product of two small lists.

# Example 1:
# Input: list1 = [1, 2], list2 = ['a', 'b']
# Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Example 2:
# Input: list1 = ['H', 'T'], list2 = [1, 2]
# Output: [('H', 1), ('H', 2), ('T', 1), ('T', 2)]

import itertools

list1 = [1, 2]
list2 = ['a', 'b']
prod = list(itertools.product(list1, list2))
print(prod)
