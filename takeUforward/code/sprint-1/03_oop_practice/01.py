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
        self.name = name 
        self.marks = marks 

    def get_result(self):
        if self.marks >= 40 :
            return "Pass"
        else : 
            return "Fail"

    def get_profile(self):
        return f"{self.name}: {self.get_result()}"


def solution(name, marks):
    s = Student(name, marks) 
    return s.get_profile()


# ---- TEST CASES ----
assert solution("Asha", 75) == "Asha: Pass", "Test 1 Failed"
assert solution("Rohan", 32) == "Rohan: Fail", "Test 2 Failed"
assert solution("Pooja", 40) == "Pooja: Pass", "Test 3 Failed"
assert solution("Amit", 39) == "Amit: Fail", "Test 4 Failed"

print("All test cases passed!")
