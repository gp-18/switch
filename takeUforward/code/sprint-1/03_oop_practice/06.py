# ============================================================
# Problem: Employee Salary Management
# Difficulty: Medium
# ============================================================
#
# PROBLEM STATEMENT:
# Create an Employee class with name and salary.
# Create a Manager class that inherits from Employee and adds a bonus.
# Implement a method that returns the total compensation for each.
# Implement solution() to return both compensations formatted.
#
# INPUT:
# - emp_data: tuple of (name, salary)
# - mgr_data: tuple of (name, salary, bonus)
#
# OUTPUT:
# - String with both details:
#   "<emp_name>: <total_comp>\n<mgr_name>: <total_comp>"
#
# EXAMPLE:
# Input:  ("Asha", 50000), ("Raj", 70000, 10000)
# Output: "Asha: 50000\nRaj: 80000"
#
# CONSTRAINTS:
# - salary >= 0, bonus >= 0
# ============================================================

class Employee:
    def __init__(self, name, salary):
        pass

    def get_total_compensation(self):
        pass

    def get_details(self):
        pass


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        pass

    def get_total_compensation(self):
        pass


def solution(emp_data, mgr_data):
    # Create Employee and Manager, and return formatted compensation string
    pass


# ---- TEST CASES ----
assert solution(("Asha", 50000), ("Raj", 70000, 10000)) == "Asha: 50000\nRaj: 80000", "Test 1 Failed"
assert solution(("Vikram", 45000), ("Sneha", 80000, 15000)) == "Vikram: 45000\nSneha: 95000", "Test 2 Failed"
assert solution(("Rahul", 30000), ("Priya", 60000, 0)) == "Rahul: 30000\nPriya: 60000", "Test 3 Failed"

print("All test cases passed!")
