# ============================================================
# Problem: Rectangle Calculator
# Difficulty: Easy
# ============================================================
#
# PROBLEM STATEMENT:
# Create a Rectangle class with length and width attributes.
# Implement methods to calculate the area and perimeter of the
# rectangle. Reject non-positive dimensions by returning "Invalid Dimensions".
# Implement solution() returning "Area: <area>, Perimeter: <perimeter>".
#
# INPUT:
# - length: number (int or float)
# - width: number (int or float)
#
# OUTPUT:
# - "Area: <area>, Perimeter: <perimeter>" or "Invalid Dimensions"
#
# EXAMPLE:
# Input:  (10, 5)
# Output: "Area: 50, Perimeter: 30"
#
# CONSTRAINTS:
# - length and width are real numbers
# ============================================================

class Rectangle:
    def __init__(self, length, width):
        pass

    def is_valid(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def get_stats(self):
        pass


def solution(length, width):
    # Create Rectangle and return stats
    pass


# ---- TEST CASES ----
assert solution(10, 5) == "Area: 50, Perimeter: 30", "Test 1 Failed"
assert solution(7, 3) == "Area: 21, Perimeter: 20", "Test 2 Failed"
assert solution(0, 5) == "Invalid Dimensions", "Test 3 Failed"
assert solution(4, -2) == "Invalid Dimensions", "Test 4 Failed"

print("All test cases passed!")
