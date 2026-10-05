# Compare two Counter objects and explain the result of their addition, subtraction, intersection, and union.

# Example 1:
# Input: c1 = Counter(a=3, b=1), c2 = Counter(a=1, b=2)
# Output: c1 + c2 = Counter({'a': 4, 'b': 3}), c1 - c2 = Counter({'a': 2})

# Example 2:
# Input: c1 = Counter(x=2, y=3), c2 = Counter(x=1, y=4)
# Output: c1 & c2 = Counter({'y': 3, 'x': 1}), c1 | c2 = Counter({'y': 4, 'x': 2})

from collections import Counter

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"c1 + c2 = {c1 + c2}")
print(f"c1 - c2 = {c1 - c2}")
print(f"c1 & c2 = {c1 & c2}")
print(f"c1 | c2 = {c1 | c2}")
