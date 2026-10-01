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
        self.length = length
        self.width = width

    def is_valid(self):
        return self.length > 0 and self.width > 0

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def get_stats(self):
        if self.is_valid() :
            return f"Area: {self.area()}, Perimeter: {self.perimeter()}"
        else :
            return "Invalid Dimensions"


def solution(length, width):
    # Create Rectangle and return stats
    r = Rectangle(length, width)
    return r.get_stats()


# ---- TEST CASES ----
assert solution(10, 5) == "Area: 50, Perimeter: 30", "Test 1 Failed"
assert solution(7, 3) == "Area: 21, Perimeter: 20", "Test 2 Failed"
assert solution(0, 5) == "Invalid Dimensions", "Test 3 Failed"
assert solution(4, -2) == "Invalid Dimensions", "Test 4 Failed"

print("All test cases passed!")
