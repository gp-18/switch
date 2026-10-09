# Parameterized Constructor with Validation
# Write a class Employee whose __init__(self, name, salary) stores both attributes.
# Inside the constructor, validate the inputs:
# - Raise ValueError if name is empty.
# - Raise ValueError if salary is negative.
# The constructor should guarantee a valid object from the very first line.
#
# Example 1:
# Input:  e = Employee("Raj", 10000)
# Output: e.name == "Raj", e.salary == 10000
#
# Example 2:
# Input:  Employee("", 100)
# Output: ValueError
#
# Example 3:
# Input:  Employee("Raj", -1)
# Output: ValueError
#

# Write your solution below:


class Employee:
    def __init__(self, name, salary):
        if name == "":
            raise ValueError("Name cannot be empty")

        if salary < 0:
            raise ValueError("Salary cannot be negative")

        self.name = name
        self.salary = salary


e = Employee("Raj", 10000)

print(e.name)
print(e.salary)

