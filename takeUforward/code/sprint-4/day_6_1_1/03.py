# Q3. Student Academic Grade Tracker (Practice - Encapsulation)
#
# Task:
# Design a `Student` class to track subject grades.
# Grades must be validated strictly between 0 and 100 before being accepted into the student's record.
#
# Attributes:
# - student_id (str) : Unique student identifier (public).
# - name (str) : Student name (public).
# - __grades (dict[str, float]) : Dictionary mapping subject name to grade score (private).
#
# Methods:
# - __init__(self, student_id: str, name: str):
#     Initializes student with an empty grades dictionary.
# - add_grade(self, subject: str, score: float):
#     If 0.0 <= score <= 100.0, records __grades[subject] = score.
#     Otherwise prints "Invalid grade. Must be between 0 and 100.".
# - get_grade(self, subject: str) -> float | None:
#     Returns the score for subject, or None if the subject has not been graded.
# - calculate_average(self) -> float:
#     Returns the average score across all graded subjects. Returns 0.0 if no grades exist.
# - get_report_card(self) -> dict[str, float]:
#     Returns a copy of all recorded subject-grade pairs.
#
# Example 1:
# Input:
# student = Student("S101", "Rahul")
# student.add_grade("Math", 95.0)
# student.add_grade("Science", 88.0)
# student.add_grade("History", 105.0)  # Invalid grade
# print(student.calculate_average())
# print(student.get_report_card())
# Output:
# Invalid grade. Must be between 0 and 100.
# 91.5
# {'Math': 95.0, 'Science': 88.0}
#
# Example 2:
# Input:
# student = Student("S102", "Pooja")
# student.add_grade("English", 78.5)
# print("English Grade:", student.get_grade("English"))
# print("Physics Grade:", student.get_grade("Physics"))
# Output:
# English Grade: 78.5
# Physics Grade: None
#
# Example 3 (Edge Case):
# Input:
# student = Student("S103", "Aman")
# student.add_grade("Art", -10.0)
# print("Average without grades:", student.calculate_average())
# print("Empty Report Card:", student.get_report_card())
# Output:
# Invalid grade. Must be between 0 and 100.
# Average without grades: 0.0
# Empty Report Card: {}
#
# Think About:
# - Hiding `__grades` prevents external code from inserting corrupt values like negative numbers or scores over 100.
# - Returning `self.__grades.copy()` preserves encapsulation against external dictionary mutations.
# - Time Complexity: O(1) per grade insertion/lookup; O(K) for average calculation where K is number of subjects.
# - Space Complexity: O(K) memory.

# Write your Student class below:

class Student:
    def __init__(self, student_id: str, name: str):
        # Write your code here
        pass

    def add_grade(self, subject: str, score: float):
        # Write your code here
        pass

    def get_grade(self, subject: str) -> float:
        # Write your code here
        pass

    def calculate_average(self) -> float:
        # Write your code here
        pass

    def get_report_card(self) -> dict:
        # Write your code here
        pass

