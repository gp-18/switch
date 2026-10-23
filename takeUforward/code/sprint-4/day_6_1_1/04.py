# Q4. Employee Salary & Performance Manager (Practice - Encapsulation)
#
# Task:
# Design an `Employee` class where salary changes and performance bonuses require manager
# authorization and strict bounds checking.
#
# Attributes:
# - emp_id (int) : Employee ID (public).
# - department (str) : Employee department (public).
# - __base_salary (float) : Monthly base salary (private).
# - __performance_rating (int) : Integer rating from 1 to 5 (private).
#
# Methods:
# - __init__(self, emp_id: int, department: str, base_salary: float, rating: int):
#     Initializes employee. Base salary must be >= 0 and rating must be in [1, 5].
# - update_salary(self, new_salary: float, is_manager: bool):
#     Only updates __base_salary if is_manager == True and new_salary >= self.__base_salary.
#     Otherwise prints "Unauthorized or invalid salary update.".
# - set_rating(self, new_rating: int):
#     Updates __performance_rating if 1 <= new_rating <= 5.
#     Otherwise prints "Rating must be between 1 and 5.".
# - calculate_bonus(self) -> float:
#     Rating 5: 20% of base salary
#     Rating 4: 15% of base salary
#     Rating 3: 10% of base salary
#     Rating 1 or 2: 0% bonus
# - get_total_compensation(self) -> float:
#     Returns __base_salary + calculate_bonus().
#
# Example 1:
# Input:
# emp = Employee(1001, "Engineering", 80000.0, 4)
# print("Bonus:", emp.calculate_bonus())
# emp.update_salary(75000.0, is_manager=True)   # Attempt salary reduction
# emp.update_salary(90000.0, is_manager=False)  # Unauthorized
# emp.update_salary(95000.0, is_manager=True)   # Valid update
# emp.set_rating(5)
# print("Total Compensation:", emp.get_total_compensation())
# Output:
# Bonus: 12000.0
# Unauthorized or invalid salary update.
# Unauthorized or invalid salary update.
# Total Compensation: 114000.0
#
# Example 2:
# Input:
# emp = Employee(1002, "Marketing", 50000.0, 3)
# print("Total Compensation:", emp.get_total_compensation())
# Output:
# Total Compensation: 55000.0
#
# Example 3 (Edge Case):
# Input:
# emp = Employee(1003, "Support", 40000.0, 1)
# emp.set_rating(7)   # Invalid rating
# print("Bonus for Rating 1:", emp.calculate_bonus())
# Output:
# Rating must be between 1 and 5.
# Bonus for Rating 1: 0.0
#
# Think About:
# - Encapsulation ensures salary cannot be decremented or modified by unauthorized non-manager callers.
# - Bonus calculation is isolated inside the class so business rules remain centralized.
# - Time Complexity: O(1) for all operations.
# - Space Complexity: O(1) auxiliary space.

# Write your Employee class below:

class Employee:
    def __init__(self, emp_id: int, department: str, base_salary: float, rating: int):
        # Write your code here
        pass

    def update_salary(self, new_salary: float, is_manager: bool):
        # Write your code here
        pass

    def set_rating(self, new_rating: int):
        # Write your code here
        pass

    def calculate_bonus(self) -> float:
        # Write your code here
        pass

    def get_total_compensation(self) -> float:
        # Write your code here
        pass
