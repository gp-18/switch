# Copy Constructor — Shallow vs Deep Copy
# Add a @classmethod called from_employee(cls, other) that creates a new Employee
# with the same data as `other`.
# Then use copy.copy (shallow copy) and copy.deepcopy (deep copy) on an Employee
# that has a `skills` list. Observe which copy shares the inner list and which one
# is fully independent.
#
# Example:
# Input:
#   e1 = Employee("Raj", 10000)
#   e1.skills.append("Python")
#   e2 = copy.copy(e1);     e2.skills.append("SQL")
#   e3 = copy.deepcopy(e1); e3.skills.append("Go")
# Output:
#   e1.skills == ["Python", "SQL"]  # shallow copy SHARES the inner list
#   "Go" not in e1.skills           # deep copy is FULLY INDEPENDENT
#

# Write your solution below:


import copy


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.skills = []

    @classmethod
    def from_employee(cls, other):
        new_employee = cls(other.name, other.id)
        new_employee.skills = other.skills.copy()
        return new_employee


e1 = Employee("Raj", 10000)
e1.skills.append("Python")

e2 = copy.copy(e1)
e2.skills.append("SQL")

e3 = copy.deepcopy(e1)
e3.skills.append("Go")

print("e1 skills:", e1.skills)
print("e2 skills:", e2.skills)
print("e3 skills:", e3.skills)

# Using the custom class method
e4 = Employee.from_employee(e1)
e4.skills.append("Java")

print("e1 skills after e4 update:", e1.skills)
print("e4 skills:", e4.skills)


        
