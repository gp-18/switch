# Convert a dictionary to a sorted list of key-value tuples.
# Example 1: Input: {'b': 1, 'a': 2} -> Output: [('a', 2), ('b', 1)]
# Example 2: Input: {'z': 10, 'x': 5} -> Output: [('x', 5), ('z', 10)]

data = {'b': 1, 'a': 2, 'c': 3}

sorted_tuples = sorted(data.items())
print("Dictionary:", data)
print("Sorted key-value tuples:", sorted_tuples)
