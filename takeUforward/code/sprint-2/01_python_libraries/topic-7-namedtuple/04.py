# Attempt to modify a named-tuple field and explain the result.

# Example 1:
# Input: p = Point(1, 2); p.x = 10
# Output: Raises AttributeError: can't set attribute (immutable tuple)

# Example 2:
# Input: p._replace(x=10)
# Output: Point(x=10, y=2) (creates a new instance with replaced field)

