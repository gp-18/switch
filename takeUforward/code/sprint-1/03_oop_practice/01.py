# ============================================================
# Problem: Student Profile
# Difficulty: Easy
# ============================================================
#
# PROBLEM STATEMENT:
# Create a Student class with name and marks attributes.
# Add a method that returns "Pass" if marks are at least 40;
# otherwise, return "Fail".
# Implement solution() to create a student and return profile
# in format "<name>: <Pass/Fail>".
#
# INPUT:
# - name: string
# - marks: non-negative integer
#
# OUTPUT:
# - Profile string in format "<name>: <Pass/Fail>"
#
# EXAMPLE:
# Input:  ("Asha", 75)
# Output: "Asha: Pass"
#
# CONSTRAINTS:
# - 0 <= marks <= 100
# - name is a non-empty string
# ============================================================

class Student:
    def __init__(self, name, marks):
        pass

    def get_result(self):
        pass

    def get_profile(self):
        pass


def solution(name, marks):
    # Create a Student and return profile
    pass


# ---- TEST CASES ----
assert solution("Asha", 75) == "Asha: Pass", "Test 1 Failed"
assert solution("Rohan", 32) == "Rohan: Fail", "Test 2 Failed"
assert solution("Pooja", 40) == "Pooja: Pass", "Test 3 Failed"
assert solution("Amit", 39) == "Amit: Fail", "Test 4 Failed"

print("All test cases passed!")
