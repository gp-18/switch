# Convert a key-value list to a flat dictionary.
# Example 1: Input: [('a', 1), ('b', 2)] -> Output: {'a': 1, 'b': 2}
# Example 2: Input: [('x', 10), ('y', 20)] -> Output: {'x': 10, 'y': 20}

kv_list = [('a', 1), ('b', 2), ('c', 3)]

flat_dict = dict(kv_list)
print("Key-value list:", kv_list)
print("Flat dictionary:", flat_dict)
