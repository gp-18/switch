# Alternative Constructors with @classmethod
# Add three @classmethod factory methods to Employee:
#   1. from_string("Neha, 15000") — parses a comma-separated string
#   2. from_dict({"name": "Raj", "salary": 100}) — builds from a dictionary
#   3. intern("Riya") — creates an employee with salary 0
# All factory methods must return an instance through cls(...) (not hardcoded Employee(...))
# so that subclasses inherit them correctly.
#
# Example 1:
# Input:  e1 = Employee.from_string("Neha, 15000")
# Output: e1.name == "Neha", e1.salary == 15000
#
# Example 2:
# Input:  e2 = Employee.from_dict({"name": "Raj", "salary": 100})
# Output: e2.name == "Raj", e2.salary == 100
#
# Example 3:
# Input:  e3 = Employee.intern("Riya")
# Output: e3.name == "Riya", e3.salary == 0
#

# Write your solution below:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name.strip(), int(salary.strip()))

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["salary"])

    @classmethod
    def intern(cls, name):
        return cls(name, 0)


# Example 1: Create an employee from a string
e1 = Employee.from_string("Neha, 15000")
print(e1.name, e1.salary)

# Example 2: Create an employee from a dictionary
e2 = Employee.from_dict({"name": "Raj", "salary": 100})
print(e2.name, e2.salary)

# Example 3: Create an intern with salary 0
e3 = Employee.intern("Riya")
print(e3.name, e3.salary)
