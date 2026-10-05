# Given a dictionary, remove an entry safely and handle a key that does not exist.

# Example 1:
# Input: d = {'a': 1, 'b': 2}; d.pop('a', None)
# Output: 1 (removed), remaining: {'b': 2}

# Example 2:
# Input: d.pop('z', 'Not Found')
# Output: 'Not Found' (no KeyError raised)

d = {'a': 1, 'b': 2}
val = d.pop('a', None)
print(f"Popped: {val}, remaining: {d}")
missing = d.pop('z', 'Not Found')
print(f"Missing key popped: {missing}")
