# Return a named tuple from a function that calculates two related values.

# Example 1:
# Input: divide(10, 3)
# Output: DivResult(quotient=3, remainder=1)

# Example 2:
# Input: circle_calc(radius=5)
# Output: CircleStats(area=78.5, perimeter=31.4)

from collections import namedtuple

DivResult = namedtuple('DivResult', ['quotient', 'remainder'])

def divide(a, b):
    return DivResult(a // b, a % b)

res = divide(10, 3)
print(f"DivResult: {res}")
