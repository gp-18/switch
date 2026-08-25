# Create a dictionary mapping lowercase letters to their uppercase versions.
# Example 1: Input: ['a', 'b', 'c'] -> Output: {'a': 'A', 'b': 'B', 'c': 'C'}
# Example 2: Input: ['x', 'y'] -> Output: {'x': 'X', 'y': 'Y'}

letters = ['a', 'b', 'c', 'd']

char_map = {char: char.upper() for char in letters}
print("Letters:", letters)
print("Lowercase to Uppercase map:", char_map)
