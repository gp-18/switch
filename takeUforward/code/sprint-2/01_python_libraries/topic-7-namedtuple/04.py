# Attempt to modify a named-tuple field and explain the result.

# Example 1:
# Input: p = Point(1, 2); p.x = 10
# Output: Raises AttributeError: can't set attribute (immutable tuple)

# Example 2:
# Input: p._replace(x=10)
# Output: Point(x=10, y=2) (creates a new instance with replaced field)

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

try:
    p.x = 10
except AttributeError as e:
    print(f"AttributeError: {e}")

p_new = p._replace(x=10)
print(f"Replaced using _replace: {p_new}")
