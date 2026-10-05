# Create a Point named tuple containing x and y.

# Example 1:
# Input: Point = namedtuple('Point', ['x', 'y']); p = Point(10, 20)
# Output: p.x = 10, p.y = 20

# Example 2:
# Input: p = Point(3, 4)
# Output: p[0] = 3, p[1] = 4

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"p.x = {p.x}, p.y = {p.y}")
