# ============================================================
# Problem: Shape Area Calculator
# Difficulty: Medium
# ============================================================
#
# PROBLEM STATEMENT:
# Create a common Shape interface or base class with an area() method.
# Implement Rectangle and Circle so each calculates its own area.
# Use pi = 3.14.
# Implement solution() to process a list of shapes and return their
# areas in input order, rounded to 2 decimal places.
#
# INPUT:
# - shapes_data: list of tuples:
#   ("rectangle", length, width) or ("circle", radius)
#
# OUTPUT:
# - List of area strings rounded to two decimal places
#
# EXAMPLE:
# Input:  [("rectangle", 4, 5), ("circle", 2)]
# Output: ["20.00", "12.56"]
#
# CONSTRAINTS:
# - dimensions > 0
# - use pi = 3.14
# ============================================================

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        pass

    def area(self):
        pass


def solution(shapes_data):
    # Process shapes and return list of area strings
    pass


# ---- TEST CASES ----
assert solution([("rectangle", 4, 5), ("circle", 2)]) == ["20.00", "12.56"], "Test 1 Failed"
assert solution([("rectangle", 3, 6), ("circle", 5), ("rectangle", 2.5, 4)]) == ["18.00", "78.50", "10.00"], "Test 2 Failed"
assert solution([("circle", 1), ("circle", 10)]) == ["3.14", "314.00"], "Test 3 Failed"

print("All test cases passed!")
