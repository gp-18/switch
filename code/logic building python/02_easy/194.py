# Merge two dictionaries.
# Example 1: Input: dict1={'a': 1}, dict2={'b': 2} -> Output: {'a': 1, 'b': 2}
# Example 2: Input: dict1={'x': 10}, dict2={'y': 20} -> Output: {'x': 10, 'y': 20}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)
