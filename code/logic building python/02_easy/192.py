# Extract unique values from a dictionary.
# Example 1: Input: {'a': 1, 'b': 2, 'c': 1, 'd': 3} -> Output: [1, 2, 3]
# Example 2: Input: {'x': 10, 'y': 10} -> Output: [10]

# Sample dictionary
data = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

unique_vals = list(set(data.values()))
print("Original dictionary:", data)
print("Unique values:", unique_vals)
