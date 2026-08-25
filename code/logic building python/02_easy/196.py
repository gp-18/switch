# Sort a dictionary by key or value.
# Example 1: Input: {'b': 3, 'a': 1, 'c': 2} -> Output: By key: {'a': 1, 'b': 3, 'c': 2}
# Example 2: Input: {'x': 20, 'y': 10} -> Output: By value: {'y': 10, 'x': 20}

data = {'b': 3, 'a': 1, 'c': 2}

sorted_by_key = dict(sorted(data.items()))
sorted_by_val = dict(sorted(data.items(), key=lambda item: item[1]))

print("Sorted by key:", sorted_by_key)
print("Sorted by value:", sorted_by_val)
